//! 17-traits / 09-associated-fn
//!
//! TASK
//! `News::headline()`.
//!
//! SIGNATURE
//! fn headline() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
struct News;
impl News { fn headline() -> String { todo!() } }
fn headline() -> String { News::headline() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/09-associated-fn.rs"]
mod tests;
