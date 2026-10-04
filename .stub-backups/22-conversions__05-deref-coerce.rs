//! 22-conversions / 05-deref-coerce
//!
//! TASK
//! Complete `05-deref-coerce` (deref coerce).
//!
//! SIGNATURE
//! fn upper(s: &str) -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::ops::Deref;
struct S(String);
impl Deref for S { type Target = str; fn deref(&self) -> &str { &self.0 } }
fn upper(s: &str) -> String {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-deref-coerce.rs"]
mod tests;
