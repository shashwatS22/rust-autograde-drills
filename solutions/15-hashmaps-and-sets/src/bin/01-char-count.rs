use std::collections::HashMap;
fn main() {
    let s = "banana";
    let mut map: HashMap<char, u32> = HashMap::new();
    for c in s.chars() { map.insert(c, map.get(&c).unwrap_or(&0) + 1); }
    let mut pairs: Vec<(char, u32)> = map.into_iter().collect();
    pairs.sort_by_key(|p| p.0);
    let parts: Vec<String> = pairs.iter().map(|(c, n)| format!("{c}:{n}")).collect();
    println!("{}", parts.join(" "));
}
