fn main() {
    let v = vec![4, 8, 15, 16, 23, 42];
    let sum: i32 = v.iter().sum();
    println!("{sum}");
    println!("{:.2}", sum as f64 / v.len() as f64);
}
