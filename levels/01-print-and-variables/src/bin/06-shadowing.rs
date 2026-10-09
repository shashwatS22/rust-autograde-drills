//! 01-print-and-variables / 06-shadowing
//!
//! TASK
//! `let x = 5;` print it. Shadow it with `let x = x * 2;` print it. Shadow it again with `let x = "now a word";` print it.
//!
//! CONCEPT
//! Shadowing is a new let with the same name; it hides the old binding. The new variable can have a different type. let mut changes one binding; shadowing creates a new one.
//!
//! EXPECTED OUTPUT
//! `5
//! 10
//! now a word`

fn main() {
    // ---- GIVEN ----
    let x = 5;
    // ---------------

    // Your code below
    println!("{x}");

    let x = x*2;
    println!("{x}");
    let x = "now a word";
    println!("{x}");
    
}