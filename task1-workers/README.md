# Task 1 job workers

**Task:** 6.1 Make the FN1 and FN2 diagrams executable in Camunda (parts a, d, e and f)
**Status:** draft. The job workers and the mock services are complete for all paths of FN1 and FN2. The test runs are in [test-runs.md](test-runs.md).

## 1. Purpose

This folder contains the Python job workers of the two executable processes:

- FN1 Process order (`process_order`), [process-order.md](../task1-bpmn/operational/process-order.md)
- FN2 Process payment (`process_payment`), [process-payment.md](../task1-bpmn/operational/process-payment.md)

Each worker completes the jobs of one job type. The job types and the variables come from section 8 of each design document. The workers call mock services. They call no real service and use no card data (NFR03).

The folder is outside `task1-bpmn/`, because Camunda reads each `.json` file in the synced folder.

## 2. Who does each activity

| Actor | Activities | Where to see it |
|---|---|---|
| The customer | The user tasks, with the Camunda Forms | Tasklist |
| The process engine | The gateways, the timers, the message events, the compensation and the FEEL script of FN2 | Operate |
| The job workers (this folder) | The service, send and business rule tasks | The worker console and Operate |
| The mock services | The stock service, the postcode distance service, the payment service and the notification service | The worker console |

## 3. Files

| File | Content |
|---|---|
| `handlers.py` | One handler for each of the 20 job types |
| `mock_services.py` | The mock catalogue (5 products, 3 producers) and the mock services |
| `worker.py` | Runs all the handlers until you press Ctrl+C |
| `deploy.py` | Deploys both processes and their four forms in one deployment |
| `start.py` | Starts a test instance of either process |
| `check.py` | Offline checks. No cluster is necessary |
| `tests/test_workers.py` | Unit tests with pytest. No cluster is necessary |
| `requirements-dev.txt` | The packages for the unit tests |
| `connection.py` | The connection to the cluster, with the settings of `.env` |
| `.env.example` | The settings, with no secret values |
| `test-runs.md` | The record of each test run |

## 4. Set up

You need Python 3.12 and access to the Camunda 8 cluster of the module.

1. Create an API client for the cluster. In Camunda Console, open **Clusters**, then the module cluster, then **API**. Select **Create new client** and the scope **Zeebe**. Keep the client secret. Console shows it only once.
2. Install the packages:

   ```
   cd task1-workers
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env`. Paste the values of the API client. Set `CUSTOMER_ID` to your Camunda login.
4. Run the offline checks: `python check.py`. All checks must pass.
5. Run the unit tests: `pip install -r requirements-dev.txt`, then `python -m pytest`. All tests must pass.

Do not commit `.env`. The file `.gitignore` excludes it.

If you cannot create an API client, ask the tutor for one. Another option is a local Camunda 8 Run installation: set `ZEEBE_LOCAL=1` and `ZEEBE_ADDRESS=localhost:26500`.

## 5. Deploy

Use one of these two methods:

- **Web Modeler.** Sync the Camunda project with GitHub. Open each process and select **Deploy**. Make sure that the four forms are also deployed.
- **Script.** Run `git fetch`, then `python deploy.py`. The script takes the files from `origin/main` and deploys both processes and the four forms together. Until PR #186 is merged, use `python deploy.py --ref origin/6.1`, because the new options of the payment form are only on that branch.

## 6. Run the main path

1. Start the workers in one terminal: `python worker.py`. Keep this terminal open.
2. In a second terminal, start FN1: `python start.py order`.
3. In Tasklist, open "Review and confirm order". Check the order lines, the total and the food miles. Select **Confirm**.
4. In Operate, check that the instance ended at "Order awaiting payment". Take a screenshot.
5. Start FN2: `python start.py payment`.
6. In Tasklist, open "Give payment details". Select `pm_card_visa`.
7. After 3 seconds, the mock payment service publishes `payment-confirmed`. In Operate, check that the instance ended at "Order confirmed". Take a screenshot.
8. Record each run in [test-runs.md](test-runs.md).

FN1 does not start FN2. The start of FN2 is open question S2 (a call activity or a message). Until the group decides S2, start FN2 with `start.py`.

## 7. Other paths

| Path | How to start it |
|---|---|
| Unavailable item and amendment | `python start.py order --unavailable`. In "Amend order or cancel", accept "Dark rye loaf" and select **Amend** |
| No postcode, so no food miles | `python start.py order --no-postcode` |
| Payment declined | In "Give payment details", select `pm_card_chargeDeclined` |
| Payment service unavailable | In "Give payment details", select `pm_simulate_unavailable`. Another method: set `MOCK_PAYMENT_SERVICE_DOWN=1` in `.env` and start the workers again |
| No answer from the payment service | In "Give payment details", select `pm_simulate_no_answer`. The request completes, no message arrives, and the 5-minute timer fires |
| Stock service unavailable | Set `MOCK_STOCK_SERVICE_DOWN=1` |
| Stock taken by another customer after the check | Set `MOCK_STOCK_TAKEN=P-201` and start the workers again. "Reserve stock" throws `INSUFFICIENT_STOCK`, and the amend path starts |
| Stock update fails after the payment | Set `MOCK_STOCK_UPDATE_FAILS=1` |
| One producer notification fails | Set `MOCK_FAIL_NOTIFY_PRODUCER=PR-02` |

A mock service that is down fails the job until no retries remain. Then the worker throws the BPMN error of the model, for example `PAYMENT_SERVICE_UNAVAILABLE`.

## 8. Limits

- The stock levels of the mock catalogue do not change. A reservation does not reduce the stock.
- The workers do not cover `settle-producer-payments.bpmn` (task 5.5).
- `customerId` must be the login of a Tasklist user, because `process_payment` assigns its user tasks to `=customerId`.
- The retry counters `declineCount` and `unavailableCount` and the commission are FEEL in the diagram, not worker code. The unit tests check the commission rule against runs P1 and P8. Runs P2, P3, P5 and P6 check the counters on the cluster.

## 9. Job types

Each job type has one handler in `handlers.py`. `python -m pytest` checks that each job type of both diagrams has a handler.

| Job type | Process | Task | Reads | Sets | BPMN error |
|---|---|---|---|---|---|
| `check-stock` | FN1 | Check stock | `basket`, and after an amendment `amendDecision`, `unavailableItems`, `substitutes`, `acceptedSubstitutes` | `allAvailable`, `unavailableItems`, and after an amendment `basket` | `STOCK_SERVICE_UNAVAILABLE` |
| `reserve-stock` | FN1 | Reserve stock | `basket` | `reservationId`, `reservationExpiresAt`, `reservationReminderAt` | `INSUFFICIENT_STOCK`, `STOCK_SERVICE_UNAVAILABLE` |
| `find-substitutes` | FN1 | Find substitutes from other producers | `unavailableItems` | `unavailableItems`, `substitutes` | None |
| `identify-producers` | FN1 | Identify producers | `basket` | `producers`, `addOnSuggestions` | None |
| `determine-arrangements` | FN1 | Determine delivery or collection per producer | `producers`, `postcode` | `arrangements` | None |
| `calculate-food-miles` | FN1 | Calculate food miles | `postcode`, `producers` | `foodMiles`, only when there is a postcode | None |
| `calculate-order-total` | FN1 | Calculate order total with surplus discounts | `basket` | `orderLines`, `orderTotal` | None |
| `create-order` | FN1 | Create marketplace order | None | `orderId` | None |
| `split-order` | FN1 | Split into producer order elements | `orderId`, `orderLines` | `producerOrders` | None |
| `release-stock` | FN1, FN2 | Release stock | `reservationId` | None | None |
| `notify-customer` | FN1, FN2 | Send hold reminder, Tell customer that checkout is unavailable, Tell the customer | `customerId`, `reservationExpiresAt`, `orderId`, `paymentStatus` | None | None |
| `submit-payment` | FN2 | Send payment request | `orderId`, `paymentMethod`, `orderTotal` | `lastPaymentAttempt`. The mock then publishes `payment-confirmed` (with `paymentReference`) or `payment-declined`, with `orderId` as the correlation key | `PAYMENT_SERVICE_UNAVAILABLE` |
| `refund-payment` | FN2 | Refund payment (compensation) | `paymentReference` | `refundStatus` | None |
| `confirm-order` | FN2 | Confirm order | `orderId` | `orderStatus` | None |
| `update-stock` | FN2 | Update stock | `reservationId` | None | `STOCK_UPDATE_FAILED` |
| `record-stock-discrepancy` | FN2 | Record stock discrepancy | `orderId` | None | None |
| `notify-producer` | FN2 | Notify producer | `producerOrder` | None | `NOTIFICATION_FAILED` |
| `record-failed-notification` | FN2 | Record failed notification | `producerOrder` | None | None |
| `record-payment` | FN2 | Record payment for settlement | `paymentReference`, `paymentSplit` | `settlementRecordId` | None |
| `cancel-order` | FN2 | Cancel order | `orderId`, `paymentStatus` | `orderStatus` | None |
