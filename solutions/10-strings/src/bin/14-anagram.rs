fn main() {
    let a = "listen";
    let b = "silent";
    let mut ac: Vec<char> = a.chars().collect();
    let mut bc: Vec<char> = b.chars().collect();
    ac.sort();
    bc.sort();
    println!("{}", ac == bc);
}
