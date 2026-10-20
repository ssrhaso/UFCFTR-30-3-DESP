# 1.3 Interactions between the processes

**Authors:** Royden Dias, Hasaan Ahmad. Section 3 starts from a draft by Ishaq Modassir Mushtaq.
**Task:** [#81](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/81), Figure 1: strategic BPMN model
**Status:** draft for review

## 1. Purpose and scope

The brief requires "interactions between different areas of the enterprise" and "relationships between the principal business processes" (UWE Bristol, 2026c, p. 3). This document lists them for Figure 1. [#83](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/83) draws each message as a message flow.

The IDs come from [actors.md](actors.md) ([#79](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/79)) and [processes.md](processes.md) ([#80](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/80)). Process keys: P01 Manage products, P02 Verify organic certification, P03 Browse and search catalogue, P04 Process order, P05 Process payment, P06 Fulfil order, P07 Settle producer payments, P08 Handle quality incident, P09 Report food miles, P10 Offer surplus produce and P11 Share educational content.

Figure 1 shows a message only if it starts or ends a process, or carries a result that a participant needs (D1). The alternative and exception paths go to the operational models (Figure 2).

Source keys: CS is the case study (UWE Bristol, 2026a), with the page number. UC1, UC2 and UC3 are the use cases (UWE Bristol, 2026b).

## 2. Participants

The pools are the Customer (A01 to A03, collapsed), the Producer (A04) and the BRF Network (A05, with the lanes F01 to F05). The external participants are E01 (payment), E02 (certification) and E04 (postcode distance). E03 (notification) has no message flows (D3). E05 and E06 are not in the BPMN (actors.md).

A message flow connects two separate pools (Object Management Group, 2014). The lanes interact through sequence flows and data stores (section 5).

## 3. Messages between the participants

### 3.1 Messages in Figure 1

For the BRF Network, the brackets give the lane that sends or receives the message.

| No. | Sender | Receiver | Message | Process | Source |
|---|---|---|---|---|---|
| M01 | Producer | BRF Network (F01) | Product listing, with the eleven fields of UC1 | P01 | CS pp. 1–2, UC1 |
| M02 | Producer | BRF Network (F01) | Stock and seasonal availability update | P01 | CS pp. 1–2, UC1 |
| M03 | BRF Network (F04) | Certification service (E02) | Certification check request | P02 | UC1 |
| M04 | Certification service (E02) | BRF Network (F04) | Certification result (valid or not valid) | P02 | UC1 |
| M05 | Customer | BRF Network (F01) | Browse or search request | P03 | CS p. 2, UC2 |
| M06 | BRF Network (F01) | Customer | Product results, with the harvest dates, farm origin, seasonal availability, food miles and educational content | P03 | CS p. 2, UC2 |
| M07 | Customer | BRF Network (F02) | Order request (the basket at checkout) | P04 | CS p. 2, UC2 |
| M08 | BRF Network (F02) | Customer | Order summary for review (the producers, the delivery or collection arrangements and the totals) | P04 | CS p. 2, UC2 |
| M09 | Customer | BRF Network (F02) | Purchase confirmation | P04 | UC2 |
| M10 | BRF Network (F03) | Payment service (E01) | Payment request (the order reference and the total) | P05 | UC2 |
| M11 | Customer | Payment service (E01) | Payment details, entered on the payment page of the service | P05 | UC2, D6 |
| M12 | Payment service (E01) | BRF Network (F03) | Payment result (approved or declined) | P05 | UC2 |
| M13 | BRF Network (F03) | Customer | Order confirmation | P05 | UC2 |
| M14 | BRF Network (F02) | Producer | New order notification (the producer order element, with the delivery or collection arrangement) | P05 | CS pp. 1–2, UC2 |
| M15 | BRF Network (F03) | Producer | Weekly settlement (the payment and the audit trail statement) | P07 | CS p. 2 |
| M16 | Customer | BRF Network (F04) | Quality concern report | P08 | CS p. 2, UC3 |
| M17 | Producer | BRF Network (F04) | Quality concern report | P08 | CS p. 2, UC3 |
| M18 | BRF Network (F04) | Producer | Request for information about the incident | P08 | UC3 |
| M19 | Producer | BRF Network (F04) | Incident information | P08 | UC3 |
| M20 | BRF Network (F04) | Customer | Food safety notification | P08 | CS p. 2, UC3 |
| M21 | Customer | BRF Network (F05) | Postcode | P09 | CS p. 2 |
| M22 | BRF Network (F05) | Postcode distance service (E04) | Distance request | P09 | CS p. 2 |
| M23 | Postcode distance service (E04) | BRF Network (F05) | Distance result | P09 | CS p. 2 |
| M24 | Producer | BRF Network (F05) | Surplus produce report (with the discount) | P10 | CS p. 2 |
| M25 | BRF Network (F05) | Customer | Surplus offer | P10 | CS p. 2 |
| M26 | Producer | BRF Network (F05) | Educational content (recipe, storage guidance or farm story) | P11 | CS p. 2 |

**Notes:**

- M14 starts P06. The delivery or collection of the goods is not a message.
- M12 has two values: approved or declined. An unavailable service sends no message, so the failure of M10 starts the exception path in Figure 2. M04 follows the same rule (UC1).
- The food miles go inside M06 and M08. The educational content goes inside M06.
- The closure or escalation of an incident happens inside F04, so it has no message.
- The payer of M15 is open (Q2 in actors.md).

### 3.2 Messages for the operational models

These alternative and exception paths of UC2 are not in Figure 1 (D1). The operational model ([#49](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/49)) uses them. If the second functionality comes from UC1 or UC3 (T1 in processes.md), add its paths here.

| No. | Sender | Receiver | Message | Process | Source |
|---|---|---|---|---|---|
| O01 | BRF Network (F02) | Customer | Stock unavailable notice, with a request to amend the order | P04 | UC2 |
| O02 | Customer | BRF Network (F02) | Amended order | P04 | UC2 |
| O03 | BRF Network (F03) | Customer | Payment declined notice | P05 | UC2 |
| O04 | Customer | BRF Network (F03) | Payment retry | P05 | UC2 |

### 3.3 Changes from the 1.2 draft

The 1.2 messages M08, M09, M14 and M15 are now O01 to O04 (D1). The 1.2 message M18 is removed (D4), and M23 is replaced by the new M18 and M19 (D5). M11 is new (D6). The sources of M02, M07, M08, M14 and M15 are corrected.

## 4. Relationships between the processes

| Type | Meaning | Element in Figure 1 |
|---|---|---|
| Triggers | The outcome of the first process starts the second process | A sequence flow. Across a pool boundary, the message in the "Via" column |
| Provides data to | The second process uses data that the first process creates or keeps | The data store in the "Via" column (D7) |

### 4.1 Data stores

| ID | Data store | Content | Owner | Written by | Read by |
|---|---|---|---|---|---|
| DS1 | Product catalogue | Listings, stock, categories, certification status, allergens and best-before dates | F01 | P01, P02 | P03, P04, P08, P09 |
| DS2 | Order records | Marketplace orders and producer order elements, which link customers, products and producers | F02 | P04, P05 | P08 |
| DS3 | Payment and settlement records | Payment results, the amount of each producer, the 5% commission and the audit trail | F03 | P05, P07 | P07 |
| DS4 | Community content | Food miles, surplus offers and educational content | F05 | P09, P10, P11 | P03, P04 |

DS2 and DS3 show the linking records and the audit trail that the case study requires (CS p. 2). They hold personal and financial data, which the evaluation ([#50](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/50)) uses.

### 4.2 Relationships

| No. | From | Type | To | Via | Description | Source |
|---|---|---|---|---|---|---|
| R01 | P01 | Triggers | P02 | | An organic claim starts the certification check | UC1 |
| R02 | P02 | Provides data to | P01 | DS1 | The verified status, or the rejection of the claim, goes into the listing | UC1 |
| R03 | P01 | Provides data to | P03 | DS1 | The customers browse the listings, the stock and the categories | CS pp. 1–2 |
| R04 | P01 | Provides data to | P04 | DS1 | The availability check reads the stock | UC2 |
| R05 | P03 | Triggers | P04 | | The customer proceeds to checkout with the basket (M07) | UC2 |
| R06 | P04 | Triggers | P05 | | The confirmed order goes to payment | UC2 |
| R07 | P05 | Triggers | P01 | | A successful payment starts the stock update in F01 (processes.md, section 4) | UC2 |
| R08 | P05 | Triggers | P06 | M14 | After a successful payment, F02 notifies each producer (processes.md, section 4) | CS pp. 1–2, UC2 |
| R09 | P05 | Provides data to | P07 | DS3 | The producer amounts and the commission are the input of the settlement | CS p. 2, UC2 |
| R10 | P04 | Provides data to | P08 | DS2 | The order records identify the affected customers | CS p. 2, UC3 |
| R11 | P08 | Triggers | P01 | | A confirmed incident suspends the product from sale | UC3 |
| R12 | P01 | Provides data to | P09 | DS1 | The listing gives the postcode of the farm | CS p. 2 |
| R13 | P09 | Provides data to | P03 | DS4 | The food miles appear with the products | CS p. 2 |
| R14 | P09 | Provides data to | P04 | DS4 | The food miles appear in the order summary (M08) | CS p. 2 |
| R15 | P10 | Provides data to | P04 | DS4 | F02 applies the surplus discount to the order | CS p. 2 |
| R16 | P11 | Provides data to | P03 | DS4 | The educational content appears with the products | CS p. 2 |
| R17 | P01 | Provides data to | P08 | DS1 | The listing identifies the product of the incident and its producer | UC3 |

**Notes:**

- No process triggers P07. A weekly timer starts it.
- P06 has no relationship with P07, because no source says that the settlement waits for the fulfilment (D4).
- R07 and R11 change the data of P01. They do not create a new listing.

### 4.3 Start events and lint

Figure 1 must pass bpmnlint (the "recommended" rules in `.bpmnlintrc`):

- **Start events** (`no-implicit-start`): a message start event for each message that starts a process (section 3.1), and a timer for P07. The administrator report in P08 is the only none start event (`single-blank-start-event`).
- **Gateways:** merge the inputs of P01 and P08 (`fake-join`). Split the outputs of P05 (R07 and R08) with a parallel gateway (`no-implicit-split`).

## 5. Interactions between the areas of the enterprise

The areas are the lanes F01 to F05. Each cell gives the relationships from the row lane to the column lane. In Figure 1, each one is a sequence flow or a data association that crosses a lane boundary.

| From \ To | F01 | F02 | F03 | F04 | F05 |
|---|---|---|---|---|---|
| **F01** Product listing | | R04, R05 | | R01, R17 | R12 |
| **F02** Orders | | | R06 | R10 | |
| **F03** Finance | R07 | R08 | | | |
| **F04** Quality and traceability | R02, R11 | | | | |
| **F05** Quality assurance and community features | R13, R16 | R14, R15 | | | |

Each lane interacts with at least two other lanes. F01 interacts with all four, because they all use or change DS1. R03 and R09 stay inside one lane. The brackets in section 3.1 give the messages of each lane with the participants outside the network.

## 6. Interfaces

The first-class descriptor of Sprint 1 asks for "external interactions and interfaces" at "an appropriate strategic abstraction" (UWE Bristol, 2026c, p. 14). An interface is the group of message flows between two pools.

| ID | Interface | Messages | Kind | Requirement |
|---|---|---|---|---|
| I1 | Customer and network | M05 to M09, M13, M16, M20, M21, M25 | User | Browse and search, local food information, and clear supplier responsibilities at checkout (CS p. 2) |
| I2 | Producer and network | M01, M02, M14, M15, M17 to M19, M24, M26 | User | Easy to use without technical knowledge. Some producers use only email and telephone (CS p. 1) |
| I3 | Payment: network, customer and E01 | M10 to M12 | Service | Secure, compliant with data protection and financial regulations, and sandbox or mock only (CS pp. 1–2) |
| I4 | Certification: network and E02 | M03, M04 | Service | Handle a failed validation and an unavailable service (UC1) |
| I5 | Distance: network and E04 | M22, M23 | Service, TBC (Q3) | Distances from postcodes (CS p. 2) |

The demonstrations must show which activities users do and which the engine or a service does (UWE Bristol, 2026c, p. 4). I1 and I2 are the user side, and I3 to I5 are the automated side.

## 7. Traceability

### 7.1 Stakeholder needs and the i* models

The brief requires "clear alignment between the strategic process model and the stakeholder goals and dependencies" (UWE Bristol, 2026c, p. 3). Each message is a candidate resource dependency for the i* SD model: the receiver depends on the sender for the message. These messages meet a stated need, so Figure 3 starts from them:

| Message | Dependency | Stakeholder need | Source |
|---|---|---|---|
| M01, M02 | Network on producer | Listings with frequent seasonal updates | CS p. 1 |
| M06 | Customer on network | Harvest dates, farm origin and seasonal availability | CS p. 2 |
| M08 | Customer on network | Clear supplier, delivery and collection responsibilities | CS p. 2 |
| M12 | Network on payment service | A secure payment, and the 5% commission as income | CS p. 2, UC2 |
| M14 | Producer on network | Visibility of orders at least 48 hours ahead | CS pp. 1–2 |
| M15 | Producer on network | Weekly settlements with transparent audit trails | CS p. 2 |
| M20 | Customer on network | Rapid communication about food safety concerns | CS p. 2 |
| M25 | Customer on network | Surplus discounts, which reduce food waste | CS p. 2 |

The messages also show three tensions for the SR model:

- **Data quality against producer effort:** M01 has eleven validated fields (UC1), but some producers use only email and telephone (CS p. 1).
- **Transparency against less administration:** M08 shows each supplier separately (CS p. 2), but restaurants want less administration with many suppliers (CS p. 1).
- **Commission against producer income:** the network keeps 5% of each order, and M15 pays the producer only the remainder (CS p. 2).

### 7.2 Operational model

[#49](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/49) confirms or changes these planned elements in Sprint 2. The data stores of section 4.1 are the first data model of the Task 2 database.

| Message | Planned element in Figure 2 |
|---|---|
| M07 | Message start event |
| O01, O02 | Exclusive gateway on the stock, and a user task to amend the order |
| M08, M09 | User task with a Camunda Form to review and confirm the order |
| M10, M12 | Service task for M10, with an error boundary event for an unavailable service. An exclusive gateway on M12 |
| M11 | No element. The customer pays on the page of the service (D6) |
| O03, O04 | User task to retry, with a loop back to M10 |
| M13 | Service task that sends the confirmation |
| M14 | Multi-instance service task, one instance for each producer |

## 8. Decisions

The reviewers of this pull request confirm or change these decisions.

| No. | Decision | Reason |
|---|---|---|
| D1 | Figure 1 shows only the messages that start or end a process, or carry a result that a participant needs. O01 to O04 go to Figure 2 | The brief asks for "an appropriate high-level abstraction of the organisation" (UWE Bristol, 2026c, p. 3). The criteria name "inappropriate levels of detail" as a weakness (p. 14) |
| D2 | Keep M08 and M09 in Figure 1 | M08 carries the requirement for "clear communication about individual supplier responsibilities, delivery arrangements, and collection procedures" (CS p. 2). M09 completes P04 |
| D3 | E03 has no messages. The network sends M14, M20 and M25 directly | E03 only carries the messages of the network, but E01, E02 and E04 return results. If Q3 makes E03 external, add one request to E03 for each notification |
| D4 | Remove the fulfilment confirmation (1.2 message M18) | No source says that the producer confirms the fulfilment, or that the settlement waits for it |
| D5 | Replace the food safety notice to the producer (1.2 message M23) with M18 and M19 | UC3 says that the producer "is contacted and asked to provide further information about the issue" |
| D6 | The customer gives the payment details to the payment service directly (M11) | The network does not receive card details, which helps it comply with data protection and financial regulations (CS p. 2). The Camunda variables hold only the reference and the result. If the reviewers reject D6, remove M11 and put the payment details in M09 |
| D7 | Each "Provides data to" relationship goes through a data store (DS1 to DS4) | BPMN passes data between activities only through a data object or a data store (Object Management Group, 2014). One store for each main data set keeps Figure 1 clear |

## 9. Open questions

| No. | Question | Effect on this document |
|---|---|---|
| Q2 (actors.md) | Who pays the weekly settlements? | It can add a sender to M15 |
| Q3 (actors.md) | Are E03 and E04 external providers? | If E03 is external, D3 adds three requests. If E04 is internal, M22 and M23 go |
| T1 (processes.md) | Which processes become the two functionalities? | It decides the extra paths in section 3.2 and the rows of section 7.2 |
| T3 (processes.md) | Is P02 required? | It decides if M03, M04, R01, R02 and I4 stay |
| G1 (processes.md) | Is a producer onboarding process necessary? | It can add messages and relationships |

## 10. Changes needed in other documents

- processes.md, section 4, P08: remove "withdraws the product if asked". No source supports it, and R11 suspends the product inside the network.
- actors.md, section 2: change the BPMN element of A06 and A07 from "Lane in A05" to "Role in the F04 lane", as in processes.md.
- processes.md, section 4, P05: if the reviewers accept D6, F03 sends the payment request and the customer gives the payment details.

## 11. References

Object Management Group (2014) *Business Process Model and Notation (BPMN), Version 2.0.2* [online]. Needham, MA: Object Management Group. Available from: https://www.omg.org/spec/BPMN/2.0.2/ [Accessed 20 October 2026].

UWE Bristol (2026a) *Bristol Regional Food Network: digital marketplace* [Case study]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [case_study/Case Study - v2.pdf](../../case_study/Case%20Study%20-%20v2.pdf).

UWE Bristol (2026b) *Assessment Task 1 use cases* [Assessment material]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Use Case 2 is in [case_study/Case_study.txt](../../case_study/Case_study.txt).

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished.
