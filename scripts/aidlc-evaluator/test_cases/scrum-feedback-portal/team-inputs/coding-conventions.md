# PulseBoard — Coding Conventions (Team-Owned, Binding)

## Language & style

- TypeScript, strict mode. No `any` unless justified with a comment.
- Prettier defaults; ESLint must pass with zero warnings.
- Named exports; no default exports.

## Structure

- Backend layers: `src/<component>/{routes,services,repositories}.ts`.
- Zod schemas for all external input; validate at the route boundary.
- React: components in `src/components/`, hooks in `src/hooks/`.

## Naming

- Files kebab-case; types PascalCase; functions/vars camelCase.
- UI interactive elements carry a stable `data-testid` of `{feature}-{role}`
  (e.g., `feedback-submit-button`).

## Testing

- `vitest`; 80% minimum coverage on internal code paths (exclude third-party).
- One test file per source file, colocated as `*.test.ts`.

## Prohibited

- `moment` (use `date-fns`), `sequelize` (use `kysely`).
- Direct `process.env` reads outside a single typed `config` module.
