fn main() {
    println!("{}", "42".parse::<i32>().unwrap());
    match "4x".parse::<i32>() {
        Ok(v) => println!("{v}"),
        Err(_) => println!("not a number"),
    }
}
