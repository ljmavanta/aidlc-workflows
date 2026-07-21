# PulseBoard — Target Architecture (Team-Owned, Binding)

## Style

- Layered backend: `routes → services → repositories`. Route handlers never
  touch the database directly.
- Event-driven side effects: submitting feedback emits a `FeedbackSubmitted`
  domain event; Release 2 features (dashboard, sentiment) consume it.
- Single Postgres database; one schema per bounded concern.

## Components (MVP)

- `auth` — OIDC login, session, role middleware.
- `feedback` — submit + list; owns the `Feedback` table and the event.
- `web` — React SPA (Vite) for the submission form and admin list.

## Deployment

- Containerized services on AWS ECS Fargate.
- RDS PostgreSQL 15.
- Events via an in-process emitter for the MVP; a managed bus is a Release 2
  research question, not an MVP decision.

## Constraints

- No ORM that hides SQL (see prohibited libraries in coding-conventions.md).
- All external calls (IdP, email) behind an interface for testability.
