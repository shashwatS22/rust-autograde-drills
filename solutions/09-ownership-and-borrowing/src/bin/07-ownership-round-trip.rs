fn consume(s: String) -> (usize, String) { (s.len(), s) }
fn main() {
    let s = String::from("hello");
    let (len, s) = consume(s);
    println!("{len}");
    println!("{s}");
}
