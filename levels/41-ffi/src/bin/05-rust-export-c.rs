//! 41-ffi / 05-rust-export-c
//!
//! TASK
//! Export `double_in_rust` with `#[no_mangle]` for C callbacks.
//!
//! SIGNATURE
//! fn call_rust_double() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
#[unsafe(no_mangle)]
pub extern "C" fn double_in_rust(n: i32) -> i32 { n * 2 }
fn call_rust_double() -> i32 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-rust-export-c.rs"]
mod tests;