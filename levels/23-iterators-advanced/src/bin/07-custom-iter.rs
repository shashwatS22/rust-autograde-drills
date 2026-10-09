//! 23-iterators-advanced / 07-custom-iter
//!
//! TASK
//! Implement `Iterator` by hand for a small counter.
//!
//! CONCEPT
//! Implement Iterator with type Item and fn next(&mut self) -> Option<Item> for custom sequences.
//!
//! SIGNATURE
//! fn collect_counter() -> Vec<u32>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn collect_counter() -> Vec<u32> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-custom-iter.rs"]
mod tests;