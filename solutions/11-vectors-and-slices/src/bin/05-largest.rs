fn main() {
    let v = vec![3, 41, 7, 41, 19];
    let mut max = v[0];
    for &n in &v { if n > max { max = n; } }
    println!("{max}");
}
