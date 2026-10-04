//! 17-traits / 11-chain
//!
//! TASK
//! Trait `Twice`.
//!
//! SIGNATURE
//! fn twice_five() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
trait Twice { fn double(self) -> i32; }
impl Twice for i32 { fn double(self) -> i32 { todo!() } }
fn twice_five() -> i32 { 5.double() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/11-chain.rs"]
mod tests;
