# ADR-0002: Frontend Architecture for Next.js App

## Context
This ADR documents the frontend architecture decisions for the Next.js app in `apps/web`, as discussed in Session 2.

## Decisions
- **App Shell:** Uses Next.js App Router (`app/` directory) for modern routing and layout management.
- **Routing:**
  - `/` (Home)
  - `/about`
  - `/auth/sign-in`
- **Layout:**
  - Shared layout in `app/layout.tsx` for consistent navigation, metadata, and favicon.
  - Centralized metadata for SEO and branding.
- **Component Structure:**
  - UI components in `components/ui/`: Button, Input, Navbar, Sidebar, PageHeader.
  - Path aliases (`@/components`, `@/lib`) for maintainable imports.
- **TypeScript:** Strict config for type safety and reliability.
- **Testing:** Jest or Vitest for unit tests on components and logic.

## Status
Accepted

## Consequences
- Modular, scalable frontend foundation
- Improved developer experience and maintainability
- Ready for future feature expansion
