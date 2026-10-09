//! 01-print-and-variables / 08-concat
//!
//! TASK
//! GIVEN `first = "Ada"`, `last = "Lovelace"`. Build the full name with `format!` and print it.
//!
//! CONCEPT
//! format! builds a String from a format string, like println! but returns the text instead of printing it.
//!
//! EXPECTED OUTPUT
//! `Ada Lovelace`

use std::println;

fn main() {
    // ---- GIVEN ----
    let first = "Ada";
    let last = "Lovelace";
    // ---------------

    // Your code below
    let a = format!("{first} {last}");
    println!("{}", a);
}