fn main() {
    let s = "42";
    println!("{s}8");
    println!("{}", s.parse::<i32>().unwrap() + 8);
}
