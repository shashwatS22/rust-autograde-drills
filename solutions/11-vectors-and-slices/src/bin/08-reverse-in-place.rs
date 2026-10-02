fn main() {
    let mut v = vec![1, 2, 3, 4, 5];
    let mut i = 0;
    let mut j = v.len() - 1;
    while i < j { v.swap(i, j); i += 1; j -= 1; }
    let parts: Vec<String> = v.iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
}
