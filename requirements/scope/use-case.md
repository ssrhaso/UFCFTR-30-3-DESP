# Chosen use case

The group completes **Use Case 2: Customer Multi-Vendor Order, Checkout and Payment** ([Case_study.txt](../../case_study/Case_study.txt)).

## Comparison

| | Use Case 1: product listing and inventory | Use Case 2: multi-vendor order and payment | Use Case 3: food quality incident |
|---|---|---|---|
| Participants | Producer, marketplace, certification service | Customer, several producers, marketplace, payment service | Customer, producer, administrator, marketplace representative |
| Decisions | Data valid? Certification valid? Stock at zero? | Stock available? Payment accepted? | Genuine risk? Suspend the product? |
| Exception paths | Invalid data, verification service unavailable | Stock shortage, payment declined, payment service unavailable | Notification failure |
| Role in the business | Supplies the products | Core sales flow and income (5% commission) | Occasional quality process |

## Reasons

1. It is the core business flow. The marketplace earns its income from it.
2. It connects the most separate parties: the customer, several producers, the marketplace and an external payment service.
3. It covers each element in the brief (p. 4): user tasks, service tasks, decisions, an external service, and exception and retry paths.
4. It carries directly into Task 2. The order, stock and payment steps become services of the Django system.

## Constraints

- Use a sandbox or simulated payment service only. The case study does not permit live payments.
- The flow needs product and stock data from Use Case 1. The group uses test data for it.

## Agreement

Each member confirms the choice with an approval or a comment on the pull request for task 2.1.
