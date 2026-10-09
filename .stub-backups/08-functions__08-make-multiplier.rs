//! 08-functions / 08-make-multiplier
//!
//! TASK
//! `fn make_multiplier(n: i32) -> impl Fn(i32) -> i32`.
//!
//! CONCEPT
//! impl Fn(i32) -> i32 as a return type means the function returns a closure. The closure can capture n from the enclosing scope.
//!
//! SIGNATURE
//! fn make_multiplier(n: i32) -> impl Fn(i32) -> i32`
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn make_multiplier(n: i32) -> impl Fn(i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-make-multiplier.rs"]
mod tests;