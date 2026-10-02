fn main() {
    let n: u32 = 36;
    let mut parts = Vec::new();
    for i in 1..=n {
        if n % i == 0 { parts.push(i.to_string()); }
    }
    println!("{}", parts.join(" "));
}
