trait Greeter { fn name(&self) -> &str; fn greet(&self) -> String { format!("Hello, {}!", self.name()) } }
struct Ada;
impl Greeter for Ada { fn name(&self) -> &str { "Ada" } }
fn greeting() -> String { Ada.greet() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/02-default-greet.rs"]
mod tests;
