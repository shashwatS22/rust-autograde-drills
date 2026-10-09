//! 25-error-design / 03-map-err
//!
//! TASK
//! Implement `map err` as described in the stub.
//!
//! CONCEPT
//! map_err transforms the Err side of Result without touching Ok.
//!
//! SIGNATURE
//! fn wrap(s: &str) -> Result<i32, String>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
fn wrap(s: &str) -> Result<i32, String> {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-map-err.rs"]
mod tests;