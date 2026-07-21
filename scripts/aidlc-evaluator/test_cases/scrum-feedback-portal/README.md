# Test Case: scrum-feedback-portal

A golden test case for the **Scrum + team-owned-inputs** workflow. It exercises
the three lifecycle situations a team actually hits:

1. **S1 — Product initialization (MVP)**: team provides inputs; first sprint
   delivers the MVP stories.
2. **S2 — Incremental sprint (pre-defined feature)**: a later sprint pulls a
   Release-2 story that was **already defined** in the backlog/vision — no new
   authoring, and it includes a **research spike**.
3. **S3 — New/appended feature**: a brand-new story (FB-7) arrives that was
   **not** in the established backlog, and the workflow must ingest it.

> **Status: `draft`.** There is intentionally **no `golden.yaml` / `golden-aidlc-docs/`**
> yet. Per this framework, a golden baseline is *promoted from a real run*, not
> hand-written (see `test_cases/todo-app`, also draft). The "Expected behavior"
> assertions below are what a promoted baseline — or a qualitative/human review —
> must satisfy.

## Product

**PulseBoard**, an internal employee-feedback portal. See `vision.md` (harness
entry point) and `team-inputs/` (the authoritative, structured team inputs).

## Team inputs provided

| File | Role |
| ---- | ---- |
| `team-inputs/product-vision.md`      | Product vision, releases, personas |
| `team-inputs/product-backlog.md`     | Stories FB-1..FB-6 (MVP + already-defined Release 2) |
| `team-inputs/task-breakdown.md`      | Typed tasks (`research`/`design`/`coding`) under each story |
| `team-inputs/architecture.md`        | Binding target architecture |
| `team-inputs/coding-conventions.md`  | Binding coding conventions |
| `team-inputs/definition-of-done.md`  | DoD enforced at Sprint Review |
| `team-inputs/feature-request-r3-export.md` | The **new** story FB-7 for Scenario 3 |

## Scenario 1 — Product initialization (MVP)

**Sprint scope**: FB-1, FB-2, FB-3 (Release 1).

**Expected workflow traversal**

1. Workspace Detection records all six team inputs as **Present**.
2. **Backlog Refinement** loads the backlog + task breakdown, validates INVEST
   and task typing, raises `[VALIDATION]`/`[SUGGESTION]` findings, gates.
3. Requirements Analysis + User Stories run in **validation mode** (do not
   re-author).
4. Application Design conforms to `architecture.md` (intake gate: present).
5. Units Generation produces `unit-of-work-task-map.md` carrying FB-1..FB-3 tasks.
6. **Sprint Planning** sets a Sprint Goal, confirms the DoD, selects FB-1..FB-3.
7. Sprint Execution per increment: Daily Standup → (no research tasks in MVP) →
   Functional Design → Code Generation (adhering to conventions).
8. Build & Test → **Sprint Review** (verifies vs DoD) → **Sprint Retrospective**.

**Expected behavior (assertions)**

- No stage fabricates vision/stories/tasks — all trace to `team-inputs/`.
- Every generated requirement/story is tagged validation, not authored.
- `aidlc-state.md` has a `## Team Inputs` section, all Present.
- Increment meets the DoD; MVP stories delivered with tests.

## Scenario 2 — Incremental sprint (pre-defined feature, with a spike)

**Precondition**: S1 complete (brownfield: existing code + `aidlc-docs/`).
**Sprint scope**: FB-4 (live results dashboard) — already defined in the backlog.

**Expected workflow traversal**

1. Workspace Detection = brownfield; team inputs already Present.
2. Backlog Refinement confirms FB-4 already exists — **no new story authored**.
3. Sprint Planning opens a **new sprint** over FB-4 (existing backlog item).
4. Sprint Execution for FB-4:
   - **Research / Spike runs FIRST** (task FB-4 R): produces
     `construction/.../research/websocket-vs-sse-findings.md` with a
     recommendation as a `[SUGGESTION]`, and **gates for approval**.
   - Functional Design consumes the **approved** recommendation as binding.
   - Code Generation implements within conventions.
5. Build & Test → Sprint Review → Retrospective.

**Expected behavior (assertions)**

- The spike stage executes **before** design and produces a findings artifact.
- Design/code reflect the approved spike decision (traceable).
- No re-refinement authoring of FB-4 — it was already defined.
- DoD's "spike has an approved recommendation" criterion is satisfied.

## Scenario 3 — New/appended feature (not previously defined)

**Precondition**: S1 (and optionally S2) complete.
**Trigger**: team adds FB-7 (`feature-request-r3-export.md`) and appends it to
`product-backlog.md` + `task-breakdown.md`.

**Expected workflow traversal**

1. Backlog Refinement **ingests FB-7 as a team-authored story** (does not invent
   it), validates it against existing stories, raises a `[VALIDATION]` finding
   for any overlap (e.g., with a future reporting feature) and `[SUGGESTION]`s
   for missing acceptance criteria.
2. Sprint Planning pulls FB-7 into a new sprint.
3. Sprint Execution: design → coding for FB-7 (no spike needed).
4. Sprint Review + Retrospective; unfinished items (if any) return to the backlog.

**Expected behavior (assertions)**

- FB-7 is treated as team-owned input, tagged validation/suggestion — never
  silently authored or silently merged.
- Appending a story does **not** force a full re-run of prior sprints.
- The audit trail shows the intake of FB-7 and the team's approval.

## How to run (and what the harness needs first)

⚠️ **Harness prerequisites — this scenario cannot exercise the Scrum workflow until
the executor harness is updated.** As of now:

1. `packages/execution/.../agents/executor.py` hardcodes the **old** stage
   sequence (Workspace Detection → … → Build and Test). It has no Backlog
   Refinement, Research/Spike, Sprint Review, or Sprint Retrospective. Update its
   "Complete stage sequence" to match `aws-aidlc-rules/core-workflow.md`.
2. `packages/execution/.../runner.py` seeds only `vision.md` + `tech-env.md`.
   It must also copy this scenario's `team-inputs/` into the run folder's
   `aidlc-docs/team-inputs/` so the Input Intake Gates find the files present.
   (Optionally add a `team_inputs` field to `shared/scenario.py` and copy it.)
3. Scenarios 2 and 3 are **brownfield continuations**. The single-shot greenfield
   runner would need a mode that starts from a prior run's `workspace/` +
   `aidlc-docs/` (or run them manually/interactively).

Once the harness supports the above:

```bash
cd scripts/aidlc-evaluator
uv run python run.py test --scenario scrum-feedback-portal
```

## Promoting a golden baseline

After a satisfactory real run, promote it (this creates `golden.yaml` with the
run's true metrics and `golden-aidlc-docs/`) and flip `status` to `active` in
`scenario.yaml`. Do **not** hand-author `golden.yaml` — its metrics must come
from an actual run.
