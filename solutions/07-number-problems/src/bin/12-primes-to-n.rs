fn main() {
    let n: u32 = 30;
    let mut parts = Vec::new();
    for p in 2..=n {
        let mut prime = true;
        let mut i = 2;
        while i * i <= p {
            if p % i == 0 { prime = false; break; }
            i += 1;
        }
        if prime { parts.push(p.to_string()); }
    }
    println!("{}", parts.join(" "));
}
