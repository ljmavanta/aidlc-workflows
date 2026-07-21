# Team Inputs Contract

**Purpose**: Define the inputs the **team owns and provides**, the inputs the **agent may only validate or execute against**, and the mandatory **Input Intake Gate** that blocks a stage until a required input exists.

This file establishes the single most important principle of this workflow:

> **The team owns intent and engineering direction. The agent clarifies, validates, and builds — it does not invent product vision or choose architecture on the team's behalf.**

Load this file at workflow start (see `core-workflow.md`) and reference it wherever an intake gate is invoked.

## The Two Input Categories

### 1. Product Inputs (team-owned intent)

These express **what** to build and **why**. The team authors them. The agent's role is limited to validation, clarification, and clearly-marked suggestions.

| Input | Canonical file | Owner | Agent's allowed actions |
| ---------------------- | ---------------------------------------------- | ---- | ------------------------------------------------------------------ |
| Product vision         | `aidlc-docs/team-inputs/product-vision.md`     | Team | Validate for internal consistency; flag gaps; suggest additions    |
| Product backlog        | `aidlc-docs/team-inputs/product-backlog.md`    | Team | Validate stories vs INVEST; flag conflicts/overlaps; suggest splits |
| Task breakdown         | `aidlc-docs/team-inputs/task-breakdown.md`     | Team | Validate typed tasks under each story; flag missing/unmapped tasks; suggest additions |
| Sprint plan (optional) | `aidlc-docs/team-inputs/sprint-plan.md`        | Team | Validate the team's sprint scope/sequence; if absent, facilitate one |
| Requirements (if separate) | `aidlc-docs/team-inputs/requirements.md`   | Team | Cross-check against vision/backlog; flag ambiguity; ask questions  |

#### Typed Tasks Under Stories

The team owns the **task breakdown** as well as the stories. In `task-breakdown.md`, each user story carries a list of **typed tasks**. The agent validates and maps them — it does not invent the breakdown.

Recommended format:

```markdown
## Story: [STORY-ID] [title]

### Tasks
- [ ] [research] Spike: [the unknown to resolve]
- [ ] [design] [what to design]
- [ ] [coding] [what to implement]
```

**Task types and how the workflow runs each:**

| Task type | Alias | Maps to workflow stage | Notes |
| --------- | ----- | ---------------------------------------------- | ------------------------------------------ |
| `research` | `spike` | Research / Spike (`construction/research-spike.md`) | Runs FIRST in the per-increment loop; produces findings, not code |
| `design`  | —     | Functional / NFR / Infrastructure Design       | Consumes any approved spike recommendation |
| `coding`  | `code` | Code Generation (`construction/code-generation.md`) | Adheres to team coding conventions         |

**Ordering within an increment**: `research → design → coding`. A research task's approved recommendation becomes a binding input to its dependent design/coding tasks. Unknown or missing task types are a `[VALIDATION]` finding, not a silent default.

### 2. Engineering Biases (team-owned direction)

These express **how** the team wants software built. The team authors them. The agent treats them as **binding constraints** and does the manual coding within them.

| Input | Canonical file | Owner | Agent's allowed actions |
| ------------------- | ---------------------------------------------------- | ---- | -------------------------------------------------------------------- |
| Target architecture | `aidlc-docs/team-inputs/architecture.md`             | Team | Apply as a constraint; flag conflicts with requirements; suggest only |
| Coding conventions  | `aidlc-docs/team-inputs/coding-conventions.md`       | Team | Follow exactly when generating code; never override silently         |
| Definition of Done  | `aidlc-docs/team-inputs/definition-of-done.md`       | Team | Enforce at Sprint Review; report per-item compliance                 |

**Note**: The `team-inputs/` directory lives inside `aidlc-docs/` (documentation only). It is detected during Workspace Detection and its contents are recorded in `aidlc-state.md`.

## Agent Role Boundaries

**The agent MUST:**

- Treat team inputs as the **source of truth**. When an input exists, do not re-derive or replace it.
- Distinguish clearly between three response types in every artifact it produces:
  - **[VALIDATION]** — an inconsistency, gap, conflict, or ambiguity found in a team input (requires team resolution).
  - **[SUGGESTION]** — a nice-to-have addition or improvement the agent proposes (requires explicit team approval before adoption; never silently merged).
  - **[EXECUTION]** — work the agent performs within the team's constraints (code, tests, design detail).
- Do the **manual coding** itself, adhering to `coding-conventions.md` and `architecture.md`.

**The agent MUST NOT:**

- Author product vision, backlog items, or requirements from scratch when the team has not provided them — it must **ask** (see Intake Gate below).
- Choose an architecture, tech stack, or convention unprompted when the team has expressed a bias — it must apply the team's bias, and where none exists, **ask**.
- Convert a `[SUGGESTION]` into an accepted requirement or design decision without explicit team approval.

## Input Intake Gate (Hard-Blocking)

Whenever a stage declares a **Required Input**, run this gate **before** doing the stage's work.

### Gate procedure

1. **Detect**: Check `aidlc-docs/aidlc-state.md` (`## Team Inputs` section, populated during Workspace Detection) and the canonical file path for the required input.
2. **If present**: Load it as the source of truth and proceed. The stage operates in **validation/execution mode** (validate, clarify, suggest — do not re-author).
3. **If absent**: **STOP**. Do not proceed, do not fabricate the input. Raise a blocking question using `common/question-format-guide.md` format, asking the team to either:
   - **A) Provide the input** — paste content, point to a file, or confirm creation at the canonical path; or
   - **B) Explicitly waive it** — state that this input is intentionally out of scope for this work, with a one-line reason.
4. **Log** the gate prompt and the team's response in `aidlc-docs/audit.md` with an ISO 8601 timestamp and complete raw input (per `core-workflow.md` audit rules).
5. **Record** the resolution in `aidlc-state.md` under `## Team Inputs` (Provided / Waived, with reason if waived).

### Gate block format

```markdown
> ⛔ **INPUT REQUIRED — [Input Name]**
>
> This stage requires a team-owned input that is not yet set up:
> **`aidlc-docs/team-inputs/[file].md`**
>
> The agent does not author this input on the team's behalf. Please choose:
>
> **A) Provide it** — paste the content, reference an existing file, or confirm it should be created at the path above.
> **B) Waive it** — confirm this input is intentionally out of scope for this work (state a brief reason).
>
> [Answer]:
```

**Waiver semantics**: A waived input is recorded and its dependent validations are marked N/A (not a blocking finding) for the remainder of the workflow, unless the team later provides it. Waiving product vision/backlog is strongly discouraged and should be surfaced as a risk.

## Relationship to Scrum Ceremonies

- Product Inputs form the **Product Backlog** refined during Backlog Refinement (see `scrum-ceremonies.md`).
- The **Definition of Done** is enforced at Sprint Review.
- Engineering Biases constrain every design and code-generation stage within Sprint Execution.
