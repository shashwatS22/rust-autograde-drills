//! 02-operators / 07-overflow
//!
//! TASK
//! GIVEN `a: u8 = 250`. Print `a.checked_add(10)` with `{:?}`, then `a.wrapping_add(10)`, then `a.saturating_add(10)`.
//!
//! CONCEPT
//! On a fixed-size type like u8, plain + can wrap in debug builds. checked_add returns None on overflow; wrapping_add wraps; saturating_add clamps at MAX.
//!
//! EXPECTED OUTPUT
//! `None
//! 4
//! 255`

fn main() {
    // ---- GIVEN ----
    let a: u8 = 250;
    // ---------------

    // Your code below
}