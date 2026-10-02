fn main() {
    let v = vec![1, 2, 2, 5, 9];
    let mut ok = true;
    for i in 1..v.len() {
        if v[i] < v[i - 1] { ok = false; break; }
    }
    println!("{ok}");
}
