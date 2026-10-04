fn read() -> u8 { let n: u8 = 5; unsafe { std::ptr::read(&n as *const u8) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/01-raw-read.rs"]
mod tests;
