//! 17-traits / 07-trait-param
//!
//! TASK
//! Function taking `impl Summary`.
//!
//! SIGNATURE
//! fn announce(s: &str) -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
trait Summary { fn summarize(&self) -> String; }
struct Note { text: String }
impl Summary for Note { fn summarize(&self) -> String { self.text.clone() } }
fn announce_text(n: &Note) -> String { n.summarize() }
fn announce(s: &str) -> String { announce_text(&Note { text: s.into() }) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-trait-param.rs"]
mod tests;
