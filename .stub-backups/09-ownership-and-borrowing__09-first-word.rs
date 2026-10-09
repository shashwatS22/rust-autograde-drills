//! 09-ownership-and-borrowing / 09-first-word
//!
//! TASK
//! `fn first_word(s: &str) -> &str` returning everything up to the first space, or the whole string. Note the returned `&str` borrows from the input — that's why no lifetime annotation is needed.
//!
//! CONCEPT
//! &str in a parameter accepts any string slice. The returned &str borrows from the input, so no lifetime name is needed on this pattern.
//!
//! SIGNATURE
//! fn first_word(s: &str) -> &str` returning everything up to the first space, or the whole string
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn first_word(s: &str) -> &str {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/09-first-word.rs"]
mod tests;