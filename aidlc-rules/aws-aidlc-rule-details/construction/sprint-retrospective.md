# Sprint Retrospective (Scrum Ceremony)

**Purpose**: Reflect on the sprint's process — what went well, what to improve — and capture concrete action items. Improvement items that affect scope feed back into the Product Backlog for the team to prioritize.

**See `common/scrum-ceremonies.md` for the sprint loop.**

## Prerequisites

- Sprint Review must be complete (increment accepted or its unfinished items recorded)

## Execution Steps

### Step 1: Gather Sprint Evidence

- Load the sprint plan, `aidlc-docs/construction/sprint-log.md` (standups/impediments), and the Sprint Review record.
- Load `aidlc-docs/audit.md` entries for the sprint to ground the reflection in what actually happened (not impressions).

### Step 2: Facilitate Reflection

Structure the retrospective around three prompts. The agent proposes observations grounded in evidence; the team confirms, edits, or adds. Ask clarifying questions using `common/question-format-guide.md` where team judgment is needed.

- **What went well**: Practices, decisions, or tooling to keep.
- **What to improve**: Friction points — recurring impediments, ambiguous inputs, rework, failing gates.
- **Action items**: Specific, owned, and (where possible) measurable changes for the next sprint.

### Step 3: Classify Action Items

For each action item, classify its destination so nothing is lost:

| Type | Destination |
| ------------------------------ | ------------------------------------------------------------- |
| Backlog-affecting (new scope)  | Returned to `aidlc-docs/team-inputs/product-backlog.md` as a `[SUGGESTION]` for team prioritization |
| Process/convention change      | Proposed edit to `aidlc-docs/team-inputs/coding-conventions.md` or team practice (team decides) |
| Workflow tuning                | Note in the retrospective record; applied next sprint         |

**Rule**: The agent does not silently change team inputs. Backlog and convention changes are proposed as `[SUGGESTION]` items requiring explicit team approval.

### Step 4: Produce the Retrospective Record

Create `aidlc-docs/construction/sprint-retrospective/sprint-retrospective.md`:

```markdown
# Sprint Retrospective — [Sprint Goal]

## What Went Well
- [...]

## What To Improve
- [...]

## Action Items
| Action | Type | Owner | Destination |
| ------ | ---- | ----- | ----------- |
| [...]  | [Backlog/Process/Workflow] | [team/agent] | [path or note] |

## Items Returned to Product Backlog
- [list of unfinished + newly proposed items]
```

### Step 5: Update State Tracking

- Mark Sprint Retrospective complete in `aidlc-docs/aidlc-state.md`.
- Record whether another sprint follows (return to Sprint Planning) or the work is complete.

### Step 6: Log and Present Completion

- Log the approval prompt and response in `aidlc-docs/audit.md` (ISO 8601, complete raw input).

```markdown
# 🔄 Sprint Retrospective Complete

[AI summary: counts of action items by type, items returned to backlog — factual]

> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the retrospective record at: `aidlc-docs/construction/sprint-retrospective/sprint-retrospective.md`

> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Adjust action items or their classification
> ✅ **Approve & Continue** - Approve the retrospective and proceed to the **next Sprint Planning** (if more backlog remains) or **Operations**
```

- Wait for explicit approval. Record the response in `audit.md`.

## Critical Rules

- **Evidence-based**: ground observations in the sprint log and audit trail, not impressions.
- **No silent input changes**: backlog/convention changes are `[SUGGESTION]` proposals for team approval.
- **Close the loop**: every unfinished item and accepted improvement has a recorded destination.
- **Preserve governance**: approval gate, audit logging, and content validation apply.
