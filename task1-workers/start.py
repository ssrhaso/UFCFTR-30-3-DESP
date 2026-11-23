"""Start a test instance of process_order or process_payment.

    python start.py order                  main path, three items, all in stock
    python start.py order --unavailable    adds the Rye loaf, which has no stock (amend path)
    python start.py order --no-postcode    no postcode, so no food miles
    python start.py payment                FN2 with the example order of process-payment.md
"""

import argparse
import asyncio
import json
import os

from pyzeebe import ZeebeClient

import mock_services as mock
from connection import create_channel

PAYMENT_HOLD_MINUTES = 30


def order_variables(args) -> dict:
    basket = [{"productId": "P-101", "quantity": 2}, {"productId": "P-102", "quantity": 1},
              {"productId": "P-201", "quantity": 1}]
    if args.unavailable:
        basket.append({"productId": "P-202", "quantity": 1})
    variables = {"customerId": os.getenv("CUSTOMER_ID") or "customer-demo", "basket": basket}
    if not args.no_postcode:
        variables["postcode"] = "BS16 1QY"
    return variables


def payment_variables() -> dict:
    customer = os.getenv("CUSTOMER_ID")
    if not customer:
        raise SystemExit("Set CUSTOMER_ID in .env to the Tasklist user who plays the customer. "
                         "The two user tasks of process_payment are assigned to this user.")
    order_id = mock.new_id("ORD")
    return {
        "orderId": order_id,
        "customerId": customer,
        "orderTotal": 48.60,
        "producerOrders": [
            {"producerOrderId": f"{order_id}-P1", "producerId": "PR-01", "subtotal": 30.00},
            {"producerOrderId": f"{order_id}-P2", "producerId": "PR-02", "subtotal": 18.60},
        ],
        # must be in the future, or the expiry event sub-process stops the payment at once
        "reservationExpiresAt": mock.iso(mock.now() + mock.timedelta(minutes=PAYMENT_HOLD_MINUTES)),
    }


async def main(args) -> None:
    if args.process == "order":
        process_id, variables = "process_order", order_variables(args)
    else:
        process_id, variables = "process_payment", payment_variables()
    client = ZeebeClient(create_channel())
    response = await client.run_process(process_id, variables=variables)
    print(f"Started {process_id}, process instance key {response.process_instance_key}")
    print(json.dumps(variables, indent=2))
    print("Follow it in Operate. Complete the user tasks in Tasklist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("process", choices=["order", "payment"])
    parser.add_argument("--unavailable", action="store_true", help="order: add an item with no stock")
    parser.add_argument("--no-postcode", action="store_true", help="order: leave out the postcode")
    asyncio.run(main(parser.parse_args()))
