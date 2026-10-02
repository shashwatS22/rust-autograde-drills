fn main() {
    let mut v = vec![2, 3];
    v.push(4);
    v.insert(0, 1);
    let p1: Vec<String> = v.iter().map(|x| x.to_string()).collect();
    println!("{}", p1.join(" "));
    v.pop();
    v.remove(0);
    let p2: Vec<String> = v.iter().map(|x| x.to_string()).collect();
    println!("{}", p2.join(" "));
}
