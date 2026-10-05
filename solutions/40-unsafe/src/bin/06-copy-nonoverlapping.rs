fn copy_two() -> [i32; 2] { let src = [1, 2]; let mut dst = [0i32; 2]; // INVARIANT: dst has room for 2 elements
 unsafe { std::ptr::copy_nonoverlapping(src.as_ptr(), dst.as_mut_ptr(), 2); } dst }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/06-copy-nonoverlapping.rs"]
mod tests;
