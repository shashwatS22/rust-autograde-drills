fn main() {
    let v = vec![1, 1, 2, 2, 2, 3, 3];
    let mut out = Vec::new();
    for &x in &v {
        if out.last() != Some(&x) { out.push(x); }
    }
    let parts: Vec<String> = out.iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
}
