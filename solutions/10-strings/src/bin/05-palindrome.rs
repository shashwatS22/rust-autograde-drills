fn main() {
    let s = "racecar";
    let rev: String = s.chars().rev().collect();
    println!("{}", s == rev);
}
