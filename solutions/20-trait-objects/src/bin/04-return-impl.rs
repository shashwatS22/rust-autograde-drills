trait Greet { fn hi(&self) -> String; }
struct User { name: String }
impl Greet for User { fn hi(&self) -> String { format!("Hi {}", self.name) } }
fn make_greeter() -> impl Greet { User { name: "Ada".into() } }
fn greet() -> String { make_greeter().hi() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/04-return-impl.rs"]
mod tests;
