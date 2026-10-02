fn main() {
    let v = vec![1, 2, 3];
    println!("{:?}", v.get(1));
    println!("{:?}", v.get(9));
    println!("{}", v.get(9).copied().unwrap_or(-1));
    println!("{:?}", v.get(1).map(|x| x * 10));
}
