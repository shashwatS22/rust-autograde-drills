enum MathError { DivideByZero }
impl std::fmt::Display for MathError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self { MathError::DivideByZero => write!(f, "cannot divide by zero") }
    }
}
fn checked_div(a: i32, b: i32) -> Result<i32, MathError> {
    if b == 0 { Err(MathError::DivideByZero) } else { Ok(a / b) }
}
fn main() {
    match checked_div(10, 2) { Ok(v) => println!("{v}"), Err(e) => println!("{e}"), }
    match checked_div(10, 0) { Ok(v) => println!("{v}"), Err(e) => println!("{e}"), }
}
