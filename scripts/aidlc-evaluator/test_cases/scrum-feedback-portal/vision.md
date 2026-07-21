# PulseBoard — Product Vision

## One paragraph

PulseBoard is an internal web app that lets employees submit short feedback to
leadership and lets admins review it. The MVP proves the submit → review loop.
Later releases add a live results dashboard, sentiment tagging, and a weekly
digest email. The team owns the vision, the backlog, and the engineering
direction; the AI validates and clarifies these inputs and does the coding
within the team's architecture and conventions.

> **Note for the AI-DLC workflow**: This vision file is the harness-facing entry
> point. The authoritative, structured team inputs live in `team-inputs/`
> (product-vision.md, product-backlog.md, task-breakdown.md, architecture.md,
> coding-conventions.md, definition-of-done.md). Treat those as the source of
> truth and operate in validation mode — do not re-author them.

## MVP scope (Release 1 — Sprint 1)

- Employees can submit feedback (text + category).
- Admins can view a list of submitted feedback.
- SSO authentication gates both flows.

## Out of scope for the MVP (already defined, later sprints)

- Live results dashboard (Release 2).
- Sentiment tagging (Release 2).
- Weekly digest email (Release 2).

These are **already defined** as backlog items in `team-inputs/product-backlog.md`.
They are deferred, not undecided.

## Open questions (pre-declared)

- Live dashboard transport: WebSocket vs Server-Sent Events — flagged as a
  research spike in `team-inputs/task-breakdown.md` (task FB-4 R).

## Success criteria

- MVP: an employee can submit feedback and an admin can see it, behind SSO,
  meeting the Definition of Done in `team-inputs/definition-of-done.md`.
