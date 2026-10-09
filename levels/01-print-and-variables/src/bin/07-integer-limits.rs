//! 01-print-and-variables / 07-integer-limits
//!
//! TASK
//! Print `i32::MAX`, `u8::MAX`, `i64::MIN`, one per line.
//!
//! CONCEPT
//! Every integer type has constants like i32::MAX and i64::MIN on the type itself. They show the largest and smallest values that type can hold.
//!
//! EXPECTED OUTPUT
//! `2147483647
//! 255
//! -9223372036854775808`

fn main() {
    println!("{}", i32::MAX);
    println!("{}", u8::MAX);
    println!("{}", i64::MIN);
}