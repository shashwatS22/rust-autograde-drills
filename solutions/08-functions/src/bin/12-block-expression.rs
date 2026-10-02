fn main() {
    let x = { let a = 3; let b = 4; a * b };
    println!("{x}");
    let outer = "outer";
    {
        let outer = "inner";
        println!("{outer}");
    }
    println!("{outer}");
}
