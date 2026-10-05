fn first_of_three() -> i32 { let v = [10i32, 20, 30]; // INVARIANT: slice length matches allocation
 unsafe { std::slice::from_raw_parts(v.as_ptr(), 3)[0] } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/03-slice-from-raw.rs"]
mod tests;
