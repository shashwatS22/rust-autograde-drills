use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_max(a: i32, b: i32) -> i32 { if a > b { a } else { b } }
fn max_pair() -> i32 { wasm_max(3, 9) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/44-wasm-bindgen/checks/05-wasm-max.rs"]
mod tests;
