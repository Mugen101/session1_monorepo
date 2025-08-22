# AnchorRepo Monorepo

This is a TypeScript monorepo with Next.js, shared tsconfig/eslint config, and CI.

## Getting Started

1. Install dependencies:
   ```
   npm install
   ```
2. Start development server:
   ```
   npm run dev
   ```
3. Run tests:
   ```
   npm run test
   ```
4. Lint code:
   ```
   npm run lint --workspace=web
   ```

## Structure
- `apps/web`: Next.js app
- `packages/tsconfig`: Shared TypeScript config
- `packages/eslint-config`: Shared ESLint config

## CI
GitHub Actions runs build, lint, and test on every push/PR to `main`.
