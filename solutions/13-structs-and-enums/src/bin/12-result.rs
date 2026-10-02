fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 { Err(String::from("Cannot divide by zero")) } else { Ok(a / b) }
}
fn main() {
    match divide(12, 4) { Ok(v) => println!("{v}"), Err(e) => println!("{e}"), }
    match divide(1, 0) { Ok(v) => println!("{v}"), Err(e) => println!("{e}"), }
}
