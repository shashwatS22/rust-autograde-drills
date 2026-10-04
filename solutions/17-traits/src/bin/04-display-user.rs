use std::fmt;
struct User { name: String, age: u32 }
impl fmt::Display for User { fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result { write!(f, "{} ({})", self.name, self.age) } }
fn format_user() -> String { User { name: "Riya".into(), age: 27 }.to_string() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/04-display-user.rs"]
mod tests;
