//! 08-functions / 06-optional-arg
//!
//! TASK
//! `fn greet_with(name: &str, greeting: Option<&str>) -> String`. `None` means `"Hello"`. Rust has no default parameters — this is how you get them.
//!
//! CONCEPT
//! Option<&str> is either Some(value) or None. It replaces default parameters: match or unwrap to pick a fallback.
//!
//! SIGNATURE
//! fn greet_with(name: &str, greeting: Option<&str>) -> String`
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn greet_with(name: &str, greeting: Option<&str>) -> String {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-optional-arg.rs"]
mod tests;