# Content of the i* SD and SR models

**Author:** Royden Dias

**Status:** Initial Draft.

## 1. Purpose and scope

This document lists every element of the i* Strategic Dependency (SD) model and the Strategic Rationale (SR) model before they are drawn in OpenOME. The group can review the content here, and the diagrams follow it.

- **SD model:** The whole enterprise. It uses the actors of the strategic BPMN model (Figure 1), plus the regulators and the tax authority, which [actors.md](../../requirements/strategic/actors.md) marks as "i* only".
- **SR model:** Opens the four actors of Use Case 2 (Customer, Producer, BRF Network and Marketplace platform), so that it links to FN1 Process order and FN2 Process payment ([functionalities.md](../../requirements/scope/functionalities.md)).

The IDs of the other documents are used throughout: A01 to A07 and E01 to E06 ([actors.md](../../requirements/strategic/actors.md)), F01 to F05 and P01 to P11 ([processes.md](../../requirements/strategic/processes.md)), M01 to M22 and O01 to O04 ([interactions.md](../../requirements/strategic/interactions.md)), and B01 to B24 and NFR01 to NFR13 ([product-backlog.md](../../requirements/product-backlog.md)).

## 2. Notation

OpenOME uses the original i* notation. This document uses its names. The iStar 2.0 names are in brackets, for anyone who reads the models in another tool.

| Element or link | Meaning in these models |
|---|---|
| Goal | A state that the actor wants. The actor does not say how to reach it |
| Softgoal (quality) | A quality with no clear-cut test, judged as "good enough" |
| Task | A particular way of doing something |
| Resource | A physical or information entity |
| Dependency | Depender → dependum → dependee. The type of the dependum gives the freedom of the dependee: a goal leaves the "how" to the dependee, a task prescribes it |
| Means-end (OR-refinement) | A task is one way to reach a goal. Two means for one end are alternatives |
| Decomposition (AND-refinement) | A task needs all its parts: subgoals, subtasks, resources and softgoals |
| Contribution | The effect of an element on a softgoal: Make, Help, Hurt or Break |
| Is-a, is-part-of | Specialisation of an actor, and an actor inside another actor |

## 3. Actors

| ID | Actor | i* type | Strategic BPMN element | Note |
|---|---|---|---|---|
| A01 to A03 | Customer | Role | Customer pool | The order process treats all three segments the same |
| A01 | Household customer | Role, is-a Customer | Customer pool | Young professionals and families (CS p. 1) |
| A02 | Community group buyer | Role, is-a Customer | Customer pool | Educational, care and voluntary organisations (CS p. 1) |
| A03 | Restaurant or café buyer | Role, is-a Customer | Customer pool | Independent restaurants and cafés (CS p. 1) |
| A04 | Producer | Role | Producer pool | One of 40 SMEs. Delivers or hands over its part of the order (assumption, Q1) |
| A05 | BRF Network | Agent | BRF Network pool | The organisation: its business goals, rules and decisions |
| A06 | Marketplace administrator | Role, is-part-of BRF Network | Quality and traceability lane (F04) | UC3 only |
| A07 | Authorised marketplace representative | Role, is-part-of BRF Network | Quality and traceability lane (F04) | UC3 only |
| SYS | Marketplace platform | Agent | The automated activities in the lanes F01 to F05 | The system to be built. Its tasks become the service tasks of the operational models and the Task 2 services (decision DI2) |
| E01 | Payment service | Agent | Payment service pool | Sandbox or mock only (NFR02) |
| E02 | Organic certification verification service | Agent | Organic certification verification service pool | UC1 |
| E03 | Notification service | Agent | Notification service pool | External (assumption, Q3) |
| E04 | Postcode distance service | Agent | Postcode distance service pool | External (assumption, Q3) |
| E05 | Data protection and financial services regulators | Actor | Not in BPMN | i* only (actors.md) |
| E06 | Tax authority | Actor | Not in BPMN | i* only (actors.md) |

## 4. Strategic Dependency model

Each row is one dependency. "UC2" in the last column marks the dependencies that the SR model opens.

### 4.1 Customer and Marketplace platform

| ID | Depender | Dependum | Type | Dependee | Source | Scope |
|---|---|---|---|---|---|---|
| SD01 | Customer | Multi-vendor order processed | Goal | Marketplace platform | P04, M04, UC2 | UC2 |
| SD02 | Customer | Product information (harvest date, farm origin, seasonal availability, allergens) | Resource | Marketplace platform | P03, CS p. 2 | UC2 |
| SD03 | Customer | Accurate availability | Softgoal | Marketplace platform | NFR06, B01, B07 | UC2 |
| SD04 | Customer | Order confirmation (producers, arrangements, totals) | Resource | Marketplace platform | M07, B14 | UC2 |
| SD05 | Customer | Clear supplier responsibilities | Softgoal | Marketplace platform | CS p. 2, B03 | UC2 |
| SD06 | Customer | Secure payment | Softgoal | Marketplace platform | NFR03, B10 | UC2 |
| SD07 | Marketplace platform | Review and confirm order | Task | Customer | M04, B05 | UC2 |
| SD08 | Marketplace platform | Amend unavailable items | Task | Customer | O01, O02, B02 | UC2 |
| SD09 | Marketplace platform | Sandbox payment reference | Resource | Customer | B10, NFR03 (no card data) | UC2 |

### 4.2 Producer

| ID | Depender | Dependum | Type | Dependee | Source | Scope |
|---|---|---|---|---|---|---|
| SD10 | Customer | Goods delivered or collected | Goal | Producer | P06, actors.md section 4 | UC2 |
| SD11 | Marketplace platform | Product listing and updates | Resource | Producer | M01, P01 | UC2 |
| SD12 | Marketplace platform | Accurate stock levels | Softgoal | Producer | P04 responsibilities, NFR06 | UC2 |
| SD13 | Marketplace platform | Delivery or collection arrangements | Resource | Producer | P04 responsibilities, B03 | UC2 |
| SD14 | Producer | New order notification | Resource | Marketplace platform | M08, M09, B16 | UC2 |
| SD15 | Producer | Adequate lead time (48 hours or more) | Softgoal | Marketplace platform | NFR07, B04, CS p. 1 | UC2 |
| SD16 | Producer | Easy listing and updates | Softgoal | Marketplace platform | NFR10, CS p. 1 | Wider |
| SD17 | Producer | Weekly settlement with statement | Resource | BRF Network | M10, P07 | UC2 |
| SD18 | Producer | Transparent audit trail | Softgoal | BRF Network | NFR08, CS p. 2 | UC2 |

### 4.3 BRF Network and Marketplace platform

These dependencies are the socio-technical boundary: what the organisation expects from its system, and what the system needs from the organisation.

| ID | Depender | Dependum | Type | Dependee | Source | Scope |
|---|---|---|---|---|---|---|
| SD19 | BRF Network | 5% commission calculated | Goal | Marketplace platform | B13, NFR05, P05 | UC2 |
| SD20 | BRF Network | Payment and settlement records | Resource | Marketplace platform | DS3, NFR08 | UC2 |
| SD21 | Marketplace platform | Business rules (commission rate, reservation time limit, retry policy) | Resource | BRF Network | W3, S1, S3 in functionalities.md | UC2 |

### 4.4 External services

| ID | Depender | Dependum | Type | Dependee | Source | Scope |
|---|---|---|---|---|---|---|
| SD22 | Marketplace platform | Payment processed | Goal | Payment service | M05, M06 | UC2 |
| SD23 | Marketplace platform | Payment service availability | Softgoal | Payment service | UC2 exception path, NFR04 | UC2 |
| SD24 | Marketplace platform | Notifications delivered | Goal | Notification service | M08, M14, M20 | UC2 |
| SD25 | Marketplace platform | Organic certification verified | Goal | Organic certification verification service | M02, M03, P02 | Wider |
| SD26 | Marketplace platform | Postcode distance | Resource | Postcode distance service | M17, M18, P09 | Wider |

### 4.5 Customer segments

These show why the three segments are separate in actors.md: each one has a different expectation.

| ID | Depender | Dependum | Type | Dependee | Source | Scope |
|---|---|---|---|---|---|---|
| SD27 | Household customer | Convenient ordering (not limited to farm shop hours) | Softgoal | Marketplace platform | CS p. 1 | UC2 |
| SD28 | Community group buyer | Reliable, consistent suppliers | Softgoal | BRF Network | CS p. 1 | UC2 |
| SD29 | Restaurant or café buyer | Low supplier admin | Softgoal | Marketplace platform | CS p. 1 | UC2 |

### 4.6 Compliance and quality

| ID | Depender | Dependum | Type | Dependee | Source | Scope |
|---|---|---|---|---|---|---|
| SD30 | Customer | Personal data protected | Softgoal | BRF Network | NFR01 | Wider |
| SD31 | Regulators | Regulations complied with | Goal | BRF Network | NFR01, CS p. 2 | Wider |
| SD32 | Tax authority | Producer tax report | Resource | Producer | P07, E06 in actors.md | Wider |
| SD33 | Marketplace administrator | Records linking customers, products and producers | Resource | Marketplace platform | R10, DS2, CS p. 2 | Wider |
| SD34 | Marketplace administrator | Quality concern report | Resource | Customer | M11, UC3 | Wider |
| SD35 | Marketplace administrator | Incident information | Resource | Producer | M12, UC3 | Wider |
| SD36 | Customer | Food safety notification | Resource | BRF Network | M14, M15, UC3 | Wider |
| SD37 | Authorised marketplace representative | Incident report | Resource | Marketplace administrator | UC3 | Wider |

### 4.7 Community features

| ID | Depender | Dependum | Type | Dependee | Source | Scope |
|---|---|---|---|---|---|---|
| SD38 | BRF Network | Surplus produce report | Resource | Producer | M19, P10 | Wider |
| SD39 | BRF Network | Educational content | Resource | Producer | M22, P11 | Wider |
| SD40 | Customer | Food miles information | Resource | Marketplace platform | M16, P09, B09 | Wider |
| SD41 | Customer | Order issue resolved (redelivery or refund) | Goal | Marketplace platform | P12, M24, M25, D8 | Wider |

## 5. Strategic Rationale model

The SR model opens Customer, Producer, BRF Network and Marketplace platform. The other actors stay closed. The "Link" column gives the link from the element to its parent.

### 5.1 Customer

| ID | Element | Type | Link | Source |
|---|---|---|---|---|
| CU01 | Local produce bought | Goal | Top element | CS p. 1 |
| CU02 | Buy through the marketplace | Task | Means-end to CU01 | P03 to P05 |
| CU03 | Buy from farm shops and markets | Task | Means-end to CU01 (the current practice) | CS p. 1 |
| CU04 | Products found | Goal | Decomposes CU02 | P03, B18 |
| CU05 | Check out the order | Task | Decomposes CU02 | FN1 |
| CU06 | Basket | Resource | Decomposes CU05 | B19 |
| CU07 | Review and confirm order | Task | Decomposes CU05 | B05 |
| CU08 | Amend unavailable items | Task | Decomposes CU05 | B02 |
| CU09 | Pay for the order | Task | Decomposes CU02 | FN2 |
| CU10 | Give sandbox payment reference | Task | Decomposes CU09 | B10 |
| CU11 | Retry or cancel after decline | Task | Decomposes CU09 | B11 |
| CU12 | Goods received | Goal | Decomposes CU02 | P06 |
| CU13 | Convenience | Softgoal | Mainly A01 | CS p. 1 |
| CU14 | Reliable local supply | Softgoal | Mainly A02 | CS p. 1 |
| CU15 | Low supplier admin | Softgoal | Mainly A03 | CS p. 1 |
| CU16 | Quick delivery | Softgoal | All segments | Assumption (TN4) |
| CU17 | Safe payment and personal data | Softgoal | All segments | NFR01, NFR03 |
| CU18 | Order problems put right | Goal | Decomposes CU02 | P12, D8 |

**Contributions:**

| From | To | Contribution | Reason |
|---|---|---|---|
| CU02 Buy through the marketplace | CU13 Convenience | Help | Orders at any time |
| CU02 | CU14 Reliable local supply | Help | One place to find 40 producers |
| CU02 | CU15 Low supplier admin | Help | One checkout for many suppliers |
| CU03 Buy from farm shops and markets | CU13 | Hurt | Restricted opening hours (CS p. 1) |
| CU03 | CU14 | Hurt | Hard to find reliable sources (CS p. 1) |
| CU03 | CU15 | Break | Admin of many small suppliers is "prohibitively time-consuming" (CS p. 1) |
| CU08 Amend unavailable items | CU13 | Hurt | Extra effort when stock runs out |
| CU10 Give sandbox payment reference | CU17 | Help | No card data in the forms (NFR03) |

### 5.2 Producer

| ID | Element | Type | Link | Source |
|---|---|---|---|---|
| PR01 | Products sold to more customers | Goal | Top element | CS p. 1 |
| PR02 | Sell through the marketplace | Task | Means-end to PR01 | P01, P06 |
| PR03 | Sell by email, telephone and markets | Task | Means-end to PR01 (the current practice) | CS p. 1 |
| PR04 | List and update products | Task | Decomposes PR02 | P01, M01 |
| PR05 | Keep stock levels accurate | Task | Decomposes PR04 | P04 responsibilities |
| PR06 | Set delivery or collection arrangements | Task | Decomposes PR02 | P04 responsibilities |
| PR07 | Prepare and hand over orders | Task | Decomposes PR02 | P06 |
| PR08 | New order notification | Resource | Decomposes PR07 | M09 |
| PR09 | Weekly settlement received | Goal | Decomposes PR02 | P07 |
| PR10 | Accept 5% commission | Task | Decomposes PR02 | CS p. 2 |
| PR11 | Low effort (limited time and skills) | Softgoal | | CS p. 1, NFR10 |
| PR12 | Fair income per sale | Softgoal | | NFR05 |
| PR13 | Enough time to prepare | Softgoal | | CS p. 1, NFR07 |
| PR14 | Tax-ready accounts | Softgoal | | CS p. 2, NFR08 |

**Contributions:**

| From | To | Contribution | Reason |
|---|---|---|---|
| PR03 Sell by email, telephone and markets | PR11 Low effort | Hurt | About 15 hours each week on communication (CS p. 1) |
| PR02 Sell through the marketplace | PR11 | Help | One place for all orders |
| PR05 Keep stock levels accurate | PR11 | Hurt | Frequent seasonal updates (TN2) |
| PR10 Accept 5% commission | PR12 Fair income | Hurt | TN1 |
| PR08 New order notification | PR13 Enough time to prepare | Help | Sent 48 hours or more ahead (NFR07) |
| PR09 Weekly settlement received | PR14 Tax-ready accounts | Help | Comes with the audit trail |

### 5.3 BRF Network

| ID | Element | Type | Link | Source |
|---|---|---|---|---|
| NW01 | Local food network sustained | Goal | Top element | CS p. 1 |
| NW02 | Run the digital marketplace | Task | Means-end to NW01 | CS p. 1 |
| NW03 | Commission income earned | Goal | Decomposes NW02 | CS p. 2 |
| NW04 | Charge 5% commission on each order | Task | Means-end to NW03 | CS p. 2, P05 |
| NW05 | Set business rules | Task | Decomposes NW02 | W3, S1, S3 |
| NW06 | Settle producers weekly | Task | Decomposes NW02 | P07 |
| NW07 | Handle quality incidents | Task | Decomposes NW02 | P08, A06, A07 |
| NW08 | Promote surplus offers, food miles and education | Task | Decomposes NW02 | P09, P10, P11 |
| NW09 | Regulations complied with | Goal | Decomposes NW02 | NFR01, E05 |
| NW15 | Resolve order issues after the sale | Task | Decomposes NW02 | P12, D8 |
| NW10 | Financial viability | Softgoal | | CS p. 2 |
| NW11 | Producers attracted and kept | Softgoal | | CS p. 1 |
| NW12 | Sustainability (fewer food miles, less waste) | Softgoal | | CS p. 2 |
| NW13 | Community connections | Softgoal | | CS p. 2 |
| NW14 | Customer and producer trust | Softgoal | | CS p. 2 |

**Contributions:**

| From | To | Contribution | Reason |
|---|---|---|---|
| NW04 Charge 5% commission | NW10 Financial viability | Help | The only income in the case study |
| NW04 | NW11 Producers attracted and kept | Hurt | Lower producer income (TN1) |
| NW06 Settle producers weekly | NW11 | Help | Regular, transparent payment |
| NW07 Handle quality incidents | NW14 Trust | Help | Rapid contact when food safety is at risk (CS p. 2) |
| NW08 Promote surplus offers, food miles and education | NW12 Sustainability | Help | CS p. 2 |
| NW08 | NW13 Community connections | Help | CS p. 2 |
| NW09 Regulations complied with | NW14 | Help | NFR01 |

### 5.4 Marketplace platform

This actor holds the two functionalities. Its tasks name the planned job types of [functionalities.md](../../requirements/scope/functionalities.md) section 4.

| ID | Element | Type | Link | Source |
|---|---|---|---|---|
| MP01 | Customer order completed | Goal | Top element | UC2 |
| MP02 | Run automated checkout | Task | Means-end to MP01 | UC2 |
| MP03 | Order processed | Goal | Decomposes MP02 | FN1, P04 |
| MP04 | Payment processed | Goal | Decomposes MP02 | FN2, P05 |
| MP05 | Process order (`process_order`) | Task | Means-end to MP03 | FN1 |
| MP06 | Check stock (`check-stock`) | Task | Decomposes MP05 | B01 |
| MP07 | Ask customer to amend order | Task | Decomposes MP05 | B02, O01 |
| MP08 | Identify producers and arrangements (`identify-producers`) | Task | Decomposes MP05 | B03, B04 |
| MP09 | Get customer confirmation | Task | Decomposes MP05 | B05 |
| MP10 | Create and split marketplace order (`create-order`, `split-order`) | Task | Decomposes MP05 | B06 |
| MP11 | Product catalogue and stock | Resource | Decomposes MP05 | DS1 |
| MP12 | Stock protected during checkout | Goal | Decomposes MP05 | W3 |
| MP13 | Reserve stock for a time limit | Task | Means-end to MP12 (proposed) | B07, B08 |
| MP14 | Check stock only at payment | Task | Means-end to MP12 (alternative) | W3 |
| MP15 | Process payment (`process_payment`) | Task | Means-end to MP04 | FN2 |
| MP16 | Submit payment (`submit-payment`) | Task | Decomposes MP15 | B10, M05, M06 |
| MP17 | Calculate producer amounts and 5% commission | Task | Decomposes MP15 | B13 |
| MP18 | Confirm order and update stock (`confirm-order`, `update-stock`) | Task | Decomposes MP15 | B14, B15 |
| MP19 | Notify each producer (`notify-producer`) | Task | Decomposes MP15 | B16 |
| MP20 | Record every payment attempt | Task | Decomposes MP15 | NFR08 |
| MP21 | Declined payment handled | Goal | Decomposes MP15 | B11 |
| MP22 | Let customer retry or cancel | Task | Means-end to MP21 | O03, O04, `PAYMENT_DECLINED` |
| MP23 | Payment service failure handled | Goal | Decomposes MP15 | B12 |
| MP24 | Retry, then cancel and release stock | Task | Means-end to MP23 (proposed) | B17, S3 |
| MP25 | End the process at once | Task | Means-end to MP23 (rejected) | UC2: not "simply terminating" |
| MP26 | No oversell | Softgoal | | NFR06 |
| MP27 | Stock open to other buyers | Softgoal | | W3 |
| MP28 | Reliable checkout | Softgoal | | NFR04 |
| MP29 | Quick checkout | Softgoal | | NFR10 |
| MP33 | Handle order issue | Task | Decomposes MP01 (after the order) | P12, D8 |
| MP30 | Secure payment | Softgoal | | NFR03 |
| MP31 | Accurate amounts | Softgoal | | NFR05 |
| MP32 | Auditability | Softgoal | | NFR08 |

**Contributions:**

| From | To | Contribution | Reason |
|---|---|---|---|
| MP13 Reserve stock for a time limit | MP26 No oversell | Help | One unit cannot go to two customers (W3) |
| MP13 | MP27 Stock open to other buyers | Hurt | Abandoned checkouts hold stock until the time limit (TN3) |
| MP14 Check stock only at payment | MP26 | Hurt | Two customers can buy the last unit |
| MP14 | MP27 | Help | No stock is held |
| MP24 Retry, then cancel and release stock | MP28 Reliable checkout | Help | Every failure ends in a modelled state (NFR04) |
| MP24 | MP29 Quick checkout | Hurt | The customer waits during the retries (TN5) |
| MP25 End the process at once | MP28 | Break | Against UC2 |
| MP25 | MP29 | Help | No wait |
| MP16 Submit payment | MP30 Secure payment | Help | Sandbox reference only, no card data (NFR03) |
| MP17 Calculate producer amounts and 5% commission | MP31 Accurate amounts | Make | Amounts plus commission equal the total (NFR05) |
| MP20 Record every payment attempt | MP32 Auditability | Make | NFR08 |
| MP22 Let customer retry or cancel | MP28 | Help | A decline does not lose the order |

### 5.5 Dependencies in the SR model

In the SR model, each UC2 dependency of section 4 starts and ends at an element inside the actors.

| SD dependency | Depender element | Dependee element |
|---|---|---|
| SD01 Multi-vendor order processed | CU05 Check out the order | MP05 Process order |
| SD03 Accurate availability | CU05 Check out the order | MP13 Reserve stock for a time limit |
| SD04 Order confirmation | CU09 Pay for the order | MP18 Confirm order and update stock |
| SD06 Secure payment | CU17 Safe payment and personal data | MP16 Submit payment |
| SD07 Review and confirm order | MP09 Get customer confirmation | CU07 Review and confirm order |
| SD08 Amend unavailable items | MP07 Ask customer to amend order | CU08 Amend unavailable items |
| SD09 Sandbox payment reference | MP16 Submit payment | CU10 Give sandbox payment reference |
| SD10 Goods delivered or collected | CU12 Goods received | PR07 Prepare and hand over orders |
| SD11 Product listing and updates | MP11 Product catalogue and stock | PR04 List and update products |
| SD12 Accurate stock levels | MP06 Check stock | PR05 Keep stock levels accurate |
| SD13 Delivery or collection arrangements | MP08 Identify producers and arrangements | PR06 Set delivery or collection arrangements |
| SD14 New order notification | PR08 New order notification | MP19 Notify each producer |
| SD15 Adequate lead time | PR13 Enough time to prepare | MP08 Identify producers and arrangements |
| SD17 Weekly settlement with statement | PR09 Weekly settlement received | NW06 Settle producers weekly |
| SD19 5% commission calculated | NW04 Charge 5% commission | MP17 Calculate producer amounts and 5% commission |
| SD21 Business rules | MP13 and MP24 | NW05 Set business rules |
| SD22 Payment processed | MP16 Submit payment | Payment service (closed) |
| SD23 Payment service availability | MP23 Payment service failure handled | Payment service (closed) |
| SD24 Notifications delivered | MP19 Notify each producer | Notification service (closed) |

## 6. Tensions and competing goals

| ID | Tension | Where the models show it | Effect on the design |
|---|---|---|---|
| TN1 | The network needs its 5% commission, but the commission lowers producer income and can drive producers away | NW04 helps NW10 and hurts NW11. PR10 hurts PR12 | The commission is calculated openly and shown in the settlement statement (B13, NFR05, NFR08) |
| TN2 | Customers and the platform need accurate stock and product data, but producers have little time and mixed skills | SD12. PR05 hurts PR11 | Simple forms in the words of the case study (NFR10). Stock check and reservation in FN1 |
| TN3 | Reserving stock stops overselling, but abandoned checkouts hold stock that others could buy | MP13 and MP14 against MP26 and MP27 | A reservation with a time limit (B07, B08). The limit is open (S1) |
| TN4 | Producers need 48 hours to prepare, but customers may want quick delivery | SD15 against CU16 | Arrangement dates are at least 48 hours ahead (B04). The confirmation states the dates (M07) |
| TN5 | Retrying a failed payment keeps the sale, but the customer waits | MP24 against MP28 and MP29 | A limited retry policy, then cancellation and stock release (B12, B17). The limits are open (S3) |
| TN6 | Payment must be secure and compliant, but easy for customers | SD06, MP16, MP30, SD31 | A sandbox payment reference, with no card data in forms or variables (NFR02, NFR03) |
| TN7 | One checkout for many producers is convenient, but each producer keeps its own delivery or collection responsibilities | SD05, SD13, CU15 | The order is split by producer, and the confirmation lists each producer's arrangement (B03, B06, M07) |

## 7. Traceability

### 7.1 From the i* models to the BPMN models

The operational models are not built yet. The last two columns use the planned elements of functionalities.md section 4.

| i* element | Strategic BPMN (Figure 1) | Operational BPMN (planned) | Stories |
|---|---|---|---|
| CU07 Review and confirm order | Customer pool, Order message (M04) | `process_order`: user task with a Camunda Form | B05 |
| CU08 Amend unavailable items | Items in stock? gateway, Amend order message (M23) | `process_order`: user task and a loop back to the stock check | B02 |
| CU10 Give sandbox payment reference | Customer pool | `process_payment`: user task with a Camunda Form | B10 |
| CU11 Retry or cancel after decline | Customer pool (O03, O04) | `process_payment`: user task after `PAYMENT_DECLINED` | B11 |
| MP06 Check stock | Items in stock? gateway (Catalogue management lane), before Process order | Service task `check-stock` | B01, B21 |
| MP07 Ask customer to amend order | Amend order requested event, Amend order message (M23) | `process_order`: user task after the stock check | B02 |
| MP11 Product catalogue and stock | Not drawn; DS1 in interactions.md section 4.1 | Product service (W1) | B01 |
| MP13 Reserve stock for a time limit | Process order (Order management lane) | Reservation, with a timer boundary event on the review task | B07, B08 |
| MP08 Identify producers and arrangements | Process order (Order management lane) | Service task `identify-producers` | B03, B04 |
| MP10 Create and split marketplace order | Process order (Order management lane) | Service tasks `create-order` and `split-order` | B06 |
| MP16 Submit payment | Process payment (Finance and settlements lane), Payment service (M05, M06) | Service task `submit-payment` | B10, B20 |
| MP17 Calculate producer amounts and 5% commission | Process payment (Finance and settlements lane) | FEEL expressions in output mappings | B13 |
| MP18 Confirm order and update stock | Process payment (Finance and settlements lane), Order confirmation (M07) | Service tasks `confirm-order` and `update-stock` | B14, B15 |
| MP19 Notify each producer | Process payment (Finance and settlements lane), Notification service (M08, M09) | Multi-instance service task `notify-producer` | B16, B23 |
| MP22 Let customer retry or cancel | Payment successful? gateway | Error boundary event `PAYMENT_DECLINED` | B11 |
| MP24 Retry, then cancel and release stock | Payment not completed end event | Retry loop, then cancellation (`PAYMENT_SERVICE_UNAVAILABLE`) | B12, B17 |
| PR07 Prepare and hand over orders | Fulfil order (Producer pool) | Out of scope | None |
| NW06 Settle producers weekly | Settle producer payments (Finance and settlements lane) | Out of scope | None |
| NW07 Handle quality incidents | Handle quality incident (Quality and traceability lane) | Out of scope | None |
| CU18 Order problems put right, NW15, MP33 | Handle order issue (Order management lane), M24, M25 | Out of scope (Task 2, FR21) | None |

### 7.2 From the softgoals to the requirements

Each softgoal comes from a candidate in the last column of the non-functional requirements in [product-backlog.md](../../requirements/product-backlog.md).

| Softgoal | NFR |
|---|---|
| SD06, CU17, MP30 Secure payment | NFR01, NFR03 |
| MP28 Reliable checkout, SD23 | NFR04 |
| MP31 Accurate amounts, PR12 | NFR05 |
| SD03, SD12, MP26 Accurate availability, no oversell | NFR06 |
| SD15, PR13 Lead time | NFR07 |
| SD18, MP32, PR14 Audit trail | NFR08 |
| SD16, PR11, MP29 Low effort, quick checkout | NFR10 |
| SD30, SD31 Data protection, compliance | NFR01 |

## 8. Modelling decisions

| ID | Decision | Reason |
|---|---|---|
| DI1 | Customer is one role. The three segments are is-a specialisations, with one softgoal each | The order process treats them the same, but their needs differ (actors.md note) |
| DI2 | The Marketplace platform is an agent of its own, separate from the BRF Network | It shows the socio-technical boundary (section 4.3), and its tasks map to the service tasks and the Task 2 services |
| DI3 | The stock service (W1) is not an actor. Its work is in the platform tasks MP06 and MP13 | It becomes part of the product service in Task 2 (functionalities.md, W1) |
| DI4 | No logistics actor. Each producer delivers or hands over its goods | Assumption Q1 in actors.md. The tutor has not answered yet |
| DI5 | The notification and postcode distance services are external agents | Assumption Q3 in actors.md. The tutor has not answered yet |
| DI6 | The BRF Network pays the weekly settlement | Q2 in actors.md is open |
| DI7 | The SR model opens only the four UC2 actors. The services stay closed | Agreed scope. It keeps the SR model readable |

## 9. Questions for the stand-up

1. Does the group agree DI2 and DI3?
2. CU16 Quick delivery is an assumption, not a statement of the case study. Keep it for TN4, or remove it?
3. Should the regulators (E05) be one actor or two (data protection and financial services)?
4. Who checks the models against the operational BPMN models when they are drawn?

## 10. Source keys

CS is the case study, with the page number. UC1, UC2 and UC3 are the three use cases.