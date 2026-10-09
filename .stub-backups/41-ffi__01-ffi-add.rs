//! 41-ffi / 01-ffi-add
//!
//! TASK
//! Call C `add_int` from `native/add.c` via FFI.
//!
//! CONCEPT
//! extern "C" links to C functions; follow the exact ABI and keep pointers valid across the boundary.
//!
//! SIGNATURE
//! fn add_via_ffi(a: i32, b: i32) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn add_via_ffi(a: i32, b: i32) -> i32 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-ffi-add.rs"]
mod tests;