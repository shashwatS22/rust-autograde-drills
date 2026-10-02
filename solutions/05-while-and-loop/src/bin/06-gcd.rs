fn main() {
    let mut a = 48;
    let mut b = 18;
    while b != 0 {
        let t = b;
        b = a % b;
        a = t;
    }
    println!("{a}");
}
