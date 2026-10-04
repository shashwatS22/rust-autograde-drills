trait Displayable { fn show(&self) -> String; }
struct Item { t: String }
impl Displayable for Item { fn show(&self) -> String { self.t.clone() } }
fn boxed() -> String { let b: Box<dyn Displayable> = Box::new(Item { t: "hi".into() }); b.show() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/01-trait-object.rs"]
mod tests;
