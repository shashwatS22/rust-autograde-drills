"""Learner README bodies for levels 17–48 (appended after scaffold header)."""

LEVEL_README_BODY: dict[str, str] = {
    "26-testing-and-cargo": """
## What you'll learn
- Unit tests, `assert!` / `assert_eq!`, and `#[should_panic]`
- Test modules and testing `Result`

## Cargo (read, not graded here)
Workspaces, feature flags, `dev-dependencies`, semver, and docs.rs are part of every crate in this repo — open any `Cargo.toml` and compare level crates to `projects/api`. You do not need a separate drill for each knob.
""",
    "28-channels-and-sync": """
## What you'll learn
- Channels, `Arc<Mutex<_>>`, and why `Send` / `Sync` matter

## Why not `Rc` across threads?
`Rc` is **not** `Sync`. The compiler rejects sharing an `Rc` between threads — that is the lesson. You will see `E0277` if you try; use `Arc` instead.
""",
    "29-async-tokio": """
## What you'll learn
- `async`/`await`, Tokio tasks, channels, and `timeout`

## Do not block the executor
Never call `thread::sleep` or heavy CPU work inside an async task without `spawn_blocking`. It stalls every other task on that runtime worker.
""",
    "35-sqlx": """
## What you'll learn
- SQLite in memory with SQLx: queries, binds, transactions

## Postgres in the capstone
`query!` macros, migrations, and connection pooling use **Postgres** in [`projects/api`](../../projects/api/README.md). These drills stay on `sqlite::memory:` so they run offline and fast.
""",
    "41-ffi": """
## What you'll learn
- Calling C from Rust via `extern "C"` and `#[no_mangle]` exports

## bindgen
For real C headers, teams use **bindgen** to generate Rust declarations. This level uses hand-written `extern` blocks and `native/add.c` so the link step stays visible.
""",
    "42-performance": """
## What you'll learn
- Allocation patterns: capacity, avoiding extra `collect`, cheap iteration

## Profiling (read later)
`criterion` benches, flamegraphs, and `#![no_std]` are covered when you build [`projects/systems`](../../projects/systems/README.md). The drills here stay in safe std-only code.
""",
    "45-web-sys-dom": """
## What you'll learn
- DOM-shaped operations (create, append, query, remove) in Rust

## Mapping to `web_sys`
| In-memory drill | Real browser (`web_sys`) |
|---|---|
| `MiniDocument::create_element` | `document.create_element("p")` |
| `set_text_content` | `element.set_text_content(Some("…"))` |
| `query_selector` | `document.query_selector("p")` |

Practice clicking a real page in [`projects/web-fundamentals`](../../projects/web-fundamentals/README.md).
""",
    "46-leptos-components": """
## What you'll learn
- `view!`, props, lists, conditionals, nested components (SSR HTML)

## Events and forms
Controlled inputs and DOM events need a browser. Do those in [`projects/web-fundamentals/03-dom-todo`](../../projects/web-fundamentals/03-dom-todo/).
""",
    "48-leptos-server-fns": """
## What you'll learn
- Serde request/response shapes that server functions use

## Real `#[server]` functions
The `#[server]` macro runs on the server with HTTP + SSR. Wire that up in [`projects/web`](../../projects/web/README.md); these drills call the same logic directly so the grader stays native.
""",
}
