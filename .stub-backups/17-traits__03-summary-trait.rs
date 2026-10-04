//! 17-traits / 03-summary-trait
//!
//! TASK
//! Trait `Summary` for `Article`.
//!
//! SIGNATURE
//! fn blurb() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
struct Article { title: String, author: String }
trait Summary { fn summarize(&self) -> String; }
impl Summary for Article { fn summarize(&self) -> String { todo!() } }
fn blurb() -> String { Article { title: "Rust".into(), author: "Ada".into() }.summarize() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-summary-trait.rs"]
mod tests;
