# Level 28-channels-and-sync — Channels and sync

Phase 3 drills. Work through the numbered exercises in order.

## What you'll learn
- Channels, `Arc<Mutex<_>>`, and why `Send` / `Sync` matter

## Why not `Rc` across threads?
`Rc` is **not** `Sync`. The compiler rejects sharing an `Rc` between threads — that is the lesson. You will see `E0277` if you try; use `Arc` instead.

## Exercises
Save each file under `src/bin/` to grade it with `cargo dev`.
