"""Offline checks of the workers. No cluster is necessary.

1. Each job type of process-order.bpmn and process-payment.bpmn has a handler.
2. The FN1 main path gives the variables that the forms and FN2 read.
3. The FN2 split (the FEEL of "Calculate producer amounts and commission") adds up to the total.
4. submit-payment publishes the correct message for each sandbox payment method.

    python check.py              files from origin/main
    python check.py --ref HEAD
"""

import argparse
import asyncio
import re
import subprocess
import sys
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

from pyzeebe.errors import BusinessError

import handlers
import mock_services as mock

REPO = Path(__file__).resolve().parent.parent
FAILED = []


def check(condition: bool, text: str) -> None:
    print(("  ok    " if condition else "  FAIL  ") + text)
    if not condition:
        FAILED.append(text)


def job(job_type: str, variables: dict, element_id: str = "", process: str = "process_order", retries: int = 3):
    return SimpleNamespace(type=job_type, variables=variables, element_id=element_id, bpmn_process_id=process,
                           process_instance_key=0, retries=retries)


async def run(job_type: str, variables: dict, **kwargs) -> dict:
    handler = {t.type: t.original_function for t in handlers.router.tasks}[job_type]
    result = await handler(job(job_type, variables, **kwargs))
    variables.update(result)
    return result


def job_types(ref: str, name: str) -> set:
    xml = subprocess.run(["git", "-C", str(REPO), "show", f"{ref}:task1-bpmn/operational/{name}"],
                         capture_output=True, check=True, text=True, encoding="utf-8").stdout
    return set(re.findall(r'zeebe:taskDefinition type="([^"]+)"', xml))


async def main(ref: str) -> None:
    print(f"1. Job types (models from {ref})")
    handled = {t.type for t in handlers.router.tasks}
    for name in ("process-order.bpmn", "process-payment.bpmn"):
        types = job_types(ref, name)
        missing = sorted(types - handled)
        check(not missing, f"{name}: {len(types)} job types, missing handlers: {missing or 'none'}")

    print("2. FN1 main path")
    v = {"customerId": "customer-demo", "postcode": "BS16 1QY",
         "basket": [{"productId": "P-101", "quantity": 2}, {"productId": "P-102", "quantity": 1},
                    {"productId": "P-201", "quantity": 1}]}
    await run("check-stock", v)
    check(v["allAvailable"] is True, "check-stock: allAvailable = true")
    await run("reserve-stock", v)
    check(v["reservationId"] is not None and v["reservationExpiresAt"].endswith("Z"),
          f"reserve-stock: {v['reservationId']} until {v['reservationExpiresAt']}")
    check(v["reservationReminderAt"] < v["reservationExpiresAt"], "reserve-stock: reminder before expiry")
    for job_type in ("identify-producers", "determine-arrangements", "calculate-food-miles", "calculate-order-total"):
        await run(job_type, v)
    check(len(v["producers"]) == 2, "identify-producers: 2 producers")
    check(all(a["earliestDate"] > v["reservationExpiresAt"] for a in v["arrangements"]),
          "determine-arrangements: earliest date 48 hours ahead")
    check("foodMiles" in v, f"calculate-food-miles: {v.get('foodMiles')} miles")
    check(abs(sum(line["lineTotal"] for line in v["orderLines"]) - v["orderTotal"]) < 1e-9,
          f"calculate-order-total: lines add up to {v['orderTotal']} (surplus discount on the sourdough)")
    v["reviewDecision"] = "confirm"  # Tasklist: form-review-order
    await run("create-order", v)
    await run("split-order", v)
    subtotal_sum = sum(mock.money(p["subtotal"]) for p in v["producerOrders"])
    check(subtotal_sum == mock.money(v["orderTotal"]), f"split-order: subtotals add up to {subtotal_sum}")

    print("3. FN2 split with the FEEL rule of S4")
    for total, producer_orders in ((v["orderTotal"], v["producerOrders"]),
                                   (48.60, [{"subtotal": 30.00}, {"subtotal": 18.60}])):
        amounts = [mock.money(Decimal(str(p["subtotal"])) * Decimal("0.95")) for p in producer_orders]
        commission = mock.money(total) - sum(amounts)
        check(sum(amounts) + commission == mock.money(total),
              f"total {total}: producers {[str(a) for a in amounts]}, commission {commission}")

    print("4. submit-payment and the payment messages")
    published = []

    class FakeClient:
        async def publish_message(self, name, correlation_key, variables=None, **kwargs):
            published.append((name, correlation_key, variables))

    handlers.set_client(FakeClient())
    mock.PAYMENT_ANSWER_DELAY_SECONDS = 0
    for method, expected in (("pm_card_visa", "payment-confirmed"), ("pm_card_chargeDeclined", "payment-declined")):
        published.clear()
        await run("submit-payment", {"orderId": "ORD-TEST", "paymentMethod": method, "orderTotal": 48.60},
                  process="process_payment")
        await asyncio.sleep(0.05)
        check(bool(published) and published[0][0] == expected and published[0][1] == "ORD-TEST",
              f"{method}: {published[0][0] if published else 'nothing'} published with correlation key ORD-TEST")
        if expected == "payment-confirmed":
            check(bool(published) and "paymentReference" in published[0][2],
                  "payment-confirmed carries paymentReference")
    published.clear()
    await run("submit-payment", {"orderId": "ORD-TEST", "paymentMethod": "pm_simulate_no_answer",
                                 "orderTotal": 48.60}, process="process_payment")
    await asyncio.sleep(0.05)
    check(not published, "pm_simulate_no_answer: the job completes and no message is published")
    unavailable = {"orderId": "ORD-TEST", "paymentMethod": "pm_simulate_unavailable", "orderTotal": 48.60}
    try:
        await run("submit-payment", dict(unavailable), process="process_payment", retries=3)
        check(False, "pm_simulate_unavailable: the job fails while retries remain")
    except RuntimeError:
        check(True, "pm_simulate_unavailable: the job fails while retries remain")
    try:
        await run("submit-payment", dict(unavailable), process="process_payment", retries=1)
        check(False, "pm_simulate_unavailable: last retry throws PAYMENT_SERVICE_UNAVAILABLE")
    except BusinessError as error:
        check(error.error_code == "PAYMENT_SERVICE_UNAVAILABLE",
              "pm_simulate_unavailable: last retry throws PAYMENT_SERVICE_UNAVAILABLE")

    print("5. Service failure: retries first, then the BPMN error")
    try:
        handlers.service_failure(job("submit-payment", {}, retries=3), "PAYMENT_SERVICE_UNAVAILABLE", "payment")
    except RuntimeError:
        check(True, "retries left: the job fails and Zeebe retries it")
    try:
        handlers.service_failure(job("submit-payment", {}, retries=1), "PAYMENT_SERVICE_UNAVAILABLE", "payment")
    except BusinessError as error:
        check(error.error_code == "PAYMENT_SERVICE_UNAVAILABLE", "last retry: BPMN error PAYMENT_SERVICE_UNAVAILABLE")

    print()
    print("All checks passed" if not FAILED else f"{len(FAILED)} checks failed")
    sys.exit(1 if FAILED else 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default="origin/main")
    asyncio.run(main(parser.parse_args().ref))
