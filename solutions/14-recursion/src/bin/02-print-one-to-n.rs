fn print_upto(i: u32, n: u32) {
    if i > n { return; }
    println!("{i}");
    print_upto(i + 1, n);
}
fn main() { print_upto(1, 5); }
