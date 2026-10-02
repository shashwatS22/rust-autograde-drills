use std::collections::HashMap;
fn main() {
    let v = vec![2, 7, 11, 15];
    let target = 9;
    let mut map: HashMap<i32, usize> = HashMap::new();
    for (i, &x) in v.iter().enumerate() {
        let need = target - x;
        if let Some(&j) = map.get(&need) {
            println!("{j} {i}");
            return;
        }
        map.insert(x, i);
    }
}
