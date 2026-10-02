fn main() {
    let mut n: u32 = 360;
    let mut parts = Vec::new();
    let mut d = 2;
    while d * d <= n {
        while n % d == 0 { parts.push(d.to_string()); n /= d; }
        d += 1;
    }
    if n > 1 { parts.push(n.to_string()); }
    println!("{}", parts.join(" "));
}
