struct Counter { n: u32 }
impl Iterator for Counter { type Item = u32; fn next(&mut self) -> Option<Self::Item> { if self.n < 3 { let c = self.n; self.n += 1; Some(c) } else { None } } }
fn collect_counter() -> Vec<u32> { Counter { n: 0 }.collect() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/07-custom-iter.rs"]
mod tests;
