fn main() {
    let s = "abcdefgh";
    println!("{}", &s[2..5]);
    println!("{}", &s[5..]);
    println!("{:?}", s.get(2..5));
}
