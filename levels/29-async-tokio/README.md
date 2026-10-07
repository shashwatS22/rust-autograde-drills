# Level 29-async-tokio — Async Tokio

Phase 3 drills. Work through the numbered exercises in order.

## What you'll learn
- `async`/`await`, Tokio tasks, channels, and `timeout`

## Do not block the executor
Never call `thread::sleep` or heavy CPU work inside an async task without `spawn_blocking`. It stalls every other task on that runtime worker.

## Exercises
Save each file under `src/bin/` to grade it with `cargo dev`.
