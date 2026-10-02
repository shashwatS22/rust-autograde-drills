fn main() {
    let text = std::fs::read_to_string("data/sample.txt").unwrap();
    println!("{}", text.trim());
}
