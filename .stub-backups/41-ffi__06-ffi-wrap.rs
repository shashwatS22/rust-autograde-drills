//! 41-ffi / 06-ffi-wrap
//!
//! TASK
//! Guard huge inputs before calling FFI.
//!
//! SIGNATURE
//! fn wrap_add(a: i32, b: i32) -> Option<i32>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn wrap_add(a: i32, b: i32) -> Option<i32> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-ffi-wrap.rs"]
mod tests;
