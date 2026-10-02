fn main() {
    let v = vec![1, 2, 3, 4];
    let doubled: Vec<i32> = v.iter().map(|x| x * 2).collect();
    let parts: Vec<String> = doubled.iter().map(|x| x.to_string()).collect();
    println!("{}", parts.join(" "));
}
