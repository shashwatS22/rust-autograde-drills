# Level 45-web-sys-dom — web-sys DOM stubs

Phase 6 drills. Work through the numbered exercises in order.

## What you'll learn
- DOM-shaped operations (create, append, query, remove) in Rust

## Mapping to `web_sys`
| In-memory drill | Real browser (`web_sys`) |
|---|---|
| `MiniDocument::create_element` | `document.create_element("p")` |
| `set_text_content` | `element.set_text_content(Some("…"))` |
| `query_selector` | `document.query_selector("p")` |

Practice clicking a real page in [`projects/web-fundamentals`](../../projects/web-fundamentals/README.md).

## Exercises
Save each file under `src/bin/` to grade it with `cargo dev`.
