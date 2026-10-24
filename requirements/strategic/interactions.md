# 1.3 Interactions between the processes

**Authors:** Royden Dias, Hasaan Ahmad. Section 3 starts from a draft by Ishaq Modassir Mushtaq.
**Task:** [#81](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/81), Figure 1: strategic BPMN model
**Status:** draft for review. Revised after the review of Thu 22 Oct 2026 (section 3.4)

## 1. Purpose and scope

This document identifies the interactions to be represented in the strategic BPMN model (Figure 1) and records supporting design decisions and traceability. It covers:

- The messages between the participants (section 3). [#83](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/83) will model the selected messages as message flows.
- The relationships between the principal processes and their proposed shared information (section 4).
- The interactions between the enterprise's internal functions (section 5).
- The business-level interfaces between participants (section 6).
- The links to stakeholder needs and inputs to operational modelling (section 7).

The brief requires "interactions between different areas of the enterprise" and "relationships between the principal business processes" (UWE Bristol, 2026c, p. 3).

The participants are defined in [actors.md](actors.md) ([#79](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/79)). The processes and functions are defined in [processes.md](processes.md) ([#80](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/80)). This document uses their IDs.

Process keys: P01 Manage products; P02 Verify organic certification; P03 Browse and search catalogue; P04 Process order; P05 Process payment; P06 Fulfil order; P07 Settle producer payments; P08 Handle quality incident; P09 Report food miles; P10 Offer surplus produce; P11 Share educational content.

The level is strategic. Under D1, section 3.1 shows one message for each business document that passes between organisations. Screen steps and detailed alternative and exception flows are left to the operational models (Figure 2). Section 3.2 records the associated messages for that later work.

Source keys: CS is the case study (UWE Bristol, 2026a), with the page number. UC1, UC2 and UC3 are the three use cases (UWE Bristol, 2026b).

## 2. Participants

The table identifies the participants relevant to this interaction register and their proposed representation in Figure 1.

| Participant | IDs | Proposed BPMN representation | Sends or receives messages in Figure 1 |
|---|---|---|---|
| Customer | A01 to A03 | Shared collapsed pool | Yes |
| Producer | A04 | Pool | Yes |
| BRF Network | A05, with the lanes F01 to F05 | Pool containing the network's functional lanes | Yes |
| Payment service | E01 | External participant (collapsed pool) | Yes |
| Organic certification verification service | E02 | External participant (collapsed pool) | Yes |
| Notification service | E03 | External participant (collapsed pool), subject to Q3 (D3) | Yes |
| Postcode distance service | E04 | Provisionally represented as an external participant (collapsed pool), subject to Q3 | Yes, if represented as an external participant |

Message flows connect separate participant pools. Sequence flows describe execution order within a pool and may cross its lane boundaries. Information dependencies between internal functions are recorded separately in section 4; they are not automatically sequence flows.

A06 and A07 are internal roles within the BRF Network, represented within F04 in processes.md. They are not separate lanes or participants in this interaction register.

E05 and E06 are not represented as participants in Figure 1, in line with actors.md. No message flows involving them are included here.

## 3. Messages between the participants

### 3.1 Messages in Figure 1

For messages involving the BRF Network, the lane ID in brackets identifies the responsible internal function. The participant remains the BRF Network.

Under D3, the notification service (E03) delivers the notifications M09, M15 and M21. The network sends a notification request to E03 for each of them (M08, M14 and M20).

| No. | Sender | Receiver | Message | Process | Source |
|---|---|---|---|---|---|
| M01 | Producer | BRF Network (F01) | Product listing and its updates (name, description, category, price, quantity, availability period and farm origin, with harvest date, organic certification claim, allergens and best-before date where relevant; later changes to the stock and the seasonal availability) | P01 | CS pp. 1-2, UC1 |
| M02 | BRF Network (F04) | Certification service (E02) | Certification check request | P02 | UC1 |
| M03 | Certification service (E02) | BRF Network (F04) | Certification result | P02 | UC1 |
| M04 | Customer | BRF Network (F02) | Order (the basket, confirmed by the customer) | P04 | CS p. 2, UC2 |
| M05 | BRF Network (F03) | Payment service (E01) | Payment request (the order reference and the total) | P05 | UC2; request contents are a group design choice |
| M06 | Payment service (E01) | BRF Network (F03) | Payment response, where received (success, decline or an explicit service error) | P05 | UC2 |
| M07 | BRF Network (F03) | Customer | Order confirmation (the producers, the delivery or collection arrangements and the totals) | P05 | CS p. 2, UC2 |
| M08 | BRF Network (F02) | Notification service (E03) | Notification request (new producer order) | P05 | CS pp. 1-2, UC2 |
| M09 | Notification service (E03) | Producer | New order notification (the producer order element, with the delivery or collection arrangement) | P05 | CS pp. 1-2, UC2 |
| M10 | BRF Network (F03) | Producer | Weekly settlement (the payment and the audit trail statement) | P07 | CS p. 2 |
| M11 | Customer | BRF Network (F04) | Quality concern report | P08 | CS p. 2, UC3 |
| M12 | Producer | BRF Network (F04) | Quality concern or incident information | P08 | CS p. 2, UC3 |
| M13 | BRF Network (F04) | Producer | Incident notice (the enquiry and the outcome, such as a suspension or a request to withdraw the product) | P08 | UC3 |
| M14 | BRF Network (F04) | Notification service (E03) | Notification request (food safety notice) | P08 | UC3 |
| M15 | Notification service (E03) | Customer | Food safety notification | P08 | CS p. 2, UC3 |
| M16 | Customer | BRF Network (F05) | Postcode | P09 | CS p. 2 |
| M17 | BRF Network (F05) | Postcode distance service (E04) | Distance request | P09 | CS p. 2 |
| M18 | Postcode distance service (E04) | BRF Network (F05) | Distance result | P09 | CS p. 2 |
| M19 | Producer | BRF Network (F05) | Surplus produce report (with the discount) | P10 | CS p. 2 |
| M20 | BRF Network (F05) | Notification service (E03) | Notification request (surplus offer) | P10 | CS p. 2 |
| M21 | Notification service (E03) | Customer | Surplus offer | P10 | CS p. 2 |
| M22 | Producer | BRF Network (F05) | Educational content (recipe, storage guidance or farm story) | P11 | CS p. 2 |

Notes:

- P06 (fulfil order) has no separate message of its own in this register. M09 initiates producer fulfilment. The physical delivery or collection of the goods is not a message.
- Payment-service unavailability may be indicated by an explicit error response or detected when no response is received. M06 represents a response only where one is received. The operational model handles the appropriate exception or retry path.
- Food miles and educational content appear on the product and checkout screens of P03 and P04. Under D1, screen steps have no message in Figure 1. The customer's review of the order summary is modelled in #49 (D2).
- UC3 requires the outcomes of the notifications to be recorded and the failures to be followed up. The operational models handle this between the network and E03.
- Incident handling and review occur internally within F04, involving A06 and A07. These internal interactions are not represented as message flows between separate pools.
- M10 represents the business-level settlement interaction between the network and the producer. The payment provider and any additional payment instructions or confirmations remain subject to Q2 in actors.md.
- The lane annotations identify responsibility for the external interactions. In particular, M08 is sent by F02 following successful payment handled by F03. The corresponding internal relationship is addressed in section 4.

### 3.2 Messages for the operational models

These messages support the alternative and exception paths associated with P04 and P05. Figure 1 omits them under the strategic abstraction in D1. They stay here until Sprint 2 starts, and then move into the operational model of Use Case 2 ([#49](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/49)).

| No. | Sender | Receiver | Message | Process | Source |
|---|---|---|---|---|---|
| O01 | BRF Network (F02) | Customer | Stock unavailable notice, with a request to amend the order | P04 | UC2 |
| O02 | Customer | BRF Network (F02) | Amended order | P04 | UC2 |
| O03 | BRF Network (F03) | Customer | Payment declined notice | P05 | UC2 |
| O04 | Customer | BRF Network (F03) | Payment retry | P05 | UC2 |

Payment-service unavailability is handled through the exception or retry path described in section 3.1. No additional received message is assumed where the service does not respond.

This table currently covers UC2. UC1 and UC3 remain relevant to the enterprise-wide strategic model. If either contributes to an additional selected operational functionality, review this table and add the relevant alternative and exception messages.

### 3.3 Changes and refinements from the 1.2 draft

This section summarises how the process responsibilities in the 1.2 draft have been developed into the interaction register, including refinements made during review.

- Strategic and operational separation: O01 to O04 record the stock-amendment and payment-retry exchanges for operational modelling. These are omitted from Figure 1 under D1.

- Lane responsibilities: messages involving the BRF Network identify the responsible function, F01 to F05, without treating those lanes as separate participants.

- Fulfilment confirmation: no separate fulfilment-confirmation message is included. The supplied requirements do not explicitly require one or state that weekly settlement depends on it (D4).

- Producer incident communication: M12 carries the information of the producer, and M13 carries the enquiry and the outcome described in UC3 (D5).

- Product and customer information: M01 identifies the product information described in UC1. Food miles and educational content appear on the screens of P03 and P04, so they have no message of their own (D1).

- Payment-service responses: M06 distinguishes a received payment response from unavailability detected when no response arrives. The associated exception or retry handling belongs to the operational model.

- Internal incident handling: A06 and A07 are roles within F04, consistent with processes.md. Their internal interactions are not listed as message flows between separate pools.

- Settlement routing: M10 remains a business-level settlement interaction. The provider and any additional payment instructions or confirmations remain subject to Q2 in actors.md.

- Source references: weekly settlement (M10) cites CS p. 2. Producer order visibility (M09) cites CS pp. 1-2. M01 also cites UC1, and M04 also cites CS p. 2.

### 3.4 Changes after the review of 22 Oct 2026

The review of Thu 22 Oct 2026 changed D1 to D7. Figure 1 now has 22 messages instead of 26. The review estimated about 15 messages. This register keeps both messages of each exchange with an external service, because the strategic model must show the external organisations and services and their interactions (UWE Bristol, 2026c, p. 3).

The table maps the earlier IDs to the new IDs.

| Earlier ID | Change | New ID |
|---|---|---|
| M01, M02 | Merged into one listing document with its updates (D1) | M01 |
| M03, M04 | New number only | M02, M03 |
| M05, M06 | Removed. The browse request and the product results are screen steps (D1) | None |
| M07 | Changed to the order that the customer confirms (D2) | M04 |
| M08, M09 | Removed. #49 models the review step (D2) | None |
| M10 | New number only | M05 |
| M11 | Removed (D6) | None |
| M12 | New number only | M06 |
| M13 | Changed. It gives the producers, the delivery or collection arrangements and the totals (D2) | M07 |
| None | Added: notification request for a new producer order (D3) | M08 |
| M14 | Changed. E03 sends it (D3) | M09 |
| M15, M16 | New number only | M10, M11 |
| M17 | Changed to the concern or the incident information of the producer (D5) | M12 |
| M18 | Changed to one incident notice with the enquiry and the outcome (D5) | M13 |
| M19 | Removed. M12 carries the reply of the producer (D5) | None |
| None | Added: notification request for a food safety notice (D3) | M14 |
| M20 | Changed. E03 sends it (D3) | M15 |
| M21 to M24 | New number only | M16 to M19 |
| None | Added: notification request for a surplus offer (D3) | M20 |
| M25 | Changed. E03 sends it (D3) | M21 |
| M26 | New number only | M22 |

## 4. Relationships between the processes

This section identifies the relationships between the processes defined in processes.md. The relationship types distinguish process initiation from the use or update of shared information.

| Type | Meaning |
|---|---|
| Triggers | An event or outcome associated with the first process initiates the second process, subject to any stated condition |
| Provides data to | The second process uses data that the first process creates or keeps |
| Updates records used by | The first process changes records managed or used by the second process, without necessarily starting that process |

These are relationship labels for this register, not additional BPMN connector types.

Where activities form part of the same process flow within the BRF Network pool, their execution order may be represented by sequence flows. A relationship across participant pools uses the relevant message flow. Data relationships do not automatically imply execution order. Figure 1 does not show the data stores (D7).

### 4.1 Proposed shared data stores

The following logical data stores identify the shared information supporting the process relationships. Under D7, they are logical groups of information, and Figure 1 does not show them. They do not define the physical database schema for the later implementation.

| ID | Data store | Content | Responsible function | Written or updated by | Read by |
|---|---|---|---|---|---|
| DS1 | Product catalogue | Product listings, stock, categories, certification status, sale availability and product/producer information, including farm postcode, allergens and best-before dates | F01 | P01; certification results from P02; stock updates arising from P05; suspension updates arising from P08 | P01, P03, P04, P08, P09 |
| DS2 | Order records | Marketplace orders and producer-specific order elements linking customers, products and producers, including order and payment status | F02 | P04, P05 | P05, P08 |
| DS3 | Payment and settlement records | Payment responses, producer allocations, marketplace commission, settlement records and audit trail | F03 | P05, P07 | P07 |
| DS4 | Community information and content | Calculated food miles, surplus offers and discounts, and educational content | F05 | P09, P10, P11 | P03, P04 |

The process references identify the origin and use of information, not necessarily the function that performs every storage operation. In particular, stock and suspension updates arising from P05 and P08 remain the responsibility of F01, as described in R07 and R11.

DS2 supports the links between customers, products and producers used for traceability. DS3 supports the financial information and audit trail used for weekly settlement. DS1 and DS4 make the proposed shared information dependencies explicit.

### 4.2 Relationships

The "Via" column identifies the relevant message or proposed shared data store. A dash means that no separate message or shared data store is specified for that relationship in this register.

| No. | From | Type | To | Via | Description | Source |
|---|---|---|---|---|---|---|
| R01 | P01 Manage products | Triggers | P02 Verify organic certification | - | A listing that claims organic certification requires a verification check before publication | UC1 |
| R02 | P02 Verify organic certification | Provides data to | P01 Manage products | DS1 | The verification result is returned to P01 and recorded with the listing. Where certification is claimed, the required validation must succeed before the product is published | UC1 |
| R03 | P01 Manage products | Provides data to | P03 Browse and search catalogue | DS1 | Customers browse the published listings, availability and categories maintained through P01 | CS pp. 1-2 |
| R04 | P01 Manage products | Provides data to | P04 Process order | DS1 | The availability check at checkout uses the product and stock information maintained through P01 | UC2 |
| R05 | P03 Browse and search catalogue | Triggers | P04 Process order | M04 | P04 starts when the customer chooses to proceed to checkout with the basket; browsing alone does not initiate checkout | UC2 |
| R06 | P04 Process order | Triggers | P05 Process payment | - | After the customer confirms the purchase and the marketplace order is created and split by producer, the order awaiting payment proceeds to P05 | UC2 |
| R07 | P05 Process payment | Updates records used by | P01 Manage products | DS1 | Successful payment causes the relevant stock quantities to be updated by F01. This does not restart the product-listing process | UC2 |
| R08 | P05 Process payment | Triggers | P06 Fulfil order | M08, M09 | Following successful payment, F02 asks E03 to send the producer its order notification. The producer begins preparing the goods for the agreed delivery or collection | CS pp. 1-2, UC2 |
| R09 | P05 Process payment | Provides data to | P07 Settle producer payments | DS3 | Producer allocations and commission information from successful payments support the weekly settlement calculation | CS p. 2, UC2 |
| R10 | P04 Process order | Provides data to | P08 Handle quality incident | DS2 | Order records link customers, products and producers. P08 uses these records to identify affected orders and customers | CS p. 2, UC3 |
| R11 | P08 Handle quality incident | Updates records used by | P01 Manage products | DS1 | A confirmed issue causes the affected product to be temporarily suspended from further sale where appropriate. F01 updates the product's sale availability | UC3 |
| R12 | P01 Manage products | Provides data to | P09 Report food miles | DS1 | Product/producer information supplies the farm postcode used in the distance calculation | CS p. 2 |
| R13 | P09 Report food miles | Provides data to | P03 Browse and search catalogue | DS4 | Calculated food miles may be shown with the product results where the required postcode information is available | CS p. 2 |
| R14 | P09 Report food miles | Provides data to | P04 Process order | DS4 | Calculated food miles may be shown in the order summary at checkout where the required postcode information is available | CS p. 2 |
| R15 | P10 Offer surplus produce | Provides data to | P04 Process order | DS4 | Surplus-offer information supplies the applicable discount when the customer orders the offered products | CS p. 2 |
| R16 | P11 Share educational content | Provides data to | P03 Browse and search catalogue | DS4 | Published educational content may be presented alongside the producer's products | CS p. 2 |
| R17 | P01 Manage products | Provides data to | P08 Handle quality incident | DS1 | Product and producer information helps P08 identify the affected product and responsible producer | UC3 |

Notes:

- Each of the eleven processes has at least one relationship in this register.
- P02 is conditional on an organic certification claim. R01 does not mean that every product requires certification verification.
- P07 starts on the weekly settlement schedule. R09 supplies financial data; it does not trigger a settlement after every payment.
- No fulfilment-to-settlement dependency is included because the supplied requirements do not explicitly require settlement to wait for P06 (D4).
- R07 and R11 describe updates to product records, not the start of a new listing or a repeat of certification verification.
- R08 describes the business-level initiation of producer fulfilment through M08 and M09. The allocation of payment handling to F03 and producer notification to F02 is reflected in section 3.1.
- Collecting the farm postcode through P01, showing food miles on the product and checkout screens, presenting educational content alongside products, and assigning discount application to F02 are group design choices supporting the case-study requirements.
- DS1 to DS4 identify proposed shared information groupings. Their use in this register does not mean that every information exchange requires persistent storage or that each store must become a separate database.

## 5. Interactions between the areas of the enterprise

The internal areas of the BRF Network are represented by the functional lanes F01 to F05 defined in processes.md. This section groups the relationships in section 4 by the functions involved.

Each matrix entry identifies an interaction from the row function to the column function. The entries summarise process initiation, shared information or record updates; they do not introduce additional BPMN connector types or mean that every interaction is a sequence flow.

| From \ To | F01 | F02 | F03 | F04 | F05 |
|---|---|---|---|---|---|
| F01 | - | R04, R05 | - | R01, R17 | R12 |
| F02 | - | - | R06 | R10 | - |
| F03 | R07 | Successful-payment handover for producer notification (see R08, M08 and M09) | - | - | - |
| F04 | R02, R11 | - | - | - | - |
| F05 | R13, R16 | R14, R15 | - | - | - |

A dash means that no interaction is listed for that direction in this register. It does not mean that the functions could never interact.

### 5.1 Interpretation of the interactions

- F01 supplies product and stock information to order processing (R04). R05 records the transition from browsing to checkout when the customer submits M04; browsing alone does not start order processing.
- F01 initiates certification verification by F04 when an organic claim requires checking (R01). It also supplies product and producer information for incident handling (R17).
- F01 supplies the farm postcode information used by F05 for food-mile calculations (R12).
- F02 passes the confirmed order to payment processing in F03 (R06) and supplies order records to F04 for incident traceability (R10).
- Following successful payment, F03 initiates the stock update performed by F01 (R07) and makes the successful-payment outcome available to F02 for producer notification. F02 then sends the notification request M08, and E03 delivers M09 to the producer.
- F04 returns certification information to F01 (R02) and causes the affected product's sale availability to be updated where an incident requires suspension (R11).
- F05 supplies food-mile information and educational content to browsing in F01 (R13 and R16), and food-mile and surplus-discount information to order processing in F02 (R14 and R15).

### 5.2 Internal and external boundaries

R03 remains within F01, and R09 remains within F03, so neither appears as a cross-function entry in the matrix.

The F03-to-F02 entry describes the internal coordination needed before producer notification. It is not a separate message flow between those lanes. R08 describes the resulting business-level initiation of P06 in the Producer pool through M08 and M09.

Shared information and record updates are supported by the proposed data stores in section 4.1. Their inclusion does not automatically impose an execution order between the functions.

External interactions are recorded separately in section 3.1, where the lane annotations identify the BRF Network function responsible for each message.

## 6. Interfaces

This section groups the messages in section 3 into business-level interfaces between the participants. These groupings describe the purpose and scope of the interactions; they do not specify screen designs, API contracts, communication protocols or implementation technologies.

| ID | Interface | Messages in Figure 1 | Interaction type | Requirements and scope |
|---|---|---|---|---|
| I1 | Customer and BRF Network | M04, M07, M11, M16 | Customer-facing | Place orders; communicate supplier responsibilities and delivery or collection arrangements in the order confirmation; receive quality concerns and postcodes (CS p. 2, UC2, UC3). Browsing and the review of the order summary are screen steps of P03 and P04 (D1, D2) |
| I2 | Producer and BRF Network | M01, M10, M12, M13, M19, M22 | Producer-facing | Support product and stock updates, weekly settlement and its audit trail, incident communication, surplus offers and educational content. The interaction design must account for producers with limited technical knowledge, including those currently using email and telephone (CS pp. 1-2, UC1, UC3) |
| I3 | Payment between the BRF Network and E01 | M05, M06 | Service exchange | Submit payment requests and receive payment responses through an external or simulated service. #49 and Task 2 decide how the customer enters the payment details (D6). Use a sandbox or simulated service for assessment, not live payments (UC2) |
| I4 | Organic certification verification between the BRF Network and E02 | M02, M03 | Service exchange | Request verification when organic certification is claimed and receive the result. Failed validation and service unavailability require appropriate handling in the relevant operational model (UC1) |
| I5 | Postcode distance calculation between the BRF Network and E04 | M17, M18 | Proposed external service exchange, subject to Q3 | Request a postcode-based distance calculation and receive the result supporting food-mile information. E04's status as an external provider remains provisional (CS p. 2; Q3 in actors.md) |
| I6 | Notifications through E03 | M08, M09, M14, M15, M20, M21 | Service exchange, with delivery to customers and producers | Send notification requests to E03, which delivers the new order notifications, the food safety notifications and the surplus offers. Record the outcomes and follow up failures (CS pp. 1-2, UC2, UC3; Q3 in actors.md) |

### 6.1 Relationship to the message register

I1 and I2 group the business interactions with customers and producers. They do not assume that every interaction uses a single screen or communication channel.

The associated operational exchanges O01 to O04 also belong to I1 but are omitted from Figure 1 under D1. They are retained in section 3.2 for detailed modelling.

I3 connects the BRF Network with E01 through M05 and M06. The customer's entry of the payment details is not a message in Figure 1 (D6).

The customer supplies the postcode to the BRF Network through M16 in I1. The network's proposed distance-service request and result are grouped separately under I5.

The notifications to customers and producers go through E03 in I6 (D3). They are therefore not in I1 or I2.

### 6.2 Provisional routing and implementation boundaries

- Notification delivery goes through E03 under D3. If the tutor says that E03 is an internal capability (Q3), the network sends M09, M15 and M21 directly, and M08, M14, M20 and I6 are removed.
- M10 remains part of the producer-facing business interface I2. It does not settle whether E01 or another provider executes the weekly payment. Any additional settlement-service interactions remain subject to Q2 in actors.md.
- If E04 is agreed to be an internal capability, remove I5 and the separate messages M17 and M18 while retaining the distance-calculation capability and its information dependencies.
- Detailed user activities, automated activities, forms, service integrations and exception handling will be determined in the relevant operational models. The interface groupings do not prescribe those implementation choices.

## 7. Traceability

This section links the interaction register to stakeholder needs and identifies the behaviour to carry forward into operational modelling. It supports consistency between the models without prescribing their detailed notation or implementation.

### 7.1 Stakeholder needs and the i* models

The brief requires "clear alignment between the strategic process model and the stakeholder goals and dependencies" (UWE Bristol, 2026c, p. 3).

The following table identifies candidate stakeholder dependencies supported by the interactions. The dependency descriptions state who relies on whom and for what. Their representation in the i* models remains subject to review against the agreed stakeholder goals and modelling scope.

| Messages | Candidate dependency | Stakeholder need | Source |
|---|---|---|---|
| M01 | BRF Network depends on producers for product listings and stock or seasonal updates | Accurate product information and frequent updates to availability | CS pp. 1-2, UC1 |
| None (P03 screens, D1) | Customer depends on the BRF Network for product information | Access to harvest dates, farm origin and seasonal availability, with food miles and educational content where available | CS p. 2; presentation choices in section 3.1 |
| M07 | Customer depends on the BRF Network for the order confirmation | Clear communication of the producers involved and the delivery or collection arrangements. The review before the purchase is a screen step of P04 (D2) | CS p. 2, UC2 |
| M06 | BRF Network depends on the payment service for a payment response | Determine whether payment succeeded, was declined or returned an explicit service error | UC2 |
| M08, M09 | Producer depends on the BRF Network, and the network depends on the notification service, for order information | Visibility of orders and the delivery or collection arrangements needed for fulfilment, including the case-study requirement for order visibility at least 48 hours ahead | CS pp. 1-2, UC2 |
| M10 | Producer depends on the BRF Network for weekly settlement and its statement | Regular payment with a transparent audit trail | CS p. 2 |
| M12, M13 | BRF Network depends on the responsible producer for incident information | Obtain the information needed to assess a reported quality or safety concern, and tell the producer the outcome | UC3 |
| M14, M15 | Affected customer depends on the BRF Network for food-safety information | Rapid communication when a quality or food-safety concern affects purchased products | CS p. 2, UC3 |
| M20, M21 | Customer depends on the BRF Network for surplus-offer information | Access to discounted surplus produce, supporting the reduction of food waste | CS p. 2 |

The messages provide evidence for reviewing stakeholder dependencies; they do not establish a one-to-one mapping between message flows and i* dependencies. The final models should distinguish the information exchanged from the goals, tasks and quality expectations that the exchange supports.

For example, M06 supplies a payment response. Secure payment and marketplace commission income are broader stakeholder concerns supported by payment processing and the financial records, rather than information supplied by M06 alone.

The order-visibility requirement associated with M09 also needs checking against the agreed ordering and fulfilment arrangements. Listing the notification does not, by itself, demonstrate that the required lead time is achieved.

The following candidate tensions can inform review of the stakeholder rationale model:

- Product-information quality and producer effort: the listing and validation requirements must be considered alongside the limited technical knowledge of some producers (CS p. 1, UC1).
- Supplier transparency and reduced administration: checkout must communicate individual supplier responsibilities, while restaurant customers seek less administration when purchasing from multiple suppliers (CS pp. 1-2).
- Marketplace income and producer returns: the 5% commission supports the network's income while reducing the amount attributable to the producer from each order (CS p. 2, UC2).

These are candidate considerations for the stakeholder analysis, not confirmed conflicts between stakeholder goals.

### 7.2 Inputs to operational modelling

The operational modelling work ([#49](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/49)) should review the following interactions and associated behaviour for the UC2-focused operational scope currently recorded here. This table identifies what needs to be represented without fixing particular task types, forms or integration mechanisms.

| Messages or relationships | Behaviour to carry forward | Qualification |
|---|---|---|
| M04 | Receive the customer's confirmed basket at checkout and begin order processing | The operational model determines the appropriate initiation mechanism |
| O01, O02 | Inform the customer of unavailable stock and accept an amended order | Include the alternative path back to the relevant availability check |
| Review step (no message, D2) | Present the order summary and obtain purchase confirmation before creating the marketplace order and producer-specific elements | Preserve the supplier and delivery or collection information required for review |
| R06 | Pass the created order awaiting payment from order processing to payment processing | Preserve the allocation of responsibilities between F02 and F03 |
| M05, M06 | Submit the payment request and handle the response where received | Distinguish successful payment, decline and service failure, including cases where no response arrives |
| Payment details (no message, D6) | Decide how the customer enters the payment details for the simulated payment service | The operational model and Task 2 decide this |
| O03, O04 | Inform the customer of a declined payment and support retry | Determine the retry interaction and its return point in the operational flow |
| M07 | Confirm the order to the customer following successful payment | Do not treat a declined payment as a successful order confirmation |
| R07 | Update the relevant stock quantities following successful payment | Preserve F01's responsibility without restarting the whole product-listing process |
| M08, M09, R08 | Notify each relevant producer of its order element and fulfilment arrangements following successful payment | Distinguish the internal F03-to-F02 coordination from the request to E03 and the notification to the producer |
| R09 | Retain producer allocations and commission information for weekly settlement | Supplying this information does not initiate a settlement after every payment |

The data stores in section 4.1 provide candidate information groupings for later data modelling. The operational design must determine the required records, identifiers, validation and storage arrangements; DS1 to DS4 are not a completed database schema.

If another selected operational functionality draws on UC1 or UC3, extend the traceability review and the operational message register in section 3.2 to cover its relevant behaviour.

## 8. Decisions

The following decisions explain the scope, abstraction and design choices used in this interaction register. The review of Thu 22 Oct 2026 changed D1 to D7. The reviewers of this pull request confirm them before approval.

| No. | Decision | Reason |
|---|---|---|
| D1 | Figure 1 shows one message for each business document that passes between organisations. Request and response pairs between a person and the network, and screen steps, are left to the operational models. A request to an external service and its result are two separate documents, so Figure 1 shows both. The stock-amendment and payment-retry exchanges O01 to O04 stay in section 3.2 and move into #49 when Sprint 2 starts. | Figure 1 is for business stakeholders. The brief requires an appropriate high-level abstraction of the organisation. Detailed alternative and exception flows are addressed in the operational models (UWE Bristol, 2026c, pp. 3-4). |
| D2 | The order summary and the purchase confirmation are not separate messages in Figure 1. M04 is the order that the customer confirms. M07 gives the producers, the delivery or collection arrangements and the totals. #49 models the review step. | The case study requires the checkout to communicate the supplier responsibilities, the delivery arrangements and the collection procedures (CS p. 2). M07 carries this information. |
| D3 | Figure 1 shows the notification service (E03) as a collapsed pool. The network sends a notification request to E03 (M08, M14 and M20), and E03 delivers the notifications to the recipients (M09, M15 and M21). | UC3 requires the outcomes of the notifications to be recorded and the failures to be followed up, so the delivery channel is visible in Figure 1. actors.md lists E03 as an external participant. If the tutor says that E03 is internal (Q3), the network sends M09, M15 and M21 directly. |
| D4 | No separate fulfilment-confirmation message or fulfilment-to-settlement dependency is included in this register. Producers are settled for an order when its payment succeeds, not when the goods are delivered. | The supplied case study and use cases do not explicitly require either. M09 initiates producer fulfilment, while P07 follows the weekly settlement schedule using the relevant financial records. The settlement rule is a business assumption. The group asks the tutor to confirm it. |
| D5 | One incident notice (M13) goes from the network to the producer. It contains the enquiry and the outcome, for example a suspension or a request to withdraw the product. The producer sends its concern or its incident information in M12. | UC3 describes contacting the responsible producer for further information. processes.md has the producer withdraw the product if asked, so the outcome must reach the producer. M15 separately represents notifying affected customers. |
| D6 | The network sends the payment request (M05) and receives the payment response where one is returned (M06). Figure 1 does not show how the customer enters the payment details. #49 and Task 2 decide this. | UC2 states that "Payment is submitted to an external or simulated payment service". The group uses a simulated service, so the capture of the payment details is an implementation choice. Whether payment details pass through the network is a point for the critical evaluation (#51). |
| D7 | DS1 to DS4 are logical groups of information. They show which process writes each group and which process reads it. Figure 1 does not show them. | They are not databases, and they do not set the Task 2 schema. Figure 1 stays at enterprise level, and section 4.2 records the data dependencies. Data relationships do not automatically imply execution order. |

## 9. Open questions

The following questions are carried forward from actors.md and processes.md. This section records their effects on the interaction register rather than resolving the wider design decisions. Their current status and wording should be confirmed against those documents during review.

| No. | Question | Effect on this document |
|---|---|---|
| Q1 (actors.md) | Is the assumption that producers deliver their goods or customers collect them accepted? | If a separate logistics participant is agreed, review the participant list, fulfilment messages, R08 and the relevant interface groupings. The current register does not assume a separate logistics participant. |
| Q2 (actors.md) | How are weekly settlements paid to producers: through E01 or another provider? | M10 currently represents the business-level settlement interaction between the BRF Network and the producer. The agreed arrangement may require additional participants, payment instructions, confirmations or changes to message routing. Review I2 and any settlement-service interface accordingly. |
| Q3 (actors.md) | Are the notification service (E03) and postcode distance service (E04) internal capabilities or external providers? | Figure 1 shows E03 as an external participant (D3). If E03 is internal, remove M08, M14, M20 and I6, and send M09, M15 and M21 from the network directly. If E04 is internal, remove its separate participant representation, M17/M18 and I5 while retaining the distance-calculation capability and its information dependencies. |
| T1 (processes.md) | Which processes become the two operational functionalities? | Sections 3.2 and 7.2 currently cover UC2. Confirm how the selected functionalities map to the processes and use cases. If either draws on UC1 or UC3, extend the operational message register and traceability review with the relevant behaviour. |
| T3 (processes.md) | Is P02 (verify organic certification) required within the agreed model scope? | The current register includes conditional verification where organic certification is claimed, reflecting UC1. If a different scope is agreed, review P02, E02, M02/M03, R01/R02, I4 and the affected data-store and lane-matrix entries. Record the rationale for any departure from the supplied use case. |
| G1 (processes.md) | Does the agreed enterprise scope include a producer onboarding process? | If onboarding is included, assess whether additional participants, messages, shared information, interfaces and process relationships are needed. No onboarding interactions are assumed in the current register. |

The review of Thu 22 Oct 2026 settled D1 to D7 in section 8. D4 contains a business assumption that the tutor must confirm. The IDs above remain traceable to their originating documents.

## 10. Related-document updates

The following checks and proposed updates support consistency between this interaction register and the related documents. Review the current versions before making changes; where the documents already agree, no further edit is needed.

| Document or model | Check or proposed update | Reason |
|---|---|---|
| actors.md: A06 and A07 | Confirm that both are described as internal roles within F04, rather than separate lanes or participants | Aligns with section 2 and the internal incident-handling responsibilities recorded in section 3 |
| actors.md: E03 and E04 | Keep their internal or external status consistent with Q3 and the representations used here | Changes to their status affect the participant list, message routing and interfaces |
| actors.md: settlement arrangements | Once Q2 is resolved, record the agreed payment provider and any additional participant responsibilities | M10 currently represents the business-level settlement interaction without specifying the complete payment route |
| processes.md: P05 | Confirm that F03 handles the payment request and response, while F02 sends the producer order notification through E03 following successful payment | Aligns with M05, M06, M08, M09 and the internal coordination described in section 5 |
| processes.md: P07 | Once the tutor confirms D4, record that producers are settled for an order when its payment succeeds | Keeps the settlement rule in one place |
| processes.md: P01, P05 and P08 | Confirm that stock and sale-availability updates are assigned consistently to F01, without implying that they restart the whole product-listing process | Aligns with R07, R11 and the proposed DS1 responsibilities |
| processes.md: P08 | Keep "withdraws the product if asked". M13 tells the producer the outcome, for example a suspension or a request to withdraw the product (D5) | Aligns the process description with M13 and the suspension behaviour recorded in R11 |
| processes.md: operational scope | Confirm T1 and update the selected functionality descriptions where necessary | Sections 3.2 and 7.2 currently provide UC2-focused inputs and may need extending once the operational scope is agreed |
| Figure 1 modelling work (#83) | Use the message IDs of section 3.1. Show E03 as a collapsed pool (D3). Do not draw DS1 to DS4 (D7) | Prevents the diagram from mixing the previous numbering or superseded assumptions with this register |
| 2.2 functionalities.md (#115) | Use the message IDs of section 3.1. Section 3.4 maps the earlier IDs | functionalities.md uses the message IDs of this register |
| Stakeholder and operational models | Review the candidate dependencies and operational inputs in section 7 against the agreed scope | Maintains traceability without treating the proposed mappings as completed modelling decisions |

These entries do not approve changes to the related documents or establish that those changes have already been made. Any agreed update should be reflected consistently in this register and the affected document or model.

## 11. References

UWE Bristol (2026a) *Bristol Regional Food Network: digital marketplace* [Case study]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [case_study/Case Study - v2.pdf](../../case_study/Case%20Study%20-%20v2.pdf).

UWE Bristol (2026b) *Assessment Task 1 use cases* [Assessment material]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Use Case 2 is in [case_study/Case_study.txt](../../case_study/Case_study.txt).

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished.
