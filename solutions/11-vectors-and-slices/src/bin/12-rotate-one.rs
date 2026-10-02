fn main() {
    let mut v = vec![1, 2, 3, 4, 5];
    if !v.is_empty() {
        let first = v.remove(0);
        v.push(first);
    }
    let parts: Vec<String> = v.iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
}
