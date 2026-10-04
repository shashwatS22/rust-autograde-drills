struct News;
impl News { fn headline() -> String { "Breaking".into() } }
fn headline() -> String { News::headline() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/09-associated-fn.rs"]
mod tests;
