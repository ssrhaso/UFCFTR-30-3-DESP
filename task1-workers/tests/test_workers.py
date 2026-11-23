"""Unit tests of the job workers. No cluster is necessary.

    cd task1-workers
    python -m pytest
"""

import asyncio
import re
from datetime import datetime, timedelta, timezone
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path
from types import SimpleNamespace

import pytest
from pyzeebe.errors import BusinessError

import handlers
import mock_services as mock

MODELS = Path(__file__).resolve().parents[2] / "task1-bpmn" / "operational"
HANDLERS = {task.type: task.original_function for task in handlers.router.tasks}
BASKET = [{"productId": "P-101", "quantity": 2}, {"productId": "P-102", "quantity": 1},
          {"productId": "P-201", "quantity": 1}]


def job(job_type: str, variables: dict, retries: int = 3, key: int = 1):
    return SimpleNamespace(type=job_type, variables=variables, element_id="", bpmn_process_id="test",
                           process_instance_key=key, retries=retries)


def run(job_type: str, variables: dict, **kwargs) -> dict:
    result = asyncio.run(HANDLERS[job_type](job(job_type, variables, **kwargs)))
    variables.update(result)
    return result


@pytest.mark.parametrize("model", ["process-order.bpmn", "process-payment.bpmn"])
def test_each_job_type_of_the_diagram_has_a_handler(model):
    types = set(re.findall(r'zeebe:taskDefinition type="([^"]+)"', (MODELS / model).read_text(encoding="utf-8")))
    assert types and types <= set(HANDLERS)


def test_order_split_adds_up_to_the_order_total():
    v = {"basket": [dict(line) for line in BASKET]}
    for job_type in ("check-stock", "calculate-order-total", "create-order", "split-order"):
        run(job_type, v)
    assert v["allAvailable"] is True
    subtotals = sum(Decimal(str(p["subtotal"])) for p in v["producerOrders"])
    assert subtotals == mock.money(v["orderTotal"])
    assert {p["producerId"] for p in v["producerOrders"]} == {"PR-01", "PR-02"}


def test_surplus_discount_on_the_sourdough():
    v = {"basket": [{"productId": "P-201", "quantity": 1}]}
    run("calculate-order-total", v)
    assert v["orderTotal"] == 4.05  # 4.50 less the 10% surplus discount (R15)


def test_earliest_date_is_at_least_48_hours_after_the_order():
    v = {"producers": [{"producerId": "PR-01", "producerName": "Valley Farm"}], "postcode": "BS16 1QY"}
    run("determine-arrangements", v)
    earliest = datetime.strptime(v["arrangements"][0]["earliestDate"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    assert earliest >= datetime.now(timezone.utc) + timedelta(hours=48) - timedelta(minutes=1)
    assert v["arrangements"][0]["method"] == "delivery"


@pytest.mark.parametrize("total, subtotals, amounts, commission", [
    ("48.60", ["30.00", "18.60"], ["28.50", "17.67"], "2.43"),            # run P1 on the cluster
    ("25.44", ["12.35", "8.10", "4.99"], ["11.73", "7.70", "4.74"], "1.27"),  # run P8 on the cluster
])
def test_commission_rule_of_the_script_task(total, subtotals, amounts, commission):
    # the FEEL of "Calculate producer amounts and commission":
    # amount = round half up(subtotal * 0.95, 2), commission = orderTotal - sum(amounts)
    got = [Decimal(s) * Decimal("0.95") for s in subtotals]
    got = [a.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) for a in got]
    assert got == [Decimal(a) for a in amounts]
    assert Decimal(total) - sum(got) == Decimal(commission)
    assert sum(got) + Decimal(commission) == Decimal(total)


async def _submit(method: str, retries: int = 3) -> list:
    published = []

    class FakeClient:
        async def publish_message(self, name, correlation_key, variables=None, **kwargs):
            published.append((name, correlation_key, variables or {}))

    handlers.set_client(FakeClient())
    await HANDLERS["submit-payment"](job("submit-payment", {"orderId": "ORD-T", "paymentMethod": method,
                                                            "orderTotal": 48.60}, retries=retries))
    await asyncio.sleep(0.05)
    return published


@pytest.mark.parametrize("method, message", [
    ("pm_card_visa", "payment-confirmed"),
    ("pm_card_chargeDeclined", "payment-declined"),
    ("pm_simulate_no_answer", None),
])
def test_mock_payment_result_for_each_sandbox_method(monkeypatch, method, message):
    monkeypatch.setattr(mock, "PAYMENT_ANSWER_DELAY_SECONDS", 0)
    published = asyncio.run(_submit(method))
    if message is None:
        assert published == []
    else:
        assert [(name, key) for name, key, _ in published] == [(message, "ORD-T")]
    if message == "payment-confirmed":
        assert "paymentReference" in published[0][2]


def test_payment_service_unavailable_fails_then_throws_the_bpmn_error():
    with pytest.raises(RuntimeError):
        asyncio.run(_submit("pm_simulate_unavailable", retries=3))
    with pytest.raises(BusinessError) as error:
        asyncio.run(_submit("pm_simulate_unavailable", retries=1))
    assert error.value.error_code == "PAYMENT_SERVICE_UNAVAILABLE"


def test_stock_taken_after_the_check_throws_insufficient_stock(monkeypatch):
    monkeypatch.setenv("MOCK_STOCK_TAKEN", "P-201")
    v = {"basket": [dict(line) for line in BASKET]}
    run("check-stock", v)
    assert v["allAvailable"] is True  # the check runs before the other customer takes the stock
    with pytest.raises(BusinessError) as error:
        run("reserve-stock", v, key=7)
    assert error.value.error_code == "INSUFFICIENT_STOCK"
    run("find-substitutes", v, key=7)
    assert [item["productId"] for item in v["unavailableItems"]] == ["P-201"]


def test_amendment_replaces_the_unavailable_line_with_the_accepted_substitute():
    basket = [{"productId": "P-101", "quantity": 1}, {"productId": "P-202", "quantity": 1}]
    unavailable = mock.check_lines(basket)
    substitutes = mock.substitutes_for(unavailable)
    assert [s["productId"] for s in substitutes] == ["P-301"]
    amended = mock.amend_basket(basket, unavailable, substitutes, ["P-301"])
    assert [line["productId"] for line in amended] == ["P-101", "P-301"]
    assert mock.check_lines(amended) == []
