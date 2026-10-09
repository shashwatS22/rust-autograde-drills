//! 17-traits / 02-default-greet
//!
//! TASK
//! Trait with default method.
//!
//! CONCEPT
//! Traits can provide default method bodies. Types override only what they need.
//!
//! SIGNATURE
//! fn greeting() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
trait Greeter { fn name(&self) -> &str; fn greet(&self) -> String { todo!() } }
struct Ada;
impl Greeter for Ada { fn name(&self) -> &str { "Ada" } }
fn greeting() -> String { Ada.greet() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-default-greet.rs"]
mod tests;