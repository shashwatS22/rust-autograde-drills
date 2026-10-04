//! 17-traits / 08-partial-eq-trait
//!
//! TASK
//! Trait `Equals` wrapper.
//!
//! SIGNATURE
//! fn same(a: i32, b: i32) -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
trait Equals { fn eq(&self, other: &Self) -> bool; }
impl Equals for i32 { fn eq(&self, other: &Self) -> bool { todo!() } }
fn same(a: i32, b: i32) -> bool { Equals::eq(&a, &b) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-partial-eq-trait.rs"]
mod tests;
