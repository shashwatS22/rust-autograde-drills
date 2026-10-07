# Level 41-ffi — FFI

Phase 5 drills. Work through the numbered exercises in order.

## What you'll learn
- Calling C from Rust via `extern "C"` and `#[no_mangle]` exports

## bindgen
For real C headers, teams use **bindgen** to generate Rust declarations. This level uses hand-written `extern` blocks and `native/add.c` so the link step stays visible.

## Exercises
Save each file under `src/bin/` to grade it with `cargo dev`.
