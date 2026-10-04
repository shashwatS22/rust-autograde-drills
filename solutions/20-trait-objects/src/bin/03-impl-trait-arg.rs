trait Speak { fn speak(&self) -> &str; }
struct Dog;
impl Speak for Dog { fn speak(&self) -> &str { "woof" } }
fn talk(s: &dyn Speak) -> &str { s.speak() }
fn dog() -> &'static str { talk(&Dog) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/03-impl-trait-arg.rs"]
mod tests;
