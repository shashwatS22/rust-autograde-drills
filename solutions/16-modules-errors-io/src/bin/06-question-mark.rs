fn double(s: &str) -> Result<i32, std::num::ParseIntError> {
    Ok(s.parse::<i32>()? * 2)
}
fn main() {
    match double("21") {
        Ok(v) => println!("{v}"),
        Err(_) => println!("could not parse"),
    }
    match double("x") {
        Ok(v) => println!("{v}"),
        Err(_) => println!("could not parse"),
    }
}
