use std::collections::BTreeMap;
fn main() {
    let s = "banana";
    let mut map: BTreeMap<char, u32> = BTreeMap::new();
    for c in s.chars() { *map.entry(c).or_insert(0) += 1; }
    let parts: Vec<String> = map.iter().map(|(c, n)| format!("{c}:{n}")).collect();
    println!("{}", parts.join(" "));
}
