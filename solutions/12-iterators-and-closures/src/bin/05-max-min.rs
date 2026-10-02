fn main() {
    let v = vec![4, 19, 7, 2];
    println!("{}", v.iter().max().unwrap());
    println!("{}", v.iter().min().unwrap());
}
