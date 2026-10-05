static mut COUNT: u32 = 0;
fn bump_unsafe() -> u32 { // INVARIANT: single-threaded test only
 unsafe { COUNT += 1; COUNT } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/08-static-mut-counter.rs"]
mod tests;
