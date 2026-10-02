use std::collections::BTreeMap;
fn main() {
    let words = ["apple", "avocado", "banana", "blueberry", "cherry"];
    let mut map: BTreeMap<char, Vec<&str>> = BTreeMap::new();
    for w in words {
        let c = w.chars().next().unwrap();
        map.entry(c).or_default().push(w);
    }
    for (c, list) in map {
        println!("{c}: {}", list.join(", "));
    }
}
