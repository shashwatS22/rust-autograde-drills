trait Cloneable: Clone { fn val(&self) -> i32; }
#[derive(Clone)]
struct N(i32);
impl Cloneable for N { fn val(&self) -> i32 { self.0 } }
fn dup(n: &N) -> i32 { n.clone().val() }
fn v() -> i32 { dup(&N(4)) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/09-clone-dyn.rs"]
mod tests;
