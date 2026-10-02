fn main() {
    let v = vec![7, 3, 9, 1];
    let target = 9;
    let mut idx = -1;
    for (i, &x) in v.iter().enumerate() {
        if x == target { idx = i as i32; break; }
    }
    println!("{idx}");
}
