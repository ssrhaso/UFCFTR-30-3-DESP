# Strategic BPMN model

The strategic-level BPMN model of the enterprise system architecture. It shows the whole system at a high level. The detail of each component is in the [operational](../operational/) models.

## Model

| Item | Value |
|---|---|
| File | `strategic-architecture.bpmn` |
| Export | `strategic-architecture.svg` (or `.png`) |
| Camunda process ID | `strategic-architecture` |
| Camunda project / folder | `strategic` |
| Owner | |
| Last updated | |

## Scenario

<!-- Two or three sentences: what the enterprise does and what the system is for. -->

## Actors and systems (one pool each)

| Pool | Type (person, organisation or system) | Responsibility | Operational model |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## Main interactions (message flows)

| From | To | Message | Purpose |
|---|---|---|---|
| | | | |
| | | | |

## Modelling rules

- One pool for each actor or system. Connect pools with message flows, not sequence flows.
- Keep each pool to a few high-level steps. Forms, scripts and error handling belong in the operational models.
- Each system pool has an operational model with the same name in `../operational/`.
- Use the same actor names as in the i* model in `../istar/`.

## Workflow

1. Edit the model in the Camunda Web Modeler.
2. Download the `.bpmn` file and export the `.svg`.
3. Replace the files in this folder and commit them with a message that names the change.
