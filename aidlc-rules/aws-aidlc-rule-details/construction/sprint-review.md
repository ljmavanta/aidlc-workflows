# Sprint Review (Scrum Ceremony)

**Purpose**: Demonstrate and verify the sprint's increment against the **Sprint Goal** and the **Definition of Done (DoD)**, using the Build and Test outputs. Produce a review record and a go/no-go decision on the increment.

**See `common/scrum-ceremonies.md` for the sprint loop.**
**See `common/team-inputs.md` for the Definition of Done input.**

## Prerequisites

- All increments/units planned for the sprint have completed Code Generation
- Build and Test must be complete for the sprint (see `construction/build-and-test.md`)
- Sprint Goal is recorded in the sprint plan (from Sprint Planning)

## Required Inputs (Intake Gate)

Run the Input Intake Gate from `team-inputs.md` for the **Definition of Done**:

- `aidlc-docs/team-inputs/definition-of-done.md`

**If absent**: STOP and raise the blocking gate. The Sprint Review cannot certify an increment "Done" without the team's DoD. Wait for the team to provide it or explicitly waive (a waiver is recorded and the review reports "DoD not defined — increment accepted without a Done standard").

## Execution Steps

### Step 1: Assemble the Increment

- Load the sprint plan (Sprint Goal, selected increments/units, story coverage).
- Load Build and Test results from `aidlc-docs/construction/build-and-test/build-and-test-summary.md`.
- Load the standup log (`aidlc-docs/construction/sprint-log.md`) for impediments encountered.

### Step 2: Verify Against the Definition of Done

For each DoD criterion, record status with evidence:

```markdown
## Definition of Done Verification
| DoD Criterion | Status | Evidence |
| ------------- | ------ | -------- |
| [Criterion]   | [Met/Not Met/N/A] | [Path to artifact, test result, or rationale] |
```

- Any **Not Met** criterion is a blocking finding — the increment is **not** Done.

### Step 3: Verify Against the Sprint Goal and Stories

- Map each committed story/backlog item to its implemented, tested output.
- Mark each as **Delivered**, **Partially Delivered**, or **Not Delivered**, with the reason.
- Confirm team coding conventions and architecture (engineering biases) were followed — reference `code-generation.md` compliance notes.

### Step 4: Produce the Sprint Review Record

Create `aidlc-docs/construction/sprint-review/sprint-review.md`:

```markdown
# Sprint Review — [Sprint Goal]

## Increment Summary
- **Sprint Goal**: [goal]
- **Increments/Units**: [list]

## Story Delivery
[Delivered / Partially / Not Delivered per story, with reasons]

## Definition of Done Verification
[Table from Step 2]

## Build & Test Outcome
[Summary referencing build-and-test-summary.md]

## Decision
- **Increment Accepted**: [Yes/No]
- **Unfinished Items** (return to Product Backlog): [list]
```

### Step 5: Update State Tracking

- Mark Sprint Review complete in `aidlc-docs/aidlc-state.md`.
- List unfinished items to be returned to the Product Backlog for re-prioritization.

### Step 6: Log and Present Completion

- Log the approval prompt and response in `aidlc-docs/audit.md` (ISO 8601, complete raw input).

```markdown
# 🔍 Sprint Review Complete

[AI summary: stories delivered vs committed, DoD criteria met vs not — factual]

> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the sprint review record at: `aidlc-docs/construction/sprint-review/sprint-review.md`

> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Address unmet Definition of Done criteria or undelivered stories
> ✅ **Approve & Continue** - Accept the increment and proceed to **Sprint Retrospective**
```

- Wait for explicit approval. Record the response in `audit.md`.

## Critical Rules

- **DoD is binding**: an increment with any unmet, non-waived DoD criterion is not Done.
- **Honest delivery reporting**: never mark a story delivered without tested evidence.
- **Unfinished work returns to the backlog**: it is not silently dropped.
- **Preserve governance**: approval gate, audit logging, and content validation apply.
