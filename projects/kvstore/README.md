# KV store (TDD capstone)

Implement the same key-value API four ways:

1. In-memory `HashMap`
2. File-backed persistence
3. Thread-safe wrapper with `Arc<Mutex<_>>`
4. Async store on Tokio

Run the spec tests:

```bash
cargo test -p kvstore -- --ignored
```

## Milestones

- [ ] `KvStore` trait + in-memory backend
- [ ] File backend survives reload
- [ ] Shared backend across threads
- [ ] `AsyncKvStore` with Tokio
