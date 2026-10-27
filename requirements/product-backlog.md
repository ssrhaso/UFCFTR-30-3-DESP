# 2.5 Initial product backlog

**Authors:** Ishaq Modassir Mushtaq
**Task:** [#90](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/90), Criterion 2: analysis and planning
**Status:** draft for review. The owners and the sprint capacity are set at sprint planning ([#94](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/94) and [#91](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/91)).

## 1. Purpose and scope

The brief asks for "an initial product backlog and sprint plan" in Sprint 1 (UWE Bristol, 2026c, p. 5). The first-class band asks for major functionalities that are "decomposed into a comprehensive product backlog with professional sprint planning, responsibilities and priorities" (UWE Bristol, 2026c, p. 14). This document is that backlog for the two major functionalities of [functionalities.md](scope/functionalities.md):

| ID | Functionality | Process |
|---|---|---|
| FN1 | Process order | P04 |
| FN2 | Process payment | P05 |

Together they cover Use Case 2, the customer multi-vendor order, checkout and payment ([use-case.md](scope/use-case.md)). The first sentence of UC2 (browsing and the basket, P03) is not part of FN1 or FN2. It has two stories in section 6, so that the backlog covers the whole of UC2 whichever way the module team reads the scope.

The backlog has the functional stories of FN1 (section 4), of FN2 (section 5) and of the input to FN1 (section 6). The group refines the backlog at each sprint planning. The stories below are the first version.

Source keys: CS is the case study (UWE Bristol, 2026a), with the page number. UC1, UC2 and UC3 are the three use cases (UWE Bristol, 2026b). **Proposal** marks a design choice of the group that the sources do not state. The IDs of the actors (A01 to A07, E01 to E06), the processes (P01 to P11) and the functions (F01 to F05) come from [actors.md](strategic/actors.md) and [processes.md](strategic/processes.md). The message IDs (M01 to M22, O01 to O04) and the relationship IDs (R01 to R17) come from [interactions.md](strategic/interactions.md).

## 2. Conventions

| Item | Rule |
|---|---|
| Story form | "As a ⟨role⟩ I can ⟨capability⟩, so that ⟨benefit⟩" (Week 9 lecture, slides 16 and 17) |
| Acceptance criteria | Written as Given, When, Then. Each criterion can be checked by running the Camunda process or by reading its model |
| ID | B01 and up for a functional story |
| Priority | MoSCoW. **Must:** the process cannot meet UC2 without it. **Should:** UC2 works without it, but it is important and the group plans it. **Could:** wanted if there is time. |
| Estimate | Story points on the scale 1, 2, 3, 5 and 8. They are relative: 1 is a small change to one element, and 5 is a step with a decision, a service and an exception path. A story of more than 8 is split |
| Sprint | The sprint that plans the story: Sprint 2 builds the first executable version of each process, and Sprint 3 completes and integrates it (UWE Bristol, 2026c, pp. 5 and 6) |
| Owner | The member that takes the story. It is set at sprint planning, and recorded on the GitHub task. It is blank in this first version |
| Traces to | The UC2 sentence (U1 to U12 of [functionalities.md](scope/functionalities.md#5-traceability-to-use-case-2)), the messages and relationships of interactions.md, and the planned element of functionalities.md section 4 |

A story is **ready** when it has acceptance criteria, an estimate and a priority. A story is **done** when its element is in the operational model, the process runs in Camunda 8, and the work is merged through a reviewed pull request ([README](../README.md#definition-of-done)).

## 3. Summary

| ID | Functionality | Story | Priority | Points | Sprint | Traces to |
|---|---|---|---|---|---|---|
| B01 | FN1 | Check the stock at checkout | Must | 3 | 2 | U2, M04, R04 |
| B02 | FN1 | Amend the order when an item is unavailable | Must | 3 | 2 | U3, O01, O02 |
| B03 | FN1 | See the producers and the delivery or collection arrangements | Must | 3 | 2 | U4 |
| B04 | FN1 | Receive the goods at least 48 hours after the order | Should | 2 | 3 | U4, CS p. 1 |
| B05 | FN1 | Review and confirm the order | Must | 2 | 2 | U5, M04 |
| B06 | FN1 | Create the marketplace order and split it by producer | Must | 5 | 2 | U6, R06, R10 |
| B07 | FN1 | Reserve the stock for a time limit | Should | 5 | 3 | W3, S1 |
| B08 | FN1 | Cancel or time out and release the reserved stock | Should | 3 | 3 | W3, S1 |
| B09 | FN1 | See the food miles in the order summary | Could | 2 | 3 | R14, M16 to M18 |
| B10 | FN2 | Pay through the sandbox payment service | Must | 5 | 2 | U7, U12, M05, M06 |
| B11 | FN2 | Be told of a declined payment, and retry or cancel | Must | 3 | 2 | U9, O03, O04 |
| B12 | FN2 | Follow a retry or exception path when the payment service is unavailable | Must | 5 | 3 | U10, S3 |
| B13 | FN2 | Calculate the amount of each producer and the 5% commission | Must | 5 | 2 | U11, R09, S4 |
| B14 | FN2 | Receive the order confirmation after a successful payment | Must | 2 | 2 | U8, M07 |
| B15 | FN2 | Update the stock after a successful payment | Must | 3 | 3 | U8, R07 |
| B16 | FN2 | Notify each producer of its order element | Must | 3 | 3 | U8, M08, M09, R08 |
| B17 | FN2 | Cancel the order and release the stock after the last failed payment | Should | 3 | 3 | S3 (proposal) |
| B18 | Input | Browse and search for products | Should | 5 | Not planned | U1, P03 |
| B19 | Input | Add products from several producers to a basket | Should | 3 | Not planned | U1, P03 |

**Total:** 65 points. 42 are Must (16 in FN1 and 26 in FN2), 21 are Should and 2 are Could. Sprint 2 plans 31 points and Sprint 3 plans 26 points. B18 and B19 are the 8 points that are not planned.

## 4. FN1 Process order (P04)

Owning function: F02 Orders. The process starts when the customer proceeds to checkout (M04) and ends when the marketplace order and its producer order elements exist (R06).

### B01 Check the stock at checkout

As a customer I can have the stock of each item in my basket checked when I go to checkout, so that I do not order goods that the producers cannot supply.

- **Given** a basket and a stock level for each product, **when** the customer proceeds to checkout, **then** the process compares the requested quantity of each item with its stock.
- **Given** that every item is available in the requested quantity, **when** the check ends, **then** the process continues to the identification of the producers (B03).
- **Given** that an item is unavailable or has too little stock, **when** the check ends, **then** the process follows the amendment path (B02) and does not create an order.

Priority: Must. Points: 3. Sprint: 2. Traces to: U2, M04, R04. Planned element: service task `check-stock` and an exclusive gateway.

### B02 Amend the order when an item is unavailable

As a customer I can change my order when an item is unavailable or the stock is too low, so that I can still complete the purchase.

- **Given** an item that fails the check, **when** the process finds it, **then** the customer sees which item is short and how many are available (O01).
- **Given** the notice, **when** the customer changes the quantity or removes the item and submits (O02), **then** the check of B01 runs again on the amended order.
- **Given** that the customer removes all the items, **then** the process ends without an order.

Priority: Must. Points: 3. Sprint: 2. Traces to: U3, O01, O02. Planned element: user task with a Camunda Form, and a loop back to the check.

### B03 See the producers and the delivery or collection arrangements

As a customer I can see which producers supply my order and the delivery or collection arrangement of each, so that I know who is responsible for each part of it.

- **Given** an available basket, **when** the process identifies the producers, **then** the order summary lists each producer with its items and its delivery or collection arrangement.
- **Given** a basket with items from several producers, **then** the summary shows each producer as a separate part of the order.
- **Given** the assumption that each producer delivers its goods or that the customer collects them (Q1 in actors.md), **then** no logistics partner appears in the summary.

Priority: Must. Points: 3. Sprint: 2. Traces to: U4, CS p. 2. Planned element: service tasks `identify-producers`, and a FEEL expression or a business rule task for the arrangement.

### B04 Receive the goods at least 48 hours after the order

As a producer I can prepare an order at least 48 hours before the delivery or collection, so that I have the time to prepare the goods.

- **Given** an order placed at a given time, **when** the process sets the delivery or collection date of each producer, **then** the date is at least 48 hours after the order.
- **Given** a date that the rule does not allow, **then** the process moves it to the first allowed date, and the summary shows the date.

Priority: Should. Points: 2. Sprint: 3. Traces to: U4, CS p. 1. Planned element: FEEL expression in an output mapping. The agreed delivery assumption (Q1, A4) decides the exact rule.

### B05 Review and confirm the order

As a customer I can review the order summary and confirm the purchase, so that I commit only to an order that I have checked.

- **Given** the summary of B03, **when** the customer opens it, **then** it shows the items, the producers, the arrangements and the total.
- **Given** the summary, **when** the customer confirms, **then** the process creates the marketplace order (B06).
- **Given** the summary, **when** the customer cancels, **then** the process ends and no order exists.

Priority: Must. Points: 2. Sprint: 2. Traces to: U5, M04 (D2 in interactions.md). Planned element: user task with a Camunda Form.

### B06 Create the marketplace order and split it by producer

As the network I can create the marketplace order and split it into one order element for each producer, so that each producer sees and fulfils only its own part.

- **Given** a confirmed order, **when** the process creates it, **then** one marketplace order exists, with an order ID.
- **Given** an order with items from several producers, **then** it has one producer order element for each producer, and each element holds only the items of that producer and its arrangement.
- **Given** the elements, **then** the amounts of the elements add up to the order total.
- **Given** the order, **then** its record links the customer, the products and the producers, so that a quality concern can be traced later (R10).
- **Given** the order, **when** the process ends, **then** it gives the order ID, the elements, the amounts and the reservation to FN2 (R06).

Priority: Must. Points: 5. Sprint: 2. Traces to: U6, R06, R10. Planned element: service tasks `create-order` and `split-order`, and process variables for the elements.

### B07 Reserve the stock for a time limit

As the network I can reserve the stock of an order for a time limit, so that two customers cannot buy the last unit of a product.

- **Given** a confirmed order, **when** the process creates it, **then** the stock of each item is reserved and the reservation has an expiry time.
- **Given** a reservation, **when** the payment succeeds before the expiry, **then** FN2 turns the reservation into a stock update (B15).
- **Given** a reservation that expires before the payment, **then** the process follows the recovery path that Sprint 2 agrees (S1).

Priority: Should. Points: 5. Sprint: 3. Traces to: W3, S1 of functionalities.md. **Proposal.** UC2 does not state a reservation. The group confirms the reservation, the time limit and the expiry in Sprint 2.

### B08 Cancel or time out and release the reserved stock

As a customer I can cancel the order, or let it expire, so that the reserved stock is released for other customers.

- **Given** a reservation, **when** the customer cancels at the review, **then** the reservation is released.
- **Given** an order that is not confirmed within the time limit, **when** the timer ends, **then** the reservation is released and the process ends.

Priority: Should. Points: 3. Sprint: 3. Traces to: W3, S1. Planned element: interrupting timer boundary event on the review task. **Proposal**, as for B07.

### B09 See the food miles in the order summary

As a customer I can see the distance that my goods travel, so that I can judge the environmental effect of my order.

- **Given** the postcode of the customer and of each farm, **when** the summary shows an item, **then** it shows the distance between them.
- **Given** a missing or an invalid postcode, **then** the summary shows no distance, and the order continues.

Priority: Could. Points: 2. Sprint: 3. Traces to: R14, M16 to M18, CS p. 2. Planned element: optional service task. It depends on Q3 (the postcode service is external or internal).

## 5. FN2 Process payment (P05)

Owning function: F03 Finance, with F01 (the stock) and F02 (the producer notifications). The process starts when FN1 gives a confirmed order that needs payment (R06).

### B10 Pay through the sandbox payment service

As a customer I can pay for my order through the payment service, so that my order is paid and can be confirmed.

- **Given** an order awaiting payment, **when** the process submits it, **then** the payment request carries the order reference and the total (M05).
- **Given** a request, **then** the payment service is a sandbox (for example Stripe test mode) or a mock service in Docker. No live payment system and no real financial data are used (CS p. 1).
- **Given** the payment form, **then** it does not ask for a card number or a card security code, including sandbox card details (functionalities.md section 4.3). It offers a simulated payment option or takes a sandbox payment reference.
- **Given** a response, **when** it arrives (M06), **then** the process reads it as success, decline or explicit service error.

Priority: Must. Points: 5. Sprint: 2. Traces to: U7, U12, M05, M06. Planned element: user task with a Camunda Form, and service task `submit-payment`.

### B11 Be told of a declined payment, and retry or cancel

As a customer I am told when my payment is declined and can retry or cancel, so that a declined payment does not lose my order.

- **Given** a decline response, **when** the process reads it, **then** the customer sees a declined notice (O03).
- **Given** the notice, **when** the customer chooses to retry (O04), **then** the process submits the payment again.
- **Given** the notice, **when** the customer chooses to cancel, **then** the process follows B17.
- **Given** a declined payment, **then** the order is not confirmed.

Priority: Must. Points: 3. Sprint: 2. Traces to: U9, O03, O04. Planned element: the worker throws the BPMN error `PAYMENT_DECLINED`, an error boundary event catches it, and a user task with a Camunda Form offers the retry or the cancellation (functionalities.md section 4.3).

### B12 Follow a retry or exception path when the payment service is unavailable

As the network I can retry or follow an exception path when the payment service does not respond, so that the process does not simply stop.

- **Given** a payment service that returns an error or does not respond, **when** the process detects it, **then** it follows a retry path and not a plain end event.
- **Given** the retry path, **then** it has a limit of attempts and a wait, which Sprint 2 agrees (S3).
- **Given** that the last attempt fails, **then** the process follows B17, and the customer is told.
- **Given** the failure, **then** job retries and incidents stay separate from the BPMN errors that the workers throw.

Priority: Must. Points: 5. Sprint: 3 (the first path in Sprint 2). Traces to: U10, S3 of functionalities.md. Planned element: timer event or a retry counter with an exclusive gateway, and the error `PAYMENT_SERVICE_UNAVAILABLE`. The cancellation after the last attempt is a **proposal**.

### B13 Calculate the amount of each producer and the 5% commission

As the network I can calculate the amount that belongs to each producer and the 5% commission of the marketplace, so that each producer is paid correctly later.

- **Given** an order with several producer elements, **when** the payment succeeds, **then** the process records the amount of each producer and the commission.
- **Given** the amounts, **then** the commission is 5% of the order, and the producer amounts plus the commission equal the order total.
- **Given** an amount that does not divide exactly, **then** the rounding rule of S4 applies, and the rounded amounts still add up to the total.
- **Given** the result, **then** the payment record keeps the amounts for the weekly settlement (R09).

Priority: Must. Points: 5. Sprint: 2. Traces to: U11, R09, S4. Planned element: FEEL expressions in output mappings, or a DMN decision table.

### B14 Receive the order confirmation after a successful payment

As a customer I receive a confirmation after my payment succeeds, so that I know that my order is placed.

- **Given** a successful payment, **when** the process ends the payment, **then** the order status is confirmed.
- **Given** the confirmation, **then** it shows the producers, the arrangements and the totals (M07).
- **Given** a declined or a failed payment, **then** the customer does not receive a confirmation.

Priority: Must. Points: 2. Sprint: 2. Traces to: U8, M07. Planned element: service task `confirm-order`.

### B15 Update the stock after a successful payment

As the network I can update the stock after a payment succeeds, so that the catalogue and the next availability check are accurate.

- **Given** a successful payment, **when** the process confirms the order, **then** the stock of each item falls by the ordered quantity (R07).
- **Given** a reservation (B07), **then** the stock update replaces it.
- **Given** the update, **then** F01 performs it and the product-listing process does not restart.
- **Given** that the update and the producer notifications (B16) do not depend on each other, **then** they run in parallel.

Priority: Must. Points: 3. Sprint: 3. Traces to: U8, R07. Planned element: service task `update-stock`, on a parallel branch.

### B16 Notify each producer of its order element

As a producer I am told of each order element that I must fulfil, with its arrangement, so that I can prepare the goods.

- **Given** a successful payment, **when** the process confirms the order, **then** each producer receives one notification for its own element (M09).
- **Given** an order with several producers, **then** the process sends one notification for each element, and not one for the whole order.
- **Given** the notification, **then** it holds the items, the delivery or collection arrangement and the date.
- **Given** the notification service (E03), **then** the network sends the request (M08) and E03 delivers it.

Priority: Must. Points: 3. Sprint: 3. Traces to: U8, M08, M09, R08. Planned element: multi-instance service task `notify-producer`. It depends on Q3 (the notification service is external).

### B17 Cancel the order and release the stock after the last failed payment

As a customer I am told when my order is cancelled after a failed payment, so that I know that nothing is reserved or charged.

- **Given** that the customer cancels after a decline, or that the last retry fails, **when** the process ends, **then** the order is cancelled.
- **Given** the cancellation, **then** the stock is released and the customer is told.
- **Given** the cancellation, **then** no confirmation and no producer notification is sent.

Priority: Should. Points: 3. Sprint: 3. Traces to: S3 of functionalities.md. **Proposal.** UC2 asks for an exception or retry path, not for a cancellation.

## 6. Input to FN1 (P03)

These two stories are the first sentence of UC2. P03 is the input of FN1 and is not one of the two functionalities (functionalities.md section 2.2). The group does not plan them in Sprint 2 or Sprint 3. They stay in the backlog so that the backlog covers UC2. If the module team requires UC2 in full, the group plans them.

### B18 Browse and search for products

As a customer I can browse the marketplace by category and search for products, so that I can find the goods that I want to buy.

- **Given** the products in the catalogue, **when** the customer browses a category, **then** the list shows its products with the harvest date, the farm origin and the seasonal availability.
- **Given** a search term, **then** the results list the products that match.

Priority: Should. Points: 5. Sprint: Not planned. Traces to: U1, P03, CS p. 2.

### B19 Add products from several producers to a basket

As a customer I can add products from one or more producers to my basket, so that I can check out one order.

- **Given** a product, **when** the customer adds it, **then** the basket holds it with its quantity.
- **Given** products from several producers, **then** one basket holds them all.
- **Given** the basket, **when** the customer proceeds to checkout, **then** FN1 starts with the basket (M04).

Priority: Should. Points: 3. Sprint: Not planned. Traces to: U1, P03, R05.
