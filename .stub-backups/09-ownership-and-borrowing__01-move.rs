//! 09-ownership-and-borrowing / 01-move
//!
//! TASK
//! GIVEN `let s1 = String::from("hello");`. Write `let s2 = s1;` and print `s2`. Then add a comment explaining, in your own words, why printing `s1` here would be `E0382`.
//!
//! CONCEPT
//! String owns its heap data. let s2 = s1 moves ownership to s2; s1 is no longer valid (error E0382 if used).
//!
//! EXPECTED OUTPUT
//! `hello`

fn main() {
    // Your code below
}