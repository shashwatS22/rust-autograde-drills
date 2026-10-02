fn main() {
    let a = 12;
    let b = 18;
    let mut x = a;
    let mut y = b;
    while y != 0 { let t = y; y = x % y; x = t; }
    let gcd = x;
    println!("{}", a * b / gcd);
}
