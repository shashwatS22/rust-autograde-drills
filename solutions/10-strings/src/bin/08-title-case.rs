fn main() {
    let s = "learning rust today";
    let titled: Vec<String> = s
        .split_whitespace()
        .map(|w| {
            let mut c = w.chars();
            match c.next() {
                None => String::new(),
                Some(f) => f.to_uppercase().collect::<String>() + c.as_str(),
            }
        })
        .collect();
    println!("{}", titled.join(" "));
}
