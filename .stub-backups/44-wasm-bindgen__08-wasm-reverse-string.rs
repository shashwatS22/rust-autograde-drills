//! 44-wasm-bindgen / 08-wasm-reverse-string
//!
//! TASK
//! Reverse a string in a bindgen function.
//!
//! SIGNATURE
//! fn rev() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_reverse(s: &str) -> String { todo!() }
fn rev() -> String { wasm_reverse("rust") }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-wasm-reverse-string.rs"]
mod tests;
