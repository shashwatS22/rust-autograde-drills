fn print_down(n: u32) {
    if n == 0 { return; }
    println!("{n}");
    print_down(n - 1);
}
fn main() { print_down(5); }
