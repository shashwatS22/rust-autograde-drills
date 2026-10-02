mod secrets {
    fn secret() -> i32 { 42 }
    pub fn reveal() -> i32 { secret() }
}
fn main() {
    println!("secret: {}", secrets::reveal());
}
