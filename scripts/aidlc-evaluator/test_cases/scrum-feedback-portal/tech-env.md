# PulseBoard — Technical Environment (Engineering Biases)

This document is the harness-facing view of the team's **engineering biases**.
The structured versions the workflow reads are `team-inputs/architecture.md` and
`team-inputs/coding-conventions.md`. These are **binding constraints** — the AI
builds within them and does not choose a different stack unprompted.

## Stack

- Language: TypeScript (Node.js 20).
- Backend: Express.
- Frontend: React 18 (Vite).
- Database: PostgreSQL 15.
- Auth: SSO via OIDC (company IdP).
- Deployment: AWS ECS Fargate; RDS PostgreSQL.

## Architecture bias

- Event-driven for the live dashboard (a domain event is emitted on each new
  feedback submission).
- Layered backend: `routes → services → repositories`.
- No direct DB access from route handlers.

## Prohibited libraries

| Library    | Reason                              | Use instead      |
| ---------- | ----------------------------------- | ---------------- |
| `moment`   | Unmaintained, heavy                 | `date-fns`       |
| `sequelize`| Team standard is query-first        | `kysely`         |

## Testing

- Unit tests with `vitest`; minimum 80% coverage on internal code paths.
- Contract tests for the REST API.

## Example patterns

Endpoint (Express):

```ts
router.post("/feedback", async (req, res) => {
  const input = FeedbackInput.parse(req.body);
  const saved = await feedbackService.submit(input);
  res.status(201).json(saved);
});
```

Test (vitest):

```ts
it("submits feedback", async () => {
  const res = await request(app).post("/feedback").send(valid);
  expect(res.status).toBe(201);
});
```
