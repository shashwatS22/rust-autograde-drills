//! 08-functions / 02-expression-return
//!
//! TASK
//! `fn multiply(a: i32, b: i32) -> i32`, written with **no** `return` keyword and no semicolon on the last line.
//!
//! CONCEPT
//! Omitting return and the final semicolon makes the last expression the return value. A semicolon on that line would return () instead.
//!
//! SIGNATURE
//! fn multiply(a: i32, b: i32) -> i32`, written with **no** `return` keyword and no semicolon on the last line
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn multiply(a: i32, b: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-expression-return.rs"]
mod tests;