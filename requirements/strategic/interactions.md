# 1.3 Interactions between the processes

**Authors:** Royden Dias, Hasaan Ahmad. Section 3 starts from a draft by Ishaq Modassir Mushtaq.
**Task:** [#81](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/81), Figure 1: strategic BPMN model
**Status:** draft for review

## 1. Purpose and scope

This document lists the interactions that the strategic BPMN model (Figure 1) shows. It has two parts:

- The messages between the participants (section 3). [#83](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/83) draws each message as a message flow.
- The relationships between the principal processes (section 4).

The brief requires "interactions between different areas of the enterprise" and "relationships between the principal business processes" (UWE Bristol, 2026c, p. 3).

The participants are in [actors.md](actors.md) ([#79](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/79)). The processes and the functions are in [processes.md](processes.md) ([#80](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/80)). This document uses their IDs. The link to processes.md resolves after [#100](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/100) merges.

The level is strategic. Figure 1 shows a message only if it starts or ends a process, or carries a result that a participant needs. The alternative and exception paths inside a process belong to the operational models (Figure 2). Section 3.2 keeps them for that work.

Source keys: CS is the case study (UWE Bristol, 2026a), with the page number. UC1, UC2 and UC3 are the three use cases (UWE Bristol, 2026b).

## 2. Participants

| Participant | IDs | BPMN element (actors.md) | Sends or receives messages in Figure 1 |
|---|---|---|---|
| Customer | A01 to A03 | Pool (collapsed) | Yes |
| Producer | A04 | Pool | Yes |
| BRF Network | A05, with the lanes F01 to F05 | Pool | Yes |
| Payment service | E01 | External participant | Yes |
| Organic certification verification service | E02 | External participant | Yes |
| Notification service | E03 | External participant, TBC (Q3 in actors.md) | No (D3) |
| Postcode distance service | E04 | External participant, TBC (Q3 in actors.md) | Yes |

A message crosses a pool boundary. The lanes inside the BRF Network pool use sequence flows, so they send no messages. E05 and E06 are not in the BPMN (actors.md), so they send and receive no messages.

## 3. Messages between the participants

### 3.1 Messages in Figure 1

| No. | Sender | Receiver | Message | Process | Source |
|---|---|---|---|---|---|
| M01 | Producer | BRF Network | Product listing (name, description, category, price, quantity, availability period, farm origin, harvest date, organic claim, allergens and best-before date) | P01 | CS pp. 1–2, UC1 |
| M02 | Producer | BRF Network | Stock and seasonal availability update | P01 | CS pp. 1–2, UC1 |
| M03 | BRF Network | Certification service (E02) | Certification check request | P02 | UC1 |
| M04 | Certification service (E02) | BRF Network | Certification result | P02 | UC1 |
| M05 | Customer | BRF Network | Browse or search request | P03 | CS p. 2, UC2 |
| M06 | BRF Network | Customer | Product results (with the harvest dates, the farm origin, the seasonal availability, the food miles and the educational content) | P03 | CS p. 2, UC2 |
| M07 | Customer | BRF Network | Order request (the basket at checkout) | P04 | CS p. 2, UC2 |
| M08 | BRF Network | Customer | Order summary for review (the producers, the delivery or collection arrangements and the totals) | P04 | CS p. 2, UC2 |
| M09 | Customer | BRF Network | Purchase confirmation | P04 | UC2 |
| M10 | BRF Network | Payment service (E01) | Payment request | P05 | UC2 |
| M11 | Payment service (E01) | BRF Network | Payment result (success, decline or unavailable) | P05 | UC2 |
| M12 | BRF Network | Customer | Order confirmation | P05 | UC2 |
| M13 | BRF Network | Producer | New order notification (the producer order element, with the delivery or collection arrangement) | P05 | CS pp. 1–2, UC2 |
| M14 | BRF Network | Producer | Weekly settlement (the payment and the audit trail statement) | P07 | CS p. 2 |
| M15 | Customer | BRF Network | Quality concern report | P08 | CS p. 2, UC3 |
| M16 | Producer | BRF Network | Quality concern report | P08 | CS p. 2, UC3 |
| M17 | BRF Network | Producer | Request for information about the incident | P08 | UC3 |
| M18 | Producer | BRF Network | Incident information | P08 | UC3 |
| M19 | BRF Network | Customer | Food safety notification | P08 | CS p. 2, UC3 |
| M20 | Customer | BRF Network | Postcode | P09 | CS p. 2 |
| M21 | BRF Network | Postcode distance service (E04) | Distance request | P09 | CS p. 2 |
| M22 | Postcode distance service (E04) | BRF Network | Distance result | P09 | CS p. 2 |
| M23 | Producer | BRF Network | Surplus produce report (with the discount) | P10 | CS p. 2 |
| M24 | BRF Network | Customer | Surplus offer | P10 | CS p. 2 |
| M25 | Producer | BRF Network | Educational content (recipe, storage guidance or farm story) | P11 | CS p. 2 |

**Notes:**

- P06 (fulfil order) has no message of its own. M13 starts it. The physical delivery or collection of the goods is not a message.
- When the payment service is unavailable, no message comes back. M11 shows "unavailable" as an outcome of the call. The retry or exception path starts in the network, and Figure 2 shows it.
- The food miles reach the customer inside M06 and M08. The educational content reaches the customer inside M06. So they have no message of their own.
- The network closes or escalates an incident in its own lanes (A06 and A07), so this step has no message.
- The payer of the weekly settlement in M14 is open (Q2 in actors.md).

### 3.2 Messages for the operational models

These messages are the alternative and exception paths inside P04 and P05. Figure 1 does not show them (D1). The operational model of Use Case 2 ([#49](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/49)) uses them.

| No. | Sender | Receiver | Message | Process | Source |
|---|---|---|---|---|---|
| O01 | BRF Network | Customer | Stock unavailable notice, with a request to amend the order | P04 | UC2 |
| O02 | Customer | BRF Network | Amended order | P04 | UC2 |
| O03 | BRF Network | Customer | Payment declined notice | P05 | UC2 |
| O04 | Customer | BRF Network | Payment retry | P05 | UC2 |

UC1 and UC3 have similar paths: the correction of invalid listing details (UC1), and the follow-up of each failed notification (UC3). The group does not model these use cases in detail, so this table does not list them.

### 3.3 Changes from the 1.2 draft

- The messages have new numbers. The draft messages M08, M09, M14 and M15 are now O01 to O04 (D1).
- The draft message M18 (fulfilment confirmation) is removed (D4).
- The draft message M23 (food safety notice to the producer) is replaced by M17 and M18 (D5).
- Source corrections: the weekly settlement (M14) is on CS p. 2, not p. 1. The order visibility for producers (M13) is on CS pp. 1–2. M02 also cites UC1, and M07 and M08 also cite CS p. 2.
- M01 lists the product fields of UC1. M06 lists the information that the case study shows with the products.

## 4. Relationships between the processes

A relationship links two processes of processes.md. Each relationship has a type.

| Type | Meaning |
|---|---|
| Triggers | The outcome of the first process starts the second process |
| Provides data to | The second process uses data that the first process creates or keeps |

In Figure 1, a "Triggers" relationship inside the BRF Network pool is a sequence flow. A "Triggers" relationship across a pool boundary uses the message in the "Via" column. A "Provides data to" relationship is shared data, for example a data store that both processes use.

| No. | From | Type | To | Via | Description | Source |
|---|---|---|---|---|---|---|
| R01 | P01 Manage products | Triggers | P02 Verify organic certification | | An organic claim in a listing starts the certification check | UC1 |
| R02 | P02 Verify organic certification | Provides data to | P01 Manage products | | The verified organic status, or the rejection of the claim, goes into the listing | UC1 |
| R03 | P01 Manage products | Provides data to | P03 Browse and search catalogue | | The customers browse the listings, the stock and the categories that P01 keeps | CS pp. 1–2 |
| R04 | P01 Manage products | Provides data to | P04 Process order | | The availability check at checkout reads the stock that P01 keeps | UC2 |
| R05 | P03 Browse and search catalogue | Triggers | P04 Process order | | The customer proceeds to checkout with the basket (M07) | UC2 |
| R06 | P04 Process order | Triggers | P05 Process payment | | The confirmed order goes to payment | UC2 |
| R07 | P05 Process payment | Triggers | P01 Manage products | | A successful payment starts the stock update, which F01 performs (decision in section 4 of processes.md) | UC2 |
| R08 | P05 Process payment | Triggers | P06 Fulfil order | M13 | The new order notification starts the preparation of the goods by the producer | CS pp. 1–2, UC2 |
| R09 | P05 Process payment | Provides data to | P07 Settle producer payments | | The amount of each producer and the 5% commission are the input of the weekly settlement | CS p. 2, UC2 |
| R10 | P04 Process order | Provides data to | P08 Handle quality incident | | The orders link customers, products and producers. P08 uses these records to find the affected customers | CS p. 2, UC3 |
| R11 | P08 Handle quality incident | Triggers | P01 Manage products | | A confirmed incident suspends the product from sale | UC3 |
| R12 | P01 Manage products | Provides data to | P09 Report food miles | | The listing gives the postcode of the farm | CS p. 2 |
| R13 | P09 Report food miles | Provides data to | P03 Browse and search catalogue | | The food miles appear with the products | CS p. 2 |
| R14 | P09 Report food miles | Provides data to | P04 Process order | | The food miles appear in the order summary (M08) | CS p. 2 |
| R15 | P10 Offer surplus produce | Provides data to | P04 Process order | | F02 applies the surplus discount to the order | CS p. 2 |
| R16 | P11 Share educational content | Provides data to | P03 Browse and search catalogue | | The educational content appears with the products of the producer | CS p. 2 |

**Notes:**

- Each of the eleven processes has at least one relationship.
- No other process triggers P07. The weekly settlement date starts it (a timer).
- The sources do not say that the settlement waits for the fulfilment. So P06 has no relationship with P07 (D4).
- R07 and R11 change the data that P01 keeps. They do not start a new listing.

## 5. Decisions

The reviewers of this pull request confirm or change these decisions.

| No. | Decision | Reason |
|---|---|---|
| D1 | Figure 1 shows the messages that start or end a process, or that carry a result that a participant needs. The alternative and exception loops (O01 to O04) go to the operational models | The brief asks for "an appropriate high-level abstraction of the organisation" (UWE Bristol, 2026c, p. 3). The marking criteria name "inappropriate levels of detail" as a weakness (p. 14) |
| D2 | M08 (order summary) and M09 (purchase confirmation) stay in Figure 1 | M08 carries a requirement: "clear communication about individual supplier responsibilities, delivery arrangements, and collection procedures" (CS p. 2). M09 is the commitment of the customer, which completes P04 |
| D3 | E03 sends and receives no messages in Figure 1. The network sends each notification (M13, M19 and M24) directly | E01, E02 and E04 return a result that the network needs. E03 only carries the messages of the network. If the tutor makes E03 an external participant (Q3), add one request from the network to E03 for each notification |
| D4 | Remove the fulfilment confirmation (M18 of the 1.2 draft) | No source says that the producer confirms the fulfilment, or that the settlement waits for it |
| D5 | Replace the food safety notice to the producer (M23 of the 1.2 draft) with M17 and M18 | UC3 says that the producer "is contacted and asked to provide further information about the issue". It does not describe a notice to the producer |

## 6. Open questions

These questions from actors.md and processes.md have an effect on this document.

| No. | Question | Effect on this document |
|---|---|---|
| Q2 (actors.md) | Who pays the weekly settlements to the producers? | It can add a sender to M14 |
| Q3 (actors.md) | Are E03 and E04 part of the platform, or external providers? | If E03 is external, D3 adds three requests to E03. If E04 is part of the platform, M21 and M22 go |
| T3 (processes.md) | Is P02 (verify organic certification) required? | It decides if M03, M04, R01 and R02 stay |
| G1 (processes.md) | Does the model need a producer onboarding process? | It can add messages and relationships |

## 7. References

UWE Bristol (2026a) *Bristol Regional Food Network: digital marketplace* [Case study]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [case_study/Case Study - v2.pdf](../../case_study/Case%20Study%20-%20v2.pdf).

UWE Bristol (2026b) *Assessment Task 1 use cases* [Assessment material]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Use Case 2 is in [case_study/Case_study.txt](../../case_study/Case_study.txt).

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished.
