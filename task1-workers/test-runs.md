# Test runs

**Task:** 6.1 ([#171](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/171)), part f. The FN2 runs are for 6.3 ([#175](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/175))

Each run records the path, the input, the result, the process instance key and an Operate screenshot. The screenshots are in [screenshots/](screenshots/). `Pn.png` shows the instance in Operate, and `Pn-test.png` shows the same run in the Test mode of the Web Modeler.

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
