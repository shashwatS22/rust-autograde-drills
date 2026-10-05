fn write_seven() -> i32 { let mut n = 0i32; // INVARIANT: exclusive mutable access
 unsafe { std::ptr::write(&mut n as *mut i32, 7); } n }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/02-ptr-write.rs"]
mod tests;
