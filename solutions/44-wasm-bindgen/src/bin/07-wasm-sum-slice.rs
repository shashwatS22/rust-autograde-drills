use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_sum_slice(vals: &[i32]) -> i32 { vals.iter().sum() }
fn sum_three() -> i32 { wasm_sum_slice(&[1, 2, 3]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/44-wasm-bindgen/checks/07-wasm-sum-slice.rs"]
mod tests;
