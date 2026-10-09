//! 41-ffi / 08-ffi-triple
//!
//! TASK
//! Multiply by three using only `add_int`.
//!
//! SIGNATURE
//! fn triple(n: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn triple(n: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-ffi-triple.rs"]
mod tests;