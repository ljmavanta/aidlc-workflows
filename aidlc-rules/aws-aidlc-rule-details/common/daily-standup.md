# Daily Standup Checkpoint

**Purpose**: A lightweight, recurring checkpoint during Sprint Execution that keeps sprint state visible. This is **not** an approval gate — it does not block — but it MUST be recorded.

**Cadence**: Run at the start of each work session within the CONSTRUCTION phase (i.e., each time work resumes on the sprint), and before starting a new increment/unit.

## Procedure

1. Load the current sprint plan and `aidlc-docs/aidlc-state.md`.
2. Answer the three standup questions (below) based on actual state — do not summarize optimistically.
3. Append an entry to `aidlc-docs/construction/sprint-log.md` (create the file if it does not exist).
4. If an impediment is a blocking gate (e.g., a missing team input — see `team-inputs.md`), surface it to the team immediately rather than working around it.

## The Three Questions

- **Done since last standup**: Which increments/units, steps, or stories were completed?
- **Next**: What will be worked on before the next standup?
- **Impediments**: What is blocking progress? Include any open Input Intake Gates, unresolved `[VALIDATION]` findings, or failing builds/tests.

## Standup Log Entry Format

```markdown
## Standup — [ISO 8601 timestamp]

- **Sprint**: [sprint identifier / goal]
- **Current Increment**: [unit-name or stage]
- **Done**: [bullet list]
- **Next**: [bullet list]
- **Impediments**: [bullet list, or "None"]
- **Blocking gates open**: [list open intake/approval gates, or "None"]

---
```

## Rules

- **Always append, never overwrite** `sprint-log.md` (same rule as `audit.md`).
- The standup does not replace stage approval gates — it complements them.
- Impediments recorded here must be reflected honestly in Sprint Review and Retrospective.
