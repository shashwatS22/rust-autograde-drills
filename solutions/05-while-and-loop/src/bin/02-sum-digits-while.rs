fn main() {
    let n: u32 = 48291;
    let mut sum = 0;
    let mut x = n;
    while x > 0 {
        sum += x % 10;
        x /= 10;
    }
    println!("{sum}");
}
