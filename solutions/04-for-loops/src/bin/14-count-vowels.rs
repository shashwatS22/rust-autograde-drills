fn main() {
    let s = "learning rust is fun";
    let mut count = 0;
    for c in s.chars() {
        if "aeiou".contains(c) {
            count += 1;
        }
    }
    println!("{count}");
}
