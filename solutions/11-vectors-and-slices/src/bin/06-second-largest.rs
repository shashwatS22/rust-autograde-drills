fn main() {
    let v = vec![12, 35, 1, 10, 34, 35];
    let mut first = v[0];
    let mut second = v[0];
    for &n in &v {
        if n > first { second = first; first = n; }
        else if n > second && n != first { second = n; }
    }
    println!("{second}");
}
