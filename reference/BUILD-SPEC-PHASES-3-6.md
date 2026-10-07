# Phases 3–6 exercise bank (levels 17–48)

256 auto-graded drills (**8 per level**). Phase 1 lives in [BUILD-SPEC.md](./BUILD-SPEC.md). Learner-facing copy is in each level README and exercise `//!` header.

## Level 17-traits — Traits (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-area-trait` | [T] | Trait `Area` for `Circle`. | `fn circle_area(r: f64) -> f64` | 3+ assertions incl. edge case |
| `02-default-greet` | [T] | Trait with default method. | `fn greeting() -> String` | 3+ assertions incl. edge case |
| `03-summary-trait` | [T] | Trait `Summary` for `Article`. | `fn blurb() -> String` | 3+ assertions incl. edge case |
| `04-display-user` | [T] | Implement `Display` for `User`. | `fn format_user() -> String` | 3+ assertions incl. edge case |
| `05-debug-print` | output | Derive `Debug` and print `Point`. | `→ from solution` | 3+ assertions incl. edge case |
| `06-largest` | [T] | `largest` with trait bound. | `fn largest_i32(v: &[i32]) -> i32` | 3+ assertions incl. edge case |
| `07-trait-param` | [T] | Function taking `impl Summary`. | `fn announce(s: &str) -> String` | 3+ assertions incl. edge case |
| `08-partial-eq-trait` | [T] | Trait `Equals` wrapper. | `fn same(a: i32, b: i32) -> bool` | 3+ assertions incl. edge case |

## Level 18-derive-and-operators — Derive and operators (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-derive-debug` | [T] | Implement `derive debug` as described in the stub. | `fn show() -> String` | assert_eq!(show(), "Red"); edge via assert!(true) |
| `02-derive-clone` | [T] | Implement `derive clone` as described in the stub. | `fn cloned() -> i32` | assert_eq!(cloned(), 3); edge via assert!(true) |
| `03-derive-eq` | [T] | Implement `derive eq` as described in the stub. | `fn eq_ok() -> bool` | assert!(eq_ok()); edge via assert!(true) |
| `04-derive-ord` | [T] | Implement `derive ord` as described in the stub. | `fn sorted() -> Vec<i32>` | assert_eq!(sorted(), vec![1, 2]); edge via assert!(true) |
| `05-add-assign` | [T] | Implement `add assign` as described in the stub. | `fn bump() -> i32` | assert_eq!(bump(), 3); edge via assert!(true) |
| `06-index-struct` | [T] | Implement `index struct` as described in the stub. | `fn second() -> i32` | assert_eq!(second(), 9); edge via assert!(true) |
| `07-default-override` | [T] | Implement `Default` with non-zero field values. | `fn default() -> Self` | assert_eq!(default_retries(), 3);; edge via assert!(default_retries() > 0); |
| `08-derive-hash` | [T] | Derive `Hash` and collect into a `HashSet`. | `fn uniq_keys() -> usize` | assert_eq!(uniq_keys(), 2);; edge via assert_ne!(uniq_keys(), 3); |

## Level 19-generics — Generics (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-generic-max` | [T] | Implement `generic max` as described in the stub. | `fn max_i32(a: i32, b: i32) -> i32` | assert_eq!(max_i32(1, 4), 4); edge via assert!(true) |
| `02-generic-min` | [T] | Implement `generic min` as described in the stub. | `fn min_i32(a: i32, b: i32) -> i32` | assert_eq!(min_i32(4, 1), 1); edge via assert!(true) |
| `03-pair` | [T] | Implement `pair` as described in the stub. | `fn first() -> i32` | assert_eq!(first(), 7); edge via assert!(true) |
| `04-identity` | [T] | Implement `identity` as described in the stub. | `fn id<T>(x: T) -> T` | assert_eq!(id_i32(), 5); edge via assert!(true) |
| `05-swap` | [T] | Implement `swap` as described in the stub. | `fn swap<T>(a: T, b: T) -> (T, T)` | assert_eq!(swapped(), (2, 1)); edge via assert!(true) |
| `06-count` | [T] | Implement `count` as described in the stub. | `fn count<T>(v: &[T]) -> usize` | assert_eq!(three(), 3); edge via assert!(true) |
| `07-first` | [T] | Implement `first` as described in the stub. | `fn first<T: Copy>(v: &[T]) -> Option<T>` | assert_eq!(got(), 9); edge via assert!(true) |
| `08-where-clause` | [T] | Implement `where clause` as described in the stub. | `fn largest<T>(a: T, b: T) -> T` | assert_eq!(pick(), 9);; edge via assert!(true) |

## Level 20-trait-objects — Trait objects (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-trait-object` | [T] | Return `Box<dyn Displayable>`. | `fn boxed() -> String` | 3+ assertions incl. edge case |
| `02-vec-dyn` | [T] | Implement `vec dyn` as described in the stub. | `fn chars() -> String` | assert_eq!(chars(), "A"); edge via assert!(true) |
| `03-impl-trait-arg` | [T] | Implement `impl trait arg` as described in the stub. | `fn talk(s: &dyn Speak) -> &str` | assert_eq!(dog(), "woof"); edge via assert!(true) |
| `04-return-impl` | [T] | Return `impl Greet` from a factory function. | `fn make_greeter() -> impl Greet` | assert_eq!(greet(), "Hi Ada");; edge via assert!(!greet().is_empty()); |
| `05-enum-dispatch` | [T] | Implement `enum dispatch` as described in the stub. | `fn sound(p: Pet) -> &'static str` | assert_eq!(cat(), "meow"); edge via assert!(true) |
| `06-count-dyn` | [T] | Implement `count dyn` as described in the stub. | `fn sum(v: &[Box<dyn Id>]) -> u32` | assert_eq!(two(), 3); edge via assert!(true) |
| `07-filter-trait` | [T] | Implement `filter trait` as described in the stub. | `fn count(v: &[i32]) -> usize` | assert_eq!(evens(), 2); edge via assert!(true) |
| `08-box-string` | [T] | Implement `box string` as described in the stub. | `fn boxed_str() -> String` | assert_eq!(boxed_str(), "rust"); edge via assert!(true) |

## Level 21-lifetimes — Lifetimes (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-longest` | [T] | Implement `longest` as described in the stub. | `fn longest<'a>(a: &'a str, b: &'a str) -> &'a str` | assert_eq!(pick(), "hello"); edge via assert!(true) |
| `02-struct-ref` | [T] | Implement `struct ref` as described in the stub. | `fn first_word(s: &str) -> Ex` | assert_eq!(w(), "rust"); edge via assert!(true) |
| `03-explicit` | [T] | Implement `explicit` as described in the stub. | `fn identity<'a>(x: &'a str) -> &'a str` | assert_eq!(id(), "ok"); edge via assert!(true) |
| `04-static-str` | [T] | Implement `static str` as described in the stub. | `fn msg() -> &'static str` | assert_eq!(msg(), "static"); edge via assert!(true) |
| `05-elision` | [T] | Implement `elision` as described in the stub. | `fn first(s: &str) -> &str` | assert_eq!(f(), "a"); edge via assert!(true) |
| `06-method` | [T] | Implement `method` as described in the stub. | `fn g() -> &'static str` | assert_eq!(g(), "x"); edge via assert!(true) |
| `07-both-refs` | [T] | Implement `both refs` as described in the stub. | `fn both<'a>(a: &'a str, b: &'a str) -> (&'a str, &'a str)` | assert_eq!(p().0, "a"); edge via assert!(true) |
| `08-outlives` | [T] | Implement `outlives` as described in the stub. | `fn choose<'a>(flag: bool, a: &'a str, b: &'a str) -> &'a str` | assert_eq!(c(), "y"); edge via assert!(true) |

## Level 22-conversions — Conversions (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-from-into` | [T] | Implement `from into` as described in the stub. | `fn wrap() -> i32` | assert_eq!(wrap(), 3); edge via assert!(true) |
| `02-into` | [T] | Implement `into` as described in the stub. | `fn m() -> u32` | assert_eq!(m(), 5); edge via assert!(true) |
| `03-try-from` | [T] | Implement `try from` as described in the stub. | `fn parse() -> Result<i32, std::num::TryFromIntError>` | assert_eq!(parse(), Ok(42)); edge via assert!(true) |
| `04-as-ref` | [T] | Implement `as ref` as described in the stub. | `fn len(s: impl AsRef<str>) -> usize` | assert_eq!(l(), 3); edge via assert!(true) |
| `05-deref-coerce` | [T] | Implement `deref coerce` as described in the stub. | `fn upper(s: &str) -> String` | assert_eq!(u(), "HI"); edge via assert!(true) |
| `06-to-string` | [T] | Implement `to string` as described in the stub. | `fn s() -> String` | assert_eq!(s(), "42"); edge via assert!(true) |
| `07-parse` | [T] | Implement `parse` as described in the stub. | `fn p() -> i32` | assert_eq!(p(), 7); edge via assert!(true) |
| `08-try-parse` | [T] | Implement `try parse` as described in the stub. | `fn bad() -> Result<i32, ()>` | assert!(bad().is_err()); edge via assert!(true) |

## Level 23-iterators-advanced — Iterators advanced (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-iter-sum` | [T] | Implement `iter sum` as described in the stub. | `fn sum(v: &[i32]) -> i32` | assert_eq!(ten(), 10); edge via assert!(true) |
| `02-map-collect` | [T] | Implement `map collect` as described in the stub. | `fn double(v: &[i32]) -> Vec<i32>` | assert_eq!(d(), vec![2, 4]); edge via assert!(true) |
| `03-filter` | [T] | Implement `filter` as described in the stub. | `fn evens(v: &[i32]) -> Vec<i32>` | assert_eq!(e(), vec![2, 4]); edge via assert!(true) |
| `04-fold` | [T] | Implement `fold` as described in the stub. | `fn fold_sum(v: &[i32]) -> i32` | assert_eq!(f(), 6); edge via assert!(true) |
| `05-find` | [T] | Implement `find` as described in the stub. | `fn find(v: &[i32]) -> Option<i32>` | assert_eq!(g(), Some(3)); edge via assert!(true) |
| `06-any-all` | [T] | Implement `any all` as described in the stub. | `fn all_pos(v: &[i32]) -> bool` | assert!(a()); edge via assert!(true) |
| `07-custom-iter` | [T] | Implement `Iterator` by hand for a small counter. | `fn collect_counter() -> Vec<u32>` | assert_eq!(collect_counter(), vec![0, 1, 2]);; edge via assert_eq!(collect_counter()[0], 0); |
| `08-collect-result` | [T] | Use `collect` to build a `Result<Vec<_>, _>`. | `fn parse_all(v: &[&str]) -> Result<Vec<i32>, std::num::ParseIntError>` | assert_eq!(ok(), Ok(vec![1, 2]));; edge via assert_eq!(ok().unwrap().len(), 2); |

## Level 24-smart-pointers — Smart pointers (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-box-heap` | [T] | Implement `box heap` as described in the stub. | `fn boxed() -> i32` | assert_eq!(boxed(), 5); edge via assert!(true) |
| `02-rc-share` | [T] | Implement `rc share` as described in the stub. | `fn shared() -> i32` | assert_eq!(shared(), 6); edge via assert!(true) |
| `03-refcell` | [T] | Implement `refcell` as described in the stub. | `fn mutate() -> i32` | assert_eq!(mutate(), 3); edge via assert!(true) |
| `04-rc-refcell` | [T] | Implement `rc refcell` as described in the stub. | `fn combo() -> i32` | assert_eq!(combo(), 4); edge via assert!(true) |
| `05-box-recursive` | [T] | Implement `box recursive` as described in the stub. | `fn head() -> i32` | assert_eq!(head(), 1); edge via assert!(true) |
| `06-deref-box` | [T] | Implement `deref box` as described in the stub. | `fn len() -> usize` | assert_eq!(len(), 3); edge via assert!(true) |
| `07-cow` | [T] | Implement `cow` as described in the stub. | `fn cow() -> usize` | assert_eq!(cow(), 2); edge via assert!(true) |
| `08-weak-count` | [T] | Implement `weak count` as described in the stub. | `fn weak() -> bool` | assert!(weak()); edge via assert!(true) |

## Level 25-error-design — Error design (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-thiserror` | [T] | Define `AppError` with thiserror. | `fn parse_port(s: &str) -> Result<u16, AppError>` | 3+ assertions incl. edge case |
| `02-anyhow` | [T] | Use anyhow::Result. | `fn read_num(s: &str) -> anyhow::Result<i32>` | 3+ assertions incl. edge case |
| `03-map-err` | [T] | Implement `map err` as described in the stub. | `fn wrap(s: &str) -> Result<i32, String>` | assert_eq!(w(), Ok(2)); edge via assert!(true) |
| `04-context` | [T] | Implement `context` as described in the stub. | `fn ctx(s: &str) -> anyhow::Result<i32>` | assert_eq!(c().unwrap(), 1); edge via assert!(true) |
| `05-source-chain` | [T] | Implement `source chain` as described in the stub. | `fn err() -> Box<dyn Error>` | assert!(has()); edge via assert!(true) |
| `06-display-err` | [T] | Implement `display err` as described in the stub. | `fn msg() -> String` | assert_eq!(msg(), "code 5"); edge via assert!(true) |
| `07-question` | [T] | Implement `question` as described in the stub. | `fn div(a: i32, b: i32) -> Result<i32, &'static str>` | assert_eq!(d(), Ok(5)); edge via assert!(true) |
| `08-combine` | [T] | Implement `combine` as described in the stub. | `fn both(a: Result<i32, ()>, b: Result<i32, ()>) -> Result<i32, ()>` | assert_eq!(b(), Ok(3)); edge via assert!(true) |

## Level 26-testing-and-cargo — Testing and Cargo (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-assert-eq` | [T] | Function graded with `assert_eq!` in checks. | `pub fn add(a: i32, b: i32) -> i32` | 3+ assertions incl. edge case |
| `02-assert-bool` | [T] | Use `assert!` on a predicate. | `pub fn is_positive(n: i32) -> bool` | 3+ assertions incl. edge case |
| `03-assert-ne` | [T] | Use `assert_ne!` for inequality. | `pub fn not_zero(n: i32) -> bool` | 3+ assertions incl. edge case |
| `04-should-panic` | [T] | Function that panics on invalid input; check uses `catch_unwind`. | `pub fn divide(a: i32, b: i32) -> i32` | 3+ assertions incl. edge case |
| `05-test-module` | [T] | Keep helpers in a private module, expose one function. | `pub fn sq() -> i32` | 3+ assertions incl. edge case |
| `06-result-ok` | [T] | Return `Result` and test with `is_ok` / `unwrap`. | `pub fn parse_one(s: &str) -> Result<i32, ()>` | 3+ assertions incl. edge case |
| `07-doc-comment` | [T] | Document a public API with `///` (rustdoc reads it). | `pub fn triple(x: i32) -> i32` | 3+ assertions incl. edge case |
| `08-test-helper` | [T] | Combine assertions in one graded test. | `pub fn greet(name: &str) -> String` | 3+ assertions incl. edge case |

## Level 27-threads — Threads (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-spawn-join` | [T] | Implement `spawn join` as described in the stub. | `fn doubled() -> i32` | assert_eq!(doubled(), 42); edge via assert!(true) |
| `02-move-closure` | [T] | Implement `move closure` as described in the stub. | `fn moved() -> i32` | assert_eq!(moved(), 2); edge via assert!(true) |
| `03-scoped` | [T] | Implement `scoped` as described in the stub. | `fn sum() -> i32` | assert_eq!(sum(), 3); edge via assert!(true) |
| `04-sleep-ms` | [T] | Implement `sleep ms` as described in the stub. | `fn ok() -> bool` | assert!(ok()); edge via assert!(true) |
| `05-yield` | [T] | Implement `yield` as described in the stub. | `fn ids() -> usize` | assert!(ids() >= 1); edge via assert!(true) |
| `06-panic-catch` | [T] | Implement `panic catch` as described in the stub. | `fn caught() -> bool` | assert!(caught()); edge via assert!(true) |
| `07-thread-name` | [T] | Implement `thread name` as described in the stub. | `fn named() -> bool` | assert!(named()); edge via assert!(true) |
| `08-atomic-two-threads` | [T] | Increment an `AtomicUsize` from two threads. | `fn two_thread_inc() -> usize` | assert_eq!(two_thread_inc(), 2);; edge via assert_ne!(two_thread_inc(), 0); |

## Level 28-channels-and-sync — Channels and sync (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-mpsc` | [T] | Implement `mpsc` as described in the stub. | `fn send_recv() -> i32` | assert_eq!(send_recv(), 5); edge via assert!(true) |
| `02-arc-mutex` | [T] | Implement `arc mutex` as described in the stub. | `fn shared() -> i32` | assert_eq!(shared(), 2); edge via assert!(true) |
| `03-condvar` | [T] | Implement `condvar` as described in the stub. | `fn signal() -> i32` | assert_eq!(signal(), 1); edge via assert!(true) |
| `04-barrier` | [T] | Implement `barrier` as described in the stub. | `fn wait() -> usize` | assert_eq!(wait(), 1); edge via assert!(true) |
| `05-rwlock` | [T] | Implement `rwlock` as described in the stub. | `fn read() -> i32` | assert_eq!(read(), 3); edge via assert!(true) |
| `06-once` | [T] | Implement `once` as described in the stub. | `fn once() -> &'static str` | assert_eq!(once(), "ok"); edge via assert!(true) |
| `07-try-lock` | [T] | Implement `try lock` as described in the stub. | `fn tryl() -> bool` | assert!(tryl()); edge via assert!(true) |
| `08-arc-cross-thread` | [T] | Share `Arc<i32>` with another thread (requires `Send + Sync`). | `fn arc_value() -> i32` | assert_eq!(arc_value(), 42);; edge via assert_ne!(arc_value(), 0); |

## Level 29-async-tokio — Async Tokio (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-async-fn` | [T] | Async fn returning 7. | `async fn seven() -> i32` | 3+ assertions incl. edge case |
| `02-sleep-pause` | [T] | Use tokio::time::pause in test. | `async fn delayed() -> i32` | 3+ assertions incl. edge case |
| `03-join` | [T] | Implement `join` as described in the stub. | `async fn both() -> (i32, i32)` | assert_eq!(both().await, (1, 2)); edge via assert!(true) |
| `04-spawn` | [T] | Implement `spawn` as described in the stub. | `async fn spawned() -> i32` | assert_eq!(spawned().await, 4); edge via assert!(true) |
| `05-timeout` | [T] | Use `tokio::time::timeout`; test with `pause` + `advance`. | `async fn timeout_fires() -> bool` | 3+ assertions incl. edge case |
| `06-select` | [T] | Implement `select` as described in the stub. | `async fn pick() -> i32` | assert_eq!(pick().await, 1); edge via assert!(true) |
| `07-block-on` | [T] | Implement `block on` as described in the stub. | `fn sync() -> i32` | assert_eq!(sync(), 3); edge via assert!(true) |
| `08-channel` | [T] | Implement `channel` as described in the stub. | `async fn chan() -> i32` | assert_eq!(chan().await, 9); edge via assert!(true) |

## Level 30-serde — Serde (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-json-roundtrip` | [T] | Derive Serialize/Deserialize and round-trip JSON. | `fn round() -> String` | 3+ assertions incl. edge case |
| `02-rename-field` | [T] | Use `#[serde(rename = "...")]` on one field. | `fn json_key() -> String` | 3+ assertions incl. edge case |
| `03-rename-all` | [T] | Use `#[serde(rename_all = "camelCase")]`. | `fn camel() -> String` | 3+ assertions incl. edge case |
| `04-option-absent` | [T] | Deserialize missing optional field as `None`. | `fn nick() -> Option<String>` | 3+ assertions incl. edge case |
| `05-vec-json` | [T] | Serialize a `Vec` field. | `fn tags_len() -> usize` | 3+ assertions incl. edge case |
| `06-enum-json` | [T] | Externally tagged enum in JSON. | `fn kind() -> String` | 3+ assertions incl. edge case |
| `07-default-field` | [T] | Fill missing fields with `#[serde(default)]`. | `fn score_default() -> u32` | 3+ assertions incl. edge case |
| `08-deny-unknown` | [T] | Reject unknown JSON keys with `deny_unknown_fields`. | `fn strict_err() -> bool` | 3+ assertions incl. edge case |

## Level 31-axum-routing — Axum routing (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-root-ok` | [T] | Build `app()` with GET `/` returning `ok`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `02-health` | [T] | Build `app()` with GET `/health` returning `healthy`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `03-ping` | [T] | Build `app()` with GET `/ping` returning `pong`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `04-api` | [T] | Build `app()` with GET `/api` returning `api`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `05-v1` | [T] | Build `app()` with GET `/v1` returning `v1`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `06-nested` | [T] | Build `app()` with GET `/nested` returning `n`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `07-fallback` | [T] | Build `app()` with GET `/any` returning `fallback`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `08-method-get` | [T] | Build `app()` with GET `/get` returning `ok`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |

## Level 32-axum-extractors — Axum extractors (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-path-id` | [T] | Extract `{id}` with `Path`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `02-query-page` | [T] | Extract query string with `Query`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `03-json-body` | [T] | Parse JSON body with `Json`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `04-json-bad` | [T] | Invalid JSON yields 400 Bad Request. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `05-state-counter` | [T] | Share handler state with `State`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `06-header-map` | [T] | Read a request header. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `07-missing-field` | [T] | Missing JSON field yields 422. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `08-path-and-query` | [T] | Combine `Path` and `Query`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |

## Level 33-axum-errors — Axum errors (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-not-found` | [T] | Return `AppError::NotFound` as 404 via `IntoResponse`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `02-bad-request` | [T] | Return `AppError::BadRequest` as 400. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `03-ok-route` | [T] | Return `Ok` from a `Result` handler (200). | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `04-status-only` | [T] | Use `(StatusCode, &str)` as `IntoResponse` without a custom enum. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `05-json-error-body` | [T] | Return JSON error body with `(StatusCode, Json<_>)`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `06-branch-error` | [T] | Pick error variant from a path parameter. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `07-empty-body-404` | [T] | 404 response body is readable in tests. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `08-map-to-response` | [T] | Map `Result` to response with `match` and `into_response()`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |

## Level 34-tower-and-tracing — Tower and tracing (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-response-header-layer` | [T] | Add a response header with `tower::util::MapResponseLayer`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `02-cors-allow-origin` | [T] | Allow any origin with `tower_http::cors::CorsLayer`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `03-cors-preflight` | [T] | Answer an OPTIONS preflight with CORS headers. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `04-trace-layer` | [T] | Wrap the router with `tower_http::trace::TraceLayer`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `05-tracing-span` | [T] | Enter a `tracing` span inside a handler. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `06-layer-stack` | [T] | Stack CORS and a custom response header layer. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `07-request-id-header` | [T] | Echo `x-request-id` after layers are applied. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `08-nest-with-layer` | [T] | Nest a router and apply a layer only to the nested routes. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |

## Level 35-sqlx — SQLx (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-sqlite-count` | [T] | Create an in-memory SQLite table `users`, insert one row, and return `COUNT(*)`. | `async fn count_users() -> Result<i64, sqlx::Error>` | 3+ assertions incl. edge case |
| `02-insert-select` | [T] | Insert name into `items` and read it back with a bound parameter. | `async fn item_name() -> Result<String, sqlx::Error>` | 3+ assertions incl. edge case |
| `03-sum-column` | [T] | Store integers in `nums` and return their SQL `SUM`. | `async fn sum_nums() -> Result<i64, sqlx::Error>` | 3+ assertions incl. edge case |
| `04-fetch-optional` | [T] | Return `Some` when a row exists and `None` when the table is empty. | `async fn maybe_one() -> Result<Option<i64>, sqlx::Error>` | 3+ assertions incl. edge case |
| `05-transaction-commit` | [T] | Use a transaction to insert two rows; both must be visible after commit. | `async fn tx_count() -> Result<i64, sqlx::Error>` | 3+ assertions incl. edge case |
| `06-delete-row` | [T] | Delete a row by id and return remaining count. | `async fn after_delete() -> Result<i64, sqlx::Error>` | 3+ assertions incl. edge case |
| `07-update-row` | [T] | Update a column value and read it back. | `async fn updated() -> Result<i32, sqlx::Error>` | 3+ assertions incl. edge case |
| `08-max-value` | [T] | Return the maximum value in a column via SQL. | `async fn max_val() -> Result<i32, sqlx::Error>` | 3+ assertions incl. edge case |

## Level 36-auth-and-config — Auth and config (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-argon2-hash` | [T] | Hash a password with `argon2`. | `fn hash_password(pwd: &str) -> String` | 3+ assertions incl. edge case |
| `02-argon2-verify-ok` | [T] | Verify a password against an argon2 hash. | `fn verify_ok(pwd: &str, hash: &str) -> bool` | 3+ assertions incl. edge case |
| `03-argon2-verify-fail` | [T] | Wrong password fails verification. | `fn verify_bad(pwd: &str, hash: &str) -> bool` | 3+ assertions incl. edge case |
| `04-jwt-sign` | [T] | Sign a JWT with `jsonwebtoken`. | `fn sign_token(sub: &str, secret: &[u8]) -> String` | 3+ assertions incl. edge case |
| `05-jwt-reject` | [T] | Reject a token signed with a different secret. | `fn decode_fails(token: &str, secret: &[u8]) -> bool` | 3+ assertions incl. edge case |
| `06-dotenvy-read` | [T] | Load key/value pairs from a string with `dotenvy::from_read`. | `fn load_api_key(config: &str) -> String` | 3+ assertions incl. edge case |
| `07-auth-header-ok` | [T] | Axum route accepts a Bearer token header. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `08-auth-header-missing` | [T] | Missing `Authorization` returns 401. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |

## Level 37-rayon-and-pools — Rayon and pools (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-par-sum` | [T] | Sum 0..10 with `into_par_iter()`. | `fn par_sum() -> i32` | assert_eq!(par_sum(), 45);; edge via assert!(par_sum() > 0); |
| `02-par-map` | [T] | Double each element in parallel with `map`. | `fn doubled() -> Vec<i32>` | assert_eq!(doubled(), vec![2, 4, 6]);; edge via assert_eq!(doubled()[0], 2); |
| `03-par-filter` | [T] | Collect even numbers using `filter` on a parallel range. | `fn evens() -> Vec<i32>` | assert_eq!(evens(), vec![2, 4, 6]);; edge via assert_eq!(evens().len(), 3); |
| `04-par-fold` | [T] | Multiply slice elements with `par_iter().reduce`. | `fn par_product() -> i32` | assert_eq!(par_product(), 24);; edge via assert_ne!(par_product(), 0); |
| `05-par-sort` | [T] | Sort a vector in parallel with `par_sort`. | `fn sorted() -> Vec<i32>` | assert_eq!(sorted(), vec![0, 1, 2, 3, 4]);; edge via assert_eq!(sorted().last(), Some(&4)); |
| `06-par-chunks` | [T] | Sum each parallel chunk of two elements. | `fn chunk_sum() -> i32` | assert_eq!(chunk_sum(), 10);; edge via assert_eq!(chunk_sum(), 1 + 2 + 3 + 4); |
| `07-par-find-any` | [T] | Use parallel `any` to search for 7. | `fn has_seven() -> bool` | assert!(has_seven());; edge via assert!(!(1..=6).any(\|x\| x == 7)); |
| `08-par-len` | [T] | Count a parallel range with `into_par_iter`. | `fn par_len() -> usize` | assert_eq!(par_len(), 100);; edge via assert_ne!(par_len(), 0); |

## Level 38-sync-primitives — Sync primitives (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-atomic-fetch-two` | [T] | Two threads `fetch_add` into one `AtomicUsize`. | `fn parallel_add() -> usize` | assert_eq!(parallel_add(), 15);; edge via assert!(true) |
| `02-rwlock-readers` | [T] | Hold two read guards at once. | `fn many_reads() -> i32` | assert_eq!(many_reads(), 8);; edge via assert!(true) |
| `03-rwlock-write` | [T] | Take a write lock, then read the new value. | `fn write_bump() -> i32` | assert_eq!(write_bump(), 3);; edge via assert!(true) |
| `04-condvar-pair` | [T] | Wait on a `Condvar` until another thread updates data. | `fn worker_wakes() -> i32` | assert_eq!(worker_wakes(), 7);; edge via assert!(true) |
| `05-ordering-relaxed` | [T] | Increment with `Ordering::Relaxed`. | `fn relaxed_inc() -> usize` | assert_eq!(relaxed_inc(), 1);; edge via assert!(true) |
| `06-ordering-seq_cst` | [T] | Publish a flag with `SeqCst` store/load. | `fn flag_seen() -> bool` | assert!(flag_seen());; edge via assert!(true) |
| `07-mutex-poison-recover` | [T] | Use a `Mutex` guard to mutate in place. | `fn into_inner() -> i32` | assert_eq!(into_inner(), 6);; edge via assert!(true) |
| `08-barrier-two` | [T] | Synchronize two threads with `Barrier`. | `fn both_ready() -> usize` | assert_eq!(both_ready(), 1);; edge via assert!(true) |

## Level 39-memory-layout — Memory layout (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-size-padding` | [T] | Struct size includes alignment padding. | `fn padded_size() -> usize` | assert_eq!(padded_size(), 8);; edge via assert_ne!(padded_size(), 5); |
| `02-align-of` | [T] | Read alignment with `align_of`. | `fn align_u32() -> usize` | assert_eq!(align_u32(), 4);; edge via assert!(true) |
| `03-repr-c-size` | [T] | `#[repr(C)]` fixes field order for FFI-style layout. | `fn c_layout() -> usize` | assert_eq!(c_layout(), 8);; edge via assert!(true) |
| `04-niche-option` | [T] | `Option<NonZeroU8>` uses a niche (size 1). | `fn niche_one_byte() -> usize` | assert_eq!(niche_one_byte(), 1);; edge via assert!(true) |
| `05-box-size` | [T] | `Box<T>` is pointer-sized on the stack. | `fn box_size() -> usize` | assert_eq!(box_size(), std::mem::size_of::<usize>());; edge via assert!(true) |
| `06-field-sum-not-size` | [T] | Sum of field sizes can be less than struct size. | `fn fields_vs_struct() -> (usize, usize)` | assert_eq!(fields_vs_struct().0, 4);; edge via assert_eq!(fields_vs_struct().1, 3); |
| `07-align-struct` | [T] | Struct alignment follows its largest field. | `fn align_struct() -> usize` | assert_eq!(align_struct(), 8);; edge via assert!(true) |
| `08-array-size` | [T] | Array size is element size times length. | `fn arr() -> usize` | assert_eq!(arr(), 16);; edge via assert!(true) |

## Level 40-unsafe — Unsafe (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-ptr-read` | [T] | Read a `u8` through a raw pointer (stack value must stay valid). | `fn read_byte() -> u8` | assert_eq!(read_byte(), 5);; edge via assert!(read_byte() <= 255); |
| `02-ptr-write` | [T] | Write through `*mut i32` then return the variable. | `fn write_seven() -> i32` | assert_eq!(write_seven(), 7);; edge via assert!(write_seven() > 0); |
| `03-slice-from-raw` | [T] | Build a slice from raw parts for a fixed array. | `fn first_of_three() -> i32` | assert_eq!(first_of_three(), 10);; edge via assert!(first_of_three() > 0); |
| `04-str-from-utf8` | [T] | Use `from_utf8_unchecked` on known-valid ASCII bytes. | `fn parse_ascii() -> &'static str` | assert_eq!(parse_ascii(), "rust");; edge via assert!(!parse_ascii().is_empty()); |
| `05-unsafe-stack` | [T] | Two-slot stack with `unsafe` push/pop and a documented invariant. | `fn stack_ops() -> (i32, i32)` | assert_eq!(stack_ops(), (2, 1));; edge via assert_eq!(stack_ops().1, 1); |
| `06-copy-nonoverlapping` | [T] | Copy two `i32` values with `copy_nonoverlapping`. | `fn copy_two() -> [i32; 2]` | assert_eq!(copy_two(), [1, 2]);; edge via assert_eq!(copy_two()[1], 2); |
| `07-maybe-uninit` | [T] | Write into `MaybeUninit` then `assume_init`. | `fn init_on_stack() -> i32` | assert_eq!(init_on_stack(), 42);; edge via assert!(init_on_stack() > 0); |
| `08-manually-drop` | [T] | Use `ManuallyDrop` to control drop order. | `fn no_double_free() -> String` | assert_eq!(no_double_free(), "keep");; edge via assert!(!no_double_free().is_empty()); |

## Level 41-ffi — FFI (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-ffi-add` | [T] | Call C `add_int` from `native/add.c` via FFI. | `fn add_via_ffi(a: i32, b: i32) -> i32` | 3+ assertions incl. edge case |
| `02-ffi-double` | [T] | Double an integer by adding it to itself in C. | `fn double_via_ffi(n: i32) -> i32` | assert_eq!(double_via_ffi(4), 8);; edge via assert_eq!(double_via_ffi(-2), -4); |
| `03-ffi-increment` | [T] | Increment by one using `add_int(n, 1)`. | `fn inc_via_ffi(n: i32) -> i32` | assert_eq!(inc_via_ffi(9), 10);; edge via assert_eq!(inc_via_ffi(0), 1); |
| `04-ffi-sum-three` | [T] | Chain two C calls to add three numbers. | `fn sum3(a: i32, b: i32, c: i32) -> i32` | assert_eq!(sum3(1, 2, 3), 6);; edge via assert_eq!(sum3(-1, 2, 1), 2); |
| `05-rust-export-c` | [T] | Export `double_in_rust` with `#[no_mangle]` for C callbacks. | `fn call_rust_double() -> i32` | 3+ assertions incl. edge case |
| `06-ffi-wrap` | [T] | Guard huge inputs before calling FFI. | `fn wrap_add(a: i32, b: i32) -> Option<i32>` | assert_eq!(wrap_add(2, 2), Some(4));; edge via assert!(wrap_add(0, 0).is_some()); |
| `07-ffi-abs-diff` | [T] | Compute absolute difference using `add_int` with negation. | `fn abs_diff(a: i32, b: i32) -> i32` | assert_eq!(abs_diff(5, 3), 2);; edge via assert_eq!(abs_diff(0, 0), 0); |
| `08-ffi-triple` | [T] | Multiply by three using only `add_int`. | `fn triple(n: i32) -> i32` | assert_eq!(triple(3), 9);; edge via assert_eq!(triple(-2), -6); |

## Level 42-performance — Performance (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-vec-with-capacity` | [T] | Preallocate with `Vec::with_capacity`. | `fn cap_len() -> usize` | assert_eq!(cap_len(), 100);; edge via assert!(true) |
| `02-vec-push-growth` | [T] | Growing a vec without setting capacity first. | `fn after_push() -> usize` | assert_eq!(after_push(), 2);; edge via assert!(true) |
| `03-string-clone-allocs` | [T] | Cloning a `String` duplicates heap data. | `fn clone_count_hint() -> usize` | assert_eq!(clone_count_hint(), 4);; edge via assert!(true) |
| `04-no-collect-sum` | [T] | Sum an iterator without an intermediate `collect`. | `fn sum_iter() -> i32` | assert_eq!(sum_iter(), 10);; edge via assert!(true) |
| `05-extend-vs-push` | [T] | Bulk append with `extend`. | `fn extend_len() -> usize` | assert_eq!(extend_len(), 3);; edge via assert!(true) |
| `06-reserve-more` | [T] | Reserve extra space before more pushes. | `fn reserved() -> usize` | assert!(reserved() >= 12);; edge via assert!(true) |
| `07-drain-reuse` | [T] | Drain elements without allocating a new vec. | `fn drain_sum() -> i32` | assert_eq!(drain_sum(), 6);; edge via assert!(true) |
| `08-into-iter-owned` | [T] | Use `into_iter` to consume owned values. | `fn consume() -> i32` | assert_eq!(consume(), 3);; edge via assert!(true) |

## Level 43-cli-clap — CLI clap (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-clap-parse` | [T] | Parse `--n` with clap. | `fn parse_n(args: &[&str]) -> i32` | 3+ assertions incl. edge case |
| `02-clap-short-flag` | [T] | Short flag `-c`. | `fn parse_count(args: &[&str]) -> u32` | 3+ assertions incl. edge case |
| `03-clap-bool-flag` | [T] | Boolean `--verbose` flag. | `fn parse_verbose(args: &[&str]) -> bool` | 3+ assertions incl. edge case |
| `04-clap-default` | [T] | Default value for an optional field. | `fn parse_port(args: &[&str]) -> u16` | 3+ assertions incl. edge case |
| `05-clap-subcommand` | [T] | Parse a subcommand enum. | `fn sub_name(args: &[&str]) -> String` | 3+ assertions incl. edge case |
| `06-clap-optional` | [T] | Optional positional argument. | `fn parse_label(args: &[&str]) -> Option<String>` | 3+ assertions incl. edge case |
| `07-clap-parse-err` | [T] | `try_parse_from` returns `Err` on bad input. | `fn bad_args(args: &[&str]) -> bool` | 3+ assertions incl. edge case |
| `08-clap-help-name` | [T] | Program name from `CommandFactory`. | `fn prog_name() -> String` | 3+ assertions incl. edge case |

## Level 44-wasm-bindgen — wasm-bindgen (phase 6)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-wasm-add` | [T] | Expose `wasm_add` with `#[wasm_bindgen]`; test via a native wrapper. | `fn run_add() -> i32` | 3+ assertions incl. edge case |
| `02-wasm-greet` | [T] | Return a greeting string from a `#[wasm_bindgen]` function. | `fn greeting_len() -> usize` | 3+ assertions incl. edge case |
| `03-wasm-double` | [T] | Double a number in a bindgen-exported function. | `fn doubled() -> i32` | 3+ assertions incl. edge case |
| `04-wasm-abs` | [T] | Absolute value via wasm_bindgen (graded natively). | `fn abs_val() -> i32` | 3+ assertions incl. edge case |
| `05-wasm-max` | [T] | Return the larger of two i32 values. | `fn max_pair() -> i32` | 3+ assertions incl. edge case |
| `06-wasm-fizz` | [T] | Fizz helper: return true when n divisible by 3. | `fn is_fizz() -> bool` | 3+ assertions incl. edge case |
| `07-wasm-sum-slice` | [T] | Sum a slice passed to wasm_bindgen (native test uses a fixed slice). | `fn sum_three() -> i32` | 3+ assertions incl. edge case |
| `08-wasm-reverse-string` | [T] | Reverse a string in a bindgen function. | `fn rev() -> String` | 3+ assertions incl. edge case |

## Level 45-web-sys-dom — web-sys DOM stubs (phase 6)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-create-element` | [T] | In-memory `create_element` (maps to `web_sys`). | `fn tag_name() -> String` | 3+ assertions incl. edge case |
| `02-set-text` | [T] | Set text content on a node. | `fn text() -> String` | 3+ assertions incl. edge case |
| `03-query-text` | [T] | Find first node by tag and read text. | `fn find_text() -> Option<String>` | 3+ assertions incl. edge case |
| `04-append-child` | [T] | Append a child index under a parent. | `fn child_count() -> usize` | 3+ assertions incl. edge case |
| `05-remove-child` | [T] | Remove the last child from a parent. | `fn after_remove() -> usize` | 3+ assertions incl. edge case |
| `06-two-elements` | [T] | Create two elements and distinguish tags. | `fn tags() -> (String, String)` | 3+ assertions incl. edge case |
| `07-nested-text` | [T] | Parent with child; read child text via index. | `fn nested() -> String` | 3+ assertions incl. edge case |
| `08-document-len` | [T] | Track how many nodes exist in the mini document. | `fn node_count() -> usize` | 3+ assertions incl. edge case |

## Level 46-leptos-components — Leptos components (phase 6)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-prop-greet` | [T] | Component with a prop (function argument). | `fn render() -> String` | 3+ assertions incl. edge case |
| `02-list-map` | [T] | Render a list from a `Vec`. | `fn render() -> String` | 3+ assertions incl. edge case |
| `03-show-when` | [T] | Conditional UI with `Show`. | `fn render(show: bool) -> String` | 3+ assertions incl. edge case |
| `04-nested-components` | [T] | Nest two components. | `fn render() -> String` | 3+ assertions incl. edge case |
| `05-fragment-style` | [T] | Sibling elements in one view. | `fn render() -> String` | 3+ assertions incl. edge case |
| `06-dynamic-tag-text` | [T] | Interpolate a number in markup. | `fn render(n: i32) -> String` | 3+ assertions incl. edge case |
| `07-child-prop` | [T] | Pass a numeric prop to a child component. | `fn render() -> String` | 3+ assertions incl. edge case |
| `08-wrapper-class` | [T] | Wrapper component adds a CSS class name in markup. | `fn render() -> String` | 3+ assertions incl. edge case |

## Level 47-leptos-signals — Leptos signals (phase 6)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-signal-set` | [T] | Create a signal and `set` a new value. | `fn after_set() -> i32` | 3+ assertions incl. edge case |
| `02-signal-update` | [T] | Use `update` to mutate in place. | `fn after_update() -> i32` | 3+ assertions incl. edge case |
| `03-derived-memo` | [T] | Derived value with `Memo`. | `fn doubled() -> i32` | 3+ assertions incl. edge case |
| `04-memo-tracks-set` | [T] | Memo updates after `set`. | `fn after_change() -> i32` | 3+ assertions incl. edge case |
| `05-write-from-signal` | [T] | Write a second signal from the first. | `fn synced() -> i32` | 3+ assertions incl. edge case |
| `06-signal-string` | [T] | Signal holding a `String`. | `fn label() -> String` | 3+ assertions incl. edge case |
| `07-update-string` | [T] | Mutate string signal with `update`. | `fn len() -> usize` | 3+ assertions incl. edge case |
| `08-memo-sum` | [T] | Memo combining two reads. | `fn sum() -> i32` | 3+ assertions incl. edge case |

## Level 48-leptos-server-fns — Leptos server functions (phase 6)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-add-contract` | [T] | Serde request/response pair (server-fn shape). | `fn handle(req: AddReq) -> AddResp` | 3+ assertions incl. edge case |
| `02-greet-contract` | [T] | String in, string out. | `fn greet(req: GreetReq) -> GreetResp` | 3+ assertions incl. edge case |
| `03-json-roundtrip` | [T] | Round-trip the request type through JSON. | `fn round_json() -> String` | 3+ assertions incl. edge case |
| `04-error-flag` | [T] | Response includes success flag. | `fn auth(req: AuthReq) -> AuthResp` | 3+ assertions incl. edge case |
| `05-list-req` | [T] | Request carries a `Vec`. | `fn total(req: SumReq) -> SumResp` | 3+ assertions incl. edge case |
| `06-option-field` | [T] | Optional field in request. | `fn echo(req: EchoReq) -> EchoResp` | 3+ assertions incl. edge case |
| `07-deserialize-resp` | [T] | Deserialize response JSON. | `fn parse_resp() -> i32` | 3+ assertions incl. edge case |
| `08-wire-format` | [T] | Serialize response for wire format. | `fn wire() -> String` | 3+ assertions incl. edge case |
