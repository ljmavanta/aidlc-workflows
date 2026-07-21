# Research / Spike (Task Type)

**Purpose**: Resolve a specific unknown before design or coding proceeds. A research task (spike) produces a **findings + recommendation** artifact that later stages consume — it does not produce production code.

**See `common/team-inputs.md` for the typed-task model and the task → stage mapping.**

## When This Stage Runs

- Execute for each increment that has one or more `research` (a.k.a. `spike`) tasks in the team's task breakdown.
- **Ordering**: Research runs **first in the per-increment loop — before Functional Design** — because a spike's purpose is usually to decide the design. If a research task has no design/coding dependents, it may still run standalone.
- **Skip** for increments with no research tasks.

## Prerequisites

- The increment's tasks are known (from Units Generation / the team task breakdown)
- A Daily Standup entry has been recorded for this work session

## Execution Steps

### Step 1: Frame the Spike

For each research task, capture (do not answer yet):

- **Question**: the exact unknown to resolve (e.g., "WebSocket vs SSE for the live dashboard?")
- **Why it matters**: which story/design/coding tasks depend on the answer
- **Decision criteria**: what dimensions decide it (e.g., latency, browser support, ops cost, team familiarity — cross-check against `team-inputs/architecture.md` and `team-inputs/coding-conventions.md`)
- **Timebox**: the team's bound on the investigation, if any

If the question or criteria are unclear, raise a `[VALIDATION]` finding and ask the team using `common/question-format-guide.md` before investigating.

### Step 2: Investigate

- Gather evidence: read the existing codebase (brownfield), the team's architecture/conventions, relevant docs, and — where available — run small experiments or prototypes in a scratch location (NEVER commit spike code into the workspace as production code; keep it clearly separate or discard it).
- Evaluate each option against the decision criteria from Step 1.
- Respect the team's engineering biases: an option that conflicts with `team-inputs/architecture.md` is noted as such and is not recommended unless the team relaxes the constraint.

### Step 3: Produce the Findings Artifact

Create `aidlc-docs/construction/{unit-name}/research/{task-slug}-findings.md`:

```markdown
# Spike Findings — [task title]

## Question
[the unknown]

## Options Evaluated
| Option | Pros | Cons | Conforms to team architecture? |
| ------ | ---- | ---- | ------------------------------ |
| [A]    | ...  | ...  | [Yes/No — why]                 |
| [B]    | ...  | ...  | [Yes/No — why]                 |

## Evidence
[Benchmarks, prototype notes, doc references — factual]

## Recommendation
- **Recommended option**: [A/B/...]
- **Rationale**: [tied to the decision criteria]
- **Impact on design/coding tasks**: [what this decides for dependents]
- **[SUGGESTION]** (if any): follow-ups the team may want to consider

## Status
- [Recommended / Inconclusive — needs team decision]
```

**The recommendation is a `[SUGGESTION]`** until the team approves it. Do NOT let a spike silently set a binding architectural decision — that belongs to the team (see `team-inputs.md`).

### Step 4: Update State Tracking

- Record the research task as complete in `aidlc-docs/aidlc-state.md` and mark it `[x]` in the increment's task list.
- Note the decision so downstream design/coding tasks can reference it.

### Step 5: Present Completion Message

- Log the approval prompt and response in `aidlc-docs/audit.md` (ISO 8601, complete raw input).

```markdown
# 🔬 Spike Complete - [unit-name] - [task title]

[AI summary: the question and the recommended option with one-line rationale — factual]

> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the findings at: `aidlc-docs/construction/[unit-name]/research/[task-slug]-findings.md`

> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for more investigation or different options
> ✅ **Approve & Continue** - Accept the recommendation; it becomes an input to the design/coding tasks
```

- Wait for explicit approval. If the team picks a different option or refines the question, update the findings and re-present.
- Record the approved decision; the subsequent design stages MUST honor it.

## Critical Rules

- **Findings, not code**: a spike produces a recommendation artifact, not production code.
- **Recommendations are `[SUGGESTION]`s**: binding decisions require team approval.
- **Runs before design**: resolve the unknown first so design and code build on a decided foundation.
- **Respect team biases**: options conflicting with the team's architecture/conventions are flagged, not silently chosen.
- **Preserve governance**: approval gate, audit logging, and content validation apply.
