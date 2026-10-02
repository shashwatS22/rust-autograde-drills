fn main() {
    let a = 12;
    let b = 4;
    let op: char = '/';
    let result = match op {
        '+' => a + b,
        '-' => a - b,
        '*' => a * b,
        '/' => a / b,
        _ => 0,
    };
    println!("{result}");
}
