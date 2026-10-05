//! 41-ffi / 02-ffi-double
//!
//! TASK
//! Double an integer by adding it to itself in C.
//!
//! SIGNATURE
//! fn double_via_ffi(n: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn double_via_ffi(n: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-ffi-double.rs"]
mod tests;
