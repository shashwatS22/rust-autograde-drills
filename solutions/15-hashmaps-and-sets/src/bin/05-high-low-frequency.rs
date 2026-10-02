use std::collections::HashMap;
fn main() {
    let v = vec![10, 5, 10, 15, 10, 5];
    let mut map: HashMap<i32, u32> = HashMap::new();
    for x in v { *map.entry(x).or_insert(0) += 1; }
    let mut best = (i32::MIN, 0u32);
    let mut worst = (i32::MAX, 0u32);
    for (val, cnt) in map {
        if cnt > best.1 || (cnt == best.1 && val < best.0) { best = (val, cnt); }
        if cnt < worst.1 || (cnt == worst.1 && val < worst.0) { worst = (val, cnt); }
    }
    println!("highest: {}", best.0);
    println!("lowest: {}", worst.0);
}
