fn main() {
    let v = vec![1, 3, 3, 5, 3];
    let target = 3;
    let mut c = 0;
    for &x in &v { if x == target { c += 1; } }
    println!("{c}");
}
