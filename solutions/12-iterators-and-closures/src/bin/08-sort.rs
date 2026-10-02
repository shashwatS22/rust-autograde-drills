fn main() {
    let mut v = vec![10, 9, 100, 2];
    v.sort();
    let p1: Vec<String> = v.iter().map(|x| x.to_string()).collect();
    println!("{}", p1.join(" "));
    v.sort_by(|a, b| b.cmp(a));
    let p2: Vec<String> = v.iter().map(|x| x.to_string()).collect();
    println!("{}", p2.join(" "));
}
