use wasm_bindgen::prelude::*;
#[wasm_bindgen]
pub fn wasm_greet(name: &str) -> String { format!("Hello, {}!", name) }
fn greeting_len() -> usize { wasm_greet("Ada").len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/44-wasm-bindgen/checks/02-wasm-greet.rs"]
mod tests;
