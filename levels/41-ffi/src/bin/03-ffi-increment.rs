//! 41-ffi / 03-ffi-increment
//!
//! TASK
//! Increment by one using `add_int(n, 1)`.
//!
//! SIGNATURE
//! fn inc_via_ffi(n: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn inc_via_ffi(n: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-ffi-increment.rs"]
mod tests;
