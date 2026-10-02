use std::collections::HashMap;
fn main() {
    let s = "swiss";
    let mut map: HashMap<char, u32> = HashMap::new();
    for c in s.chars() { *map.entry(c).or_insert(0) += 1; }
    for c in s.chars() {
        if map[&c] == 1 {
            println!("{c}");
            return;
        }
    }
    println!("none");
}
