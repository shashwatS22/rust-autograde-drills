fn print_times(n: u32) {
    if n == 0 { return; }
    println!("learning");
    print_times(n - 1);
}
fn main() { print_times(4); }
