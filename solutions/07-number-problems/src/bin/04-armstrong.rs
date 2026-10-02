fn main() {
    let n: u32 = 371;
    let mut sum = 0;
    let mut x = n;
    while x > 0 {
        let d = x % 10;
        sum += d * d * d;
        x /= 10;
    }
    println!("{}", sum == n);
}
