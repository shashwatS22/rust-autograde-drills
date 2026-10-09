//! 41-ffi / 04-ffi-sum-three
//!
//! TASK
//! Chain two C calls to add three numbers.
//!
//! SIGNATURE
//! fn sum3(a: i32, b: i32, c: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn sum3(a: i32, b: i32, c: i32) -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-ffi-sum-three.rs"]
mod tests;