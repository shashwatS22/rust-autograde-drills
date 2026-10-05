use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_fizz(n: u32) -> bool { n % 3 == 0 }
fn is_fizz() -> bool { wasm_fizz(9) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/44-wasm-bindgen/checks/06-wasm-fizz.rs"]
mod tests;
