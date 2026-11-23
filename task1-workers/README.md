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
| Stock update fails after the payment | Set `MOCK_STOCK_UPDATE_FAILS=1` |
| One producer notification fails | Set `MOCK_FAIL_NOTIFY_PRODUCER=PR-02` |

A mock service that is down fails the job until no retries remain. Then the worker throws the BPMN error of the model, for example `PAYMENT_SERVICE_UNAVAILABLE`.

## 8. Limits

- The stock levels of the mock catalogue do not change. A reservation does not reduce the stock.
- The workers do not cover `settle-producer-payments.bpmn` (task 5.5).
- `customerId` must be the login of a Tasklist user, because `process_payment` assigns its user tasks to `=customerId`.
