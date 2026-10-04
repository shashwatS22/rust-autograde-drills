//! 41-ffi / 08-ffi-8
//!
//! TASK
//! Complete `08-ffi-8` (ffi 8).
//!
//! SIGNATURE
//! fn v() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn v() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-ffi-8.rs"]
mod tests;
