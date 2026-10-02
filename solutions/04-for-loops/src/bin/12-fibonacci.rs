fn main() {
    let n = 10;
    let mut a = 0u64;
    let mut b = 1u64;
    for _ in 0..n {
        println!("{a}");
        let next = a + b;
        a = b;
        b = next;
    }
}
