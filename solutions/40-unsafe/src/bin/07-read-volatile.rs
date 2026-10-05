fn read_volatile() -> i32 { let x = 99i32; // INVARIANT: `x` is not mutated concurrently
 unsafe { std::ptr::read_volatile(&x as *const i32) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/07-read-volatile.rs"]
mod tests;
