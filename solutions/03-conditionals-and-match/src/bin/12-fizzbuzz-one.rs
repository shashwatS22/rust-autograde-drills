fn main() {
    let n = 15;
    match (n % 3, n % 5) {
        (0, 0) => println!("FizzBuzz"),
        (0, _) => println!("Fizz"),
        (_, 0) => println!("Buzz"),
        _ => println!("{n}"),
    }
}
