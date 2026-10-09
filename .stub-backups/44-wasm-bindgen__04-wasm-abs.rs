//! 44-wasm-bindgen / 04-wasm-abs
//!
//! TASK
//! Absolute value via wasm_bindgen (graded natively).
//!
//! SIGNATURE
//! fn abs_val() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_abs(n: i32) -> i32 { todo!() }
fn abs_val() -> i32 { wasm_abs(-7) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-wasm-abs.rs"]
mod tests;