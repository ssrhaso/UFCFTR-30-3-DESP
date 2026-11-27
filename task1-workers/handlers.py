"""Job workers for FN1 Process order (process_order) and FN2 Process payment (process_payment).

The job types and the variable names come from task1-bpmn/operational/process-order.md
(section 8) and process-payment.md (section 8).

Do not add "from __future__ import annotations" to this file: pyzeebe finds the Job
parameter by its annotation object.
"""

import asyncio
import logging
from collections import OrderedDict

from pyzeebe import Job, ZeebeClient, ZeebeTaskRouter
from pyzeebe.errors import BusinessError

import mock_services as mock

router = ZeebeTaskRouter()
log = logging.getLogger("workers")

_client: ZeebeClient | None = None
_background: set = set()
payment_attempts: list = []  # record of each payment attempt (NFR08)
_stock_taken: dict = {}  # process instance key -> lines taken between check-stock and reserve-stock


def set_client(client) -> None:
    global _client
    _client = client


def info(job: Job, text: str) -> None:
    log.info("%-15s %s | %-26s %s", job.bpmn_process_id, job.process_instance_key, job.type, text)


def service_failure(job: Job, error_code: str, service: str) -> None:
    """Fail the job while retries remain, then throw the BPMN error of the model."""
    if job.retries > 1:
        info(job, f"{service} unavailable, {job.retries - 1} retries left")
        raise RuntimeError(f"mock {service} unavailable")
    info(job, f"{service} unavailable after the retries, BPMN error {error_code}")
    raise BusinessError(error_code)


# FN1 Process order

@router.task(task_type="check-stock")
async def check_stock(job: Job) -> dict:
    v = job.variables
    if mock.stock_service_down():
        service_failure(job, "STOCK_SERVICE_UNAVAILABLE", "stock service")
    basket = v.get("basket") or []
    result = {}
    if v.get("amendDecision") == "amend":
        basket = mock.amend_basket(basket, v.get("unavailableItems") or [], v.get("substitutes") or [],
                                   v.get("acceptedSubstitutes") or [])
        result.update({"basket": basket, "amendDecision": None, "acceptedSubstitutes": [], "substitutes": []})
    unavailable = mock.check_lines(basket)
    result.update({"allAvailable": not unavailable, "unavailableItems": unavailable})
    info(job, f"{len(basket)} lines, {len(unavailable)} unavailable")
    return result


@router.task(task_type="reserve-stock")
async def reserve_stock(job: Job) -> dict:
    if mock.stock_service_down():
        service_failure(job, "STOCK_SERVICE_UNAVAILABLE", "stock service")
    taken = mock.taken_lines(job.variables.get("basket") or [])
    if taken:
        # error variables stay on the catch event (no output mapping), so find-substitutes reads them from here
        _stock_taken[job.process_instance_key] = taken
        info(job, f"{len(taken)} lines taken by another customer, BPMN error INSUFFICIENT_STOCK")
        raise BusinessError("INSUFFICIENT_STOCK")
    expires = mock.now() + mock.timedelta(minutes=mock.HOLD_MINUTES)
    reminder = expires - mock.timedelta(minutes=mock.REMINDER_MINUTES_BEFORE)
    reservation_id = mock.new_id("RES")
    info(job, f"{reservation_id} held until {mock.iso(expires)}")
    return {"reservationId": reservation_id, "reservationExpiresAt": mock.iso(expires),
            "reservationReminderAt": mock.iso(reminder)}


@router.task(task_type="find-substitutes")
async def find_substitutes(job: Job) -> dict:
    unavailable = _stock_taken.pop(job.process_instance_key, None) or job.variables.get("unavailableItems") or []
    substitutes = mock.substitutes_for(unavailable)
    info(job, f"{len(unavailable)} unavailable lines, {len(substitutes)} substitutes found")
    return {"unavailableItems": unavailable, "substitutes": substitutes}


@router.task(task_type="identify-producers")
async def identify_producers(job: Job) -> dict:
    basket = job.variables.get("basket") or []
    producers = OrderedDict()
    for line in basket:
        product = mock.CATALOGUE[line["productId"]]
        producers.setdefault(product["producerId"], {"producerId": product["producerId"],
                                                     "producerName": product["producerName"]})
    in_basket = {line["productId"] for line in basket}
    suggestions = [p["productName"] for pid, p in mock.CATALOGUE.items()
                   if p["producerId"] in producers and pid not in in_basket and p["stock"] > 0][:3]
    info(job, f"{len(producers)} producers: {', '.join(p['producerName'] for p in producers.values())}")
    return {"producers": list(producers.values()), "addOnSuggestions": suggestions}


@router.task(task_type="determine-arrangements")
async def determine_arrangements(job: Job) -> dict:
    v = job.variables
    earliest = mock.iso(mock.now() + mock.timedelta(hours=mock.ARRANGEMENT_LEAD_HOURS))
    method = "delivery" if v.get("postcode") else "collection"
    arrangements = [{"producerId": p["producerId"], "producerName": p["producerName"], "method": method,
                     "earliestDate": earliest} for p in v.get("producers") or []]
    info(job, f"{method} for {len(arrangements)} producers, earliest {earliest}")
    return {"arrangements": arrangements}


@router.task(task_type="calculate-food-miles")
async def calculate_food_miles(job: Job) -> dict:
    v = job.variables
    postcode = v.get("postcode")
    if not postcode:
        info(job, "no postcode, food miles left out")
        return {}
    miles = mock.food_miles(postcode, [p["producerId"] for p in v.get("producers") or []])
    info(job, f"{miles} miles from {postcode}")
    return {"foodMiles": miles}


@router.task(task_type="calculate-order-total")
async def calculate_order_total(job: Job) -> dict:
    lines, total = [], mock.money(0)
    for line in job.variables.get("basket") or []:
        product = mock.CATALOGUE[line["productId"]]
        line_total = mock.money(mock.money(product["unitPrice"]) * line["quantity"])
        if product["surplus"]:
            line_total = mock.money(line_total * (1 - mock.SURPLUS_DISCOUNT))
        total += line_total
        lines.append({"productId": line["productId"], "productName": product["productName"],
                      "producerId": product["producerId"], "producerName": product["producerName"],
                      "quantity": line["quantity"], "lineTotal": float(line_total)})
    info(job, f"{len(lines)} lines, total {total}")
    return {"orderLines": lines, "orderTotal": float(total)}


@router.task(task_type="create-order")
async def create_order(job: Job) -> dict:
    order_id = mock.new_id("ORD")
    info(job, f"order {order_id} created")
    return {"orderId": order_id}


@router.task(task_type="split-order")
async def split_order(job: Job) -> dict:
    v = job.variables
    subtotals = OrderedDict()
    for line in v.get("orderLines") or []:
        subtotals[line["producerId"]] = subtotals.get(line["producerId"], mock.money(0)) + mock.money(line["lineTotal"])
    producer_orders = [{"producerOrderId": f"{v['orderId']}-P{n}", "producerId": pid, "subtotal": float(amount)}
                       for n, (pid, amount) in enumerate(subtotals.items(), start=1)]
    info(job, f"{len(producer_orders)} producer orders: "
              + ", ".join(f"{p['producerId']} {p['subtotal']:.2f}" for p in producer_orders))
    return {"producerOrders": producer_orders}


# shared by FN1 and FN2

@router.task(task_type="release-stock")
async def release_stock(job: Job) -> dict:
    info(job, f"reservation {job.variables.get('reservationId')} released")
    return {}


@router.task(task_type="notify-customer")
async def notify_customer(job: Job) -> dict:
    v = job.variables
    if job.element_id == "Task_SendReminder":
        text = f"reminder: items reserved until {v.get('reservationExpiresAt')}"
    elif job.element_id == "Task_TellCustomerUnavailable":
        text = "checkout is not available now, please try again later"
    else:
        text = f"order {v.get('orderId')} cancelled, reason {v.get('paymentStatus')}"
    info(job, f"to customer {v.get('customerId')}: {text}")
    return {}


# FN2 Process payment

async def _answer_later(order_id: str, result: str, reference: str) -> None:
    await asyncio.sleep(mock.PAYMENT_ANSWER_DELAY_SECONDS)
    if result == "confirmed":
        name, variables = "payment-confirmed", {"paymentReference": reference}
    else:
        name, variables = "payment-declined", {"declineReason": "card_declined"}
    await _client.publish_message(name, correlation_key=order_id, variables=variables,
                                  time_to_live_in_milliseconds=120000, message_id=f"{name}-{reference}")
    log.info("%-15s %s | %-26s %s", "payment service", order_id, "message", f"{name} published ({reference})")


@router.task(task_type="submit-payment")
async def submit_payment(job: Job) -> dict:
    v = job.variables
    if mock.payment_service_down():
        service_failure(job, "PAYMENT_SERVICE_UNAVAILABLE", "payment service")
    order_id, method = v["orderId"], v.get("paymentMethod")
    result = mock.payment_result(method)
    if result == "unavailable":
        # the request does not reach the service, so no attempt is recorded and nothing is refunded
        service_failure(job, "PAYMENT_SERVICE_UNAVAILABLE", "payment service")
    reference = mock.new_id("pi_mock")
    payment_attempts.append({"orderId": order_id, "paymentMethod": method, "amount": v.get("orderTotal"),
                             "reference": reference, "result": result})
    if result == "no_answer":
        # the service accepts the request and sends no message, so the 5-minute timer fires
        info(job, f"{v.get('orderTotal')} GBP with {method}, accepted, no answer will come")
        return {"lastPaymentAttempt": reference}
    # the sandbox answers later, like a webhook
    task = asyncio.create_task(_answer_later(order_id, result, reference))
    _background.add(task)
    task.add_done_callback(_background.discard)
    info(job, f"{v.get('orderTotal')} GBP with {method}, answer in {mock.PAYMENT_ANSWER_DELAY_SECONDS:g}s: {result}")
    return {"lastPaymentAttempt": reference}


@router.task(task_type="refund-payment")
async def refund_payment(job: Job) -> dict:
    reference = job.variables.get("paymentReference")
    status = "REFUNDED" if reference else "NOTHING_TO_REFUND"
    info(job, f"compensation: {status} {reference or ''}")
    return {"refundStatus": status}


@router.task(task_type="confirm-order")
async def confirm_order(job: Job) -> dict:
    info(job, f"order {job.variables.get('orderId')} confirmed, confirmation sent to the customer")
    return {"orderStatus": "CONFIRMED"}


@router.task(task_type="update-stock")
async def update_stock(job: Job) -> dict:
    if mock.stock_update_fails():
        service_failure(job, "STOCK_UPDATE_FAILED", "stock update")
    info(job, f"reservation {job.variables.get('reservationId')} turned into a sale")
    return {}


@router.task(task_type="record-stock-discrepancy")
async def record_stock_discrepancy(job: Job) -> dict:
    info(job, f"stock discrepancy recorded for order {job.variables.get('orderId')}")
    return {}


@router.task(task_type="notify-producer")
async def notify_producer(job: Job) -> dict:
    producer_order = job.variables.get("producerOrder") or {}
    if mock.notification_fails_for(producer_order.get("producerId")):
        service_failure(job, "NOTIFICATION_FAILED", "notification service")
    info(job, f"producer {producer_order.get('producerId')} notified of {producer_order.get('producerOrderId')}")
    return {}


@router.task(task_type="record-failed-notification")
async def record_failed_notification(job: Job) -> dict:
    producer_order = job.variables.get("producerOrder") or {}
    info(job, f"failed notification recorded for {producer_order.get('producerOrderId')}")
    return {}


@router.task(task_type="record-payment")
async def record_payment(job: Job) -> dict:
    v = job.variables
    split = v.get("paymentSplit") or {}
    info(job, f"payment {v.get('paymentReference')} recorded, commission {split.get('commission')}")
    return {"settlementRecordId": mock.new_id("SET")}


@router.task(task_type="cancel-order")
async def cancel_order(job: Job) -> dict:
    info(job, f"order {job.variables.get('orderId')} cancelled, reason {job.variables.get('paymentStatus')}")
    return {"orderStatus": "CANCELLED"}
