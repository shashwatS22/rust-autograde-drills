fn main() {
    enum Direction { North, South, East, West }
    let d = Direction::South;
    match d { Direction::South => println!("going south"), _ => {} }
}
