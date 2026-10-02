fn main() {
    println!("{}", "42".parse::<i32>().expect("the config value must be a number"));
    let recovered = "x".parse::<i32>().unwrap_or_else(|_| {
        println!("recovered");
        0
    });
    let _ = recovered;
}
