trait Greet { fn hi(&self) -> String; }
struct User { name: String }
impl Greet for User { fn hi(&self) -> String { format!("Hi {}", self.name) } }
fn greet() -> String { User { name: "Ada".into() }.hi() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/04-return-impl.rs"]
mod tests;
