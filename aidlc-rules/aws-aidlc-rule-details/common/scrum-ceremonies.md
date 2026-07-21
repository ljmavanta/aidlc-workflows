# Scrum Ceremonies Reference

**Purpose**: Shared reference for the Scrum framing of this workflow. Ceremonies are **first-class stages** with their own gates. This file defines each ceremony, its intent, and how it maps onto the workflow's phases and directories.

Load this file at workflow start (see `core-workflow.md`). Individual ceremony stages have their own detailed rule files (referenced below).

## Framing

This workflow runs a Scrum cadence **on top of** the existing three-phase structure. Directory names and phase IDs (`inception/`, `construction/`, `operations/`) are unchanged — Scrum is layered as ceremonies and vocabulary.

- **Product Backlog** = the team's Product Inputs (see `team-inputs.md`), refined during Backlog Refinement.
- **Sprint** = one pass through the CONSTRUCTION per-increment loop (an increment ≈ a Unit of Work).
- **Increment** = the working, tested output of a sprint that satisfies the Definition of Done.
- **Tasks** = the team's typed work items under each story (`research`/`design`/`coding`; see `team-inputs.md`). Within an increment they run in order `research → design → coding`.

## Ceremony Map

| Ceremony | Phase | Detailed rule file | Cadence | Gate |
| ---------------------- | -------------------- | ------------------------------------------ | ---------------------- | ----------------- |
| Backlog Refinement     | 🔵 INCEPTION         | `inception/backlog-refinement.md`          | Start of work / ongoing | Approval gate     |
| Sprint Planning        | 🔵 INCEPTION         | `inception/workflow-planning.md`           | Start of each sprint   | Approval gate     |
| Daily Standup          | 🟢 CONSTRUCTION      | `common/daily-standup.md`                  | Each work session      | Lightweight (log) |
| Sprint Review          | 🟢 CONSTRUCTION      | `construction/sprint-review.md`            | End of each sprint     | Approval gate     |
| Sprint Retrospective   | 🟢 CONSTRUCTION      | `construction/sprint-retrospective.md`     | End of each sprint     | Approval gate     |

## Ceremony Definitions

### Backlog Refinement

Ingest and validate the team's Product Backlog. The agent checks stories/requirements for consistency, gaps, and INVEST quality; raises `[VALIDATION]` findings; and offers `[SUGGESTION]` additions. It does **not** author the backlog. Runs the Input Intake Gate for Product Inputs.

### Sprint Planning

Select the backlog items (increments/units) for the upcoming sprint, define the **Sprint Goal**, and confirm the **Definition of Done**. This is the reframed Workflow Planning stage — it still produces the execution plan, now expressed as a sprint plan.

### Daily Standup

A lightweight per-session checkpoint recorded in `aidlc-docs/construction/sprint-log.md`: what was completed, what is next, and any impediments/blocking gates. Not an approval gate — it keeps the sprint state visible and honest.

### Sprint Review

Demonstrate and verify the increment against the Sprint Goal and Definition of Done, using the Build and Test outputs. Produces a review record and a go/no-go on the increment. Approval gate.

### Sprint Retrospective

Capture what went well, what to improve, and concrete action items. Improvement items that affect scope or the backlog feed back into the Product Backlog for the team to prioritize. Approval gate.

## Sprint Loop

```text
   Backlog Refinement  ──►  Sprint Planning  ──►  ┌─ Sprint Execution ──────────────┐
                                                  │  Daily Standup (each session)   │
                                                  │  per increment, per task type:  │
                                                  │  Research → Design → Coding     │
                                                  │  Build & Test                   │
                                                  └─────────────────────────────────┘
                                                             │
                                                             ▼
                                       Sprint Review  ──►  Sprint Retrospective
                                                             │
                                        (improvements + unfinished items ──► Product Backlog)
```

**Note**: All ceremony gates preserve the existing governance model — approval gates, `audit.md` logging, checkbox enforcement, and content validation apply exactly as defined in `core-workflow.md`.
