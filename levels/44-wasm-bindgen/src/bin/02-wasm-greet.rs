//! 44-wasm-bindgen / 02-wasm-greet
//!
//! TASK
//! Return a greeting string from a `#[wasm_bindgen]` function.
//!
//! SIGNATURE
//! fn greeting_len() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_greet(name: &str) -> String { todo!() }
fn greeting_len() -> usize { wasm_greet("Ada").len() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-wasm-greet.rs"]
mod tests;