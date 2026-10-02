fn main() {
    let n: u32 = 28;
    let mut sum = 0;
    for i in 1..=n { if n % i == 0 { sum += i; } }
    println!("{sum}");
}
