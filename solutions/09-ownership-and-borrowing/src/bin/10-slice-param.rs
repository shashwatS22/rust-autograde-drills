fn total(v: &[i32]) -> i32 { v.iter().sum() }
fn main() {
    let v = vec![1, 2, 3];
    println!("{}", total(&v));
    let parts: Vec<String> = v.iter().map(|n| n.to_string()).collect();
    println!("{}", parts.join(" "));
}
