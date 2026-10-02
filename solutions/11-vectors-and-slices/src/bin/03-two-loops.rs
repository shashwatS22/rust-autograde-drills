fn main() {
    let v = vec!["a", "b", "c"];
    for i in 0..v.len() { println!("{}", v[i]); }
    for x in &v { println!("{x}"); }
}
