# Systems capstone (Phase 5)

Parallel `grep`-style CLI. **Gate:** `cargo test -p systems` and `cargo bench -p systems`.

## Milestones

1. `pgrep` binary: search files for a pattern (line numbers + paths)
2. Sequential baseline implementation
3. Parallel version with `rayon` (or scoped threads)
4. Criterion bench showing measurable speedup vs baseline (document ratio in README)
5. `clap` derive CLI with `--help` and sensible exit codes

## Requirement

Report before/after benchmark numbers in this file when done.
