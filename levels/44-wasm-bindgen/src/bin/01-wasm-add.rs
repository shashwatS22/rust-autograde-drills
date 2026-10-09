//! 44-wasm-bindgen / 01-wasm-add
//!
//! TASK
//! Expose `wasm_add` with `#[wasm_bindgen]`; test via a native wrapper.
//!
//! CONCEPT
//! #[wasm_bindgen] exports Rust functions to JavaScript in WASM builds.
//!
//! SIGNATURE
//! fn run_add() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_add(a: i32, b: i32) -> i32 { todo!() }
fn run_add() -> i32 { wasm_add(2, 3) }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-wasm-add.rs"]
mod tests;