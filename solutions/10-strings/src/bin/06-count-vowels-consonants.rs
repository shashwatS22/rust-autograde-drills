fn main() {
    let s = "hello world";
    let mut vowels = 0;
    let mut consonants = 0;
    for c in s.chars() {
        if c.is_ascii_alphabetic() {
            if "aeiouAEIOU".contains(c) { vowels += 1; } else { consonants += 1; }
        }
    }
    println!("vowels: {vowels}");
    println!("consonants: {consonants}");
}
