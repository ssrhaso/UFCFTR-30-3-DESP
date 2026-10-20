# 1.3 Interactions between the processes

**Authors:** Royden Dias, Hasaan Ahmad. Section 3 starts from a draft by Ishaq Modassir Mushtaq.
**Task:** [#81](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/81), Figure 1: strategic BPMN model
**Status:** draft for review

## 1. Purpose and scope

This document identifies the interactions to be represented in the strategic BPMN model (Figure 1). It covers:

- The messages between the participants (section 3). [#83](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/83) will model the selected messages as message flows.
- The relationships between the principal processes (section 4).

The brief requires "interactions between different areas of the enterprise" and "relationships between the principal business processes" (UWE Bristol, 2026c, p. 3).

The participants are in [actors.md](actors.md) ([#79](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/79)). The processes and the functions are in [processes.md](processes.md) ([#80](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/80)). This document uses their IDs.
The level is strategic. Section 3.1 selects messages that initiate or complete a business process, or communicate information or results required by another participant. Detailed alternative and exception flows are left to the operational models (Figure 2). Section 3.2 records the associated messages for that later work.

Source keys: CS is the case study (UWE Bristol, 2026a), with the page number. UC1, UC2 and UC3 are the three use cases (UWE Bristol, 2026b).

## 2. Participants

The table identifies the participants relevant to this interaction register and their proposed 
representation in Figure 1.

| Participant | IDs | Proposed BPMN representation | Sends or receives messages in Figure 1 |
|---|---|---|---|
| Customer | A01 to A03 | Shared collapsed pool | Yes |
| Producer | A04 | Pool | Yes |
| BRF Network | A05, with the lanes F01 to F05 | Pool containing the network's functional lanes | Yes |
| Payment service | E01 | External participant (collapsed pool) | Yes |
| Organic certification verification service | E02 | External participant (collapsed pool) | Yes |
| Notification service | E03 | Not shown separately under the current abstraction (D3); external-provider status remains subject to Q3 | No separate message flows under D3 |
| Postcode distance service | E04 | Provisionally represented as an external participant (collapsed pool), subject to Q3 | Yes, if represented as an external participant |

Message flows connect separate participant pools. Sequence flows describe execution order within a pool 
and may cross its lane boundaries. Information dependencies between internal functions are recorded 
separately in section 4; they are not automatically sequence flows.

A06 and A07 are internal roles within the BRF Network, represented within F04 in processes.md. They are not 
separate participants in this message register.

E05 and E06 are not represented as participants in Figure 1, in line with actors.md. No message flows involving 
them are included here.

## 3. Messages between the participants

### 3.1 Messages in Figure 1

| No. | Sender | Receiver | Message | Process | Source |
|---|---|---|---|---|---|
| M01 | Producer | BRF Network | Product listing (name, description, category, price, quantity, availability period, farm origin, harvest date, organic claim, allergens and best-before date) | P01 | CS pp. 1–2, UC1 |
| M02 | Producer | BRF Network | Stock and seasonal availability update | P01 | CS pp. 1–2, UC1 |
| M03 | BRF Network | Certification service (E02) | Certification check request | P02 | UC1 |
| M04 | Certification service (E02) | BRF Network | Certification result | P02 | UC1 |
| M05 | Customer | BRF Network | Browse or search request | P03 | CS p. 2, UC2 |
| M06 | BRF Network | Customer | Product results (with the harvest dates, the farm origin, the seasonal availability, and food miles and educational content where available) | P03 | CS p. 2, UC2 |
| M07 | Customer | BRF Network | Order request (the basket at checkout) | P04 | CS p. 2, UC2 |
| M08 | BRF Network | Customer | Order summary for review (the producers, the delivery or collection arrangements, the totals and the food miles where calculable) | P04 | CS p. 2, UC2 |
| M09 | Customer | BRF Network | Purchase confirmation | P04 | UC2 |
| M10 | BRF Network | Payment service (E01) | Payment request | P05 | UC2 |
| M11 | Payment service (E01) | BRF Network | Payment response, where received (success, decline or an explicit service error) | P05 | UC2 |
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
- Payment-service unavailability may be indicated by an explicit error response or detected when no response is received. M11 represents a response only where one is received. The operational model handles the appropriate exception or retry path.
- Food miles are included in M06 and M08 where the required postcode information is available. Educational content may be presented through M06. These presentation choices avoid the need for separate messages for those results.
- Incident handling and review occur internally within F04, involving A06 and A07. These internal interactions are not represented as message flows between separate pools.
- M14 represents the business-level settlement interaction between the network and the producer. The payment provider and any additional payment instructions or confirmations remain subject to Q2 in actors.md.

### 3.2 Messages for the operational models

These messages support the alternative and exception paths associated with P04 and P05. Figure 1 omits them under the strategic abstraction in D1. They are retained here for the operational model of Use Case 2 ([#49](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/49)).

| No. | Sender | Receiver | Message | Process | Source |
|---|---|---|---|---|---|
| O01 | BRF Network | Customer | Stock unavailable notice, with a request to amend the order | P04 | UC2 |
| O02 | Customer | BRF Network | Amended order | P04 | UC2 |
| O03 | BRF Network | Customer | Payment declined notice | P05 | UC2 |
| O04 | Customer | BRF Network | Payment retry | P05 | UC2 |

Payment-service unavailability is handled through the exception or retry path described in section 3.1. No additional received message is assumed where the service does not respond.

As a group, we have selected UC2 for detailed operational modelling. UC1 and UC3 remain relevant to the enterprise-wide strategic model, but their detailed alternative and exception messages are not listed in this UC2-focused table.

### 3.3 Changes and refinements from the 1.2 draft

This section summarises how the process responsibilities in the 1.2 draft
have been developed into the interaction register, including refinements
made during review.

- Strategic and operational separation: O01 to O04 record the
  stock-amendment and payment-retry exchanges for operational modelling.
  These are omitted from Figure 1 under D1.

- Fulfilment confirmation: no separate fulfilment-confirmation message
  is included. The supplied requirements do not explicitly require one
  or state that weekly settlement depends on it (D4).

- Producer incident communication: M17 and M18 represent the request for
  further incident information and the producer's response described in
  UC3 (D5).

- Product and customer information: M01 identifies the product
  information described in UC1. M06 includes food miles and educational
  content where available, while M08 includes food miles where
  calculable. These presentation choices are group design decisions;
  food miles depend on the required postcode information being available.

- Payment-service responses: M11 distinguishes a received payment
  response from unavailability detected when no response arrives.
  The associated exception or retry handling belongs to the operational
  model.

- Internal incident handling: A06 and A07 are roles within F04, consistent
  with processes.md. Their internal interactions are not listed as
  message flows between separate pools.

- Settlement routing: M14 remains a business-level settlement interaction.
  The provider and any additional payment instructions or confirmations
  remain subject to Q2 in actors.md.

- Source references: weekly settlement (M14) cites CS p. 2. Producer
  order visibility (M13) cites CS pp. 1–2. M02 also cites UC1, and M07
  and M08 also cite CS p. 2.

## 4. Relationships between the processes

This section identifies the relationships between the processes defined 
in processes.md. The relationship types distinguish process initiation 
from the use or update of shared information.

| Type | Meaning |
|---|---|
| Triggers | An event or outcome associated with the first process initiates the second process, subject to any stated condition |
| Provides data to | The second process uses data that the first process creates or keeps |
| Updates records used by | The first process changes records managed or used by the second process, without necessarily starting that process |

These are relationship labels for this register, not additional BPMN connector types.

Where activities form part of the same process flow within the BRF Network pool, their execution order may be represented by sequence flows. A relationship across participant pools uses the relevant message flow. Data relationships do not automatically imply execution order; where shown in Figure 1, they may be represented using data objects or data stores with appropriate data associations.

| No. | From | Type | To | Via | Description | Source |
|---|---|---|---|---|---|---|
| R01 | P01 Manage products | Triggers | P02 Verify organic certification | - | A listing that claims organic certification requires a verification check before publication | UC1 |
| R02 | P02 Verify organic certification | Provides data to | P01 Manage products | - | The verification result is returned to P01. Where certification is claimed, the required validation must succeed before the product is published | UC1 |
| R03 | P01 Manage products | Provides data to | P03 Browse and search catalogue | - | Customers browse the published listings, availability and categories maintained through P01 | CS pp. 1–2 |
| R04 | P01 Manage products | Provides data to | P04 Process order | - | The availability check at checkout uses the product and stock information maintained through P01 | UC2 |
| R05 | P03 Browse and search catalogue | Triggers | P04 Process order | M07 | P04 starts when the customer chooses to proceed to checkout with the basket; browsing alone does not initiate checkout | UC2 |
| R06 | P04 Process order | Triggers | P05 Process payment | - | After the customer confirms the purchase and the marketplace order is created and split by producer, the order awaiting payment proceeds to P05 | UC2 |
| R07 | P05 Process payment | Updates records used by | P01 Manage products | - | Successful payment causes the relevant stock quantities to be updated by F01. This does not restart the product-listing process | UC2 |
| R08 | P05 Process payment | Triggers | P06 Fulfil order | M13 | Following successful payment, the producer receives its order notification and begins preparing the goods for the agreed delivery or collection | CS pp. 1–2, UC2 |
| R09 | P05 Process payment | Provides data to | P07 Settle producer payments | - | Producer allocations and commission information from successful payments support the weekly settlement calculation | CS p. 2, UC2 |
| R10 | P04 Process order | Provides data to | P08 Handle quality incident | - | Order records link customers, products and producers. P08 uses these records to identify affected orders and customers | CS p. 2, UC3 |
| R11 | P08 Handle quality incident | Updates records used by | P01 Manage products | - | A confirmed issue causes the affected product to be temporarily suspended from further sale where appropriate | UC3 |
| R12 | P01 Manage products | Provides data to | P09 Report food miles | - | Product/producer information supplies the farm postcode used in the distance calculation | CS p. 2 |
| R13 | P09 Report food miles | Provides data to | P03 Browse and search catalogue | - | Calculated food miles may be included in product results where the required postcode information is available (M06) | CS p. 2 |
| R14 | P09 Report food miles | Provides data to | P04 Process order | - | Calculated food miles may be included in the order summary where the required postcode information is available (M08) | CS p. 2 |
| R15 | P10 Offer surplus produce | Provides data to | P04 Process order | - | Surplus-offer information supplies the applicable discount when the customer orders the offered products | CS p. 2 |
| R16 | P11 Share educational content | Provides data to | P03 Browse and search catalogue | - | Published educational content may be presented alongside the producer's products in M06 | CS p. 2 |

**Notes:**

- Each of the eleven processes has at least one relationship in this register.
- P02 is conditional on an organic certification claim. The relationship
  does not mean that every product requires certification verification.
- P07 starts on the weekly settlement schedule. R09 supplies financial
  data; it does not trigger a settlement after every payment.
- No fulfilment-to-settlement dependency is included because the supplied
  requirements do not explicitly require settlement to wait for P06 (D4).
- R07 and R11 describe updates to product records, not the start of a new
  listing or a repeat of certification verification.
- Collecting the farm postcode through P01, showing food miles in M06/M08,
  presenting educational content alongside products, and assigning
  discount application to F02 are group design choices supporting the
  case-study requirements.

## 5. Decisions

The following proposed decisions explain the scope and abstraction of this interaction register. The reviewers of this pull request confirm or amend them before approval.

| No. | Decision | Reason |
|---|---|---|
| D1 | Figure 1 shows selected messages that initiate or complete a business process, or communicate information or results required by another participant. The detailed stock-amendment and payment-retry exchanges O01 to O04 are retained for the operational model rather than shown in Figure 1. | The brief requires an appropriate high-level abstraction of the organisation. Detailed alternative and exception flows are addressed in the operational models (UWE Bristol, 2026c, pp. 3–4). |
| D2 | M08 (order summary) and M09 (purchase confirmation) remain in Figure 1. | M08 communicates the producers, delivery or collection arrangements and totals for customer review. M09 records the customer's confirmation before the marketplace order is created and payment begins. These are significant business interactions in UC2. Food miles in M08 are a group presentation choice, included where calculable. |
| D3 | Under the current abstraction, notification delivery is represented by messages from the BRF Network directly to the recipients: M13, M19 and M24. E03 is not shown as a separate participant. Its internal or external status remains subject to Q3 in actors.md. | This keeps Figure 1 focused on the business sender and recipient without committing to a notification provider. If E03 is modelled as an external participant, its requests, delivery interactions and relevant results must be represented consistently. The abstraction does not remove UC3's requirement to record notification outcomes and follow up failures. |
| D4 | No separate fulfilment-confirmation message or fulfilment-to-settlement dependency is included in this register. | The supplied case study and use cases do not explicitly require either. M13 initiates producer fulfilment, while P07 follows the weekly settlement schedule using the relevant financial records. This is a scope decision, not a claim that fulfilment confirmation could never be added. |
| D5 | Producer communication during an incident is represented by M17 (request for incident information) and M18 (producer response). No additional producer food safety notice is included in the current register. | UC3 explicitly describes contacting the responsible producer for further information and using the information received to assess the incident. M19 separately represents notifying affected customers. This does not prevent further producer communication if later agreed as necessary. |

## 6. Open questions

The following questions remain open in actors.md and processes.md.
This section records their effects on the interaction register rather
than resolving the wider design decisions.

| No. | Question | Effect on this document |
|---|---|---|
| Q1 (actors.md) | Is the assumption that producers deliver their goods or customers collect them accepted? | If a separate logistics participant is agreed, the participant list and relevant fulfilment messages and relationships will need updating. |
| Q2 (actors.md) | How are weekly settlements paid to producers: through E01 or another provider? | M14 currently represents the business-level settlement interaction. The agreed arrangement may require additional participants, payment instructions, confirmations or changes to message routing. |
| Q3 (actors.md) | Are the notification service (E03) and postcode distance service (E04) internal capabilities or external providers? | If E03 is represented externally, revise the participant list and notification interactions consistently with D3. If E04 is internal, remove its separate participant representation and M21/M22 while retaining the distance-calculation capability. |
| G1 (processes.md) | Does the agreed enterprise scope include a producer onboarding process? | If onboarding is included, assess whether additional participants, messages and process relationships are needed. No onboarding interactions are assumed in the current register. |

## 7. References

UWE Bristol (2026a) *Bristol Regional Food Network: digital marketplace* [Case study]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [case_study/Case Study - v2.pdf](../../case_study/Case%20Study%20-%20v2.pdf).

UWE Bristol (2026b) *Assessment Task 1 use cases* [Assessment material]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Use Case 2 is in [case_study/Case_study.txt](../../case_study/Case_study.txt).

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished.
