use std::collections::HashMap;
fn main() {
    let v = vec![10, 5, 10, 15, 10, 5];
    let mut map: HashMap<i32, u32> = HashMap::new();
    for x in v { *map.entry(x).or_insert(0) += 1; }
    let mut pairs: Vec<(i32, u32)> = map.into_iter().collect();
    pairs.sort_by_key(|p| p.0);
    let parts: Vec<String> = pairs.iter().map(|(k, n)| format!("{k}:{n}")).collect();
    println!("{}", parts.join(" "));
}
