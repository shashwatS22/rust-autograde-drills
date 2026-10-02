fn main() {
    let s = String::from("hello world");
    println!("{}", &s[0..5]);
    println!("{}", &s[6..]);
}
