# 2.2 Two major functionalities

**Authors:** the group chose the two functionalities at stand-up 2 (Mon 19 Oct 2026). Hasaan Ahmad recorded the choice and wrote this draft. Ishaq Modassir Mushtaq, Royden Dias and Shamy reviewed it in [#115](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/115). Royden Dias revised the draft after the review.
**Task:** [#86](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/86), Criterion 2: analysis and planning
**Status:** draft for review. The module team has not agreed the choice yet (section 6).

## 1. Purpose and scope

The brief requires two major business functionalities from the strategic analysis (UWE Bristol, 2026c, p. 4). The module team must agree them "before detailed implementation begins". Each functionality gets one operational BPMN model and one executable Camunda process. The Task 2 product must include both.

The brief also gives the test for a functionality. It must be "sufficiently substantial to demonstrate an end-to-end business process". It must also give opportunities for six points: user interaction, automated processing, business decisions, service interaction, data processing, and alternative or exceptional flows (UWE Bristol, 2026c, p. 4).

This document has three parts:

1. **Identify:** the candidate functionalities and their assessment (section 2).
2. **Scope:** the choice of two, the reasons, and the scope of each (sections 3 to 5).
3. **Agree:** the record of the agreement with the module team (section 6).

The document uses the IDs of [actors.md](../strategic/actors.md) (A01 to A07, E01 to E06) and [processes.md](../strategic/processes.md) (F01 to F05, P01 to P11). The message IDs (M01 to M26, O01 to O04) and the relationship IDs (R01 to R17) come from [interactions.md](../strategic/interactions.md). That document is task 1.3, merged through [#102](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/102). The chosen use case is Use Case 2 ([use-case.md](use-case.md)).

Source keys: CS is the case study (UWE Bristol, 2026a), with the page number. UC1, UC2 and UC3 are the three use cases (UWE Bristol, 2026b). **Proposal** marks a design choice of this draft that the sources do not state. The reviewers confirm or change each proposal.

## 2. Candidate functionalities

### 2.1 Criteria

| No. | Criterion | Source |
|---|---|---|
| K1 | The candidate is an end-to-end business process. It has its own trigger, owner and outcome | Brief p. 4 |
| K2 | The candidate gives opportunities for each of the six points | Brief p. 4 |
| K3 | The candidate is part of the chosen use case. The brief says that the group completes one use case. On 12 Oct 2026, the tutor said that the group models everything for that use case | Brief p. 3, tutor |

### 2.2 Candidates

Each candidate is one process of processes.md, or a set of processes that work together. The use case links go to the comparison of the three use cases in use-case.md.

| ID | Candidate | Processes | Owning function | Actors and services | Use case | Trigger | Outcome |
|---|---|---|---|---|---|---|---|
| C1 | Process order | [P04](../strategic/processes.md#3-major-processes) | F02 Orders | Customer (A01 to A03). Producer (A04), through its stock and its delivery or collection arrangements | [UC2](use-case.md#comparison) | The customer proceeds to checkout (M04) | The marketplace order exists and is split into producer order elements (R06) |
| C2 | Process payment | [P05](../strategic/processes.md#3-major-processes) | F03 Finance, with F01 and F02 | Customer, Producer, E01 Payment service, E03 Notification service | [UC2](use-case.md#comparison) | A confirmed order needs payment (R06) | The order is confirmed, the stock is updated and the producers are notified (M07, M08, M09, R07). Or the decline and unavailable paths apply |
| C3 | Checkout and payment (all of UC2) | [P04 and P05](../strategic/processes.md#3-major-processes) | F02 and F03 | As C1 and C2 | [UC2](use-case.md#comparison) | The customer proceeds to checkout (M04) | As C2 |
| C4 | Product listing and certification | [P01 and P02](../strategic/processes.md#3-major-processes) | F01 and F04 | Producer, E02 Certification service | [UC1](use-case.md#comparison) (not chosen) | A producer has a new product, or a change to a product | The product is listed with a verified organic status, or the claim is rejected |
| C5 | Settle producer payments | [P07](../strategic/processes.md#3-major-processes) | F03 Finance | Producer, E06 Tax authority. The payer is open (Q2 in actors.md) | None (CS p. 2) | The weekly settlement date | Each producer receives its amount less the 5% commission, with an audit trail |
| C6 | Handle quality incident | [P08](../strategic/processes.md#3-major-processes) | F04 Quality and traceability | Customer, Producer, A06, A07, E03, E05 | [UC3](use-case.md#comparison) (not chosen) | A customer, a producer or the administrator reports a concern | The incident is closed, or further action is requested |
| C7 | Offer surplus produce | [P10](../strategic/processes.md#3-major-processes) | F05 Quality assurance and community features | Producer, Customer, E03 | None (CS p. 2) | A producer has surplus produce | A discount is published and the interested customers are told |

These processes are not candidates:

- **P03 Browse and search catalogue:** it has few decisions and no exception path. Its basket is the input of C1.
- **P06 Fulfil order:** the producer does this work outside the platform. Most of it is physical work, with little to automate.
- **P09 Report food miles:** it is one calculation. It can be a step of C1 (R14).
- **P11 Share educational content:** it publishes content and has no business decision.

### 2.3 Assessment

Strong: the sources give clear examples. Partial: examples exist, but they are few or they depend on a proposal. Weak: the sources give almost no examples.

| ID | K1 End-to-end | User interaction | Automated processing | Business decisions | Service interaction | Data processing | Alternative or exception flows | K3 In UC2 |
|---|---|---|---|---|---|---|---|---|
| C1 | Strong | Strong | Strong | Strong | Partial (W1) | Strong | Strong | Yes |
| C2 | Strong | Partial | Strong | Strong | Strong | Strong | Strong | Yes |
| C3 | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Yes |
| C4 | Strong | Strong | Strong | Strong | Strong | Strong | Strong | No |
| C5 | Strong | Weak | Strong | Partial | Partial | Strong | Weak | No |
| C6 | Strong | Strong | Partial | Strong | Partial | Strong | Strong | No |
| C7 | Partial | Partial | Partial | Weak | Partial | Weak | Weak | No |

## 3. Choice

### 3.1 Decision

The group chose C1 and C2 at [stand-up 2](../../sprints/task1-sprint1/standups.md#stand-up-2-mon-19-oct-2026) on Mon 19 Oct 2026. All four members agreed. The proposal is in a [comment on #100](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/100#issuecomment-6263861128). This choice answers T1 and T2 in [processes.md](../strategic/processes.md#6-open-questions).

| ID | Functionality | Process | Owning function | Candidate |
|---|---|---|---|---|
| FN1 | Process order | P04 | F02 Orders | C1 |
| FN2 | Process payment | P05 | F03 Finance | C2 |

### 3.2 Reasons

1. Both are in UC2 (K3). Thus the group completes one use case, as the brief and the tutor require.
2. processes.md already separates P04 and P05. They have different owning functions, triggers and outcomes (K1).
3. Each one maps to one call activity in the strategic model ([#84](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/84)), one operational model, one Camunda process and one Task 2 service.
4. The boundary between them is one clear interface: FN1 gives the order to FN2 (R06). This shows the components, interfaces and services of MO1.
5. Together they cover each sentence of UC2 (section 5).
6. Each one has examples of all six points (section 4).

### 3.3 Other candidates

- **C3** is the strongest single candidate, but it puts all of UC2 into one functionality. If the module team rejects the split into P04 and P05, the group proposes C3 as FN1. The group then agrees the second functionality and the change of scope with the module team (W2, A2).
- **C4 and C6** are strong, but they are outside UC2. They also need actors and services that UC2 does not use (E02, A06 and A07). C4 is a possible FN2 in the fallback, because it is strong on all six points (section 2.3).
- **C5** settles the producer payments that follow the checkout and the payment. It is weak on user interaction and on exception flows, and its payer is open (Q2 in actors.md). C5 is the other possible FN2 in the fallback. The group asks the module team which of C4 and C5 it accepts, and which change of scope it permits (A2).
- **C7** is a small process with few decisions.

### 3.4 Weak points

| No. | Weak point | Effect | Response |
|---|---|---|---|
| W1 | UC2 gives P04 no external service | FN1 is weak on service interaction | **Proposal:** FN1 calls a stock service through service tasks, to check and reserve the stock. In Task 1 it is a mock service in Docker. In Task 2 it becomes part of the product service. The food miles in the order summary (R14) can add the postcode distance service (E04), if Q3 makes it external |
| W2 | The module team can see P04 and P05 as two halves of one process | The Sprint 2 fail band includes functionalities that "do not represent meaningful end-to-end processes" (UWE Bristol, 2026c, p. 15) | Each functionality has its own trigger, owner, outcome, exception paths and service (section 4). The group asks the module team about this directly (A2). If the module team rejects the split, the fallback is C3 as FN1 and C4 or C5 as FN2. The module team must agree the choice of FN2. Both options extend the scope beyond UC2. Section 3.3 compares them |
| W3 | The stock can change between the check in FN1 and the update in FN2 | Two customers can buy the last unit of a product | **Proposal:** FN1 reserves the stock for a time limit. FN2 changes the reservation into a stock update after a successful payment. The reservation is released when the order is cancelled or the reservation expires. Sprint 2 defines the expiry during the payment and its retries. It also defines the result of a payment that succeeds after the expiry (S1) |

## 4. Scope

### 4.1 Summary

| | FN1 Process order | FN2 Process payment |
|---|---|---|
| Process | P04 | P05 |
| Owning lane | F02 Orders | F03 Finance |
| Other lanes | F01 Product listing (the stock) | F01 (the stock update) and F02 (the producer notifications) |
| Participants | Customer, BRF Network, stock service (proposal, W1) | Customer, BRF Network, Producer, E01 Payment service, E03 Notification service (Q3) |
| Start | The customer proceeds to checkout with the basket (M04) | FN1 gives a confirmed order that needs payment (R06) |
| Normal end | The marketplace order and the producer order elements exist. The stock is reserved (proposal, W3) | The order is confirmed (M07). The stock is updated (R07). Each producer is notified (M08, M09) |
| Other ends | The customer cancels. The customer does not confirm within the time limit (proposal, W3) | The customer cancels after a decline (proposal). The payment service stays unavailable after the last retry, and the order is cancelled (proposal, S3) |
| Data to the next step | To FN2: the order ID, the producer order elements, the amounts and the reservation | To P06: the producer order elements (M08, M09). To P07: the producer amounts and the commission (R09) |
| In scope | The stock check, the amendment, the producers and their arrangements, the review and confirmation, the order and the split | The payment request, the decline and retry, the unavailable path, the producer amounts and the commission, the confirmation, the stock update and the notifications |
| Out of scope | The browsing and the basket (P03). The surplus discounts (P10, R15) | The weekly settlement (P07). Refunds. Fulfilment (P06). Live payments |
| Planned process ID | `process_order` | `process_payment` |
| Planned files | `task1-bpmn/operational/process-order.bpmn` and `process-order.png` | `task1-bpmn/operational/process-payment.bpmn` and `process-payment.png` |
| Task 2 service | Order service | Payment service |

The operational models decide the pools and the lanes in Sprint 2. **Proposal:** each customer step is a user task with a Camunda Form in the executable process. The demonstration must show which activities the users do and which the engine or the services do (UWE Bristol, 2026c, p. 4).

### 4.2 FN1 Process order

| Point | Example | Source | Planned element |
|---|---|---|---|
| User interaction | The customer amends the order when an item is unavailable (O01, O02) | UC2 | User task with a Camunda Form |
| User interaction | The customer reviews the order summary and confirms the purchase (M04; D2 in interactions.md) | UC2 | User task with a Camunda Form |
| Automated processing | The system checks the stock of each item in the basket | UC2 | Service task, job type `check-stock` |
| Automated processing | The system identifies the producers, creates the marketplace order and splits it into producer order elements | UC2 | Service tasks `identify-producers`, `create-order` and `split-order` |
| Business decisions | Is each item available in the requested quantity? | UC2 | Exclusive gateway with a FEEL condition |
| Business decisions | Delivery or collection for each producer, with a date at least 48 hours after the order | UC2, CS p. 1 | FEEL expression in an output mapping, or a business rule task |
| Service interaction | The stock service checks and reserves the stock | Proposal (W1) | Service task with a job worker. The service is a mock in Docker |
| Service interaction | The postcode distance service gives the food miles for the order summary | CS p. 2, R14 (Q3) | Optional service task |
| Data processing | The basket lines, the stock levels, the producer IDs and the delivery or collection choices become the marketplace order and its producer order elements | UC2 | Process variables. The order record links the customer, the products and the producers (CS p. 2, R10) |
| Alternative or exception flows | An item is unavailable: the customer is told and amends the order. Then the check runs again | UC2 | Exclusive gateway and a loop back to the check |
| Alternative or exception flows | The customer does not confirm within the time limit: the reservation is released and the process ends | Proposal (W3) | Interrupting timer boundary event on the review task |
| Alternative or exception flows | The stock service does not respond: the process retries the call, then a modelled recovery path tells the customer | Proposal | Sprint 2 agrees the retry and recovery design. Exhausted job retries raise an incident. They do not trigger an error boundary event. If the recovery uses an error boundary event, the worker must explicitly throw a matching BPMN error |

### 4.3 FN2 Process payment

| Point | Example | Source | Planned element |
|---|---|---|---|
| User interaction | The customer selects a simulated payment option or gives a sandbox payment reference. The form does not collect card numbers or card security codes | UC2 (the sandbox or simulated payment). Proposal (the form fields) | User task with a Camunda Form. Sprint 2 agrees the fields |
| User interaction | After a decline, the customer chooses to retry or to cancel (O03, O04) | UC2 | User task with a Camunda Form |
| Automated processing | The system submits the payment (M05) and reads the response (M06) | UC2 | Service task, job type `submit-payment` |
| Automated processing | The system confirms the order, updates the stock and notifies each producer (M07, M08, M09, R07) | UC2 | Service tasks `confirm-order` and `update-stock`. A multi-instance service task `notify-producer`, with one instance for each producer order element |
| Business decisions | The payment result: success, decline or service unavailable | UC2 | Exclusive gateway and error boundary events |
| Business decisions | The amount for each producer and the 5% commission | UC2, CS p. 2 | FEEL expressions in output mappings |
| Business decisions | The retry limits, and the action when the last attempt fails | Proposal (S3) | Sprint 2 agrees the retry policy (S3). A modelled retry loop can use an exclusive gateway with a FEEL condition on a retry counter |
| Service interaction | The payment service takes the payment: a sandbox (for example, Stripe test mode) or a mock service in Docker | UC2, CS p. 1 | Service task with a job worker |
| Service interaction | The notification service sends the producer notifications | UC2 (Q3) | Service task |
| Data processing | The order total, the producer amounts, the commission, the payment reference, the payment status and the retry count | UC2 | Process variables. The payment record supplies the weekly settlement (R09) |
| Alternative or exception flows | The payment service is unavailable: the process follows an exception or retry path. **Proposal:** when the last attempt fails, the process cancels the order, releases the stock and tells the customer | UC2 (the exception or retry path). Proposal (the cancellation after the last attempt) | Sprint 2 agrees the retry and recovery design (S3). Exhausted job retries raise an incident. If the recovery uses an error boundary event, the worker must explicitly throw `PAYMENT_SERVICE_UNAVAILABLE`. A modelled retry loop can use a timer event |
| Alternative or exception flows | The stock reservation expires during the payment or its retries. Or the payment succeeds after the reservation expires | Proposal (W3) | Sprint 2 agrees the expiry and recovery design (S1). The timer on the review task in FN1 does not cover this period |
| Alternative or exception flows | The payment is declined: the customer is told and can retry (O03, O04) | UC2 | **Proposal:** the worker explicitly throws the BPMN error `PAYMENT_DECLINED`. An error boundary event catches it and starts the user task in which the customer chooses to retry or to cancel |
| Alternative or exception flows | The customer cancels after a decline: the stock is released and the order is cancelled | Proposal | Exclusive gateway and an end event |

**Constraint:** the payment form and the process variables must not hold card numbers or card security codes. This rule also applies to sandbox card details. Use a simulated payment choice or a sandbox payment reference instead. The process can keep the payment reference, the payment status and the order and accounting data above, but not the card details. Development and testing use no live payment system and no real financial data (CS p. 1). All financial transactions must obey the data protection and financial services regulations (CS p. 2).

### 4.4 Naming rules

These rules apply to both operational models. Task 1.6 ([#84](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/84)) uses the process IDs in the strategic model.

| Item | Rule | Example |
|---|---|---|
| Process ID | Lower case, with underscores between the words, as in the Week 10 lab | `process_order` |
| BPMN file | The process ID, with hyphens | `process-order.bpmn` |
| Job type | A verb and a noun, lower case, with hyphens | `check-stock` |
| Error code | Upper case, with underscores | `PAYMENT_DECLINED` |
| Process variable | camelCase, as in the Week 10 lab | `orderTotal` |

## 5. Traceability to Use Case 2

Each sentence of UC2 maps to FN1, to FN2 or to a process outside the two functionalities.

| No. | UC2 text (shortened) | Functionality | Process | Messages and relationships |
|---|---|---|---|---|
| U1 | The customer browses or searches and adds products to the basket | None (the input of FN1) | P03 | R05 (D1 in interactions.md) |
| U2 | At checkout, the system checks that all products are available in the requested quantities | FN1 | P04 | M04, R04 |
| U3 | If an item is unavailable, the customer is told and asked to amend the order | FN1 | P04 | O01, O02 |
| U4 | The system identifies the producers and the delivery or collection arrangements | FN1 | P04 | None (D2 in interactions.md) |
| U5 | The customer reviews the order and confirms the purchase | FN1 | P04 | M04 (D2 in interactions.md) |
| U6 | The system creates the marketplace order and separates it into producer order elements | FN1 | P04 | R06 |
| U7 | The payment goes to an external or simulated payment service | FN2 | P05 | M05, M06 |
| U8 | On success, the order is confirmed, the stock is updated and the producers are notified | FN2 | P05 | M07, M08, M09, R07, R08 |
| U9 | On a decline, the customer is told and can retry | FN2 | P05 | O03, O04 |
| U10 | If the payment service is unavailable, an exception or retry path applies, not a simple termination | FN2 | P05 | M06 for an explicit error response. Otherwise, the exception path for an unavailable service |
| U11 | For multi-vendor orders, the system calculates the amount of each producer and the 5% commission | FN2 | P05 | R09 |
| U12 | The group uses a sandbox or simulated payment service, not a live system | FN2 | P05 | E01 |

## 6. Agreement

### 6.1 Group

| Date | Event | Decision |
|---|---|---|
| Mon 19 Oct 2026 | Stand-up 2, all four members | FN1 is P04 Process order. FN2 is P05 Process payment. The group asks the module team to agree the choice |

### 6.2 Questions for the module team

| No. | Question | Effect |
|---|---|---|
| A1 | Do you agree P04 Process order and P05 Process payment as the two major functionalities? | The main decision of this task |
| A2 | Is each of the two sufficiently end-to-end? If one functionality must contain all of UC2, do you accept C3 as FN1 and C4 or C5 as FN2? C4 is strong on all six points. C5 is weak on user interaction and on exception flows. Which change of scope do you permit? | If the module team rejects the split, the group agrees FN2 and the scope beyond UC2 with the module team. Then the group changes the scope in section 4 |
| A3 | Is a mock stock service sufficient for the service interaction of FN1 (W1)? | It decides the service tasks of FN1 |
| A4 | Do you accept that each producer delivers its goods, or that the customer collects them (Q1 in [actors.md](../strategic/actors.md#5-open-questions))? | It decides the delivery or collection decision in FN1 |
| A5 | Are the notification service (E03) and the postcode distance service (E04) external (Q3 in actors.md)? | It decides the service tasks for the notifications in FN2 and for the food miles in FN1 |

A4 is also on the list of questions from stand-up 2.

### 6.3 Record

Complete this table after the meeting with the module team. The agreement must be in place before the Sprint 1 Review (Thu 29 Oct 2026, 14:00).

| Field | Value |
|---|---|
| Date | TBC |
| Session | TBC |
| Tutor | TBC |
| Members present | TBC |
| Decision | Pending |
| Answers to A1 to A5 | Pending |
| Changes to this document | Pending |

### 6.4 After the agreement

- Record the decision in T1 and T2 of [processes.md](../strategic/processes.md#6-open-questions).
- 1.6 ([#84](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/84)): make P04 and P05 call activities, with the process IDs of section 4.4.
- 2.5 ([#90](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/90)): write the user stories for FN1 and FN2.
- 2.6 ([#49](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/49)): this task plans one model for all of UC2 (`checkout-payment.bpmn`). Change it to two models, one for each functionality.

## 7. Open questions for the group

The reviewers of this pull request answer these questions, or move them to Sprint 2. The answers come from the reviews of Sat 24 Oct and Mon 26 Oct 2026.

| No. | Question | Reason | Answer |
|---|---|---|---|
| S1 | Do we accept the stock reservation (W3)? If so, what is the time limit? What happens when the reservation expires during the payment or its retries? | It adds the expiry and the release of the reservation to FN1 and FN2. The timer on the review task covers only the time before the customer confirms | Keep the reservation as a proposal. It follows the reserve, pay and release pattern of a saga (UWE Bristol, 2026d, slide 24). The group confirms the reservation, the time limit and the expiry in Sprint 2, when it builds the operational models. This includes an expiry during the payment or its retries, and a payment that succeeds after the expiry |
| S2 | How does FN2 start: as a call activity of a parent process, or from a message that FN1 sends? | It decides the interface between the two Camunda processes, and the call activities in #84 | Moved to Sprint 2. Until then, 1.6 ([#84](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/84)) shows P04 and P05 as call activities in Figure 1 |
| S3 | How many retries do we permit for a decline and for an unavailable service? How long is the wait? What happens when the last attempt fails? | It decides the retry counters, the timer values and the recovery policy in FN2. The design must keep job retries and incidents separate from the BPMN errors that the workers throw | Moved to Sprint 2. Agree the retry mechanism, the BPMN error codes and the recovery policy. The cancellation after the last retry of an unavailable service stays a proposal |
| S4 | How do we round the producer amounts and the commission? | The rounded amounts must add up to the order total | Moved to Sprint 2 |

The Sprint 2 plan (2.7, [#91](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/91)) gives each of S1 to S4 a task.

## 8. References

UWE Bristol (2026a) *Bristol Regional Food Network: digital marketplace* [Case study]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [case_study/Case Study - v2.pdf](../../case_study/Case%20Study%20-%20v2.pdf).

UWE Bristol (2026b) *Assessment Task 1 use cases* [Assessment material]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Use Case 2 is in [case_study/Case_study.txt](../../case_study/Case_study.txt).

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished.

UWE Bristol (2026d) *Distributed systems* [Lecture slides, week 8]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [lectures/w08 - Distributed systems (lecture).pdf](../../lectures/w08%20-%20Distributed%20systems%20%28lecture%29.pdf).
