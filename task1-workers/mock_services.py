"""Mock external services for the Task 1 job workers.

The stock service, the postcode distance service, the payment service and the
notification service are simulated here. No real service is called and no card
data is used (NFR03).
"""

import hashlib
import os
import uuid
from datetime import datetime, timedelta, timezone
from decimal import ROUND_HALF_UP, Decimal

from dotenv import load_dotenv

load_dotenv()

# mock catalogue: productId -> product. "stock" is the quantity the stock service reports.
CATALOGUE = {
    "P-101": {"productName": "Organic carrots (1 kg)", "producerId": "PR-01", "producerName": "Valley Farm",
              "unitPrice": 2.40, "stock": 40, "surplus": False, "category": "carrots"},
    "P-102": {"productName": "Free-range eggs (6)", "producerId": "PR-01", "producerName": "Valley Farm",
              "unitPrice": 3.20, "stock": 25, "surplus": False, "category": "eggs"},
    "P-201": {"productName": "Sourdough loaf", "producerId": "PR-02", "producerName": "Harbourside Bakery",
              "unitPrice": 4.50, "stock": 12, "surplus": True, "category": "bread"},
    "P-202": {"productName": "Rye loaf", "producerId": "PR-02", "producerName": "Harbourside Bakery",
              "unitPrice": 4.20, "stock": 0, "surplus": False, "category": "rye"},
    "P-301": {"productName": "Dark rye loaf", "producerId": "PR-03", "producerName": "Mill Lane Bakery",
              "unitPrice": 3.90, "stock": 20, "surplus": False, "category": "rye"},
}

SURPLUS_DISCOUNT = Decimal("0.10")  # mock rate for R15
HOLD_MINUTES = int(os.getenv("HOLD_MINUTES", "15"))
REMINDER_MINUTES_BEFORE = int(os.getenv("REMINDER_MINUTES_BEFORE", "5"))
ARRANGEMENT_LEAD_HOURS = 48  # NFR07
PAYMENT_ANSWER_DELAY_SECONDS = float(os.getenv("PAYMENT_ANSWER_DELAY_SECONDS", "3"))

# sandbox payment method ids from the form payment-details (process-payment.md, section 8)
PAYMENT_RESULTS = {"pm_card_visa": "confirmed", "pm_card_chargeDeclined": "declined",
                   "pm_simulate_unavailable": "unavailable", "pm_simulate_no_answer": "no_answer"}


def money(value) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def iso(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def now() -> datetime:
    return datetime.now(timezone.utc)


def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"


def flag(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in ("1", "true", "yes", "down")


# stock service

def stock_service_down() -> bool:
    return flag("MOCK_STOCK_SERVICE_DOWN")


def check_lines(basket: list) -> list:
    """Return the unavailable lines of the basket."""
    unavailable = []
    for line in basket:
        product = CATALOGUE[line["productId"]]
        if product["stock"] < line["quantity"]:
            unavailable.append({
                "productId": line["productId"],
                "productName": product["productName"],
                "producerName": product["producerName"],
                "requestedQuantity": line["quantity"],
                "availableQuantity": product["stock"],
            })
    return unavailable


def taken_lines(basket: list) -> list:
    """Return the lines that another customer took after the stock check (MOCK_STOCK_TAKEN)."""
    taken = {pid.strip() for pid in os.getenv("MOCK_STOCK_TAKEN", "").split(",") if pid.strip()}
    return [{"productId": line["productId"], "productName": CATALOGUE[line["productId"]]["productName"],
             "producerName": CATALOGUE[line["productId"]]["producerName"],
             "requestedQuantity": line["quantity"], "availableQuantity": 0}
            for line in basket if line["productId"] in taken]


def substitutes_for(unavailable: list) -> list:
    found = []
    for item in unavailable:
        wanted = CATALOGUE[item["productId"]]
        for product_id, product in CATALOGUE.items():
            if (product["category"] == wanted["category"] and product["producerId"] != wanted["producerId"]
                    and product["stock"] >= item["requestedQuantity"]):
                found.append({"productId": product_id, "productName": product["productName"],
                              "producerName": product["producerName"], "unitPrice": product["unitPrice"],
                              "replaces": item["productId"], "quantity": item["requestedQuantity"]})
    return found


def amend_basket(basket: list, unavailable: list, substitutes: list, accepted: list) -> list:
    """Remove the unavailable lines and add the substitutes that the customer accepted."""
    removed = {item["productId"] for item in unavailable}
    amended = [line for line in basket if line["productId"] not in removed]
    for sub in substitutes:
        if sub["productId"] in accepted:
            amended.append({"productId": sub["productId"], "quantity": sub["quantity"]})
    return amended


# postcode distance service

def food_miles(postcode: str, producer_ids: list) -> float:
    total = 0
    for producer_id in producer_ids:
        digest = hashlib.sha256(f"{postcode}|{producer_id}".encode()).digest()
        total += 3 + digest[0] % 25  # 3 to 27 miles for each producer
    return float(total)


# payment service

def payment_service_down() -> bool:
    return flag("MOCK_PAYMENT_SERVICE_DOWN")


def payment_result(payment_method: str) -> str:
    return PAYMENT_RESULTS.get(payment_method, "declined")


# notification service and stock update

def notification_fails_for(producer_id: str) -> bool:
    return producer_id and producer_id == os.getenv("MOCK_FAIL_NOTIFY_PRODUCER", "").strip()


def stock_update_fails() -> bool:
    return flag("MOCK_STOCK_UPDATE_FAILS")
