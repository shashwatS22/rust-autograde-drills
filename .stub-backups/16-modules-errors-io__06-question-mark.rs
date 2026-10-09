//! 16-modules-errors-io / 06-question-mark
//!
//! TASK
//! `fn double(s: &str) -> Result<i32, std::num::ParseIntError>` using `?` on the parse. Call with `"21"` and with `"x"`, printing the doubled value and then `could not parse`.
//!
//! CONCEPT
//! ? on a Result returns Err early from the function, otherwise unwraps Ok. The function must return Result.
//!
//! EXPECTED OUTPUT
//! `42
//! could not parse`

fn main() {
    // Your code below
}