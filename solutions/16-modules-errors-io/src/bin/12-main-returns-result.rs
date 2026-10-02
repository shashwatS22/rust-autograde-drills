fn main() -> Result<(), Box<dyn std::error::Error>> {
    let text = std::fs::read_to_string("data/sample.txt")?;
    println!("{}", text.trim());
    Ok(())
}
