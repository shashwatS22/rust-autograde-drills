fn main() {
    let text = std::fs::read_to_string("data/numbers.txt").unwrap();
    let sum = text
        .lines()
        .map(|l| l.trim().parse::<i32>().unwrap())
        .sum::<i32>();
    println!("{sum}");
}
