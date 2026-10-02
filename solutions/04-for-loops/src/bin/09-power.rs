fn main() {
    let base: u64 = 3;
    let exp = 5;
    let mut result = 1;
    for _ in 0..exp {
        result *= base;
    }
    println!("{result}");
}
