//! 44-wasm-bindgen / 05-wasm-max
//!
//! TASK
//! Return the larger of two i32 values.
//!
//! SIGNATURE
//! fn max_pair() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_max(a: i32, b: i32) -> i32 { todo!() }
fn max_pair() -> i32 { wasm_max(3, 9) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-wasm-max.rs"]
mod tests;