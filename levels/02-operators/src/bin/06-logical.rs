//! 02-operators / 06-logical
//!
//! TASK
//! GIVEN `a = true`, `b = false`. Print `a && b`, `a \
//!
//! EXPECTED OUTPUT
//! \

fn main() {
    // ---- GIVEN ----
    let a = true;
    let b = false;
    // ---------------

    // Your code below
    println!("{}", a && b);
    println!("{}", a || b);
    println!("{}", !a);
    println!("{}", !b);
}