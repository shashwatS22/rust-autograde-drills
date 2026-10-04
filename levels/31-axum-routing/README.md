# Level 31 — Axum routing

## What you'll learn
- `Router` and routes
- in-process testing with `oneshot`
- no binding ports

## Concepts

Handlers are graded with `tower::ServiceExt::oneshot` — never start a server in a drill.



## Common mistakes
- Forgetting `.with_state()` when handlers need shared state.

## Before you start
Run `cargo warm 31` if this level uses external crates (see `level.toml`). Type examples into `playground` with `cargo play`.

## Exercises
Work through the exercises in order. Save each file to check it.
