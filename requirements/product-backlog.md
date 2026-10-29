# 2.5 Initial product backlog

**Authors:** Ishaq Modassir Mushtaq (the stories), Shamy (the requirements, the enabler stories and the traceability)
**Task:** [#90](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/90), Criterion 2: analysis and planning
**Status:** draft for review. The owners and the sprint capacity are set at sprint planning ([#94](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/94) and [#91](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/91)).

## 1. Purpose and scope

The brief asks for "an initial product backlog and sprint plan" in Sprint 1 (UWE Bristol, 2026c, p. 5). The first-class band asks for major functionalities that are "decomposed into a comprehensive product backlog with professional sprint planning, responsibilities and priorities" (UWE Bristol, 2026c, p. 14). This document is that backlog for the two major functionalities of [functionalities.md](scope/functionalities.md):

| ID | Functionality | Process |
|---|---|---|
| FN1 | Process order | P04 |
| FN2 | Process payment | P05 |

Together they cover Use Case 2, the customer multi-vendor order, checkout and payment ([use-case.md](scope/use-case.md)). The first sentence of UC2 (browsing and the basket, P03) is not part of FN1 or FN2. It has two stories in section 8, so that the backlog covers the whole of UC2 whichever way the module team reads the scope.

The backlog has the functional stories of FN1 (section 6), of FN2 (section 7) and of the input to FN1 (section 8), and the enabler stories that Sprint 2 and Sprint 3 need before the functional stories can run (section 9). The group refines the backlog at each sprint planning. The stories below are the first version.

The document also holds the functional requirements (section 3) and the non-functional requirements (section 4) that the stories realise, and the traceability from the case study to the requirements, the stories, the models and the Task 2 services (section 10). [#90](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/90) asks for the two kinds of requirement in separate sections. The week 9 lecture decides the list that a sentence of the case study goes in: a behaviour of the system is a functional requirement, and a property that the system must exhibit or a constraint that it must respect is a non-functional requirement (UWE Bristol, 2026e, slides 14 and 15).

Source keys: CS is the case study (UWE Bristol, 2026a), with the page number. UC1, UC2 and UC3 are the three use cases (UWE Bristol, 2026b). **Proposal** marks a design choice of the group that the sources do not state. The IDs of the actors (A01 to A07, E01 to E06), the processes (P01 to P11) and the functions (F01 to F05) come from [actors.md](strategic/actors.md) and [processes.md](strategic/processes.md). The message IDs (M01 to M22, O01 to O04) and the relationship IDs (R01 to R17) come from [interactions.md](strategic/interactions.md). The requirement IDs (FR01 to FR20 and NFR01 to NFR13) are defined in sections 3 and 4 of this document. The week 9 lecture on requirements handling is UWE Bristol (2026e).

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
| Requirement ID | FR01 and up for a functional requirement (a behaviour of the system), NFR01 and up for a non-functional requirement (a property or a constraint), after the week 9 lecture (UWE Bristol, 2026e, slides 14 and 15). The FR list covers the whole case study, and its Scope column says which requirements are in Task 1 |
| NFR category | One of the four sources of a non-functional requirement in the week 9 lecture: business rule, quality attribute, external interface, or design and implementation constraint |
| Enabler story | A technical story that Sprint 2 or Sprint 3 needs before a functional story can run: a mock service, the deployment or the test data. Its role is the development team. It has the same ID series (B20 and up) and the same fields as a functional story. For an enabler, **Must** means that a Must functional story cannot run without it |
| Requirements | Each story names the FRs that it realises and the NFRs that constrain it, in the summary and in its last line. **Derived** marks a story that comes from a proposal of the group (W3, S3) and not from a sentence of a source |

A story is **ready** when it has acceptance criteria, an estimate and a priority. A story is **done** when its element is in the operational model, the process runs in Camunda 8, and the work is merged through a reviewed pull request ([README](../README.md#definition-of-done)). **Proposal:** the documentation field of each element in the operational model names its story ID (NFR09), so that the model and this backlog stay traceable. 2.7 ([#91](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/91)) adopts or drops this rule. The definition of done in the README is unchanged.

## 3. Functional requirements

A functional requirement is a behaviour of the system: a service, a task or a function that it performs (UWE Bristol, 2026e, slide 14). The rows come from the mapping of the case study to the processes in [processes.md](strategic/processes.md#5-mapping-to-the-requirements-of-the-case-study) and from the UC2 sentences of [functionalities.md](scope/functionalities.md#5-traceability-to-use-case-2). Where the Stakeholder Requirements and the System Requirements sections of the case study state the same need, one row merges them and cites both pages. The compliance row of processes.md section 5 is a constraint, so it is NFR01.

The list covers the whole case study, so that the Task 1 scope is visible against the full product. **Scope** says where each requirement is met: **FN1** or **FN2** (Task 1, with stories below), **Backlog, not planned** (P03, with the stories B18 and B19), or **Task 2** (a process that the Task 1 operational models do not cover; the Task 2 system meets it). U1 to U12 stay the UC2 refinement of FR05 to FR14, and a story traces to both.

| ID | Requirement | Source | Process | Scope | Stories |
|---|---|---|---|---|---|
| FR01 | A producer lists a product with its name, description, price and availability timeframe, and updates its seasonal availability and stock | CS p. 1 (Producers), p. 2 (Core functionality) | P01 | Task 2 (UC1). Its stock is the input of the check in FN1 (R04) | None. B24 provides test data |
| FR02 | A producer indicates the organic certification status, the allergen warnings and the best-before date of a product | CS p. 2 (Quality assurance) | P01, P02 | Task 2 (UC1) | None |
| FR03 | A customer browses the catalogue by category (vegetables, dairy, bakery, preserves and seasonal specialities) and searches for items | CS p. 2 (Customers) | P03 | Backlog, not planned | B18 |
| FR04 | The catalogue shows the harvest date, the farm origin and the seasonal availability of each product | CS p. 2 (Customers) | P01, P03 | Backlog, not planned | B18 |
| FR05 | A customer adds products from one or more producers to a basket and proceeds to checkout | UC2 (U1) | P03 | Backlog, not planned | B19 |
| FR06 | At checkout the system checks that each item is available in the requested quantity. When an item is unavailable or short, the customer is told and asked to amend the order | UC2 (U2, U3) | P04 | FN1 | B01, B02. Derived: B07, B08 (W3) |
| FR07 | The system identifies the producers of the order and the delivery or collection arrangement of each, with clear supplier responsibilities, for single-vendor and multi-vendor orders | CS p. 2 (Customers, Core functionality), UC2 (U4) | P04 | FN1 | B03, B04 |
| FR08 | The customer reviews the order summary and confirms or cancels the purchase | UC2 (U5); the cancel is the group's reading (functionalities.md section 4.1) | P04 | FN1 | B05. Derived: B08 (W3) |
| FR09 | The system creates the marketplace order and separates it into producer order elements (the aggregation of multi-vendor orders) | CS p. 2 (Core functionality), UC2 (U6) | P04 | FN1 | B06 |
| FR10 | The system takes the payment for a single-vendor or multi-vendor order through an external or simulated payment service | CS p. 2 (Core functionality), UC2 (U7, U12) | P05 | FN2 | B10 |
| FR11 | When a payment is declined, the customer is told and can retry | UC2 (U9) | P05 | FN2 | B11 (its cancel option is a proposal, functionalities.md section 4.3). Derived: B17 |
| FR12 | When the payment service is unavailable, the process follows an exception or retry path and does not simply terminate | UC2 (U10) | P05 | FN2 | B12. Derived: B17 (S3) |
| FR13 | After a successful payment, the order is confirmed, the stock is updated and each producer is notified of its order element | UC2 (U8) | P05 | FN2 | B14, B15, B16 |
| FR14 | For a multi-vendor order, the system calculates the amount of each producer and the 5% commission of the marketplace | CS p. 2 (Core functionality), UC2 (U11) | P05, P07 | FN2 | B13 |
| FR15 | Each producer has visibility of its incoming orders, with the lead time of NFR07 | CS p. 1 (Producers) | P05, P06 | FN2 (the notification). P06 is Task 2 | B16, B04 |
| FR16 | The network settles each producer weekly, less the commission, with a transparent audit trail for tax reporting and accounting | CS p. 2 (Producers, Core functionality) | P07 | Task 2. B13 supplies its data (R09) | None |
| FR17 | The system keeps records that link customers, products and producers, so that a quality or food safety concern reaches everyone affected | CS p. 2 (Quality assurance) | P04 (creates), P08 (uses) | FN1 creates the record. P08 is Task 2 (UC3) | B06 |
| FR18 | The system shows food miles from postcode-based distances | CS p. 2 (Environmental reporting) | P09 | FN1, optional (Could) | B09 |
| FR19 | A producer publishes a surplus produce offer with a last-minute discount, and the interested customers are told | CS p. 2 (Community features) | P10 | Task 2 | None |
| FR20 | A producer shares seasonal recipes, storage guidance and farm stories next to its products | CS p. 2 (Educational components) | P11 | Task 2 | None |

FR15 states the visibility. The 48 hours are NFR07, because they are a measurable constraint on FR13 and FR15 and not a behaviour of their own.

## 4. Non-functional requirements

A non-functional requirement is a property that the system must exhibit or a constraint that it must respect, and not an observable behaviour (UWE Bristol, 2026e, slide 15). Its sources are the four of the lecture: business rules, quality attributes, external interfaces, and design or implementation constraints. A requirement must be testable (UWE Bristol, 2026e, slide 12), so each row has an acceptance test that a reviewer can run or read, and the place where the group checks it. **Applies to** lists the stories that the requirement constrains. The last column names the candidate i* softgoal for the Strategic Rationale model of Sprint 2 (Figure 3), so that the i* work starts from the same list. The actor IDs are those of actors.md.

The sources give no performance or capacity target: the network has about forty producers and three customer segments (CS p. 1), and neither the case study nor UC2 states a response time, a throughput or a number of concurrent orders. The group does not invent one. If Sprint 2 needs one, it is added here with its source.

| ID | Requirement | Category | Source | Acceptance test | Checked by | Applies to | i* softgoal (candidate) |
|---|---|---|---|---|---|---|---|
| NFR01 | All financial transactions and the personal data of an order comply with data protection and financial services regulation (for personal data, the UK GDPR and the Data Protection Act 2018). The process holds only the data that the order needs | Business rule (legal) | CS p. 2 (Core functionality); E05 in actors.md | The process variables and the Forms hold no personal data beyond the customer reference, the items, the arrangement and the amounts. The payment record holds a payment reference, not the card | PR review with the checklist; the variable list in Camunda Operate | B06, B10, B13; every Form | Compliance with regulation (A05); personal data protected (A01 to A03) |
| NFR02 | No live payment system and no real financial data in development, testing or demonstration: a sandbox (Stripe test mode, PayPal sandbox) or a mock service in Docker only | Implementation constraint | CS p. 1 (disclaimer), UC2 (U12) | The worker configuration points at a sandbox or mock endpoint. The repository holds no live key (`.env` is ignored) | PR checklist "no secrets"; configuration review | B10, B20 | None (assessment constraint) |
| NFR03 | Secure payment handling: no card number or card security code in a Camunda Form or a process variable, including sandbox card details. The customer gives a simulated payment choice or a sandbox payment reference | Design constraint (security) | CS p. 2 ("secure payment system"); functionalities.md section 4.3 | A search of the `.form` and `.bpmn` files finds no card field, and Operate shows none | PR review; `grep` on the model files | B10, B11 | Secure payment (A01 to A03, A05) |
| NFR04 | Fault tolerance: every failure of an external service (payment, stock, notification) ends in a modelled state (a retry, a cancellation or a customer notice), never in an unmodelled stop. Job retries and incidents stay separate from the BPMN errors that the workers throw | Quality attribute (reliability) | UC2 (U10); functionalities.md sections 4.2 and 4.3; S3 | With the mock service set to "unavailable", the instance reaches the retry path and then the customer notice within the agreed attempts and wait (S3). No instance is left only as an incident | A run in Camunda 8 with the mock set to "unavailable"; the Operate history | B11, B12, B17, B20, B23; B01 and B21 for the stock service | Reliable checkout (A01 to A03); no lost sale (A05) |
| NFR05 | Monetary consistency: the commission is exactly 5% of the order, and the producer amounts plus the commission equal the order total after rounding (rule S4) | Business rule | CS p. 2 (Core functionality), UC2 (U11) | FEEL or DMN test cases, including a total that does not divide exactly, all sum to the total | Unit cases on the expressions; PR review | B06, B13 | Fair and accurate payment (A04); commission income (A05) |
| NFR06 | Stock integrity: no oversell. The check, the reservation and the update never take the stock of a product below zero, and one unit cannot be sold to two customers (W3, S1) | Business rule (data integrity) | UC2 (U2, U8); functionalities.md W3 | Two instances for the last unit of a product: one reaches the payment, the other follows the amendment path, and the stock after both is not negative | Two concurrent runs against the stock mock; Operate | B01, B07, B08, B15, B17, B21, B24 | Accurate availability (A01 to A03, A04) |
| NFR07 | Lead time: a producer sees a confirmed order at least 48 hours before its delivery or collection date | Business rule (time) | CS p. 1 (Producers) | The arrangement date that B04 sets is at least 48 hours after the order time, and the notification of B16 goes at the confirmation | A FEEL test on the date rule; the Operate timestamp of the notification | B04, B16 | Time to prepare the goods (A04) |
| NFR08 | Auditability: every payment attempt and its result are recorded with the reference, the status, the amounts and the time, so that the weekly settlement and the tax reporting have a transparent trail (DS3) | Quality attribute | CS p. 2 (Producers, Core functionality); R09 | After a run, the payment record has the reference, the status, the producer amounts, the commission and a timestamp for each attempt, including the declines | Inspection of the record and the Operate history after a demonstration run | B10, B13, B17 | Transparent audit trail (A04); tax compliance (E06) |
| NFR09 | **Proposal.** Traceability: each element of an operational model names its story (Bnn) in its documentation field, each story names its FRs and NFRs, and each FR names its process, so that i*, the strategic BPMN, the operational BPMN and the Task 2 services stay consistent | Design constraint (process) | Brief pp. 4 to 5 ("clear traceability") and p. 15; extends the README definition of done | The coverage check of section 10.3 holds, and a reviewer can go from any element to a sentence of the case study in two hops | PR review; this document | All stories; the definition of done | None (modelling constraint) |
| NFR10 | Usability for mixed technical skills: each Camunda Form asks for one decision in the words of the case study, and each notification or confirmation states the producer, the items, the arrangement, the date and the amounts in plain words. No step needs technical knowledge | Quality attribute (usability) | CS p. 1 (Producers, "without requiring extensive technical knowledge or training"), p. 2 (Customers, "clear communication") | A Form review against a short checklist: one decision, labels from the case study, no code or ID that the user must type. The confirmation and the notification show the five items | Review of the Forms and the message texts at the Sprint Review rehearsal | B02, B05, B10, B11, B14, B16 | Low effort for producers (A04); easy ordering (A01 to A03) |
| NFR11 | Deployability: both processes deploy and run on the module's Camunda 8 organisation, the job workers and the mock services run in Docker, `bpmnlint` passes, and each model has a `.png` or `.svg` export | Implementation constraint | Brief pp. 5 to 6; README definition of done; `.bpmnlintrc` | The deploy-and-run step of B22 succeeds from a clean checkout, and the BPMN lint check is green after the merge | The GitHub Actions check "BPMN lint"; the B22 script | All stories; B22 | None (platform constraint) |
| NFR12 | Maintainability: the process IDs, the file names, the job types, the error codes and the variables follow the naming rules of functionalities.md section 4.4, and each task has a documentation field (proposal, with NFR09) | Design constraint | functionalities.md section 4.4; week 10 lab | A name check over the `.bpmn` files finds no rule break, and every task has documentation | PR review; a small script in B22 | All stories; B22 | None |
| NFR13 | Replaceable external interfaces: each external service (E01 payment, E03 notification, and the stock service of W1) is behind its own job types, which carry the message contents of interactions.md section 3.1 (M05, M06, M08) and decision D6, so that the Task 2 service replaces the sandbox or mock without a change to the model | External interface | Brief p. 6 ("readiness of Task 1 components for integration into Task 2"); interactions.md sections 3.1 and 6.2 | A change of the worker's endpoint from the mock to another implementation needs no change to the `.bpmn` file | Review of the worker configuration; a demonstration with two endpoints | B10, B16, B20, B21, B23 | Readiness for Task 2 (A05) |

## 5. Summary

| ID | Functionality | Story | Priority | Points | Sprint | Traces to | Requirements |
|---|---|---|---|---|---|---|---|
| B01 | FN1 | Check the stock at checkout | Must | 3 | 2 | U2, M04, R04 | FR06; NFR04, NFR06 |
| B02 | FN1 | Amend the order when an item is unavailable | Must | 3 | 2 | U3, O01, O02 | FR06; NFR10 |
| B03 | FN1 | See the producers and the delivery or collection arrangements | Must | 3 | 2 | U4 | FR07 |
| B04 | FN1 | Receive the goods at least 48 hours after the order | Should | 2 | 3 | U4, CS p. 1 | FR07, FR15; NFR07 |
| B05 | FN1 | Review and confirm the order | Must | 2 | 2 | U5, M04 | FR08; NFR10 |
| B06 | FN1 | Create the marketplace order and split it by producer | Must | 5 | 2 | U6, R06, R10 | FR09, FR17; NFR01, NFR05 |
| B07 | FN1 | Reserve the stock for a time limit | Should | 5 | 3 | W3, S1 | FR06 (derived, W3); NFR06 |
| B08 | FN1 | Cancel or time out and release the reserved stock | Should | 3 | 3 | W3, S1 | FR06, FR08 (derived, W3); NFR06 |
| B09 | FN1 | See the food miles in the order summary | Could | 2 | 3 | R14, M16 to M18 | FR18 |
| B10 | FN2 | Pay through the sandbox payment service | Must | 5 | 2 | U7, U12, M05, M06 | FR10; NFR01, NFR02, NFR03, NFR08, NFR10, NFR13 |
| B11 | FN2 | Be told of a declined payment, and retry or cancel | Must | 3 | 2 | U9, O03, O04 | FR11; NFR03, NFR04, NFR10 |
| B12 | FN2 | Follow a retry or exception path when the payment service is unavailable | Must | 5 | 3 | U10, S3 | FR12; NFR04 |
| B13 | FN2 | Calculate the amount of each producer and the 5% commission | Must | 5 | 2 | U11, R09, S4 | FR14; NFR01, NFR05, NFR08 |
| B14 | FN2 | Receive the order confirmation after a successful payment | Must | 2 | 2 | U8, M07 | FR13; NFR10 |
| B15 | FN2 | Update the stock after a successful payment | Must | 3 | 3 | U8, R07 | FR13; NFR06 |
| B16 | FN2 | Notify each producer of its order element | Must | 3 | 3 | U8, M08, M09, R08 | FR13, FR15; NFR07, NFR10, NFR13 |
| B17 | FN2 | Cancel the order and release the stock after the last failed payment | Should | 3 | 3 | S3 (proposal) | FR11, FR12 (derived, S3); NFR04, NFR06, NFR08 |
| B18 | Input | Browse and search for products | Should | 5 | Not planned | U1, P03 | FR03, FR04 |
| B19 | Input | Add products from several producers to a basket | Should | 3 | Not planned | U1, P03, R05 | FR05 |
| B20 | Enabler | Run the sandbox or mock payment service with a controllable outcome | Must | 3 | 2 | M05, M06, E01 | Supports FR10 to FR12; NFR02, NFR04, NFR13 |
| B21 | Enabler | Run a mock stock service with check, reserve, release and update | Should | 3 | 2 | W1, A3, R04, R07 | Supports FR06, FR13; NFR04, NFR06, NFR13 |
| B22 | Enabler | Deploy both processes to Camunda 8 and start the job workers with one script | Must | 3 | 2 | README definition of done | Supports all; NFR11, NFR12 |
| B23 | Enabler | Run a notification stub that records each producer notification | Should | 2 | 3 | M08, M09, E03, A5 | Supports FR13, FR15; NFR04, NFR13 |
| B24 | Enabler | Load test products, stock and producers from Use Case 1 | Must | 2 | 2 | R04, UC1 | Supports FR06 (test data for FR01); NFR06 |

**Total:** 78 points in 24 stories: 65 in the 19 functional stories and 13 in the 5 enabler stories. 50 are Must (16 in FN1, 26 in FN2 and 8 in the enablers), 26 are Should and 2 are Could. Sprint 2 plans 42 points and Sprint 3 plans 28 points. B18 and B19 are the 8 points that are not planned. The owners are set in 2.7 ([#91](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/91)).

## 6. FN1 Process order (P04)

Owning function: F02 Orders. The process starts when the customer proceeds to checkout (M04) and ends when the marketplace order and its producer order elements exist (R06).

### B01 Check the stock at checkout

As a customer I can have the stock of each item in my basket checked when I go to checkout, so that I do not order goods that the producers cannot supply.

- **Given** a basket and a stock level for each product, **when** the customer proceeds to checkout, **then** the process compares the requested quantity of each item with its stock.
- **Given** that every item is available in the requested quantity, **when** the check ends, **then** the process continues to the identification of the producers (B03).
- **Given** that an item is unavailable or has too little stock, **when** the check ends, **then** the process follows the amendment path (B02) and does not create an order.

Priority: Must. Points: 3. Sprint: 2. Traces to: U2, M04, R04. Planned element: service task `check-stock` and an exclusive gateway. Requirements: FR06; NFR04, NFR06.

### B02 Amend the order when an item is unavailable

As a customer I can change my order when an item is unavailable or the stock is too low, so that I can still complete the purchase.

- **Given** an item that fails the check, **when** the process finds it, **then** the customer sees which item is short and how many are available (O01).
- **Given** the notice, **when** the customer changes the quantity or removes the item and submits (O02), **then** the check of B01 runs again on the amended order.
- **Given** that the customer removes all the items, **then** the process ends without an order.

Priority: Must. Points: 3. Sprint: 2. Traces to: U3, O01, O02. Planned element: user task with a Camunda Form, and a loop back to the check. Requirements: FR06; NFR10.

### B03 See the producers and the delivery or collection arrangements

As a customer I can see which producers supply my order and the delivery or collection arrangement of each, so that I know who is responsible for each part of it.

- **Given** an available basket, **when** the process identifies the producers, **then** the order summary lists each producer with its items and its delivery or collection arrangement.
- **Given** a basket with items from several producers, **then** the summary shows each producer as a separate part of the order.
- **Given** the assumption that each producer delivers its goods or that the customer collects them (Q1 in actors.md), **then** no logistics partner appears in the summary.

Priority: Must. Points: 3. Sprint: 2. Traces to: U4, CS p. 2. Planned element: service tasks `identify-producers`, and a FEEL expression or a business rule task for the arrangement. Requirements: FR07.

### B04 Receive the goods at least 48 hours after the order

As a producer I can prepare an order at least 48 hours before the delivery or collection, so that I have the time to prepare the goods.

- **Given** an order placed at a given time, **when** the process sets the delivery or collection date of each producer, **then** the date is at least 48 hours after the order.
- **Given** a date that the rule does not allow, **then** the process moves it to the first allowed date, and the summary shows the date.

Priority: Should. Points: 2. Sprint: 3. Traces to: U4, CS p. 1. Planned element: FEEL expression in an output mapping. The agreed delivery assumption (Q1, A4) decides the exact rule. Requirements: FR07, FR15; NFR07.

### B05 Review and confirm the order

As a customer I can review the order summary and confirm the purchase, so that I commit only to an order that I have checked.

- **Given** the summary of B03, **when** the customer opens it, **then** it shows the items, the producers, the arrangements and the total.
- **Given** the summary, **when** the customer confirms, **then** the process creates the marketplace order (B06).
- **Given** the summary, **when** the customer cancels, **then** the process ends and no order exists.

Priority: Must. Points: 2. Sprint: 2. Traces to: U5, M04 (D2 in interactions.md). Planned element: user task with a Camunda Form. Requirements: FR08; NFR10.

### B06 Create the marketplace order and split it by producer

As the network I can create the marketplace order and split it into one order element for each producer, so that each producer sees and fulfils only its own part.

- **Given** a confirmed order, **when** the process creates it, **then** one marketplace order exists, with an order ID.
- **Given** an order with items from several producers, **then** it has one producer order element for each producer, and each element holds only the items of that producer and its arrangement.
- **Given** the elements, **then** the amounts of the elements add up to the order total.
- **Given** the order, **then** its record links the customer, the products and the producers, so that a quality concern can be traced later (R10).
- **Given** the order, **when** the process ends, **then** it gives the order ID, the elements, the amounts and the reservation to FN2 (R06).

Priority: Must. Points: 5. Sprint: 2. Traces to: U6, R06, R10. Planned element: service tasks `create-order` and `split-order`, and process variables for the elements. Requirements: FR09, FR17; NFR01, NFR05.

### B07 Reserve the stock for a time limit

As the network I can reserve the stock of an order for a time limit, so that two customers cannot buy the last unit of a product.

- **Given** a confirmed order, **when** the process creates it, **then** the stock of each item is reserved and the reservation has an expiry time.
- **Given** a reservation, **when** the payment succeeds before the expiry, **then** FN2 turns the reservation into a stock update (B15).
- **Given** a reservation that expires before the payment, **then** the process follows the recovery path that Sprint 2 agrees (S1).

Priority: Should. Points: 5. Sprint: 3. Traces to: W3, S1 of functionalities.md. **Proposal.** UC2 does not state a reservation. The group confirms the reservation, the time limit and the expiry in Sprint 2. Requirements: FR06 (derived, W3); NFR06.

### B08 Cancel or time out and release the reserved stock

As a customer I can cancel the order, or let it expire, so that the reserved stock is released for other customers.

- **Given** a reservation, **when** the customer cancels at the review, **then** the reservation is released.
- **Given** an order that is not confirmed within the time limit, **when** the timer ends, **then** the reservation is released and the process ends.

Priority: Should. Points: 3. Sprint: 3. Traces to: W3, S1. Planned element: interrupting timer boundary event on the review task. **Proposal**, as for B07. Requirements: FR06, FR08 (derived, W3); NFR06.

### B09 See the food miles in the order summary

As a customer I can see the distance that my goods travel, so that I can judge the environmental effect of my order.

- **Given** the postcode of the customer and of each farm, **when** the summary shows an item, **then** it shows the distance between them.
- **Given** a missing or an invalid postcode, **then** the summary shows no distance, and the order continues.

Priority: Could. Points: 2. Sprint: 3. Traces to: R14, M16 to M18, CS p. 2. Planned element: optional service task. It depends on Q3 (the postcode service is external or internal). Requirements: FR18.

## 7. FN2 Process payment (P05)

Owning function: F03 Finance, with F01 (the stock) and F02 (the producer notifications). The process starts when FN1 gives a confirmed order that needs payment (R06).

### B10 Pay through the sandbox payment service

As a customer I can pay for my order through the payment service, so that my order is paid and can be confirmed.

- **Given** an order awaiting payment, **when** the process submits it, **then** the payment request carries the order reference and the total (M05).
- **Given** a request, **then** the payment service is a sandbox (for example Stripe test mode) or a mock service in Docker. No live payment system and no real financial data are used (CS p. 1).
- **Given** the payment form, **then** it does not ask for a card number or a card security code, including sandbox card details (functionalities.md section 4.3). It offers a simulated payment option or takes a sandbox payment reference.
- **Given** a response, **when** it arrives (M06), **then** the process reads it as success, decline or explicit service error.

Priority: Must. Points: 5. Sprint: 2. Traces to: U7, U12, M05, M06. Planned element: user task with a Camunda Form, and service task `submit-payment`. Requirements: FR10; NFR01, NFR02, NFR03, NFR08, NFR10, NFR13.

### B11 Be told of a declined payment, and retry or cancel

As a customer I am told when my payment is declined and can retry or cancel, so that a declined payment does not lose my order.

- **Given** a decline response, **when** the process reads it, **then** the customer sees a declined notice (O03).
- **Given** the notice, **when** the customer chooses to retry (O04), **then** the process submits the payment again.
- **Given** the notice, **when** the customer chooses to cancel, **then** the process follows B17.
- **Given** a declined payment, **then** the order is not confirmed.

Priority: Must. Points: 3. Sprint: 2. Traces to: U9, O03, O04. Planned element: the worker throws the BPMN error `PAYMENT_DECLINED`, an error boundary event catches it, and a user task with a Camunda Form offers the retry or the cancellation (functionalities.md section 4.3). Requirements: FR11; NFR03, NFR04, NFR10.

### B12 Follow a retry or exception path when the payment service is unavailable

As the network I can retry or follow an exception path when the payment service does not respond, so that the process does not simply stop.

- **Given** a payment service that returns an error or does not respond, **when** the process detects it, **then** it follows a retry path and not a plain end event.
- **Given** the retry path, **then** it has a limit of attempts and a wait, which Sprint 2 agrees (S3).
- **Given** that the last attempt fails, **then** the process follows B17, and the customer is told.
- **Given** the failure, **then** job retries and incidents stay separate from the BPMN errors that the workers throw.

Priority: Must. Points: 5. Sprint: 3 (the first path in Sprint 2). Traces to: U10, S3 of functionalities.md. Planned element: timer event or a retry counter with an exclusive gateway, and the error `PAYMENT_SERVICE_UNAVAILABLE`. The cancellation after the last attempt is a **proposal**. Requirements: FR12; NFR04.

### B13 Calculate the amount of each producer and the 5% commission

As the network I can calculate the amount that belongs to each producer and the 5% commission of the marketplace, so that each producer is paid correctly later.

- **Given** an order with several producer elements, **when** the payment succeeds, **then** the process records the amount of each producer and the commission.
- **Given** the amounts, **then** the commission is 5% of the order, and the producer amounts plus the commission equal the order total.
- **Given** an amount that does not divide exactly, **then** the rounding rule of S4 applies, and the rounded amounts still add up to the total.
- **Given** the result, **then** the payment record keeps the amounts for the weekly settlement (R09).

Priority: Must. Points: 5. Sprint: 2. Traces to: U11, R09, S4. Planned element: FEEL expressions in output mappings, or a DMN decision table. Requirements: FR14; NFR01, NFR05, NFR08.

### B14 Receive the order confirmation after a successful payment

As a customer I receive a confirmation after my payment succeeds, so that I know that my order is placed.

- **Given** a successful payment, **when** the process ends the payment, **then** the order status is confirmed.
- **Given** the confirmation, **then** it shows the producers, the arrangements and the totals (M07).
- **Given** a declined or a failed payment, **then** the customer does not receive a confirmation.

Priority: Must. Points: 2. Sprint: 2. Traces to: U8, M07. Planned element: service task `confirm-order`. Requirements: FR13; NFR10.

### B15 Update the stock after a successful payment

As the network I can update the stock after a payment succeeds, so that the catalogue and the next availability check are accurate.

- **Given** a successful payment, **when** the process confirms the order, **then** the stock of each item falls by the ordered quantity (R07).
- **Given** a reservation (B07), **then** the stock update replaces it.
- **Given** the update, **then** F01 performs it and the product-listing process does not restart.
- **Given** that the update and the producer notifications (B16) do not depend on each other, **then** they run in parallel.

Priority: Must. Points: 3. Sprint: 3. Traces to: U8, R07. Planned element: service task `update-stock`, on a parallel branch. Requirements: FR13; NFR06.

### B16 Notify each producer of its order element

As a producer I am told of each order element that I must fulfil, with its arrangement, so that I can prepare the goods.

- **Given** a successful payment, **when** the process confirms the order, **then** each producer receives one notification for its own element (M09).
- **Given** an order with several producers, **then** the process sends one notification for each element, and not one for the whole order.
- **Given** the notification, **then** it holds the items, the delivery or collection arrangement and the date.
- **Given** the notification service (E03), **then** the network sends the request (M08) and E03 delivers it.

Priority: Must. Points: 3. Sprint: 3. Traces to: U8, M08, M09, R08. Planned element: multi-instance service task `notify-producer`. It depends on Q3 (the notification service is external). Requirements: FR13, FR15; NFR07, NFR10, NFR13.

### B17 Cancel the order and release the stock after the last failed payment

As a customer I am told when my order is cancelled after a failed payment, so that I know that nothing is reserved or charged.

- **Given** that the customer cancels after a decline, or that the last retry fails, **when** the process ends, **then** the order is cancelled.
- **Given** the cancellation, **then** the stock is released and the customer is told.
- **Given** the cancellation, **then** no confirmation and no producer notification is sent.

Priority: Should. Points: 3. Sprint: 3. Traces to: S3 of functionalities.md. **Proposal.** UC2 asks for an exception or retry path, not for a cancellation. Requirements: FR11, FR12 (derived, S3); NFR04, NFR06, NFR08.

## 8. Input to FN1 (P03)

These two stories are the first sentence of UC2. P03 is the input of FN1 and is not one of the two functionalities (functionalities.md section 2.2). The group does not plan them in Sprint 2 or Sprint 3. They stay in the backlog so that the backlog covers UC2. If the module team requires UC2 in full, the group plans them.

### B18 Browse and search for products

As a customer I can browse the marketplace by category and search for products, so that I can find the goods that I want to buy.

- **Given** the products in the catalogue, **when** the customer browses a category, **then** the list shows its products with the harvest date, the farm origin and the seasonal availability.
- **Given** a search term, **then** the results list the products that match.

Priority: Should. Points: 5. Sprint: Not planned. Traces to: U1, P03, CS p. 2. Requirements: FR03, FR04.

### B19 Add products from several producers to a basket

As a customer I can add products from one or more producers to my basket, so that I can check out one order.

- **Given** a product, **when** the customer adds it, **then** the basket holds it with its quantity.
- **Given** products from several producers, **then** one basket holds them all.
- **Given** the basket, **when** the customer proceeds to checkout, **then** FN1 starts with the basket (M04).

Priority: Should. Points: 3. Sprint: Not planned. Traces to: U1, P03, R05. Requirements: FR05.

## 9. Enabler stories

Sprint 2 must show "initial executable Camunda processes" and "initial service-task implementation where appropriate" (UWE Bristol, 2026c, pp. 5 to 6). These stories are the setup that the functional stories need before they can run: the services that the processes call, the deployment, and the test data. They have the same fields as the functional stories, with the development team as the role. All five are **proposals**. They belong to task 6.1 of the Sprint 2 plan on the Task 1 board (the Camunda automation criterion), and 2.7 ([#91](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/91)) sets their owners.

### B20 Run the sandbox or mock payment service with a controllable outcome

As the development team I can run the payment service (E01) as a sandbox or a mock with an outcome that I choose, so that FN2 demonstrates the success, the decline and the unavailable paths on demand.

- **Given** the mock service in Docker, or a sandbox in test mode, **when** the worker `submit-payment` sends a request with a chosen outcome, **then** the service returns success, decline or no response, and the request and the response carry the contents of M05 and M06.
- **Given** the repository, **then** it holds no live key and no real financial data (NFR02).
- **Given** the demonstration, **when** the outcome is set to "unavailable", **then** FN2 follows the retry path of B12 and not an incident.

Priority: Must. Points: 3. Sprint: 2. Traces to: M05, M06, E01. Planned element: a Docker service, or a Stripe test mode account, behind the worker `submit-payment` (the unavailable outcome needs the mock). Requirements: Supports FR10 to FR12; NFR02, NFR04, NFR13.

### B21 Run a mock stock service with check, reserve, release and update

As the development team I can run a mock stock service with check, reserve, release and update operations, so that FN1 has a service interaction (W1, A3) and FN2 can update the stock.

- **Given** the test stock of B24, **when** `check-stock` runs, **then** the service returns the availability of each item.
- **Given** two concurrent reservations of the last unit of a product, **then** one succeeds and the other fails (NFR06).
- **Given** a successful payment, **when** `update-stock` runs, **then** the stock falls by the ordered quantity and the reservation is closed.

Priority: Should (A3 is pending). Points: 3. Sprint: 2 (the reserve and the release in Sprint 3, with B07 and B08). Traces to: W1, A3, R04, R07. Planned element: a Docker service behind the workers `check-stock` and `update-stock`. In Task 2 it becomes part of the product service. Requirements: Supports FR06, FR13; NFR04, NFR06, NFR13.

### B22 Deploy both processes to Camunda 8 and start the job workers with one script

As the development team I can deploy both processes to Camunda 8 and start the job workers with one script, so that every pull request tests its model in the same way and the definition of done can be checked.

- **Given** a clean checkout, **when** the script runs, **then** `process_order` and `process_payment` deploy to the module's Camunda 8 organisation and the workers start.
- **Given** the deployment, **when** a test instance starts with the test data of B24, **then** it completes the happy path of FN1 and FN2.
- **Given** the `.bpmn` files, **then** `bpmnlint` passes and a name check finds no break of the naming rules (NFR12).

Priority: Must. Points: 3. Sprint: 2. Traces to: README definition of done, functionalities.md section 4.4. Planned element: a script in `task1-bpmn/` (deploy, start the workers, start a test instance) and a Docker Compose file for the mock services. Requirements: Supports all; NFR11, NFR12.

### B23 Run a notification stub that records each producer notification

As the development team I can run a stub of the notification service (E03) that records each notification that it receives, so that B16 can be demonstrated and the notifications can be inspected.

- **Given** a confirmed order with several producer elements, **when** `notify-producer` runs, **then** the stub holds one record for each element, with the contents of M09 (the items, the arrangement and the date).
- **Given** the stub, **when** it is unavailable, **then** FN2 follows a modelled path (NFR04) and the order stays confirmed.

Priority: Should (A5 is pending). Points: 2. Sprint: 3. Traces to: M08, M09, E03, A5. Planned element: a Docker service behind the worker `notify-producer`. If A5 makes E03 internal, the stub becomes part of the platform and the story stays. Requirements: Supports FR13, FR15; NFR04, NFR13.

### B24 Load test products, stock and producers from Use Case 1

As the development team I can load test products, stock and producers, so that FN1 and FN2 run on realistic data without the processes of Use Case 1 (P01, P02).

- **Given** the seed file, **when** the stock service starts, **then** at least three producers and ten products with stock exist, each product with a name, a price, an availability timeframe and a farm origin (FR01, FR04).
- **Given** the seed, **then** one product has a stock of 1, for the oversell test of NFR06, and one producer has a collection arrangement and another a delivery arrangement (FR07).
- **Given** the seed, **then** it holds no real person and no real business (the case study is fictitious, CS p. 1).

Priority: Must. Points: 2. Sprint: 2. Traces to: R04, UC1, use-case.md ("The group uses test data for it"). Planned element: a seed file in the stock mock of B21. Requirements: Supports FR06 (test data for FR01); NFR06.

## 10. Traceability

### 10.1 The chain from the case study to Task 2

Each story sits on one chain. The chain starts at a page of the case study, passes through a requirement of section 3 or 4, a sentence of UC2, an element of the strategic model (Figure 1) and the story, and ends at an element of the operational model (Figure 2) and a service of the Task 2 system. The table gives the chain of each functionality. The columns of section 5 give it for each story.

| Link | FN1 Process order | FN2 Process payment |
|---|---|---|
| Case study | CS p. 2: checkout for single-vendor and multi-vendor orders, the aggregation of multi-vendor orders, and the records that link customers, products and producers | CS p. 2: secure payment for single and multiple vendor orders, and the 5% commission. CS p. 1: order visibility for the producers |
| Requirements | FR06 to FR09, FR15 (B04), FR17 and FR18 (optional); NFR01, NFR04 to NFR07 and NFR09 to NFR13 | FR10 to FR15; NFR01 to NFR13 |
| UC2 | U2 to U6 | U7 to U12 |
| Strategic model | P04 in the F02 Orders lane; M04, O01, O02; R04, R06 | P05 in the F03 Finance lane, with F01 and F02; M05 to M09, O03, O04; R06 to R09 |
| Stories | B01 to B09 | B10 to B17 |
| Operational model | `process_order`, the call activity that 1.6 ([#84](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/84)) adds to Figure 1; the job types `check-stock`, `identify-producers`, `create-order` and `split-order`; a timer boundary event (B08) | `process_payment`, the other call activity of 1.6; the job types `submit-payment`, `confirm-order`, `update-stock` and `notify-producer`; the errors `PAYMENT_DECLINED` and `PAYMENT_SERVICE_UNAVAILABLE` |
| Enablers | B21, B22, B24 | B20, B22, B23 |
| Task 2 service | Order service | Payment service |
| GitHub | The Sprint 2 tasks on the Task 1 board: 5.2 ([#146](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/146)) models the diagram, and 6.1 makes it executable in Camunda, with the enablers B21, B22 and B24. 2.7 ([#91](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/91)) sets the owners, and 7.6 plans Sprint 3 from this backlog | 5.4 ([#147](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/147)) models the diagram, and 6.1 makes it executable, with B20, B22 and B23. The owners and Sprint 3 as for FN1 |

### 10.2 From a requirement to its stories, and back

The Stories column of section 3 and the Applies to column of section 4 give the stories of each requirement. The Requirements column of section 5, and the Requirements line under each story, give the requirements of each story. The two directions were checked against each other: every pair appears in both, with two kinds of entry that are listed once. The Supports entries of B20 to B24 appear under the stories and in section 5 only, because an enabler supports a requirement without realising it. The requirements that apply to all stories (NFR09, NFR11 and NFR12) appear in section 4 only. B07, B08 and B17 are **derived**: they come from the proposals W3 and S3 of functionalities.md and not from a sentence of a source, and they say so.

### 10.3 Coverage check

- Every functional requirement in Task 1 scope (FR06 to FR15, FR17 and FR18) has at least one story.
- Every functional story (B01 to B19) realises at least one functional requirement. Every enabler story (B20 to B24) supports at least one.
- Eight functional requirements have no Task 1 story. FR03, FR04 and FR05 are B18 and B19, which the group does not plan. FR01, FR02, FR16, FR19 and FR20 are Task 2, and each names its process and is marked Task 2. None is lost.
- Every non-functional requirement applies to at least one story, or to the definition of done (NFR09, NFR11 and NFR12).
- Every strategic element of UC2 (M04 to M09, O01 to O04 and R04 to R09) appears in the Traces to of at least one story.

### 10.4 Open points that move the traces

The traces above hold for the current answers to the open questions. The module team answers A1 to A5 and Q1 to Q3, the group settles S1 to S4 in Sprint 2, and this table says what moves when an answer differs.

| Question | Where | If the answer differs |
|---|---|---|
| A1, A2 (the two functionalities) | functionalities.md section 6.2 | Sections 3 to 10 are rewritten for the new FN1 and FN2 |
| A3 (the mock stock service) | functionalities.md section 6.2 | "No" removes B21 and the stock rows of NFR04 and NFR13, and the service interaction of B01 and B15 becomes an internal task; B24 then seeds the internal stock data |
| A4 (delivery or collection by the producer) | actors.md Q1 | "No" adds a logistics participant: B03, B04 and FR07 gain the partner, and NFR07 gains its lead time |
| A5 (E03 and E04 external) | actors.md Q3 | "Internal" removes the E03 row of NFR13. B23 stays as an internal stub, and B09 and B16 keep their behaviour |
| S1 (the reservation) | functionalities.md section 7 | "No reservation" removes B07 and B08, and NFR06 keeps only the check and the update |
| S3 (the retries) | functionalities.md section 7 | Sets the attempts and the wait in B12 and NFR04. "No cancellation" removes B17 |
| S4 (the rounding) | functionalities.md section 7 | Sets the rule in B13 and NFR05 |
| Q2 (who pays the settlements) | actors.md section 5 | Changes FR16 only (Task 2) |

## 11. References

The key 2026d is the week 8 lecture, which functionalities.md cites and this document does not. The week 9 lecture takes the next key, 2026e, so that one key means one source across the folder.

UWE Bristol (2026a) *Bristol Regional Food Network: digital marketplace* [Case study]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [case_study/Case Study - v2.pdf](../case_study/Case%20Study%20-%20v2.pdf).

UWE Bristol (2026b) *Assessment Task 1 use cases* [Assessment material]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Use Case 2 is in [case_study/Case_study.txt](../case_study/Case_study.txt).

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [breif/](../breif/).

UWE Bristol (2026e) *Requirements handling* [Lecture slides, week 9]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [lectures/w09 - Requirements Handling (lecture).pdf](../lectures/w09%20-%20Requirements%20Handling%20%28lecture%29.pdf).
