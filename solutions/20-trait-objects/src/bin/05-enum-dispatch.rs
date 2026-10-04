enum Pet { Cat, Dog }
fn sound(p: Pet) -> &'static str { match p { Pet::Cat => "meow", Pet::Dog => "woof" } }
fn cat() -> &'static str { sound(Pet::Cat) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/05-enum-dispatch.rs"]
mod tests;
