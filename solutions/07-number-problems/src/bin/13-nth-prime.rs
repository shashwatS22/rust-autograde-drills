fn main() {
    let k = 20;
    let mut count = 0;
    let mut p = 2;
    while count < k {
        let mut prime = true;
        let mut i = 2;
        while i * i <= p {
            if p % i == 0 { prime = false; break; }
            i += 1;
        }
        if prime { count += 1; if count == k { println!("{p}"); return; } }
        p += 1;
    }
}
