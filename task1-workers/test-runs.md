# Test runs

**Task:** 6.1 ([#171](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/171)), part f. The FN1 runs are for 6.2 ([#174](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/174)), and the FN2 runs are for 6.3 ([#175](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/175))

Each run records the path, the input, the result, the process instance key and an Operate screenshot. The screenshots are in [screenshots/](screenshots/). `Pn.png` shows the instance in Operate, and `Pn-test.png` shows the same run in the Test mode of the Web Modeler.

## FN1 Process order (`process_order`)

**Task:** 6.2 ([#174](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/174)). **Tester:** Ishaq Modassir Mushtaq.

### Method

The runs used version 8 of `process_order`, deployed on 27 Nov 2026 with `python deploy.py --ref origin/6.1` to the module cluster (UWE Frenchay 2026, dev). Version 8 has the fixes of 5.3 ([#172](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/172)): the review form shows the delivery or collection and the earliest date of each producer, and the "Add items" loop is removed.

In each run:

- `python worker.py` ran the job workers and the mock stock and postcode services. A mock switch was set in front of the command for the run that needed it, for example `MOCK_STOCK_TAKEN=P-201 python worker.py`.
- `python start.py order` started the instance, with `--unavailable` (adds the Rye loaf, which has no stock) or `--no-postcode` where the path needs it.
- The tester completed the user tasks in Tasklist as the customer (`CUSTOMER_ID`).
- `On.png` shows the instance in Operate (history and variables). `On-test.png` shows the path that the instance took in the diagram.

The default basket is 2 x P-101 Organic carrots, 1 x P-102 Free-range eggs and 1 x P-201 Sourdough loaf, with the postcode BS16 1QY. The total is 4.80 + 3.20 + 4.05 = 12.05, because the sourdough is surplus produce with a 10% discount (4.50 less 0.45).

### Runs

| Run | Path | Input | Steps | Result | Process instance key | Status | Screenshots |
|---|---|---|---|---|---|---|---|
| O1 | Main path: all items in stock, the customer confirms | `start.py order` | Review: "Confirm the order and go to payment" | "Order awaiting payment". `orderTotal` = 12.05, `foodMiles` = 30, `orderId` = ORD-298596B9. `arrangements`: Valley Farm and Harbourside Bakery, delivery, earliest date 48 hours after the order | 2251799869565861 | Passed | [O1](screenshots/O1.png), [path](screenshots/O1-test.png) |
| O2 | An item is unavailable, the customer amends with a substitute | `start.py order --unavailable` | Amend: tick "Dark rye loaf from Mill Lane Bakery", "Amend". Review: "Confirm" | "Find substitutes" offered P-301 for P-202. "Check stock" ran again with the amended basket, and all items were available. "Order awaiting payment". `orderTotal` = 15.95 (12.05 + 3.90), `foodMiles` = 41, `orderId` = ORD-18B65130 | 4503599682758972 | Passed | [O2](screenshots/O2.png), [path](screenshots/O2-test.png) |
| O3 | An item is unavailable, the customer cancels | `start.py order --unavailable` | Amend: "Cancel" | "Amend or cancel?" (Cancel), "Stock held?" (No, the stock was never reserved), "Order ended before reservation". `amendDecision` = cancel | 6755399496442330 | Passed | [O3](screenshots/O3.png), [path](screenshots/O3-test.png) |
| O4 | The customer cancels at the review | `start.py order` | Review: "Cancel the order" | "Customer decision?" (default), "Release stock reservation", "Order not placed" | 6755399496443359 | Passed | [O4](screenshots/O4.png), [path](screenshots/O4-test.png) |
| O5 | No postcode, so no food miles | `start.py order --no-postcode` | Review: "Confirm" | No `foodMiles` variable, and the review form hides the food miles. `arrangements` method = collection. "Order awaiting payment". `producerOrders`: 8.00 (Valley Farm) and 4.05 (Harbourside Bakery), total 12.05 | 2251799869574116 | Passed | [O5](screenshots/O5.png), [path](screenshots/O5-test.png) |
| O6 | The stock hold expires at the review | `HOLD_MINUTES=3 REMINDER_MINUTES_BEFORE=1 python worker.py`, then `start.py order` | Review: no action | After 2 minutes "Hold about to expire" (non-interrupting), "Send hold reminder", "Reminder sent". After 3 minutes "Stock hold expired" interrupted the review, then "Release stock reservation" and "Order not placed". Start 17:11:20, end 17:14:21, `reservationExpiresAt` = 17:14:21 | 6755399496451358 | Passed | [O6](screenshots/O6.png), [path](screenshots/O6-test.png) |
| O7 | Another customer takes the stock after the check | `MOCK_STOCK_TAKEN=P-201 python worker.py`, then `start.py order` | Amend: "Amend" (no substitute for the sourdough). Review: "Confirm" | "All items available?" (Yes), then "Reserve stock" threw `INSUFFICIENT_STOCK` and "Stock taken by another customer" caught it. "Find substitutes" found 0 substitutes for the sourdough. After "Amend", "Check stock" and "Reserve stock" ran again without the sourdough and succeeded. `orderTotal` = 8.00, 1 producer (Valley Farm), `foodMiles` = 27, `orderId` = ORD-FE298F5B. A first attempt (2251799869584123) was not valid, because another worker on the cluster completed some of its `check-stock` jobs (see Known issues) | 6755399496465271 | Passed | [O7](screenshots/O7.png), [path](screenshots/O7-test.png), [worker log of the first attempt](screenshots/insufficiant%20_stock_error.png) |
| O8 | The stock service is unavailable | `MOCK_STOCK_SERVICE_DOWN=1 python worker.py`, then `start.py order` | None | "Check stock" failed until no retries remained, and the worker threw `STOCK_SERVICE_UNAVAILABLE`. The event sub-process "Stock service unavailable" ran "Tell customer that checkout is unavailable" and ended at "Checkout failed", 1 second after the start. No reservation and no `orderId`. A first attempt (6755399496456546) was not valid, because another worker on the cluster completed its `check-stock` jobs | 2251799869599606 | Passed | [O8](screenshots/O8.png), [path](screenshots/O8-test.png) |
| O9 | The amend time limit passes | `start.py order --unavailable` | Amend: no action for 30 minutes | "Amend time limit reached" (interrupting) after exactly 30 minutes, "Stock held?" (No), "Order ended before reservation". Start 16:20:46, end 16:50:46 | 4503599682758231 | Passed | [O9](screenshots/O9.png), [path](screenshots/O9-test.png) |

An earlier run of the main path on version 7 (2251799869555424) found that the review form and `arrangements` gave two different earliest dates. Version 8 fixes this. The "Add items at the review" path was removed with the loop in version 8, so it has no run.

### Checks

- [x] Each user task shows its Camunda Form, and each decision on the Form takes the expected path (O1 to O4, O9)
- [x] The amendment changes the basket: the unavailable line is removed, and the accepted substitute is added (O2, O7)
- [x] A stock service failure ends the checkout in the event sub-process, with no reservation and no order (O8)
- [x] Each path that holds stock and does not continue to payment releases the reservation (O4, O6)
- [x] The three timers fire at the expected times: the reminder, the stock hold expiry and the amend time limit (O6, O9)
- [x] The order total includes the surplus discount, and the producer subtotals add up to the order total (O1, O5)
- [x] O7 and O8 again, with no other worker on the cluster (the second attempts)
- [ ] An amendment that leaves the basket empty. Known issue: the process continues with an empty order. The model needs a gateway "Anything left to order?" (5.3, #172)

### Known issues

- **Other workers on the cluster.** The job types (for example `check-stock`) are shared by every worker on the module cluster. A worker of another group, or another version of this code, can complete the jobs of this process. Before a test run or the demonstration, make sure that only the workers of this repository run, or give the job types a unique prefix.
- **Empty basket after an amendment.** See the checks above.
- **Part quantities.** When fewer items are in stock than requested, the whole line is removed. The customer cannot take the part that is in stock.

## FN2 Process payment (`process_payment`)

### Method

The runs used the Test mode of the Web Modeler on the module cluster (UWE Frenchay 2026, dev, Camunda 8.9), on 20 and 21 Nov 2026. Test mode deploys the process to the cluster and starts real process instances, so each run has a process instance key and shows in Operate.

The job workers and the mock payment service of 6.3 did not exist yet. Thus, in each run:

- The member completed each service task and the send task by hand in Test mode. Each one stands for a worker. In P5 the member threw the BPMN error `PAYMENT_SERVICE_UNAVAILABLE` from "Send payment request", as the `submit-payment` worker will.
- The member published the messages `payment-confirmed` and `payment-declined` by hand, with `orderId` as the correlation key. This stands for the mock payment service (section 8 of [process-payment.md](../task1-bpmn/operational/process-payment.md)).
- The engine ran the rest: the script task "Calculate producer amounts and commission", the gateways, the counters `declineCount` and `unavailableCount`, the timers, the event sub-process, the compensation and the Forms.

Each run is saved as a test case of the Test mode, in [process-payment tests.json](../task1-bpmn/operational/process-payment%20tests.json). The group can run each one again in the Web Modeler.

When the workers and the mock exist, run each path again with them and add the new process instance keys to this file.

### Start variables

Each run has its own `orderId`, because the messages correlate on `orderId`. P1 to P7 use these variables with their own `orderId` and `producerOrderId` values:

```json
{
  "orderId": "ORD-1042",
  "customerId": "royden",
  "orderTotal": 48.60,
  "producerOrders": [
    { "producerOrderId": "ORD-1042-P1", "producerId": "PR-01", "subtotal": 30.00 },
    { "producerOrderId": "ORD-1042-P2", "producerId": "PR-02", "subtotal": 18.60 }
  ],
  "reservationExpiresAt": "2026-11-20T23:30:00Z"
}
```

`reservationExpiresAt` must be in the future when the instance starts. If it has passed, the event sub-process "Handle reservation expiry" starts at once. P7 set it to 4 minutes after the start.

P8 checks the rounding of the commission, with three producers:

```json
{
  "orderId": "ORD-1050",
  "customerId": "royden",
  "orderTotal": 25.44,
  "producerOrders": [
    { "producerOrderId": "ORD-1050-P1", "producerId": "PR-01", "subtotal": 12.35 },
    { "producerOrderId": "ORD-1050-P2", "producerId": "PR-02", "subtotal": 8.10 },
    { "producerOrderId": "ORD-1050-P3", "producerId": "PR-03", "subtotal": 4.99 }
  ],
  "reservationExpiresAt": "2026-11-21T06:00:00Z"
}
```

### Runs

All 8 runs passed.

| Run | Path | Input | Steps | Result | Process instance key | Screenshots |
|---|---|---|---|---|---|---|
| P1 | Main path: the payment succeeds | ORD-1042 | Payment details: "the payment succeeds". `payment-confirmed` | "Order confirmed". `paymentStatus` = `SUCCEEDED`. `paymentSplit`: 28.50 and 17.67, commission 2.43. "Notify each producer" ran 2 times. The message carried no payload, so `paymentReference` (`pi_test_1042`) was set by hand. The later runs sent it with the message | 2251799868174390 | [P1](screenshots/P1.png), [Test mode](screenshots/P1-test.png) |
| P2 | Decline, retry, then success | ORD-1043 | "Declined". `payment-declined`. Retry or cancel (the Form shows 1 of 3): "Try again". "Succeeds". `payment-confirmed` with `paymentReference` = `pi_test_1043` | "Order confirmed". `paymentStatus` = `SUCCEEDED`, `retryChoice` = `RETRY` | 4503599681698253 | [P2](screenshots/P2.png), [Test mode](screenshots/P2-test.png) |
| P3 | Decline limit | ORD-1045 | "Declined" 3 times, with "Try again" after the first 2 (the Form shows 1 of 3, then 2 of 3) | No retry Form after the third decline. "Decline limit reached", then "Release stock", "Cancel order", "Tell the customer" and "Order cancelled". `paymentStatus` = `DECLINED` | 2251799868183218 | [P3](screenshots/P3.png), [Test mode](screenshots/P3-test.png) |
| P4 | The customer cancels | ORD-1044 | "Declined". Retry or cancel: "Cancel the order" | "Customer cancelled", then "Release stock", "Cancel order", "Tell the customer" and "Order cancelled". `paymentStatus` = `DECLINED`, `retryChoice` = `CANCEL` | 6755399495382192 | [P4](screenshots/P4.png), [Test mode](screenshots/P4-test.png) |
| P5 | Payment service unavailable | ORD-1046 | "The payment service is unavailable". "Send payment request" throws `PAYMENT_SERVICE_UNAVAILABLE` 2 times, with the 1-minute wait between them | "Try again?" took Yes, then No. "Service unavailable", then "Order cancelled". `paymentStatus` = `SERVICE_UNAVAILABLE`. "Refund payment" did not run, because no request reached the service | 4503599681733486 | [P5](screenshots/P5.png), [Test mode](screenshots/P5-test.png) |
| P6 | No answer | ORD-1047 | "The payment service does not answer". "Send payment request" completes 2 times, and no message arrives | "No answer in 5 minutes" fired 2 times, with the 1-minute wait between them. "Service unavailable", then "Refund payment" 2 times (compensation of the 2 requests) and "Order cancelled". `paymentStatus` = `SERVICE_UNAVAILABLE` | 2251799868236273 | [P6](screenshots/P6.png), [Test mode](screenshots/P6-test.png) |
| P7 | Reservation expires | ORD-1048 | "Succeeds". "Send payment request" completes. No message. `reservationExpiresAt` = 4 minutes after the start | At the expiry time "Reservation expired" interrupted "Take payment". "Refund any payment taken" started the compensation, and "Refund payment" ran once for the request. Then "Payment stopped" and "Order cancelled". `paymentStatus` = `RESERVATION_EXPIRED` | 6755399495419270 | [P7](screenshots/P7.png), [Test mode](screenshots/P7-test.png) |
| P8 | Commission rounding | ORD-1050 | "Succeeds". `payment-confirmed` with `paymentReference` = `pi_test_1050` | "Order confirmed". `paymentSplit`: 11.73, 7.70 (8.10 x 0.95 = 7.695, rounded half up) and 4.74, commission 1.27. "Notify each producer" ran 3 times | 4503599681735188 | [P8](screenshots/P8.png), [Test mode](screenshots/P8-test.png) |

### Checks

- [x] The producer amounts and the commission add up to `orderTotal`: 28.50 + 17.67 + 2.43 = 48.60 (P1, P2) and 11.73 + 7.70 + 4.74 + 1.27 = 25.44 (P8)
- [x] The decline counter: the Form shows 1 of 3 and 2 of 3, and the third decline ends the loop (P2, P3)
- [x] The unavailable counter: the first failure leads to a new attempt after 1 minute, and the second ends the loop (P5, P6)
- [x] Compensation refunds only the requests that reached the service: none in P5, 2 in P6 and 1 in P7
- [x] The four sandbox methods of the Form `payment-details` reach the process as `paymentMethod`
- [x] No Form and no process variable holds a card number or a card security code. `paymentMethod` holds only a sandbox method ID (NFR03)
- [ ] The job types in Operate agree with section 8 of `process-payment.md` (after the workers exist)
- [ ] The runs with the workers and the mock payment service (6.3)
