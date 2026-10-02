fn main() {
    let s = "a,b,c,d";
    let parts: Vec<&str> = s.split(',').collect();
    println!("{}", parts.join(" - "));
}
