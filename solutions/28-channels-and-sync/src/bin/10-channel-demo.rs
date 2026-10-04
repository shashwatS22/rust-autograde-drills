use std::sync::mpsc;
fn main() { let (tx, rx) = mpsc::channel(); tx.send(1).unwrap(); println!("{}", rx.recv().unwrap()); }