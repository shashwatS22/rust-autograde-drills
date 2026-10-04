//! 17-traits / 01-area-trait
//!
//! TASK
//! Trait `Area` for `Circle`.
//!
//! SIGNATURE
//! fn circle_area(r: f64) -> f64
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
trait Area { fn area(&self) -> f64; }
struct Circle { r: f64 }
impl Area for Circle { fn area(&self) -> f64 { todo!() } }
fn circle_area(r: f64) -> f64 { Circle { r }.area() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-area-trait.rs"]
mod tests;
