fn main() {
    let v = vec![2, 4, 6, 7];
    println!("{}", v.iter().any(|&x| x % 2 != 0));
    println!("{}", v.iter().all(|&x| x % 2 == 0));
}
