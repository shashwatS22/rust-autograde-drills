//! 41-ffi / 03-ffi-3
//!
//! TASK
//! Complete `03-ffi-3` (ffi 3).
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
#[path = "../../checks/03-ffi-3.rs"]
mod tests;
