# PulseBoard — Product Backlog (Team-Owned)

Stories are tagged by release. Release 1 = MVP. Release 2 stories are **already
defined** (deferred, not undecided) so incremental sprints can pull them without
new authoring.

## Release 1 (MVP)

### FB-1 — Submit feedback

As an **employee**, I want to submit categorized text feedback so leadership
hears my input.

**Acceptance criteria**

- Feedback has a category (enum) and a body (10–2000 chars).
- Submission requires an authenticated session.
- On success, the feedback is persisted and a `FeedbackSubmitted` event is emitted.

### FB-2 — View feedback list (admin)

As an **admin**, I want to view submitted feedback so I can review it.

**Acceptance criteria**

- Only admins can access the list.
- List is paginated and sorted newest-first.
- Each row shows category, body, submitter, and timestamp.

### FB-3 — SSO authentication

As a **user**, I want to sign in with company SSO so access is secure.

**Acceptance criteria**

- OIDC login against the company IdP.
- Admin vs employee role derived from an IdP group claim.

## Release 2 (already defined — deferred to later sprints)

### FB-4 — Live results dashboard

As an **admin**, I want a live dashboard of incoming feedback so I can watch
trends in real time.

**Acceptance criteria**

- Dashboard updates within 2s of a new submission.
- Shows counts by category over a selectable time window.
- Transport (WebSocket vs SSE) is **to be decided by a research spike** — see
  task FB-4 R in task-breakdown.md.

### FB-5 — Sentiment tagging

As an **admin**, I want each feedback item tagged with sentiment so I can triage
quickly.

**Acceptance criteria**

- Each item gets a sentiment label (positive/neutral/negative).
- Labeling runs asynchronously off the `FeedbackSubmitted` event.

### FB-6 — Weekly digest email

As an **admin**, I want a weekly email summarizing feedback so I stay informed
without logging in.

**Acceptance criteria**

- A scheduled job sends a Monday 08:00 digest.
- Digest includes counts by category and top items.
