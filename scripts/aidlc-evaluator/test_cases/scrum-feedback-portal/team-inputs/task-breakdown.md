# PulseBoard — Task Breakdown (Team-Owned)

Typed tasks under each story. Task types: `research` (spike), `design`, `coding`.
Within an increment, tasks run in order `research → design → coding`.

## FB-1 — Submit feedback

### Tasks

- [ ] [design] Define the `Feedback` entity, the submit API contract, and the `FeedbackSubmitted` event
- [ ] [coding] Implement submit endpoint, service, repository, and the submission form

## FB-2 — View feedback list (admin)

### Tasks

- [ ] [design] Define the paginated list query and the admin-only access rule
- [ ] [coding] Implement list endpoint + admin list UI

## FB-3 — SSO authentication

### Tasks

- [ ] [design] Define the OIDC flow and the role-from-group-claim mapping
- [ ] [coding] Implement OIDC login, session handling, and role middleware

## FB-4 — Live results dashboard (Release 2)

### Tasks

- [ ] [research] Spike (FB-4 R): WebSocket vs Server-Sent Events for the live dashboard, evaluated against the event-driven architecture bias, browser support, and ECS Fargate operational cost
- [ ] [design] Design the live-update channel and the dashboard aggregation, using the spike's approved recommendation
- [ ] [coding] Implement the live channel + dashboard UI

## FB-5 — Sentiment tagging (Release 2)

### Tasks

- [ ] [research] Spike (FB-5 R): in-house rule-based tagging vs a managed sentiment API
- [ ] [design] Design the async tagging consumer off `FeedbackSubmitted`
- [ ] [coding] Implement the consumer and persistence of sentiment labels

## FB-6 — Weekly digest email (Release 2)

### Tasks

- [ ] [design] Design the scheduled digest job and the email template
- [ ] [coding] Implement the scheduler, aggregation query, and email send
