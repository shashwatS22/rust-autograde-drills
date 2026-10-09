//! 16-modules-errors-io / 07-custom-error
//!
//! TASK
//! `enum MathError { DivideByZero }` with `impl std::fmt::Display`. `fn checked_div(a: i32, b: i32) -> Result<i32, MathError>`. Print `checked_div(10, 2)` on success and the `Display` text on failure.
//!
//! CONCEPT
//! impl Display formats your error for users. Return Result<T, YourError> from fallible APIs.
//!
//! EXPECTED OUTPUT
//! `5
//! cannot divide by zero`

fn main() {
    // Your code below
}