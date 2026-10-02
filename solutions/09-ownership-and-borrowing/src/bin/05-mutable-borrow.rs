fn add_excl(s: &mut String) { s.push('!'); }
fn main() {
    let mut s = String::from("hello");
    add_excl(&mut s);
    println!("{s}");
}
