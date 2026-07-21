# Backlog Refinement (Scrum Ceremony)

**Assume the role** of a facilitator working with a Product Owner — **not** the Product Owner. The team owns the backlog; you refine and validate it.

**Purpose**: Ingest the team's Product Backlog, validate it for consistency and quality, surface gaps and conflicts, and propose clearly-marked suggestions — without authoring the backlog on the team's behalf.

**See `common/team-inputs.md` for the input contract and the Input Intake Gate.**
**See `common/scrum-ceremonies.md` for how this ceremony fits the sprint loop.**

## Prerequisites

- Workspace Detection must be complete (Team Inputs presence recorded in `aidlc-state.md`)
- Reverse Engineering must be complete (if brownfield)

## Required Inputs (Intake Gate)

Run the Input Intake Gate from `team-inputs.md` for the **Product Inputs**:

- `aidlc-docs/team-inputs/product-vision.md`
- `aidlc-docs/team-inputs/product-backlog.md`
- `aidlc-docs/team-inputs/task-breakdown.md` (typed tasks under each story)
- `aidlc-docs/team-inputs/requirements.md` (only if the team keeps requirements separate from the backlog)

**If any required Product Input is absent**: STOP and raise the blocking gate. Do not fabricate vision, backlog items, requirements, or tasks. Wait for the team to provide or explicitly waive.

## Execution Steps

### Step 1: Load Team Inputs as Source of Truth

- Load the provided Product Inputs. These are authoritative.
- Load Reverse Engineering artifacts (if brownfield) for cross-referencing against existing behavior.
- Convert any non-markdown provided content to markdown for the working copy (never alter the team's intent).

### Step 2: Validate the Backlog

Evaluate the team's backlog and produce `[VALIDATION]` findings for any of:

- **Consistency**: Items that contradict the product vision or each other.
- **Completeness gaps**: Vision goals with no backlog item; acceptance criteria missing.
- **INVEST quality**: Items that are not Independent, Negotiable, Valuable, Estimable, Small, or Testable.
- **Ambiguity**: Vague terms, undefined criteria, or overlapping scope between items.
- **Duplication / overlap**: Items that should be merged or split.

### Step 2.5: Validate the Task Breakdown

Evaluate the team's typed task breakdown (`task-breakdown.md`) against the stories and produce `[VALIDATION]` findings for any of:

- **Coverage**: A story with no tasks, or acceptance criteria not covered by any task.
- **Valid types**: Every task is typed `research`/`spike`, `design`, or `coding` (see `team-inputs.md` for the task → stage mapping). Unknown types are a finding, not a silent default.
- **Orphan tasks**: A task not tied to any story.
- **Ordering sanity**: A `coding` task that clearly depends on an unresolved `research` spike or missing `design` task.
- **`[SUGGESTION]`**: propose missing tasks (e.g., a spike for an obvious unknown, a design task for a complex story) for team approval — never add them silently.

### Step 3: Propose Suggestions (Clearly Marked)

- Where the agent sees a valuable, low-risk addition (a missing edge case, a nice-to-have story, a clarifying acceptance criterion), record it as a `[SUGGESTION]`.
- Suggestions are **proposals only**. They are never adopted into the backlog without explicit team approval.

### Step 4: Generate Clarifying Questions

- Create `aidlc-docs/inception/backlog/backlog-refinement-questions.md` following `common/question-format-guide.md`.
- Ask about every `[VALIDATION]` finding that requires a team decision and every `[SUGGESTION]` requiring approval.
- Use [Answer]: tags with A/B/C/D options plus an "Other" option where applicable.

### ⛔ GATE: Await Team Answers

DO NOT proceed until all questions are answered and analyzed. Present the questions file and STOP.

### Step 5: Produce the Refined Backlog Report

- Create `aidlc-docs/inception/backlog/refined-backlog.md` containing:
  - A reference to the authoritative team backlog (do not copy-replace it).
  - The resolved `[VALIDATION]` findings and how the team decided each.
  - Approved `[SUGGESTION]` items now folded in (with attribution as agent-proposed, team-approved).
  - Rejected suggestions listed briefly for the audit trail.
- This report is a **validation/consolidation artifact**, not an agent-authored backlog.

### Step 6: Update State Tracking

Update `aidlc-docs/aidlc-state.md`:

```markdown
## Stage Progress
### 🔵 INCEPTION PHASE
- [x] Workspace Detection
- [x] Reverse Engineering (if applicable)
- [x] Backlog Refinement
```

### Step 7: Log and Present Completion

- Log the approval prompt and response in `aidlc-docs/audit.md` (ISO 8601, complete raw input).
- Present the completion message:

```markdown
# 📋 Backlog Refinement Complete

[AI summary: counts of validation findings raised/resolved, suggestions approved/rejected — factual, no workflow instructions]

> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the refined backlog report at: `aidlc-docs/inception/backlog/refined-backlog.md`

> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for adjustments to the validation findings or suggestions
> ✅ **Approve & Continue** - Approve the refined backlog and proceed to **Requirements Analysis / User Stories**
```

- Wait for explicit approval. Record the response in `audit.md`.
- Mark Backlog Refinement complete in `aidlc-state.md`.

## Critical Rules

- **NEVER author the backlog**: the team owns it; you validate, clarify, and suggest.
- **Mark every finding**: use `[VALIDATION]` and `[SUGGESTION]` tags consistently.
- **No silent adoption**: suggestions require explicit team approval.
- **Preserve governance**: approval gate, audit logging, and content validation apply.
