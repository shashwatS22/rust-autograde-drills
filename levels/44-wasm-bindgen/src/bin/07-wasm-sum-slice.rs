//! 44-wasm-bindgen / 07-wasm-sum-slice
//!
//! TASK
//! Sum a slice passed to wasm_bindgen (native test uses a fixed slice).
//!
//! SIGNATURE
//! fn sum_three() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_sum_slice(vals: &[i32]) -> i32 { todo!() }
fn sum_three() -> i32 { wasm_sum_slice(&[1, 2, 3]) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-wasm-sum-slice.rs"]
mod tests;
