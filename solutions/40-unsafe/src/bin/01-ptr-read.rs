fn read_byte() -> u8 { let n: u8 = 5; // INVARIANT: `n` lives while pointer is used
 unsafe { std::ptr::read(&n as *const u8) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/01-ptr-read.rs"]
mod tests;
