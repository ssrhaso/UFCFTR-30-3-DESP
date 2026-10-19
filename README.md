# UFCFTR-30-3 Distributed and Enterprise Software Development

This repository holds the group project for the Distributed and Enterprise Software Development module (UFCFTR-30-3) at UWE Bristol, 2026-27.

## Assessment tasks

| Task | Weight | Content | Due |
|---|---|---|---|
| Task 1 | 40% | BPMN modelling: a strategic BPMN model, an executable operational BPMN model (Camunda 8) and an i* socio-technical model, with a critical evaluation and an in-class demonstration | Last week of TB1 (week 18, w/c 14 Dec 2026) |
| Task 2 | 60% | System development with Django, Django REST Framework, Docker and a relational database, with an in-class demonstration | Last week of TB2 (week 37, w/c 26 Apr 2027) |

The team works in Scrum sprints, and the tutor acts as the customer. The operational BPMN models from Task 1 become microservices in the Task 2 system.

## Case study

The tutor's case study is the Bristol Regional Food Network, a digital marketplace that connects about forty local food producers with customers within twenty miles of Bristol city centre. The brief is in [case_study/](case_study/):

- [Case Study - v2.pdf](case_study/Case%20Study%20-%20v2.pdf): the background, the stakeholder requirements and the system requirements
- [Case_study.txt](case_study/Case_study.txt): Use Case 2, the customer multi-vendor order, checkout and payment process. It is the first operational model ([task 2.6](https://github.com/UWE-DESP/UFCFTR-30-3-DESP/issues/49))

The stakeholders are the producers (small and medium enterprises with mixed technical skills), three customer segments (young professionals and families, community groups, and independent restaurants and cafés) and the network itself, which takes a 5% commission on each order.

The system must provide:

- Product management: listings with a name, a description, a price and an availability timeframe, with seasonal inventory updates
- Browsing and search by category, with harvest dates, farm origin and seasonal availability
- Checkout for single-vendor and multi-vendor orders, with clear supplier, delivery and collection responsibilities
- Payment for single and multi-vendor orders, with the amount for each producer, the 5% commission, and weekly settlements with an audit trail
- Order visibility for the producers, with at least 48 hours of lead time
- Traceability: organic certification, allergen warnings, best-before dates, and records that link customers, products and producers
- Food miles from postcode distances, surplus produce discounts, and recipes, storage guidance and farm stories

Payments use a sandbox or simulated service only (Stripe test mode, PayPal sandbox, or a mock service in Docker). The case study forbids live payment systems and real financial data.

## How we work

The group tracks the work in GitHub Projects: [DESD Task 1: Process modelling and automation](https://github.com/users/ssrhaso/projects/4) and [DESD Task 2: System](https://github.com/users/ssrhaso/projects/5). Each figure has one parent issue, with one sub-issue (task) for each piece of work. Each task has one owner.

### Steps for each task

1. Assign the task to yourself, and set its status to In progress.
2. Create a branch from the task (Development > Create a branch).
3. Open a pull request. Name it after the task, for example `1.1 Identify the key actors, external organisations and services`, and put `Closes #<task number>` in the body. Set the task to In review.
4. At least 1 other member reviews and approves the pull request. Then merge it with a merge commit.

When the pull request merges, GitHub closes the task, and the board moves it to Done. The GitHub checks run only when a pull request is merged into `main`. They flag each merge that has no `Closes #<task number>`, no approval from another member, or a model that fails the BPMN lint. GitHub cannot block a merge on this plan, so check these rules before you merge.

The Task 1 board has one tab for each figure and one for the critical evaluation. Figure 1 is the strategic BPMN model, Figure 2 is the operational BPMN models and Figure 3 is the i* model. The critical evaluation is the fourth parent issue ([#50](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/50)). The tasks of each parent have numbers: 1.1, 1.2 and so on, and 4.1, 4.2 and so on for the evaluation. To add a task, open the parent, create a sub-issue with the "Task" template, and start its title with the next number of that parent.

### Definition of done

A task is done when all these conditions are true:

- The work is merged into `main` through a pull request that at least 1 other member approved.
- Each model has its source file and a `.png` or `.svg` export in the correct `task1-bpmn/` folder.
- Each operational model deploys and runs in Camunda 8.

## Key dates

| Date | Event |
|---|---|
| Wed 7 Oct 2026, 23:59 | Group formation form closes |
| Mon 12 Oct 2026 | Sprint 1 of Task 1 starts. Group membership becomes final. Each member must have Camunda 8 access |
| Thu 29 Oct 2026, 14:01 | Task 1 Sprint 1 Review due on Blackboard |
| Thu 19 Nov 2026, 14:01 | Task 1 Sprint 2 Review due on Blackboard |
| Thu 10 Dec 2026, 14:01 | Task 1 Sprint 3 Review due on Blackboard |
| Thu 4 Mar 2027, 14:01 | Task 2 Sprint 1 Review due on Blackboard |
| Thu 25 Mar 2027, 14:01 | Task 2 Sprint 2 Review due on Blackboard |
| Thu 13 May 2027, 14:01 (BST) | Task 2 Sprint 3 Review due on Blackboard |

## Repository layout

| Folder | Content |
|---|---|
| [lectures/](lectures/) | Module slides and practical sheets |
| [case_study/](case_study/) | The tutor's case study and the use cases |
| [team/](team/) | Members, roles, working arrangements and the skills inventory |
| [requirements/](requirements/) | Requirements, user stories and business analysis |
| [task1-bpmn/](task1-bpmn/) | Task 1: the strategic, operational and i* models, and the critical evaluation |
| [diagrams/](diagrams/) | Architecture, component, service, deployment and data diagrams |
| [sprints/](sprints/) | Sprint plans, stand-up notes and Sprint Reviews |
| [task2-system/](task2-system/) | Task 2: the Django system (from TB2) |
