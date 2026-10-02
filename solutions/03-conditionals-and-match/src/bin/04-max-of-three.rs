fn main() {
    let a = 12;
    let b = 45;
    let c = 45;
    let m = if a >= b && a >= c { a } else if b >= c { b } else { c };
    println!("{m}");
}
