fn main() {
    let n: u32 = 74821;
    let mut count = 0;
    let mut x = n;
    while x > 0 {
        count += 1;
        x /= 10;
    }
    println!("{count}");
}
