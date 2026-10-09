//! 22-conversions / 05-deref-coerce
//!
//! TASK
//! Implement `deref coerce` as described in the stub.
//!
//! CONCEPT
//! Deref coercion turns &String into &str at call sites when a function expects &str.
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