# 1.1 Identify the Key Actors, External Organisations and Services

**Initial draft | Author: Royden Dias**

## 1. Purpose and scope

- Identifies the key actors, external organisations and services relevant to the Bristol Regional Food Network digital marketplace.

- Covers the overall marketplace described in the case study, with reference to the chosen use case: Customer Multi-Vendor Order, Checkout and Payment.

## 2. Key actors

| ID | Actor | Description and relevance |
| --- | --- | --- |
| A01 | Individual/household customer | Young professionals and families purchasing locally sourced produce for personal or household use. |
| A02 | Community organisation buyer | A buyer representing an educational institution, care facility or voluntary organisation that requires local produce for catering. |
| A03 | Restaurant/café buyer | A buyer representing an independent restaurant or café sourcing ingredients from local producers. |
| A04 | Producer/vendor | A local food supplier selling products through the marketplace. The network includes 40 small-to-medium enterprises. |
| A05 | Bristol Regional Food Network / marketplace operator | The organisation behind the marketplace, connecting producers and customers and receiving the network's 5% commission. |

**Note:** A01–A03 are distinct customer segments identified in the case study. This draft retains the segments so their differences are not lost.

## 3. External organisations

These entries identify external organisations involved in the marketplace. Where applicable, they are linked to the actor roles above.

| ID | External organisation | Relevance | Related actor |
| --- | --- | --- | --- |
| O01 | Local producer businesses | Independent food businesses supplying products through the network. | A04 |
| O02 | Educational institutions, care facilities and voluntary organisations | Organisations purchasing local produce for catering requirements. | A02 |
| O03 | Independent restaurants and cafés | Businesses purchasing locally sourced ingredients. | A03 |
| O04 | Payment service provider, if an external sandbox is selected | Supplies the external payment service used during checkout. A simulated service may be used instead, so no particular provider is confirmed. | Not applicable — service provider |

## 4. Relevant services

This table distinguishes required capabilities from decisions about whether to use an external provider.

| ID | Service | Relevance | External-service status |
| --- | --- | --- | --- |
| S01 | Sandbox or simulated payment service | Processes payment attempts for customer orders, including successful payments, declined payments and temporary service unavailability. The wider marketplace also requires weekly producer settlements, calculation of the 5% commission and financial audit records. Responsibility for these additional capabilities remains to be agreed. | Explicitly required as an external or simulated payment service. No provider has been selected, and a separate settlement provider is not specified. |
| S02 | Notification/communication service | Supports producer order notifications, communication concerning product quality or food safety issues, and surplus-produce announcements with last-minute discount offers. | Communication is required, but an external email/SMS provider is not specified. |
| S03 | Postcode-based distance calculation service | Supports the food-mile calculations required by the marketplace. | The capability is required, but an external mapping or postcode service is not specified. |

**Note:** Payment development must use a sandbox or simulated service, not live payment systems or real financial data. Stripe Test Sandbox and PayPal Sandbox are examples given in the case study, not confirmed choices.

## 5. Possible additional participant - (kindly review)

This participant is not explicitly defined in the supplied documents and is not included in the confirmed actor list.

**Delivery/logistics partner**
   - Reason: Orders involve delivery or collection arrangements.
   - Review question: Would delivery be handled by producers or a separate organisation?

## 6. Sources

- Case Study
- Use Case