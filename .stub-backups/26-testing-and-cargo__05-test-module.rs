//! 26-testing-and-cargo / 05-test-module
//!
//! TASK
//! Keep helpers in a private module, expose one function.
//!
//! SIGNATURE
//! pub fn sq() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
mod math { pub fn sq(x: i32) -> i32 { todo!() } }
pub fn sq() -> i32 { math::sq(3) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-test-module.rs"]
mod tests;
