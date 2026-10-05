use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_abs(n: i32) -> i32 { n.abs() }
fn abs_val() -> i32 { wasm_abs(-7) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/44-wasm-bindgen/checks/04-wasm-abs.rs"]
mod tests;
