fn main() {
    let v = vec![1, 2, 3, 4, 5, 6, 7];
    let k = 3;
    let n = v.len();
    let k = k % n;
    let rotated = v[k..].iter().chain(v[..k].iter()).cloned().collect::<Vec<_>>();
    let parts: Vec<String> = rotated.iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
}
