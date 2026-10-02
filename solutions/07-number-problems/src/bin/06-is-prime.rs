fn main() {
    let n: u32 = 97;
    let mut prime = n > 1;
    let mut i = 2;
    while i * i <= n {
        if n % i == 0 { prime = false; break; }
        i += 1;
    }
    println!("{}", if prime { "prime" } else { "not prime" });
}
