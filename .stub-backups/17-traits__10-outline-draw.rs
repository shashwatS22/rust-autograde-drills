//! 17-traits / 10-outline-draw
//!
//! TASK
//! Trait `Outline`.
//!
//! SIGNATURE
//! fn shapes() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
trait Outline { fn draw(&self) -> &'static str; }
struct Dot;
impl Outline for Dot { fn draw(&self) -> &'static str { todo!() } }
fn shapes() -> String { Dot.draw().into() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/10-outline-draw.rs"]
mod tests;
