fn main() {
    let v = vec![0, 1, 0, 3, 12];
    let mut out: Vec<i32> = v.iter().filter(|&x| *x != 0).cloned().collect();
    let zeros = v.iter().filter(|&x| *x == 0).count();
    for _ in 0..zeros { out.push(0); }
    let parts: Vec<String> = out.iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
}
