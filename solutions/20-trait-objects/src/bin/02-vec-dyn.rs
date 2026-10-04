trait Draw { fn draw(&self) -> char; }
struct A;
impl Draw for A { fn draw(&self) -> char { 'A' } }
fn chars() -> String { let v: Vec<Box<dyn Draw>> = vec![Box::new(A)]; v.iter().map(|d| d.draw()).collect() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/02-vec-dyn.rs"]
mod tests;
