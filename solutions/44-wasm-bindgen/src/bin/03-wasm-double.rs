use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_double(n: i32) -> i32 { n * 2 }
fn doubled() -> i32 { wasm_double(4) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/44-wasm-bindgen/checks/03-wasm-double.rs"]
mod tests;
