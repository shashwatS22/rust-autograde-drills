fn main() {
    let n: u32 = 496;
    let mut sum = 0;
    for i in 1..n { if n % i == 0 { sum += i; } }
    if sum == n { println!("perfect"); } else { println!("not perfect"); }
}
