fn main() {
    let v = vec![3, 8, 12, 5];
    println!("{:?}", v.iter().find(|&x| *x > 7));
    println!("{:?}", v.iter().position(|&x| x > 7));
}
