fn main() {
    let n: u64 = 1223334444;
    let mut freq = [0u32; 10];
    let mut x = n;
    while x > 0 { freq[(x % 10) as usize] += 1; x /= 10; }
    let mut parts = Vec::new();
    for d in 0..10u32 {
        if freq[d as usize] > 0 { parts.push(format!("{d}:{}", freq[d as usize])); }
    }
    println!("{}", parts.join(" "));
}
