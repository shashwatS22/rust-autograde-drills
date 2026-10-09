//! 44-wasm-bindgen / 03-wasm-double
//!
//! TASK
//! Double a number in a bindgen-exported function.
//!
//! SIGNATURE
//! fn doubled() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_double(n: i32) -> i32 { todo!() }
fn doubled() -> i32 { wasm_double(4) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-wasm-double.rs"]
mod tests;