# Traceability: Use Case 2 to the models

**Task:** 4.5 ([#152](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/152)) fills the i* columns. 5.1 fills the operational BPMN column, and 6.1 fills the Camunda column. 7.5 checks the table before the Sprint 2 Review.
**Status:** draft for review.

## 1. Purpose

This table links each sentence of Use Case 2 (U2 to U12) to the stories and the models. It covers the strategic BPMN model, the i* models, the operational BPMN models and the Camunda processes. The rows come from section 5 of [functionalities.md](scope/functionalities.md). U1 is the input of FN1, so the table starts at U2.

The brief asks for "strong traceability" along the chain from the i* models to the Camunda automation. The plan for Sprint 2 adds one column each week ([plan.md](../sprints/task1-sprint2/plan.md), section 5.1).

## 2. How to read the i* columns

- The **SD** column gives the dependencies that the row relies on: depender, dependum (type), dependee. A dependency records reliance. It is not a message flow, and it gives no timing (AlHaj Hassan, 2026, slide 12).
- The **SR** column gives the elements inside the actors, with the IDs of [model-content.md](../task1-bpmn/istar/model-content.md). "Chosen" and "rejected" mark the means of an OR-refinement. Only the chosen means has a BPMN element (AlHaj Hassan, 2026, slide 25).
- The **Tension** column gives the tensions of model-content.md section 6 that the row affects.

## 3. Table

| No. | UC2 text (shortened) | FN | Stories | Strategic BPMN | i* SD | i* SR | Tension | Operational BPMN (5.1) | Camunda (6.1) |
|---|---|---|---|---|---|---|---|---|---|
| U2 | The system checks that all products are available in the requested quantities | FN1 | B01, B07, B08, B21 | Process order (Orders lane). Order message from the Customer pool | SD03: Customer on Marketplace platform for Accurate availability (softgoal). SD12: Marketplace platform on Producer for Accurate stock levels (softgoal) | MP06 Check stock. MP12 Stock protected during checkout: MP13 Reserve stock for a time limit (chosen), MP14 Check stock only at payment (rejected). MP26 No oversell | TN2, TN3 | | |
| U3 | If an item is unavailable, the customer is told and asked to amend the order | FN1 | B02 | Process order (O01, O02) | SD08: Marketplace platform on Customer for Amend unavailable items (task) | MP07 Ask customer to amend order, CU08 Amend unavailable items. CU08 hurts CU13 Convenience | None | | |
| U4 | The system identifies the producers and the delivery or collection arrangements | FN1 | B03, B04 | Process order | SD13: Marketplace platform on Producer for Delivery or collection arrangements (resource). SD15: Producer on Marketplace platform for Adequate lead time (softgoal). SD05: Customer on Marketplace platform for Clear supplier responsibilities (softgoal) | MP08 Identify producers and arrangements, PR06 Set delivery or collection arrangements, PR13 Enough time to prepare | TN4, TN7 | | |
| U5 | The customer reviews the order and confirms the purchase | FN1 | B05 | Order message to Process order | SD07: Marketplace platform on Customer for Review and confirm order (task) | MP09 Get customer confirmation, CU07 Review and confirm order | None | | |
| U6 | The system creates the marketplace order and separates it into producer order elements | FN1 | B06 | Process order | SD01: Customer on Marketplace platform for Multi-vendor order processed (goal) | MP10 Create and split marketplace order. CU02 Buy through the marketplace helps CU15 Low supplier admin | TN7 | | |
| U7 | The payment goes to an external or simulated payment service | FN2 | B10, B20 | Process payment (Finance lane). Payment request and Payment response with the Payment service pool | SD22: Marketplace platform on Payment service for Payment processed (goal). SD09: Marketplace platform on Customer for Sandbox payment reference (resource). SD06: Customer on Marketplace platform for Secure payment (softgoal) | MP16 Submit payment, CU10 Give sandbox payment reference. MP16 helps MP30 Secure payment. CU10 helps CU17 Safe payment and personal data | TN6 | `process_payment`: user task "Give payment details" (form `payment-details`), service task "Submit payment" (`submit-payment`), message flows M05 and M06 | |
| U8 | On success, the order is confirmed, the stock is updated and the producers are notified | FN2 | B14, B15, B16, B23 | "Payment successful?" gateway, Update stock (Product listing lane), Notify producers (Orders lane). Order confirmation and New order notification messages | SD04: Customer on Marketplace platform for Order confirmation (resource). SD14: Producer on Marketplace platform for New order notification (resource). SD24: Marketplace platform on Notification service for Notifications delivered (goal) | MP18 Confirm order and update stock, MP19 Notify each producer. PR08 New order notification helps PR13 Enough time to prepare | TN4 | "Confirm order" (`confirm-order`), then in parallel "Update stock" (`update-stock`), multi-instance "Notify each producer" (`notify-producer`) and "Record payment for settlement" (`record-payment`) | |
| U9 | On a decline, the customer is told and can retry | FN2 | B11 | "Payment successful?" gateway (O03, O04) | **None. Gap R1:** no dependency links MP22 and CU11. Proposed: Marketplace platform on Customer for Retry or cancel after decline (task) | MP21 Declined payment handled: MP22 Let customer retry or cancel. CU11 Retry or cancel after decline. MP22 helps MP28 Reliable checkout | None | Error boundary event `PAYMENT_DECLINED`, gateway "Decline limit reached?", user task "Choose to retry or cancel" (form `retry-or-cancel`), gateway "Retry?" | |
| U10 | If the payment service is unavailable, an exception or retry path applies, not a simple termination | FN2 | B12, B17 | "Payment not completed" end event | SD23: Marketplace platform on Payment service for Payment service availability (softgoal) | MP23 Payment service failure handled: MP24 Retry, then cancel and release stock (chosen), MP25 End the process at once (rejected). MP24 helps MP28 Reliable checkout and hurts MP29 Quick checkout | TN5 | Error boundary event `PAYMENT_SERVICE_UNAVAILABLE`, gateway "Try again?", timer "Wait before the next attempt", then "Release stock", "Cancel order" and "Tell the customer" | |
| U11 | For multi-vendor orders, the system calculates the amount of each producer and the 5% commission | FN2 | B13 | Process payment (R09) | SD19: BRF Network on Marketplace platform for 5% commission calculated (goal). SD17: Producer on BRF Network for Weekly settlement with statement (resource) | MP17 Calculate producer amounts and 5% commission makes MP31 Accurate amounts. NW04 Charge 5% commission. PR10 Accept 5% commission hurts PR12 Fair income per sale | TN1 | Script task "Calculate producer amounts and commission" (FEEL) | |
| U12 | The group uses a sandbox or simulated payment service, not a live system | FN2 | B10, B20 | Payment service pool (E01) | SD22 and SD09 (see U7). E01 is a sandbox or a mock (NFR02) | MP16 Submit payment helps MP30 Secure payment | TN6 | Collapsed pool "Payment service (sandbox or mock)". Form `payment-details` offers sandbox payment methods only | |

## 4. Checks

| Check | Result |
|---|---|
| Each row has at least one SD dependency | 10 of 11. U9 has none (gap R1 in [task1-bpmn/istar/README.md](../task1-bpmn/istar/README.md), section 8.5) |
| Each row has at least one SR element | 11 of 11 |
| Each FN1 and FN2 story (B01 to B17) is in a row | Yes. B09 (Could) and B18, B19 (input) are not in UC2 rows |
| Each SR element in the table is in model-content.md | Yes |
| The operational BPMN and Camunda columns are filled | FN2 rows (U7 to U12): operational column filled from the 5.4 draft. FN1 rows and the Camunda column: not yet (5.2, 6.1) |

## 5. References

AlHaj Hassan, S. (2026) *Goal-oriented requirements engineering using i\** [Lecture slides]. UFCFTR-30-3 Distributed and Enterprise Software Development, Week 12. UWE Bristol. Unpublished. Available on Blackboard.
