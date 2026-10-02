fn main() {
    let s = "rustlang";
    println!("{}", s.contains("lang"));
    println!("{}", s.starts_with("rust"));
    println!("{}", s.ends_with("x"));
    println!("{:?}", s.find('t'));
}
