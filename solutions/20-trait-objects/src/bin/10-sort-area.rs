trait Area { fn area(&self) -> i32; }
struct S { s: i32 }
impl Area for S { fn area(&self) -> i32 { self.s * self.s } }
fn biggest(v: &[S]) -> i32 { v.iter().map(|s| s.area()).max().unwrap() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/20-trait-objects/checks/10-sort-area.rs"]
mod tests;
