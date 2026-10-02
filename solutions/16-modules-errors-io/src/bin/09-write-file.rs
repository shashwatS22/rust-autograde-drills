fn main() {
    std::fs::write("data/out.txt", "hello from a file").unwrap();
    let text = std::fs::read_to_string("data/out.txt").unwrap();
    println!("{}", text.trim_end());
}
