# Matrix library (TDD capstone)

Build a generic `Matrix<T>` with `Add`, `Mul`, `Index`, a hand-written row iterator, and a real `MatrixError` enum.

Tests are the spec. Implement until they pass:

```bash
cargo test -p matrix -- --ignored
```

## Milestones

- [ ] `Matrix::new` / `from_rows` with dimension checks
- [ ] `Index<(usize, usize)>` and `Add` / `Mul` for compatible sizes
- [ ] `MatrixRows` iterator over rows
- [ ] `MatrixError` for shape mismatches and out-of-bounds
