use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_reverse(s: &str) -> String { s.chars().rev().collect() }
fn rev() -> String { wasm_reverse("rust") }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/44-wasm-bindgen/checks/08-wasm-reverse-string.rs"]
mod tests;
