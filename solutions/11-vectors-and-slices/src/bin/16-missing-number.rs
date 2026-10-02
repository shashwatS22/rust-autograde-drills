fn main() {
    let v = vec![0, 1, 2, 4, 5];
    let n = 5;
    let expected_sum = n * (n + 1) / 2;
    let actual: u32 = v.iter().sum();
    println!("{}", expected_sum - actual);
}
