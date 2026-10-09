//! 09-ownership-and-borrowing / 06-borrow-scopes
//!
//! TASK
//! Call `add_excl` twice in sequence, printing in between. Comment on why the two `&mut` borrows are fine sequentially but would be `E0499` simultaneously.
//!
//! CONCEPT
//! Borrows end at the last use of the reference. Sequential &mut borrows are fine; overlapping ones are not (E0499).
//!
//! EXPECTED OUTPUT
//! `hello!
//! hello!!`

fn main() {
    // Your code below
}