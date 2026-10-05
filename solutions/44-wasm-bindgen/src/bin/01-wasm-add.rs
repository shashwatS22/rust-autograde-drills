use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_add(a: i32, b: i32) -> i32 { a + b }
fn run_add() -> i32 { wasm_add(2, 3) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/44-wasm-bindgen/checks/01-wasm-add.rs"]
mod tests;
