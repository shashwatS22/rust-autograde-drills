fn double(v: &[i32]) -> Vec<i32> { v.iter().map(|x| x * 2).collect() }
fn d() -> Vec<i32> { double(&[1, 2]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/02-map-collect.rs"]
mod tests;
