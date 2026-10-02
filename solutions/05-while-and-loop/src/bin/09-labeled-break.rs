fn main() {
    let mut found = (0, 0);
    'outer: for i in 1..=5 {
        for j in 1..=5 {
            if i * j == 12 {
                found = (i, j);
                break 'outer;
            }
        }
    }
    println!("{} {}", found.0, found.1);
}
