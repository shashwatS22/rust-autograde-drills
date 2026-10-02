fn main() {
    let n: u32 = 25;
    let mut x = n;
    let mut digits = Vec::new();
    while x > 0 {
        digits.push(x % 2);
        x /= 2;
    }
    let mut s = String::new();
    for d in digits.iter().rev() {
        s.push(char::from(b'0' + *d as u8));
    }
    println!("{s}");
}
