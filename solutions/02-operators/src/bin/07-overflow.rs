fn main() {
    let a: u8 = 250;
    println!("{:?}", a.checked_add(10));
    println!("{}", a.wrapping_add(10));
    println!("{}", a.saturating_add(10));
}
