//! 19-generics / 07-first
//!
//! TASK
//! Implement `first` as described in the stub.
//!
//! SIGNATURE
//! fn first<T: Copy>(v: &[T]) -> Option<T>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn first<T: Copy>(v: &[T]) -> Option<T> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-first.rs"]
mod tests;
