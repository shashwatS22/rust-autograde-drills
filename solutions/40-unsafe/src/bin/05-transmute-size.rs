fn bool_from_u8() -> bool { let b: u8 = 1; // INVARIANT: only 0/1 used as bool here
 unsafe { std::mem::transmute::<u8, bool>(b) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/05-transmute-size.rs"]
mod tests;
