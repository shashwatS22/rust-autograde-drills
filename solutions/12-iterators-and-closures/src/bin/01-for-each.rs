fn main() {
    let v = vec![10, 20, 30];
    v.iter().enumerate().for_each(|(i, x)| println!("{i}: {x}"));
}
