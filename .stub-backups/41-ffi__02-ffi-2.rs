//! 41-ffi / 02-ffi-2
//!
//! TASK
//! Complete `02-ffi-2` (ffi 2).
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
#[path = "../../checks/02-ffi-2.rs"]
mod tests;
