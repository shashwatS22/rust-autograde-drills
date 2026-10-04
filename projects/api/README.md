# API capstone (Phase 4)

Build a deployed REST API. **Gate:** `cargo test -p api` (integration tests), not `cargo dev`.

## Milestones

1. Health route `GET /health` → `{ "ok": true }`
2. Postgres via SQLx + migrations (`sqlx migrate run`)
3. CRUD for one resource you design
4. Auth: `argon2` password hash + JWT issue/verify extractor
5. `tracing` structured logs on every request
6. Integration tests with in-memory or test DB
7. Multi-stage `Dockerfile` + deploy (Fly.io, Railway, or similar)
8. Public URL documented in this README

## Env

Copy `.env.example` when you add one. Never commit secrets.
