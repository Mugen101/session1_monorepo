# Auth Stub Documentation

> **Warning:** This authentication implementation is a mock/stub for development and demo purposes only. It does not provide real security or user management. Do not use in production.

## Overview
- Uses in-memory session context and query param `?mock=1` to simulate authentication.
- `SessionProvider` wraps the app and provides session state.
- `useSession()` hook returns mock user if `?mock=1` is present, otherwise unauthenticated.
- Navbar and SignIn page update UI based on session state.

## Usage
- Visit `/auth/sign-in` to sign in (sets mock session).
- Sign out clears mock session and redirects to home.

## Limitations
- No backend, persistence, or real user management.
- For demo/testing only.
