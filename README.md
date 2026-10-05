# UFCFTR-30-3 Distributed and Enterprise Software Development

This repository holds the group project for the Distributed and Enterprise Software Development module (UFCFTR-30-3) at UWE Bristol, 2026-27.

## Assessment tasks

| Task | Weight | Content | Due |
|---|---|---|---|
| Task 1 | 40% | BPMN modelling: a strategic BPMN model, an executable operational BPMN model (Camunda 8) and an i* socio-technical model, with a critical evaluation and an in-class demonstration | Last week of TB1 (week 18, w/c 14 Dec 2026) |
| Task 2 | 60% | System development with Django, Django REST Framework, Docker and a relational database, with an in-class demonstration | Last week of TB2 (week 37, w/c 26 Apr 2027) |

The team works in Scrum sprints, and the tutor acts as the customer. The operational BPMN models from Task 1 become microservices in the Task 2 system.

## How we work

The group tracks the work at two levels:

| Level | Tool | Content |
|---|---|---|
| High | Jira, [DESD space](https://desdproject.atlassian.net/jira/software/projects/SCRUM/summary) (key `SCRUM`) | One work item for each deliverable, planned into the Jira sprints |
| Low | GitHub Projects: [DESD Task 1: Figures](https://github.com/orgs/UWE-DESP/projects/1) and [DESD Task 2: System](https://github.com/orgs/UWE-DESP/projects/2) | One parent issue for each Jira work item, with one sub-issue (task) for each piece of work. Each task has one owner |

The GitHub for Atlassian app connects Jira to this repository. Jira shows each pull request and commit that contains a `SCRUM` key on the work item with that key.

### Steps for each task

1. Assign the task to yourself, and set its status to In progress.
2. Create a branch from the task (Development > Create a branch).
3. Start each commit message with the Jira key of the figure, for example `SCRUM-12 Add the pools to the strategic model`.
4. Open a pull request. Start the title with the Jira key, and put `Closes #<task number>` in the body. Set the task to In review.
5. Another member reviews the pull request. Then merge it with a merge commit.

When the pull request merges, GitHub closes the task, and the board moves it to Done. A GitHub check fails each pull request that has no `SCRUM` key. Move the Jira work items by hand at sprint planning and at the Sprint Review.

The Task 1 board has one tab for each figure. Figure 1 is the strategic BPMN model (SCRUM-12), Figure 2 is the operational BPMN models (SCRUM-13) and Figure 3 is the i* model (SCRUM-14). The tasks of each figure have numbers: 1.1, 1.2 and so on. To add a task, open the figure, create a sub-issue with the "Task" template, and start its title with the next number of that figure.

### Definition of done

A task is done when all these conditions are true:

- The work is merged into `main` through a reviewed pull request.
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
| [team/](team/) | Members, roles, working arrangements and the skills inventory |
| [requirements/](requirements/) | Requirements, user stories and business analysis |
| [task1-bpmn/](task1-bpmn/) | Task 1: the strategic, operational and i* models, and the critical evaluation |
| [diagrams/](diagrams/) | Architecture, component, service, deployment and data diagrams |
| [sprints/](sprints/) | Sprint plans, stand-up notes and Sprint Reviews |
| [task2-system/](task2-system/) | Task 2: the Django system (from TB2) |
