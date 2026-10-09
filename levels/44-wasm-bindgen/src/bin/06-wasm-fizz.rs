//! 44-wasm-bindgen / 06-wasm-fizz
//!
//! TASK
//! Fizz helper: return true when n divisible by 3.
//!
//! SIGNATURE
//! fn is_fizz() -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_fizz(n: u32) -> bool { todo!() }
fn is_fizz() -> bool { wasm_fizz(9) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-wasm-fizz.rs"]
mod tests;