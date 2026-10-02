fn main() {
    let evens: Vec<i32> = (1..=10).filter(|x| x % 2 == 0).collect();
    let parts: Vec<String> = evens.iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
}
