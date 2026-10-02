fn main() {
    let s = "abc";
    println!("{}", s.parse::<i32>().is_err());
    println!("{}", s.parse::<i32>().unwrap_or(0));
}
