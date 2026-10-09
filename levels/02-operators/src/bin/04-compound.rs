//! 02-operators / 04-compound
//!
//! TASK
//! GIVEN `let mut total = 100;`. Apply `+= 20`, `-= 30`, `*= 2`, `/= 4` in order, printing after each.
//!
//! CONCEPT
//! Compound operators like += update a mut variable in place: total += 20 means total = total + 20.
//!
//! EXPECTED OUTPUT
//! `120
//! 90
//! 180
//! 45`

use std::println;

fn main() {
    // ---- GIVEN ----
    let mut total = 100;
    // ---------------

    // Your code below
    total += 20;
    println!("{}", total);

    total -= 30;
    println!("{}", total);

    total *= 2;
    println!("{}", total);

    total /= 4;
    println!("{}", total);
}