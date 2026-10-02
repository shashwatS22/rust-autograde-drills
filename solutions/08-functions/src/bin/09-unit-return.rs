fn five() -> i32 { 5 }
fn log_five() {
    println!("5");
}
fn main() {
    println!("{}", five());
    let r = log_five();
    println!("{:?}", r);
}
