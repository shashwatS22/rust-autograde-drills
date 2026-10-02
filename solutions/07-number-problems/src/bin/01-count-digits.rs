fn main() {
    let n: u32 = 946213;
    let mut c = 0;
    let mut x = n;
    while x > 0 { c += 1; x /= 10; }
    println!("{c}");
}
