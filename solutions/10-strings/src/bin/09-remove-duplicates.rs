fn main() {
    let s = "programming";
    let mut seen = Vec::new();
    let mut out = String::new();
    for c in s.chars() {
        if !seen.contains(&c) { seen.push(c); out.push(c); }
    }
    println!("{out}");
}
