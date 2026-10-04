//! 41-ffi / 04-ffi-4
//!
//! TASK
//! Complete `04-ffi-4` (ffi 4).
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
#[path = "../../checks/04-ffi-4.rs"]
mod tests;
