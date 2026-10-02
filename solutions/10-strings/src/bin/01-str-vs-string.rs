fn main() {
    let a: &str = "rust";
    let b: String = String::from("rust");
    println!("{a}");
    println!("{b}");
    println!("{}", b == a);
}
