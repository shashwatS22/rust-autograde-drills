fn main() {
    let mut i = 1;
    let result = loop {
        if i * i > 50 {
            break i;
        }
        i += 1;
    };
    println!("{result}");
}
