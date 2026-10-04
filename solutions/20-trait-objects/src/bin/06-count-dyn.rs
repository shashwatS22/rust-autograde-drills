trait Id { fn id(&self) -> u32; }
struct X(u32);
impl Id for X { fn id(&self) -> u32 { self.0 } }
fn sum(v: &[Box<dyn Id>]) -> u32 { v.iter().map(|x| x.id()).sum() }
fn two() -> u32 { sum(&[Box::new(X(1)), Box::new(X(2))]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/06-count-dyn.rs"]
mod tests;
