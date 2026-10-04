use std::thread;
fn main() { let _ = thread::spawn(|| println!("thread")).join(); }