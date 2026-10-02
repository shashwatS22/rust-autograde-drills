fn classify(n: i32) -> &'static str {
    if n < 0 { return "negative"; }
    if n == 0 { return "zero"; }
    "positive"
}
fn main() {
    println!("{}", classify(-5));
    println!("{}", classify(0));
    println!("{}", classify(7));
}
