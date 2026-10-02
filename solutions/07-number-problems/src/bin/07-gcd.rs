fn main() {
    let mut a = 120;
    let mut b = 45;
    while b != 0 { let t = b; b = a % b; a = t; }
    println!("{a}");
}
