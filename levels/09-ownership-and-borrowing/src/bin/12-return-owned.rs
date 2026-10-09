//! 09-ownership-and-borrowing / 12-return-owned
//!
//! TASK
//! Write `fn make_greeting(name: &str) -> String` that builds and returns an owned `String`. Comment on why returning `&str` built from a local would be `E0106`/`E0515`.
//!
//! CONCEPT
//! Returning String transfers ownership to the caller. Returning &str to locally built data would outlive the stack (E0106).
//!
//! EXPECTED OUTPUT
//! `Hello, Ada!`

fn main() {
    // Your code below
}