# PulseBoard — New Feature Request (for Scenario 3)

**Status**: NEW — not previously in the backlog or vision. Introduced mid-project
to exercise how the workflow ingests an appended story.

## FB-7 — Export feedback to CSV

As an **admin**, I want to export the feedback list to CSV so I can analyze it
in a spreadsheet.

### Acceptance criteria

- Admin-only export endpoint returns a CSV of the current filtered list.
- Columns: category, body, submitter, timestamp, sentiment (if available).
- Export respects the same access rules as the list view (FB-2).

### Tasks

- [ ] [design] Define the export endpoint and CSV schema; confirm it reuses the FB-2 query
- [ ] [coding] Implement the export endpoint + an "Export CSV" button on the admin list

## How this enters the workflow (Scenario 3)

The team adds this file (and appends FB-7 to `product-backlog.md` and
`task-breakdown.md`). On the next pass, **Backlog Refinement** must:

- Ingest FB-7 as a team-authored story (NOT invent it).
- Raise a `[VALIDATION]` finding if FB-7 conflicts with or duplicates existing
  stories (e.g., overlap with a future reporting feature).
- Confirm FB-7's tasks are typed and mapped.
- Then **Sprint Planning** pulls FB-7 into a new sprint.
