fn main() {
    let sum = (1..=10).filter(|x| x % 2 == 0).map(|x| x * x).sum::<i32>();
    println!("{sum}");
}
