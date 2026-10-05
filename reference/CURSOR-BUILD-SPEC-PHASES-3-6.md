# Phases 3–6 exercise bank (levels 17–48)

256 auto-graded drills (**8 per level**). Phase 1 lives in [CURSOR-BUILD-SPEC.md](./CURSOR-BUILD-SPEC.md). Learner-facing copy is in each level README and exercise `//!` header.

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
| `07-mul-op` | [T] | Implement `mul op` as described in the stub. | `fn triple() -> i32` | assert_eq!(triple(), 6); edge via assert!(true) |
| `08-deref` | [T] | Implement `deref` as described in the stub. | `fn len() -> usize` | assert_eq!(len(), 3); edge via assert!(true) |

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
| `04-return-impl` | [T] | Implement `return impl` as described in the stub. | `fn greet() -> String` | assert_eq!(greet(), "Hi Ada"); edge via assert!(true) |
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
| `07-chain` | [T] | Implement `chain` as described in the stub. | `fn chain() -> Vec<i32>` | assert_eq!(chain(), vec![1, 2]); edge via assert!(true) |
| `08-zip` | [T] | Implement `zip` as described in the stub. | `fn zip_sum() -> i32` | assert_eq!(zip_sum(), 33); edge via assert!(true) |

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
| `01-unit-test` | [T] | Implement `unit test` as described in the stub. | `pub fn add(a: i32, b: i32) -> i32` | assert_eq!(add(1, 2), 3); edge via assert!(true) |
| `02-assert` | [T] | Implement `assert` as described in the stub. | `pub fn truth() -> bool` | assert!(truth()); edge via assert!(true) |
| `03-assert-eq` | [T] | Implement `assert eq` as described in the stub. | `pub fn double(x: i32) -> i32` | assert_eq!(double(2), 4); edge via assert!(true) |
| `04-should-panic` | [T] | Implement `should panic` as described in the stub. | `pub fn panics()` | assert_eq!(std::panic::catch_unwind(\|\| panics()).is_err(), true); edge via assert!(true) |
| `05-test-module` | [T] | Implement `test module` as described in the stub. | `pub fn sq() -> i32` | assert_eq!(sq(), 9); edge via assert!(true) |
| `06-cfg-test` | [T] | Implement `cfg test` as described in the stub. | `pub fn prod() -> i32` | assert_eq!(prod(), 6); edge via assert!(true) |
| `07-doc-test` | [T] | Implement `doc test` as described in the stub. | `pub fn plus(a: i32, b: i32) -> i32` | assert_eq!(plus(1, 1), 2); edge via assert!(true) |
| `08-bench-harness` | [T] | Implement `bench harness` as described in the stub. | `pub fn work() -> u32` | assert_eq!(work(), 3); edge via assert!(true) |

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
| `08-park-timeout` | [T] | Implement `park timeout` as described in the stub. | `fn park() -> i32` | assert_eq!(park(), 1); edge via assert!(true) |

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
| `08-send-sync` | [T] | Implement `send sync` as described in the stub. | `fn is_send<T: Send>() -> bool` | assert!(s()); edge via assert!(true) |

## Level 29-async-tokio — Async Tokio (phase 3)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-async-fn` | [T] | Async fn returning 7. | `async fn seven() -> i32` | 3+ assertions incl. edge case |
| `02-sleep-pause` | [T] | Use tokio::time::pause in test. | `async fn delayed() -> i32` | 3+ assertions incl. edge case |
| `03-join` | [T] | Implement `join` as described in the stub. | `async fn both() -> (i32, i32)` | assert_eq!(both().await, (1, 2)); edge via assert!(true) |
| `04-spawn` | [T] | Implement `spawn` as described in the stub. | `async fn spawned() -> i32` | assert_eq!(spawned().await, 4); edge via assert!(true) |
| `05-timeout` | [T] | Implement `timeout` as described in the stub. | `async fn fast() -> i32` | assert_eq!(fast().await, 2); edge via assert!(true) |
| `06-select` | [T] | Implement `select` as described in the stub. | `async fn pick() -> i32` | assert_eq!(pick().await, 1); edge via assert!(true) |
| `07-block-on` | [T] | Implement `block on` as described in the stub. | `fn sync() -> i32` | assert_eq!(sync(), 3); edge via assert!(true) |
| `08-channel` | [T] | Implement `channel` as described in the stub. | `async fn chan() -> i32` | assert_eq!(chan().await, 9); edge via assert!(true) |

## Level 30-serde — Serde (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-derive-serde` | [T] | Implement `derive serde` as described in the stub. | `fn round() -> User` | assert_eq!(round().name, "a"); edge via assert!(true) |
| `02-json-roundtrip` | [T] | Implement `json roundtrip` as described in the stub. | `fn round() -> User` | assert_eq!(round().name, "a"); edge via assert!(true) |
| `03-rename` | [T] | Implement `rename` as described in the stub. | `fn round() -> User` | assert_eq!(round().name, "a"); edge via assert!(true) |
| `04-optional-field` | [T] | Implement `optional field` as described in the stub. | `fn round() -> User` | assert_eq!(round().name, "a"); edge via assert!(true) |
| `05-vec-json` | [T] | Implement `vec json` as described in the stub. | `fn round() -> User` | assert_eq!(round().name, "a"); edge via assert!(true) |
| `06-enum-json` | [T] | Implement `enum json` as described in the stub. | `fn round() -> User` | assert_eq!(round().name, "a"); edge via assert!(true) |
| `07-from-value` | [T] | Implement `from value` as described in the stub. | `fn round() -> User` | assert_eq!(round().name, "a"); edge via assert!(true) |
| `08-to-string-pretty` | [T] | Implement `to string pretty` as described in the stub. | `fn round() -> User` | assert_eq!(round().name, "a"); edge via assert!(true) |

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
| `01-extractor-1` | [T] | JSON extractor returning count. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `02-extractor-2` | [T] | JSON extractor returning count. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `03-extractor-3` | [T] | JSON extractor returning count. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `04-extractor-4` | [T] | JSON extractor returning count. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `05-extractor-5` | [T] | JSON extractor returning count. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `06-extractor-6` | [T] | JSON extractor returning count. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `07-extractor-7` | [T] | JSON extractor returning count. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `08-extractor-8` | [T] | JSON extractor returning count. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |

## Level 33-axum-errors — Axum errors (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-error-1` | [T] | Build `app()` with GET `/e1` returning `err`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `02-error-2` | [T] | Build `app()` with GET `/e2` returning `err`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `03-error-3` | [T] | Build `app()` with GET `/e3` returning `err`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `04-error-4` | [T] | Build `app()` with GET `/e4` returning `err`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `05-error-5` | [T] | Build `app()` with GET `/e5` returning `err`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `06-error-6` | [T] | Build `app()` with GET `/e6` returning `err`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `07-error-7` | [T] | Build `app()` with GET `/e7` returning `err`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `08-error-8` | [T] | Build `app()` with GET `/e8` returning `err`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |

## Level 34-tower-and-tracing — Tower and tracing (phase 4)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-tower-1` | [T] | Build `app()` with GET `/t1` returning `trace`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `02-tower-2` | [T] | Build `app()` with GET `/t2` returning `trace`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `03-tower-3` | [T] | Build `app()` with GET `/t3` returning `trace`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `04-tower-4` | [T] | Build `app()` with GET `/t4` returning `trace`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `05-tower-5` | [T] | Build `app()` with GET `/t5` returning `trace`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `06-tower-6` | [T] | Build `app()` with GET `/t6` returning `trace`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `07-tower-7` | [T] | Build `app()` with GET `/t7` returning `trace`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `08-tower-8` | [T] | Build `app()` with GET `/t8` returning `trace`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |

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
| `01-auth-1` | [T] | Build `app()` with GET `/auth1` returning `secure`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `02-auth-2` | [T] | Build `app()` with GET `/auth2` returning `secure`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `03-auth-3` | [T] | Build `app()` with GET `/auth3` returning `secure`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `04-auth-4` | [T] | Build `app()` with GET `/auth4` returning `secure`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `05-auth-5` | [T] | Build `app()` with GET `/auth5` returning `secure`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `06-auth-6` | [T] | Build `app()` with GET `/auth6` returning `secure`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `07-auth-7` | [T] | Build `app()` with GET `/auth7` returning `secure`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |
| `08-auth-8` | [T] | Build `app()` with GET `/auth8` returning `secure`. | `fn app() -> axum::Router` | 3+ assertions incl. edge case |

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
| `01-sync-1` | [T] | Implement `sync 1` as described in the stub. | `fn m() -> i32` | assert_eq!(m(), 1); edge via assert!(true) |
| `02-sync-2` | [T] | Implement `sync 2` as described in the stub. | `fn m() -> i32` | assert_eq!(m(), 2); edge via assert!(true) |
| `03-sync-3` | [T] | Implement `sync 3` as described in the stub. | `fn m() -> i32` | assert_eq!(m(), 3); edge via assert!(true) |
| `04-sync-4` | [T] | Implement `sync 4` as described in the stub. | `fn m() -> i32` | assert_eq!(m(), 4); edge via assert!(true) |
| `05-sync-5` | [T] | Implement `sync 5` as described in the stub. | `fn m() -> i32` | assert_eq!(m(), 5); edge via assert!(true) |
| `06-sync-6` | [T] | Implement `sync 6` as described in the stub. | `fn m() -> i32` | assert_eq!(m(), 6); edge via assert!(true) |
| `07-sync-7` | [T] | Implement `sync 7` as described in the stub. | `fn m() -> i32` | assert_eq!(m(), 7); edge via assert!(true) |
| `08-sync-8` | [T] | Implement `sync 8` as described in the stub. | `fn m() -> i32` | assert_eq!(m(), 8); edge via assert!(true) |

## Level 39-memory-layout — Memory layout (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-layout-1` | [T] | Implement `layout 1` as described in the stub. | `fn size() -> usize` | assert_eq!(size(), 4); edge via assert!(true) |
| `02-layout-2` | [T] | Implement `layout 2` as described in the stub. | `fn size() -> usize` | assert_eq!(size(), 4); edge via assert!(true) |
| `03-layout-3` | [T] | Implement `layout 3` as described in the stub. | `fn size() -> usize` | assert_eq!(size(), 4); edge via assert!(true) |
| `04-layout-4` | [T] | Implement `layout 4` as described in the stub. | `fn size() -> usize` | assert_eq!(size(), 4); edge via assert!(true) |
| `05-layout-5` | [T] | Implement `layout 5` as described in the stub. | `fn size() -> usize` | assert_eq!(size(), 4); edge via assert!(true) |
| `06-layout-6` | [T] | Implement `layout 6` as described in the stub. | `fn size() -> usize` | assert_eq!(size(), 4); edge via assert!(true) |
| `07-layout-7` | [T] | Implement `layout 7` as described in the stub. | `fn size() -> usize` | assert_eq!(size(), 4); edge via assert!(true) |
| `08-layout-8` | [T] | Implement `layout 8` as described in the stub. | `fn size() -> usize` | assert_eq!(size(), 4); edge via assert!(true) |

## Level 40-unsafe — Unsafe (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-ptr-read` | [T] | Read a `u8` through a raw pointer (stack value must stay valid). | `fn read_byte() -> u8` | assert_eq!(read_byte(), 5);; edge via assert!(read_byte() <= 255); |
| `02-ptr-write` | [T] | Write through `*mut i32` then return the variable. | `fn write_seven() -> i32` | assert_eq!(write_seven(), 7);; edge via assert!(write_seven() > 0); |
| `03-slice-from-raw` | [T] | Build a slice from raw parts for a fixed array. | `fn first_of_three() -> i32` | assert_eq!(first_of_three(), 10);; edge via assert!(first_of_three() > 0); |
| `04-str-from-utf8` | [T] | Use `from_utf8_unchecked` on known-valid ASCII bytes. | `fn parse_ascii() -> &'static str` | assert_eq!(parse_ascii(), "rust");; edge via assert!(!parse_ascii().is_empty()); |
| `05-transmute-size` | [T] | Transmute `u8` 1 to `bool` (document the invariant). | `fn bool_from_u8() -> bool` | assert!(bool_from_u8());; edge via assert_ne!(bool_from_u8() as u8, 0); |
| `06-copy-nonoverlapping` | [T] | Copy two `i32` values with `copy_nonoverlapping`. | `fn copy_two() -> [i32; 2]` | assert_eq!(copy_two(), [1, 2]);; edge via assert_eq!(copy_two()[1], 2); |
| `07-read-volatile` | [T] | Read an `i32` with `read_volatile` (document why). | `fn read_volatile() -> i32` | assert_eq!(read_volatile(), 99);; edge via assert!(read_volatile() > 50); |
| `08-static-mut-counter` | [T] | Increment a `static mut` counter inside `unsafe` (tests run serially). | `fn bump_unsafe() -> u32` | assert_eq!(bump_unsafe(), 1);; edge via assert!(bump_unsafe() >= 3); |

## Level 41-ffi — FFI (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-ffi-add` | [T] | Call C `add_int` from `native/add.c` via FFI. | `fn add_via_ffi(a: i32, b: i32) -> i32` | 3+ assertions incl. edge case |
| `02-ffi-double` | [T] | Double an integer by adding it to itself in C. | `fn double_via_ffi(n: i32) -> i32` | assert_eq!(double_via_ffi(4), 8);; edge via assert_eq!(double_via_ffi(-2), -4); |
| `03-ffi-increment` | [T] | Increment by one using `add_int(n, 1)`. | `fn inc_via_ffi(n: i32) -> i32` | assert_eq!(inc_via_ffi(9), 10);; edge via assert_eq!(inc_via_ffi(0), 1); |
| `04-ffi-sum-three` | [T] | Chain two C calls to add three numbers. | `fn sum3(a: i32, b: i32, c: i32) -> i32` | assert_eq!(sum3(1, 2, 3), 6);; edge via assert_eq!(sum3(-1, 2, 1), 2); |
| `05-ffi-ten` | [T] | Return 10 from `add_int(7, 3)`. | `fn ten() -> i32` | assert_eq!(ten(), 10);; edge via assert_ne!(ten(), 0); |
| `06-ffi-wrap` | [T] | Guard huge inputs before calling FFI. | `fn wrap_add(a: i32, b: i32) -> Option<i32>` | assert_eq!(wrap_add(2, 2), Some(4));; edge via assert!(wrap_add(0, 0).is_some()); |
| `07-ffi-abs-diff` | [T] | Compute absolute difference using `add_int` with negation. | `fn abs_diff(a: i32, b: i32) -> i32` | assert_eq!(abs_diff(5, 3), 2);; edge via assert_eq!(abs_diff(0, 0), 0); |
| `08-ffi-triple` | [T] | Multiply by three using only `add_int`. | `fn triple(n: i32) -> i32` | assert_eq!(triple(3), 9);; edge via assert_eq!(triple(-2), -6); |

## Level 42-performance — Performance (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-global-alloc` | [T] | Count allocations with GlobalAlloc. | `fn alloc_count() -> usize` | 3+ assertions incl. edge case |
| `02-perf-2` | [T] | Implement `perf 2` as described in the stub. | `fn work() -> i32` | assert_eq!(work(), 4); edge via assert!(true) |
| `03-perf-3` | [T] | Implement `perf 3` as described in the stub. | `fn work() -> i32` | assert_eq!(work(), 6); edge via assert!(true) |
| `04-perf-4` | [T] | Implement `perf 4` as described in the stub. | `fn work() -> i32` | assert_eq!(work(), 8); edge via assert!(true) |
| `05-perf-5` | [T] | Implement `perf 5` as described in the stub. | `fn work() -> i32` | assert_eq!(work(), 10); edge via assert!(true) |
| `06-perf-6` | [T] | Implement `perf 6` as described in the stub. | `fn work() -> i32` | assert_eq!(work(), 12); edge via assert!(true) |
| `07-perf-7` | [T] | Implement `perf 7` as described in the stub. | `fn work() -> i32` | assert_eq!(work(), 14); edge via assert!(true) |
| `08-perf-8` | [T] | Implement `perf 8` as described in the stub. | `fn work() -> i32` | assert_eq!(work(), 16); edge via assert!(true) |

## Level 43-cli-clap — CLI clap (phase 5)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-clap-parse` | [T] | Parse `--n` with clap. | `fn parse_n(args: &[&str]) -> i32` | 3+ assertions incl. edge case |
| `02-cli-2` | [T] | Implement `cli 2` as described in the stub. | `fn n() -> i32` | assert_eq!(n(), 2); edge via assert!(true) |
| `03-cli-3` | [T] | Implement `cli 3` as described in the stub. | `fn n() -> i32` | assert_eq!(n(), 3); edge via assert!(true) |
| `04-cli-4` | [T] | Implement `cli 4` as described in the stub. | `fn n() -> i32` | assert_eq!(n(), 4); edge via assert!(true) |
| `05-cli-5` | [T] | Implement `cli 5` as described in the stub. | `fn n() -> i32` | assert_eq!(n(), 5); edge via assert!(true) |
| `06-cli-6` | [T] | Implement `cli 6` as described in the stub. | `fn n() -> i32` | assert_eq!(n(), 6); edge via assert!(true) |
| `07-cli-7` | [T] | Implement `cli 7` as described in the stub. | `fn n() -> i32` | assert_eq!(n(), 7); edge via assert!(true) |
| `08-cli-8` | [T] | Implement `cli 8` as described in the stub. | `fn n() -> i32` | assert_eq!(n(), 8); edge via assert!(true) |

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
| `01-dom-1` | [T] | Implement `dom 1` as described in the stub. | `fn stub_html() -> String` | assert!(stub_html().contains("1")); edge via assert!(true) |
| `02-dom-2` | [T] | Implement `dom 2` as described in the stub. | `fn stub_html() -> String` | assert!(stub_html().contains("2")); edge via assert!(true) |
| `03-dom-3` | [T] | Implement `dom 3` as described in the stub. | `fn stub_html() -> String` | assert!(stub_html().contains("3")); edge via assert!(true) |
| `04-dom-4` | [T] | Implement `dom 4` as described in the stub. | `fn stub_html() -> String` | assert!(stub_html().contains("4")); edge via assert!(true) |
| `05-dom-5` | [T] | Implement `dom 5` as described in the stub. | `fn stub_html() -> String` | assert!(stub_html().contains("5")); edge via assert!(true) |
| `06-dom-6` | [T] | Implement `dom 6` as described in the stub. | `fn stub_html() -> String` | assert!(stub_html().contains("6")); edge via assert!(true) |
| `07-dom-7` | [T] | Implement `dom 7` as described in the stub. | `fn stub_html() -> String` | assert!(stub_html().contains("7")); edge via assert!(true) |
| `08-dom-8` | [T] | Implement `dom 8` as described in the stub. | `fn stub_html() -> String` | assert!(stub_html().contains("8")); edge via assert!(true) |

## Level 46-leptos-components — Leptos components (phase 6)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-leptos-1` | [T] | SSR render component. | `fn render() -> String` | 3+ assertions incl. edge case |
| `02-leptos-2` | [T] | SSR render component. | `fn render() -> String` | 3+ assertions incl. edge case |
| `03-leptos-3` | [T] | SSR render component. | `fn render() -> String` | 3+ assertions incl. edge case |
| `04-leptos-4` | [T] | SSR render component. | `fn render() -> String` | 3+ assertions incl. edge case |
| `05-leptos-5` | [T] | SSR render component. | `fn render() -> String` | 3+ assertions incl. edge case |
| `06-leptos-6` | [T] | SSR render component. | `fn render() -> String` | 3+ assertions incl. edge case |
| `07-leptos-7` | [T] | SSR render component. | `fn render() -> String` | 3+ assertions incl. edge case |
| `08-leptos-8` | [T] | SSR render component. | `fn render() -> String` | 3+ assertions incl. edge case |

## Level 47-leptos-signals — Leptos signals (phase 6)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-signal-1` | [T] | Signal get/set. | `fn signal_val() -> i32` | 3+ assertions incl. edge case |
| `02-signal-2` | [T] | Signal get/set. | `fn signal_val() -> i32` | 3+ assertions incl. edge case |
| `03-signal-3` | [T] | Signal get/set. | `fn signal_val() -> i32` | 3+ assertions incl. edge case |
| `04-signal-4` | [T] | Signal get/set. | `fn signal_val() -> i32` | 3+ assertions incl. edge case |
| `05-signal-5` | [T] | Signal get/set. | `fn signal_val() -> i32` | 3+ assertions incl. edge case |
| `06-signal-6` | [T] | Signal get/set. | `fn signal_val() -> i32` | 3+ assertions incl. edge case |
| `07-signal-7` | [T] | Signal get/set. | `fn signal_val() -> i32` | 3+ assertions incl. edge case |
| `08-signal-8` | [T] | Signal get/set. | `fn signal_val() -> i32` | 3+ assertions incl. edge case |

## Level 48-leptos-server-fns — Leptos server functions (phase 6)

| File | Grading | Task | Expected / signature | Checks contract |
|---|---|---|---|---|
| `01-server-1` | [T] | Server fn stub (native). | `fn greet() -> String` | 3+ assertions incl. edge case |
| `02-server-2` | [T] | Server fn stub (native). | `fn greet() -> String` | 3+ assertions incl. edge case |
| `03-server-3` | [T] | Server fn stub (native). | `fn greet() -> String` | 3+ assertions incl. edge case |
| `04-server-4` | [T] | Server fn stub (native). | `fn greet() -> String` | 3+ assertions incl. edge case |
| `05-server-5` | [T] | Server fn stub (native). | `fn greet() -> String` | 3+ assertions incl. edge case |
| `06-server-6` | [T] | Server fn stub (native). | `fn greet() -> String` | 3+ assertions incl. edge case |
| `07-server-7` | [T] | Server fn stub (native). | `fn greet() -> String` | 3+ assertions incl. edge case |
| `08-server-8` | [T] | Server fn stub (native). | `fn greet() -> String` | 3+ assertions incl. edge case |
