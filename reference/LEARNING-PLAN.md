# Zero to Rust — A Full-Time Learning Plan

**Audience:** a beginner who can already write a print statement, a `for` loop, and an `if`, but nothing beyond that.
**Commitment:** 3+ hours/day, ~5–6 days a week.
**End state:** comfortable in Rust — the language, then backend services, then systems work, then Rust in the browser — with a working DSA foundation on LeetCode.

There are two documents:

| File | Who it's for |
|---|---|
| `LEARNING-PLAN.md` (this file) | You and her — the roadmap, the routine, what to learn when |
| `CURSOR-BUILD-SPEC.md` | Phase 1 build spec (200 exercises, levels 01–16) |
| `CURSOR-BUILD-SPEC-PHASES-3-6.md` | Phases 3–6 drills (256 exercises, levels 17–48) |

---

## 1. The core idea

She gets one repo (`rust-bootcamp`) running locally. It's a Cargo workspace with a file watcher. She opens an exercise file, writes code, hits save, and the terminal immediately tells her **PASS** or **FAIL** with a line-by-line diff against the expected output — or, when it doesn't compile, the compiler's own error rendered in full colour.

That's the whole loop. No setup friction, no "did I run it right", no waiting for feedback. Save → verdict → fix → save. Measured on a tiny no-dependency exercise crate, a changed file rebuilds and runs in about 200–250 ms, so the verdict lands before she's looked away from the screen.

**Two parallel tracks run every day:**

- **Track A — Drills (the repo).** **456** auto-graded exercises across **48** levels (200 in Phase 1, 256 in Phases 3–6). This is where she learns the *language*.
- **Track B — DSA (LeetCode).** Problems from Striver's A2Z sheet, solved on LeetCode in Rust. This is where she learns to *think*.

Track A always stays ahead of Track B. She never gets a LeetCode problem that needs syntax she hasn't drilled.

### What's different because this is Rust

Three things change compared to a JavaScript version of this plan, and they're all deliberate:

1. **The compiler is the first grader.** In Rust most saves produce a compile error before they ever produce wrong output. That's not failure — that's the feedback loop working. The runner treats `COMPILE ERROR` as its own verdict, shows the compiler's message verbatim, and does **not** count it as a failed attempt.
2. **Ownership gets its own level.** Level 09 is ownership and borrowing, inserted between functions and strings. You cannot defer it the way you can defer, say, closures in JavaScript — the moment she passes a `String` to a function, she needs it. This is why there are 16 levels and 200 drills rather than 15 and 190.
3. **Async arrives later.** In a JS plan, Promises land in the first month because React needs them. Rust's `async`/`await` needs traits, generics, and lifetimes to make any sense at all, so it moves to Phase 3. Phase 1 ends with modules, `Result`, and file I/O instead.

---

## 2. Daily routine (3.5 hours)

| Block | Time | What |
|---|---|---|
| 1. Concept | 30 min | Read the level's `README.md` in the repo, type out the examples in `playground/src/main.rs` (`cargo play` runs it). Typing, not copy-pasting. |
| 2. Drills | 90 min | Work through that level's exercises until they're green. |
| 3. DSA | 60 min | 2–4 LeetCode problems from the current Striver section. |
| 4. Review | 20 min | Re-solve one problem from 2 days ago **from a blank file**. Then write 3 lines in `NOTES.md` about what tripped her up. |

The review block is the one people skip and it's the one that makes it stick. Don't skip it.

### Rules that matter

1. **No copy-paste into exercise files.** Type everything.
2. **Read the compiler error out loud before changing anything.** Rust's errors are a tutorial. The habit of skimming them and guessing is the single worst habit a Rust beginner can build. Read the `error[EXXXX]` code, the message, the arrow pointing at her line, and the `help:` suggestion — in that order — before touching the keyboard.
3. **15-minute rule.** Stuck for 15 min on a drill → read the level README again. Still stuck at 25 min → `cargo solution <id>`, read it, close it, delete her attempt, and rewrite it from memory.
4. **Never move to the next level until the current one is 100% green.** The runner enforces this by default (`strict_progression = true` in `config.toml`).
5. **LeetCode uses Rust**, not any other language. Consistency beats variety at this stage.
6. **No `.clone()` to silence the borrow checker.** From level 09 onward, if she reaches for `.clone()` to make an error go away, she has to write one line in `NOTES.md` explaining what was actually being moved. Cloning is sometimes right; cloning *without knowing why* is how people get to month three without understanding ownership.
7. **No `.unwrap()` after level 13.** Once she's met `Option` and `Result`, `unwrap()` in a drill needs a comment saying why it can't fail. `expect("reason")` is always better than bare `unwrap()`.
8. **One "concept debt" list.** Anything she doesn't understand goes into `NOTES.md` under `## Confused about`. You review that list with her every few days. This is your main job as the teacher.

---

## 3. Phase overview

She asked for all three directions — backend, systems, and the browser. The plan does the shared foundation once, then takes them in order: **A → B → C**. Everything in Phase 3 is used by all three, so it is the one phase that must not be rushed.

| Phase | Weeks | What | Deliverable |
|---|---|---|---|
| **1. Rust fundamentals** | 1–5 | 16 levels, 200 drills. Variables → ownership → iterators → structs/enums → `Result`. | All levels green |
| **2. DSA foundation** | 1–8 (parallel) | Striver Steps 1–3 on LeetCode, in Rust | ~60 problems solved |
| **3. Core Rust — shared by A, B and C** | 6–9 | Levels **17–29** (~140 drills): traits → lifetimes → smart pointers → errors → threads → async | Levels 17–29 green + library projects in README |
| **4. Track A — Backend services** | 10–14 | Levels **30–36** (~80 drills): serde, Axum, tower, SQLx (SQLite in drills), auth | Levels 30–36 green + **`projects/api`** deployed |
| **5. Track B — Systems Rust** | 15–18 | Levels **37–43** (~76 drills): rayon, sync, layout, `unsafe`, FFI, perf, clap | Levels 37–43 green + **`projects/systems`** benchmarked |
| **6. Track C — Rust in the browser** | 19–22 | Levels **44–48** (~54 drills): wasm-bindgen, web-sys, Leptos SSR drills | Levels 44–48 green + **`projects/web`** deployed |

**A note on Phase 6:** it opens with about a week of HTML, CSS and the DOM. She doesn't need to become a frontend developer, but a WASM UI framework is a way of *producing* HTML, and if she doesn't know what a `<div>`, a flexbox, or an event listener is, Leptos becomes memorisation. If you want to compress, cut it to four days and skip CSS grid depth — but don't skip it entirely.

**A note on ordering:** A before B before C is intentional. Backend work (A) exercises traits, async, and error handling on problems with obvious right answers, which consolidates Phase 3. Systems work (B) is where `unsafe` and FFI live, and those are much safer to learn after she's internalised what the borrow checker was protecting her from. The browser (C) adds a whole second domain — the web platform — so it goes last, when Rust itself is no longer the hard part.

---

## 4. Phase 1 in detail — the 16 levels

Each level in the repo has a `README.md` you write once (Cursor drafts it) covering the concept, then the exercises. Here's what each level teaches and what it unlocks.

| # | Level | Drills | Concepts taught | Unlocks on LeetCode |
|---|---|---|---|---|
| 01 | Print & variables | 12 | `println!`, `let`/`mut`, shadowing, integer types, format specifiers | — |
| 02 | Operators | 12 | arithmetic, integer vs float division, `as` casting, overflow behaviour, `parse` | — |
| 03 | Conditionals & match | 12 | `if`/`else if`/`else`, `if` as an expression, `match`, range patterns, `_` | Striver Lec 1 basics |
| 04 | For loops | 14 | `for … in`, ranges, `.rev()`, `.step_by()`, accumulators, `break`/`continue` | FizzBuzz, simple sums |
| 05 | While & loop | 10 | `while`, `loop`, `break` with a value, labelled breaks, digit extraction | — |
| 06 | Nested loops & patterns | 16 | loops inside loops, building a row as a `String` | Striver Lec 2 (22 patterns) |
| 07 | Number problems | 14 | primes, divisors, GCD, Armstrong, palindrome numbers | **Striver Lec 4 — Basic Maths** |
| 08 | Functions | 12 | `fn`, expression returns, closures, `impl Fn`, the unit type | Refactoring all prior work |
| 09 | **Ownership & borrowing** | 12 | move, `Copy`, `clone`, `&`, `&mut`, the borrowing rules, slices | The level everything else rests on |
| 10 | Strings | 14 | `String` vs `&str`, `chars()`, byte indices, the core string methods | Striver Strings (basic) |
| 11 | Vectors & slices | 16 | `Vec`, indexing, `&[T]` parameters, traversal, search, rotation | **Striver Step 3 — Arrays (easy)** |
| 12 | Iterators & closures | 12 | `map`, `filter`, `fold`, `find`, `sort_by`, `any`/`all`, `collect` | Cleaner LeetCode solutions |
| 13 | Structs & enums | 12 | `struct`, `impl`, methods, `enum`, `Option`, `Result`, `#[derive(Debug)]` | Data-shaped problems |
| 14 | Recursion | 10 | base case, recursive case, the call stack | **Striver Lec 5 — Recursion** |
| 15 | HashMaps & sets | 10 | `HashMap`, `BTreeMap`, `HashSet`, the entry API, `O(1)` lookup | **Striver Lec 6 — Hashing**, Two Sum |
| 16 | Modules, errors & I/O | 12 | `mod`, `pub`, `use`, `Option`/`Result` combinators, `?`, custom errors, `std::fs` | Required for Phases 3–6 |

**Total: 200 exercises.**

The full exercise list — every file name, task, fixed inputs, and expected output — is in `CURSOR-BUILD-SPEC.md` § 9.

### Suggested pacing (full-time)

| Days | Levels |
|---|---|
| 1–2 | 01, 02 |
| 3–4 | 03, 04 |
| 5–6 | 05 |
| 7–8 | 06 |
| 9–10 | 07 |
| 11–12 | 08 |
| 13–16 | 09 |
| 17–18 | 10 |
| 19–21 | 11 |
| 22–23 | 12 |
| 24–25 | 13 |
| 26–27 | 14 |
| 28 | 15 |
| 29–30 | 16 + full review |

Level 06 (patterns), level 09 (ownership) and level 14 (recursion) are the three walls. Expect her to slow down at all of them. Patterns build spatial loop reasoning, ownership replaces the mental model every other language gave her, and recursion breaks people outright. **Budget four days for level 09 and do not let her shortcut it** — every level after it assumes she has it.

---

## 5. Track B — the Striver A2Z mapping

Source: <https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z>

She reads the problem on the Striver sheet, then solves it **on LeetCode in Rust**. Striver's videos are in C++/Java — that's fine, the logic transfers. Only the syntax differs, and by then she'll know the syntax.

| Order | Striver section | Start after repo level | Approx. problems |
|---|---|---|---|
| 1 | Step 1, Lec 1 — Language basics | 03 | Covered by drills |
| 2 | Step 1, Lec 2 — Patterns (22) | 06 | 22 |
| 3 | Step 1, Lec 4 — Basic Maths | 07 | 7 |
| 4 | Step 5 — Strings (Basic) | 10 | ~7 |
| 5 | Step 3 — Arrays (Easy) | 11 | ~14 |
| 6 | Step 2 — Sorting techniques | 12 | 7 |
| 7 | Step 1, Lec 5 — Basic Recursion | 14 | 9 |
| 8 | Step 1, Lec 6 — Basic Hashing | 15 | 3 |
| 9 | Step 3 — Arrays (Medium) | 15 | ~14 |
| 10 | Step 4 — Binary Search (1D) | after Phase 1 | ~13 |

**Target by end of Phase 1: ~60 problems.** Steps 2 and 3 are the first real algorithmic work — she should still be on those when Phase 3 begins. DSA continues in the background for months; it does not need to finish before the application phases start.

**Repo tooling:** checklists live under [`dsa/`](../dsa/) (one markdown file per section). Unlock rules are in [`dsa/sections.toml`](../dsa/sections.toml). After each level goes green, run **`cargo dsa`** to see which Striver sections are unlocked and where to log progress.

### Writing Rust on LeetCode

LeetCode gives her a skeleton like this, and it trips up every Rust beginner the first time:

```rust
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    }
}
```

Four things to tell her once, up front:

- `nums` is an **owned** `Vec<i32>`, not a borrow. She can mutate it freely if she declares it `mut` in the signature.
- Index types are a constant nuisance: `.len()` gives `usize`, the problems want `i32`. Convert at the boundary with `as i32` / `as usize` and don't scatter conversions through the loop.
- Strings come as `String`. Almost always the first line should be `let b = s.as_bytes();` — byte indexing is `O(1)`, char indexing is not.
- There's no `this`/`self` on these functions. They're associated functions, so a helper has to be a free `fn` or another `pub fn` inside the same `impl`.

### LeetCode discipline

- Time-box every problem to 30 minutes. Then look at the editorial, understand it, close it, and write it from scratch.
- After solving, write the approach in one plain-English sentence in `NOTES.md`. If she can't, she didn't solve it — she guessed.
- Re-solve any problem she needed help with, 3 days later.

---

## 6. Phase 3 — Core Rust (shared foundation for A, B and C)

This is the phase that makes the other three possible. Everything here is used by the backend track, the systems track, and the browser track. Nothing here is optional.

**Setup:** levels **17–29** in the same repo (`levels/17-traits` … `levels/29-async-tokio`). Same watcher, same PASS/FAIL loop. Run `cargo warm 25` and `cargo warm 29` before those levels. Exercise bank: `reference/CURSOR-BUILD-SPEC-PHASES-3-6.md`.

**Topics, in order:**

1. **Traits** — defining one, implementing it, default methods; `Display` vs `Debug` and why `{}` and `{:?}` differ
2. **Derivable traits** — `Clone`, `Copy`, `PartialEq`, `Eq`, `PartialOrd`, `Ord`, `Hash`, `Default`
3. **Generics** — generic functions, generic structs, trait bounds, `where` clauses
4. **`impl Trait`** in argument and return position; when to reach for `Box<dyn Trait>` instead
5. **Lifetimes** — why they exist, `'a` on functions and structs, the elision rules she's been relying on without knowing
6. **The standard conversion traits** — `From`, `Into`, `TryFrom`, `AsRef`, `Deref`
7. **Iterators properly** — `Iterator` as a trait, implementing one by hand, laziness, `collect::<Result<Vec<_>, _>>()`
8. **Smart pointers** — `Box`, `Rc`, `RefCell`, interior mutability, and `Rc<RefCell<T>>` as the escape hatch it is
9. **Error design** — `std::error::Error`, `thiserror` for libraries, `anyhow` for applications, when each is appropriate
10. **Testing** — `#[test]`, `#[should_panic]`, `assert_eq!` vs `assert!`, integration tests in `tests/`, doc tests
11. **Cargo and crates** — workspaces, features, `dev-dependencies`, semver, reading docs.rs effectively
12. **Concurrency** — `std::thread`, `move` closures, `JoinHandle`, channels (`mpsc`), `Arc<Mutex<T>>`
13. **`Send` and `Sync`** — what they mean and why the compiler won't let her share a `Rc` across threads
14. **Async** — `async`/`await`, `Future` as a trait, why Rust needs a runtime, Tokio basics, `join!` and `select!`
15. **Async vs threads** — when each is the right tool; the "don't block the executor" rule

**Practice:** two small library crates, both test-driven (workspace members):
1. [`projects/matrix`](../projects/matrix/) — generic `Matrix<T>` with `Add`/`Mul`/`Index`, a hand-written iterator, and `MatrixError`.
2. [`projects/kvstore`](../projects/kvstore/) — `KvStore` trait, then in-memory, file-backed, `Arc<Mutex<_>>`, and async Tokio backends. Run `cargo test -p matrix -- --ignored` / `cargo test -p kvstore -- --ignored` as you implement.

**Duration:** 3.5–4 weeks full-time. This is the longest non-project phase for a reason.

---

## 7. Phase 4 — Track A: Backend services (levels 30–36 + `projects/api`)

1. Tokio: the runtime, tasks, `spawn`, async I/O, `tokio::time`
2. `serde`: `Serialize`/`Deserialize`, `#[serde(rename_all)]`, JSON in and out
3. Axum: routers, handlers, extractors (`Path`, `Query`, `Json`, `State`), responses
4. Error handling in a web service: a custom error type that implements `IntoResponse`
5. Middleware and `tower`: logging, timeouts, CORS
6. `tracing`: structured logs and spans instead of `println!`
7. Postgres with SQLx: compile-time-checked queries, migrations, connection pooling
8. Modelling: request types, domain types, database rows — and the conversions between them
9. Auth: password hashing with `argon2`, JWTs, an auth extractor
10. Testing a service: unit tests, integration tests against a test database
11. Configuration and secrets: environment variables, `dotenvy`, layered config
12. Packaging and deploying: a multi-stage `Dockerfile`, then Fly.io or Railway

**Capstone:** a REST API she designs — auth, a Postgres database, full CRUD, migrations, structured logs, tests, deployed and callable from the public internet. Something she actually wants to exist, not a tutorial clone. Motivation matters more than scope here.

**Duration:** ~5 weeks.

---

## 8. Phase 5 — Track B: Systems Rust (levels 37–43 + `projects/systems`)

1. Threads in anger: thread pools, `rayon` for data parallelism, `scope`d threads
2. Synchronisation: `Mutex` vs `RwLock`, `Condvar`, atomics, what a data race actually is
3. Memory layout: stack vs heap, `size_of`, `align_of`, `#[repr(C)]`, enum niche optimisation
4. `unsafe`: what it does and does not turn off, raw pointers, the five things only `unsafe` allows
5. Writing a sound abstraction over `unsafe` — building a toy `Vec` is the classic exercise and it's worth doing
6. `MaybeUninit`, `ManuallyDrop`, and the `Drop` trait
7. FFI: calling C from Rust with `extern "C"` and `bindgen`; exposing Rust to C with `#[no_mangle]`
8. Performance: `cargo bench` with `criterion`, flamegraphs, reading an optimiser's mind, when allocation is the bottleneck
9. Zero-copy parsing: `&[u8]`, `bytes`, avoiding `String` where `&str` will do
10. CLI tooling: `clap` derive API, exit codes, stdin/stdout streaming, good `--help` text
11. `no_std` — a short taste, enough to understand what the standard library actually provides
12. Reading other people's `unsafe`: walk through one real crate's internals together

**Capstone:** one genuinely systems-flavoured tool, benchmarked against an existing implementation. Good candidates: a parallel `grep`, a log file indexer, a toy allocator, or a binary file format parser. The requirement is a measured number — "2.3× faster than the naive version" — not just "it works".

**Duration:** ~4 weeks.

---

## 9. Phase 6 — Track C: Rust in the browser (levels 44–48 + `projects/web`)

**Week 1 — web fundamentals (do not skip):** non-graded mini-builds in [`projects/web-fundamentals`](../projects/web-fundamentals/) (profile page, hand-built flexbox layout, DOM to-do, fetch-and-render). Checklist README only — no level renumbering.
1. HTML: semantic structure, forms, attributes, accessibility basics
2. CSS: box model, flexbox, grid, positioning, responsive units, one layout built by hand with no framework
3. The DOM: `querySelector`, event listeners, creating and removing elements
4. Browser dev tools: elements panel, console, network tab

**Weeks 2–4 — Rust on the front end:**
5. WebAssembly: what it is, what it can and can't touch, `wasm-bindgen`, `wasm-pack`
6. `web-sys` and `js-sys`: calling browser APIs from Rust
7. Leptos: components, `view!`, props, `Signal` and fine-grained reactivity
8. Events, controlled inputs, and forms
9. Lists, keys, and conditional rendering
10. Resources and async data loading; loading and error states
11. Server functions and SSR — the part where Track A and Track C meet
12. Styling, bundling, and deploying a Leptos app

**Capstone:** one full-stack application written entirely in Rust — a Leptos front end talking to the Axum + Postgres backend patterns from Phase 4, deployed and shareable. This is the project that proves all three tracks landed.

**Duration:** ~4 weeks.

---

## 10. Milestones — how to know she's ready to move on

| Gate | Test |
|---|---|
| Leave level 09 | Can explain, without notes, why `let s2 = s1;` compiles for `i32` and moves for `String`. Can read an `E0502` or `E0382` and say which rule was broken before reading the `help:` line. |
| Leave Phase 1 | All **200** Phase 1 drills green (`cargo verify --level` 01–16). Can write "count vowels in a string" and "find the second largest in a vector" from a blank file, no reference, in under 5 minutes each. |
| Leave Phase 3 | Can write a generic function with a trait bound and a lifetime annotation, from scratch, and explain why each is needed. Can take a function that returns `Option` and rewrite it to return a custom `Result` with a real error type. |
| Leave Phase 4 | Can add a new authenticated endpoint — route, handler, extractor, query, error path, test — to her own API in one sitting without looking at the other endpoints. |
| Leave Phase 5 | Can profile a slow function, name the bottleneck, fix it, and show the before/after benchmark. Can explain what invariant a piece of `unsafe` code is upholding. |
| Done | The Phase 6 capstone is deployed, and she can explain every file in it. |

---

## 11. Your job in this

The repo handles correctness. It cannot handle the things that actually cause beginners to quit.

- **Review `NOTES.md` every 2–3 days.** The "Confused about" list is your teaching agenda.
- **Explain *why*, not *how*.** When she asks about `&mut`, don't give the rule — show her the bug that two simultaneous mutable borrows would have caused.
- **Let her struggle for 15 minutes.** Rescuing too early is the most common way well-meaning teachers slow someone down.
- **Defend level 09.** The temptation to wave through ownership "because she can get the exercises passing with `.clone()`" is the single highest-cost mistake available in this plan. Everything in Phases 3–6 compounds on it.
- **Reframe compile errors as normal.** A beginner who thinks a red terminal means they're bad at this will quit in week two. The target feeling is "the compiler is pair-programming with me", and you set that tone, not the repo.
- **Celebrate green levels.** 200 exercises is a long grind; visible progress is what carries people through week three.
- **Don't add topics ahead of schedule** because they seem interesting. The ordering here is deliberate — every level only needs things from earlier levels.
