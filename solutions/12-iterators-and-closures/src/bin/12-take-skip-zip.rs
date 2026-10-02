fn main() {
    let v = vec![1, 2, 3, 4, 5];
    let letters = vec!["a", "b"];
    let t: Vec<String> = v.iter().take(2).map(|x| x.to_string()).collect();
    println!("{}", t.join(" "));
    let s: Vec<String> = v.iter().skip(3).map(|x| x.to_string()).collect();
    println!("{}", s.join(" "));
    let z: Vec<String> = v.iter().zip(letters.iter()).map(|(a, b)| format!("{a}{b}")).collect();
    println!("{}", z.join(" "));
}
