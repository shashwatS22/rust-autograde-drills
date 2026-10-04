//! 20-trait-objects / 01-trait-object
//!
//! TASK
//! Return `Box<dyn Displayable>`.
//!
//! SIGNATURE
//! fn boxed() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
trait Displayable { fn show(&self) -> String; }
struct Item { t: String }
impl Displayable for Item { fn show(&self) -> String { self.t.clone() } }
fn boxed() -> String { let b: Box<dyn Displayable> = Box::new(Item { t: "hi".into() }); b.show() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-trait-object.rs"]
mod tests;
