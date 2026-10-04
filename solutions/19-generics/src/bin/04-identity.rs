fn id<T>(x: T) -> T { x }
fn id_i32() -> i32 { id(5) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/04-identity.rs"]
mod tests;
