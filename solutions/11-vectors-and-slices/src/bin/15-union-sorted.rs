fn main() {
    let a = vec![1, 2, 3, 4, 6];
    let b = vec![2, 3, 5];
    let mut set = std::collections::BTreeSet::new();
    for x in a { set.insert(x); }
    for x in b { set.insert(x); }
    let parts: Vec<String> = set.iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
}
