# 1.1 Key actors, external organisations and services

**Authors:** Royden Dias, Hasaan Ahmad
**Task:** [#79](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/79), Figure 1: strategic BPMN model (SCRUM-12)
**Status:** draft for review

## 1. Purpose and scope

This document identifies the actors, the external organisations and the services of the Bristol Regional Food Network marketplace. The strategic BPMN model (Figure 1) and the i* models (Figure 3) use this list.

The scope is the whole marketplace, because the strategic model shows the full enterprise. The chosen use case is Use Case 2: Customer Multi-Vendor Order, Checkout and Payment ([use-case.md](../scope/use-case.md)). The "In UC2" column shows the entries that it needs.

The "BPMN element" column gives the place of each entry in the strategic model: a pool, a lane, an external participant (a collapsed pool) or not in BPMN. The brief requires "key actors", "external organisations and services" and "interactions between different areas of the enterprise" (UWE Bristol, 2026c, p. 3).

Source keys: CS is the case study (UWE Bristol, 2026a), with the page number. UC1, UC2 and UC3 are the three use cases (UWE Bristol, 2026b).

## 2. Key actors

| ID | Actor | Role | Main need | Source | In UC2 | BPMN element |
|---|---|---|---|---|---|---|
| A01 | Household customer | Young professionals and families who buy local produce for the home | Buy from many producers without visits to farm shops in their restricted opening hours | CS p. 1 | Yes | Customer pool (collapsed), shared with A02 and A03 |
| A02 | Community group buyer | Buys local food for the catering of an educational institution, a care facility or a voluntary organisation | Find reliable and consistent local suppliers | CS p. 1 | Yes | Customer pool (shared) |
| A03 | Restaurant or café buyer | Buys ingredients for an independent restaurant or café | Buy locally without the administration of many small suppliers | CS p. 1 | Yes | Customer pool (shared) |
| A04 | Producer | One of 40 local SMEs. Lists products, updates stock and prepares orders for delivery or collection (see section 4) | Reach customers beyond farmers' markets and farm gate sales. Simple tools for mixed technical skills: some producers use only email and telephone, for about 15 hours each week. Order visibility at least 48 hours ahead. Weekly settlements with an audit trail | CS pp. 1–2, UC1, UC2 | Yes | Pool |
| A05 | Bristol Regional Food Network | The community initiative that runs the marketplace. Connects producers with customers within 20 miles of Bristol city centre. Takes a 5% commission on each order | Income from the commission. Sustainability: food miles and less food waste. Community connections and local food education | CS pp. 1–2, UC2 | Yes | Pool (the enterprise) |
| A06 | Marketplace administrator | A role in the network. Can report a food quality or safety issue | Not stated | UC3 | No | Lane in A05 |
| A07 | Authorised marketplace representative | A role in the network. Reviews each food quality incident, then closes it or requests further action | Not stated | UC3 | No | Lane in A05 |

**Notes:**

- A01, A02 and A03 have the same role in the order process. The list keeps them separate, because their needs are different. The i* models need these differences.
- A06 and A07 are roles inside A05. Only UC3 uses them. The final lane names of A05 come from task 1.2.

## 3. External organisations and services

These participants are outside the marketplace. The marketplace exchanges data with them, but it does not control them.

| ID | Participant | Type | Role | Status | Source | In UC2 | BPMN element |
|---|---|---|---|---|---|---|---|
| E01 | Payment service | Service | Takes each customer payment and returns the result: success, decline or service unavailable | Required. Use a sandbox or a mock only: Stripe test mode, PayPal Sandbox or a mock service in Docker. No provider is chosen | CS pp. 1–2, UC2 | Yes | External participant |
| E02 | Organic certification verification service | Service | Checks the organic certification that a producer claims for a product | Required by UC1, as an external or simulated service | CS p. 2, UC1 | No | External participant |
| E03 | Notification service | Service | Sends order notifications to producers, food safety notices to customers and surplus produce offers | The capability is required. The sources do not name an external email or SMS provider | CS p. 2, UC2, UC3 | Yes | External participant, TBC (Q3) |
| E04 | Postcode distance service | Service | Gives the postcode distances for the food miles calculation | The capability is required. The sources do not name an external provider | CS p. 2 | No | External participant, TBC (Q3) |
| E05 | Data protection and financial services regulators | Organisation | Set the rules for personal data and financial transactions | Implied: all financial transactions "must comply with current data protection and financial services regulations" | CS p. 2 | No | Not in BPMN (i* only) |
| E06 | Tax authority | Organisation | Receives the tax reports of the producers, which use the settlement audit trail | Implied: settlements need audit trails "suitable for tax reporting purposes" | CS p. 2 | No | Not in BPMN (i* only) |

**Note:** E05 and E06 do not take part in the order flow. The i* models and the evaluation of the legal, ethical, social and professional issues (Sprint 3) need them.

## 4. Delivery and collection

The first draft asked if a separate delivery or logistics partner takes part. The sources make delivery and collection a responsibility of each supplier:

- The checkout must give "clear communication about individual supplier responsibilities, delivery arrangements, and collection procedures" (CS p. 2).
- Order processing must keep "complete transparency regarding individual supplier responsibilities and delivery commitments" (CS p. 2).
- In UC2, "the system identifies the producers involved and determines the relevant delivery or collection arrangements".
- No source names a courier or a logistics organisation.

**Assumption:** each producer (A04) delivers its part of the order, or the customer collects it. The list has no logistics partner. The group confirms this with the tutor (Q1).

## 5. Open questions

| No. | Question | Reason |
|---|---|---|
| Q1 | Does the tutor accept the delivery assumption in section 4? | It decides if the model needs a logistics participant |
| Q2 | Who pays the weekly settlements to the producers: the network through E01, or a separate bank or provider? | The case study requires payment to producers "according to agreed timeframes" (CS p. 2), but it does not name a party |
| Q3 | Are the notification service (E03) and the postcode distance service (E04) part of the platform, or external providers? | It decides if E03 and E04 are external participants |

## 6. References

UWE Bristol (2026a) *Bristol Regional Food Network: digital marketplace* [Case study]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [case_study/Case Study - v2.pdf](../../case_study/Case%20Study%20-%20v2.pdf).

UWE Bristol (2026b) *Assessment Task 1 use cases* [Assessment material]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Use Case 2 is in [case_study/Case_study.txt](../../case_study/Case_study.txt).

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished.
