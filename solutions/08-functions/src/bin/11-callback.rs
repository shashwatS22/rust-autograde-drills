fn repeat(times: u32, f: impl Fn(u32)) {
    for i in 0..times { f(i); }
}
fn main() {
    repeat(3, |i| println!("step {i}"));
}
