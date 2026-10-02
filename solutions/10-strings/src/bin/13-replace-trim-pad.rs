fn main() {
    let s = "cat bat cat";
    println!("{}", s.replace("cat", "dog"));
    println!("{}", s.replacen("cat", "dog", 1));
    let t = "  7  ";
    println!("{}", t.trim());
    println!("{}", format!("{:0>5}", t.trim()));
}
