# 1.2 Major processes, functions and responsibilities

**Authors:** Shamy, Ishaq Modassir Mushtaq
**Task:** [#80](https://github.com/UWE-DESP/UFCFTR-30-3-DESP/issues/80), Figure 1: strategic BPMN model
**Status:** draft for review

## 1. Purpose and scope

This document lists the major business processes of the Bristol Regional Food Network marketplace, the function that owns each process, and the responsibilities of each actor in it. The strategic BPMN model (Figure 1) shows each process as one activity. The functions become the lanes of the network pool. Task 1.3 takes the messages between the processes from this list, and task 2.2 takes the candidate functionalities from it.

The actors and the external services are in [actors.md](actors.md) (task 1.1). This document uses its IDs: A01 to A07 for the actors and E01 to E06 for the external organisations and services. The chosen use case is Use Case 2: Customer Multi-Vendor Order, Checkout and Payment ([use-case.md](../scope/use-case.md)). The "In UC2" column shows the processes that it needs.

The scope is the whole marketplace, because the strategic model shows the full enterprise. The level is strategic: each process is a unit of work that one function owns, with a trigger and an outcome. The steps inside a process belong to the operational models (Figure 2).

Source keys: CS is the case study (UWE Bristol, 2026a), with the page number. UC1, UC2 and UC3 are the three use cases (UWE Bristol, 2026b). The repository holds UC2 in full. The rows from UC1 and UC3 use the summary of each in actors.md.

## 2. Functions

A function is an area of the enterprise with its own responsibility. The functions of the network (A05) are the lanes of its pool in Figure 1. The customer and the producer are separate pools, so their work is not a lane of the network.

| ID | Function | Pool | Purpose | Owns | Takes part in |
|---|---|---|---|---|---|
| F01 | Catalogue | Network (A05) | Keeps the product listings and the categories that the customers browse, and shows the content of the other lanes next to the products | P01, P03 | P09, P11 |
| F02 | Orders | Network (A05) | Turns a basket into a confirmed marketplace order, splits it by producer, and keeps each producer informed of its orders | P04 | P05, P06, P10 |
| F03 | Finance | Network (A05) | Takes the customer payments, calculates the 5% commission and settles the producers each week with an audit trail | P05, P07 | None |
| F04 | Quality and traceability | Network (A05) | Keeps the certification, allergen and best-before information, the records that link customers, products and producers, and the incident process | P02, P08 | P01 |
| F05 | Quality assurance and community features | Network (A05) | Reports food miles and runs the community features of the case study: surplus produce offers and the educational content that connects customers to the farms. Named after the section of the case study (CS p. 2) | P09, P10, P11 | None |
| F06 | Producer operations | Producer (A04) | The work that each producer does on its side: listing products, keeping stock up to date, and preparing the orders for delivery or collection | P06 | P01, P02, P04, P05, P07, P08, P10, P11 |
| F07 | Customer | Customer (A01 to A03) | The work of the customer: browsing, ordering, paying, collecting or receiving the goods, and raising a quality issue | None | P03, P04, P05, P06, P08, P09, P10, P11 |

**Notes:**

- F06 and F07 are not lanes. They name the side of the work in the producer and customer pools, so that the responsibilities in section 4 have an owner on each side. The network owns the listing (P01) and the browsing (P03), because the marketplace runs them; the producer and the customer supply the input.
- The two UC3 roles in actors.md (A06, marketplace administrator, and A07, authorised marketplace representative) sit in F04. The incident process is the only one that needs them.
- The notification service (E03) and the postcode distance service (E04) are not functions. The processes that use them are P04, P05, P08, P09 and P10. Their place in the model is open (Q3 in actors.md).

## 3. Major processes

Each process has a verb-noun name. The owning function is the lane that holds the activity in Figure 1. The second function, where present, takes part but does not own the process.

| ID | Process | Owning function | Also involved | Trigger | Outcome | Source | In UC2 |
|---|---|---|---|---|---|---|---|
| P01 | Manage product listing | F01 Catalogue | F06 Producer operations, F04 Quality | A producer has a new product, or its availability, stock or price changes | The listing shows the name, the description, the price, the availability timeframe, the stock, the category, the harvest date, the farm origin, and the organic, allergen and best-before information | CS pp. 1-2, UC1 | No (its stock data is an input) |
| P02 | Verify organic certification | F04 Quality and traceability | E02 Certification service | A producer marks a product as organic | The product shows a verified organic status, or the claim is rejected | CS p. 2, UC1 | No |
| P03 | Browse and search catalogue | F01 Catalogue | F07 Customer | A customer opens the marketplace | The customer finds products by category or by search, sees the harvest dates, the farm origin and the seasonal availability, and adds products to a basket | CS p. 2, UC2 | Yes (the start of UC2) |
| P04 | Process order | F02 Orders | F07 Customer, F06 Producer operations | A customer proceeds to checkout | The stock is checked, the producers and the delivery or collection arrangements are identified, the customer confirms, and the marketplace order is split into producer order elements | CS p. 2, UC2 | Yes |
| P05 | Process payment | F03 Finance | F07 Customer, E01 Payment service, E03 Notification service | A confirmed order needs payment | The payment succeeds and the order is confirmed, the stock is updated and the producers are notified, or the customer retries after a decline, or the process follows the exception path when the payment service is unavailable. The amount of each producer and the 5% commission are calculated | CS p. 2, UC2 | Yes |
| P06 | Fulfil order | F06 Producer operations | F02 Orders, F07 Customer | A producer receives a confirmed producer order element | The producer prepares the goods within the lead time (at least 48 hours), and delivers them or hands them over for collection | CS pp. 1-2 | No (follows UC2) |
| P07 | Settle producer payments | F03 Finance | F06 Producer operations, E06 Tax authority | The weekly settlement date | Each producer receives the amount for its orders less the 5% commission, with an audit trail that is suitable for tax reporting | CS p. 2 | No (follows UC2) |
| P08 | Handle quality incident | F04 Quality and traceability | F07 Customer, F06 Producer operations, E03 Notification service | A customer, a producer or the administrator reports a food quality or safety concern | The records that link the customer, the product and the producer identify everyone affected, they are contacted, and the representative reviews the incident and closes it or requests further action | CS p. 2, UC3 | No |
| P09 | Report food miles | F05 Quality assurance and community features | F01 Catalogue, E04 Postcode distance service | A product is shown, or an order is placed, with a customer postcode | The customer sees the distance between the farm and the delivery or collection point, from the postcodes | CS p. 2 | No |
| P10 | Offer surplus produce | F05 Quality assurance and community features | F02 Orders, F06 Producer operations, E03 Notification service | A producer has surplus produce | A last-minute discount is published and the interested customers are told | CS p. 2 | No |
| P11 | Share educational content | F05 Quality assurance and community features | F01 Catalogue, F06 Producer operations | A producer writes a seasonal recipe, storage guidance or a farm story | The content is published next to the products of the producer | CS p. 2 | No |

**Notes:**

- P04 and P05 are the two halves of Use Case 2. The use case runs from the checkout (P04) to the payment result, the stock update and the producer notifications (P05). Together they are the likely call activity for the first operational model (task 2.6). Tasks 2.2 and 2.3 make that decision.
- P03 is the first sentence of UC2 ("a customer browses or searches the marketplace and adds products ... to their basket"). It is a separate process here because browsing happens many times before one checkout.
- P01 is the listing half of Use Case 1. It is split from P02 because the certification check needs an external service and has its own exception path (service unavailable).
- The sources do not describe how a producer joins the network. There is no onboarding process in this list (Q1 below).

## 4. Responsibilities

One row for each process. Each cell gives the part of the actor in the process, or "none".

| ID | Process | Customer (A01 to A03) | Producer (A04) | Network (A05), by function | External (E01 to E06) |
|---|---|---|---|---|---|
| P01 | Manage product listing | None | Lists the product with its name, description, price and availability timeframe. Updates the stock and the seasonal availability. States the organic status, the allergens and the best-before date | F01 stores and publishes the listing. F04 keeps the traceability fields | None |
| P02 | Verify organic certification | None | Claims the certification and gives its details | F04 sends the claim for verification and records the result | E02 checks the certification |
| P03 | Browse and search catalogue | Browses by category, searches, reads the harvest date, the farm origin and the seasonal availability, and fills the basket | None | F01 serves the catalogue and the search | None |
| P04 | Process order | Proceeds to checkout, amends the order when an item is unavailable, reviews the order and confirms | Keeps the stock accurate (through P01) so that the check is right. Has set its delivery or collection arrangements | F02 checks the stock, identifies the producers and the arrangements, creates the marketplace order and splits it by producer | None |
| P05 | Process payment | Submits the payment and retries after a decline | Receives the notification of a new order | F03 submits the payment, handles the decline and the unavailable paths, confirms the order, updates the stock and calculates the producer amounts and the commission. F02 notifies the producers | E01 takes the payment and returns success, decline or unavailable. E03 sends the notifications |
| P06 | Fulfil order | Receives the delivery or collects the goods | Prepares the goods within the lead time and delivers them or hands them over | F02 shows the producer its incoming orders at least 48 hours ahead | None |
| P07 | Settle producer payments | None | Receives the settlement and uses the audit trail for its accounts and tax | F03 calculates the amount of each producer less the 5% commission, pays it weekly and keeps the audit trail | E06 receives the tax reports of the producers. The payer of the settlements is open (Q2 in actors.md) |
| P08 | Handle quality incident | Reports a concern. Receives the food safety notice | Reports a concern. Answers the questions of the network and withdraws the product if asked | F04: A06 reports or receives the concern and finds the affected customers, products and producers from the records. A07 reviews the incident and closes it or requests further action | E03 sends the notices. E05 sets the data protection rules for the records |
| P09 | Report food miles | Gives a postcode and reads the food miles | Gives the postcode of the farm (through P01) | F05 calculates the distance and F01 shows it | E04 gives the distance between the postcodes |
| P10 | Offer surplus produce | Receives the offer and orders through P04 | Reports the surplus and sets the discount | F05 publishes the offer. F02 applies the discount to the order | E03 tells the customers |
| P11 | Share educational content | Reads the content | Writes the recipes, the storage guidance and the farm stories | F05 collects the content and F01 publishes it with the products | None |

## 5. Mapping to the requirements of the case study

Each requirement of the Stakeholder Requirements and the System Requirements sections of the case study maps to at least one process. The first column is the section of the case study.

| Section | Requirement | Processes |
|---|---|---|
| Producers (CS p. 1) | List products with names, descriptions, pricing and availability timeframes | P01 |
| Producers (CS p. 1) | Frequent seasonal inventory updates without technical knowledge | P01 |
| Producers (CS p. 1) | Visibility of incoming orders with at least 48 hours of lead time | P05, P06 |
| Producers (CS p. 2) | Weekly payment settlements with transparent audit trails for tax reporting and accounting | P07 |
| Customers (CS p. 2) | Browsing by category: vegetables, dairy, bakery, preserves and seasonal specialities | P03 |
| Customers (CS p. 2) | Search for specific items | P03 |
| Customers (CS p. 2) | Harvest dates, farm origin and seasonal availability indicators | P01, P03 |
| Customers (CS p. 2) | Checkout for single-vendor and multi-vendor orders, with clear supplier responsibilities, delivery arrangements and collection procedures | P04, P06 |
| Core functionality (CS p. 2) | Product management with seasonal availability updates and inventory management | P01 |
| Core functionality (CS p. 2) | Aggregation of multi-vendor orders with transparency about supplier responsibilities and delivery commitments | P04 |
| Core functionality (CS p. 2) | Secure payment for single and multiple vendor orders | P05 |
| Core functionality (CS p. 2) | Distribution of payments to the producers according to agreed timeframes | P07 |
| Core functionality (CS p. 2) | Automatic calculation of the 5% commission | P05, P07 |
| Core functionality (CS p. 2) | Compliance with data protection and financial services regulations | P05, P07, P08 (a constraint on each, not a process of its own) |
| Quality assurance (CS p. 2) | Organic certification status, allergen warnings and best-before dates | P01, P02 |
| Quality assurance (CS p. 2) | Records that link customers, products and producers, for rapid communication on quality or food safety concerns | P04 (creates the records), P08 (uses them) |
| Environmental reporting (CS p. 2) | Food miles from postcode-based distances | P09 |
| Community features (CS p. 2) | Surplus produce communication with last-minute discounts | P10 |
| Educational components (CS p. 2) | Seasonal recipes, storage guidance and farm stories | P11 |

Use Case 2 adds these points, which the mapping also covers: the stock check at checkout and the request to amend the order (P04), the split of the marketplace order into producer order elements (P04), the stock update and the producer notifications after payment (P05), the retry after a decline and the exception path when the payment service is unavailable (P05), and the amount of each producer and the commission for a multi-vendor order (P05).

## 6. Open questions

| No. | Question | Reason |
|---|---|---|
| Q1 | Does the model need a producer onboarding process? The case study says that forty SMEs are in the network, but it does not say how a producer joins or how its account is set up | It decides if the list has a twelfth process and if the strategic model has an activity for it |
| Q2 | Is the stock update after a successful payment part of P05 (as in UC2) or of P01 (where the stock is kept)? | It decides which lane holds the stock update in the operational model of UC2, and which message the two processes exchange |
| Q3 | Is the notification of the producers a step of P05 (Finance) or of P04 (Orders)? UC2 places it after the payment, but the orders function owns the producer order elements | It decides the lane of the notification in Figure 1 and in the operational model |
| Q4 | Which two processes become the candidate functionalities of tasks 2.2 and 2.3? P04 and P05 together cover UC2. P01 with P02 covers UC1 | It decides which activities are call activities in task 1.6 |

The three open questions of actors.md (the delivery assumption, the payer of the settlements, and the place of E03 and E04) also apply to P06, P07, P05 and P09.

## 7. References

UWE Bristol (2026a) *Bristol Regional Food Network: digital marketplace* [Case study]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Copy in [case_study/Case Study - v2.pdf](../../case_study/Case%20Study%20-%20v2.pdf).

UWE Bristol (2026b) *Assessment Task 1 use cases* [Assessment material]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Use Case 2 is in [case_study/Case_study.txt](../../case_study/Case_study.txt).

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished.
