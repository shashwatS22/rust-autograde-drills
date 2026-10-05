//! 41-ffi / 05-ffi-ten
//!
//! TASK
//! Return 10 from `add_int(7, 3)`.
//!
//! SIGNATURE
//! fn ten() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn ten() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-ffi-ten.rs"]
mod tests;
