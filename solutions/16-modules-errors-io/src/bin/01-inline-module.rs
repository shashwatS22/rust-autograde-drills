mod greet {
    pub fn hello(name: &str) -> String {
        format!("Hello, {name}!")
    }
}
fn main() {
    println!("{}", greet::hello("Ada"));
}
