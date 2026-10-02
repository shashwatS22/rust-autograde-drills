use std::collections::BTreeSet;
fn main() {
    let v = vec![1, 2, 2, 3, 3, 3];
    let set: BTreeSet<i32> = v.into_iter().collect();
    let parts: Vec<String> = set.iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
    println!("{}", set.len());
}
