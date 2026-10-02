fn main() {
    let n: u32 = 1221;
    let mut rev = 0;
    let mut x = n;
    while x > 0 { rev = rev * 10 + x % 10; x /= 10; }
    println!("{}", rev == n);
}
