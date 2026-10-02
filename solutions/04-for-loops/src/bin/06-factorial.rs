fn main() {
    let n: u64 = 6;
    let mut fact = 1;
    for i in 1..=n {
        fact *= i;
    }
    println!("{fact}");
}
