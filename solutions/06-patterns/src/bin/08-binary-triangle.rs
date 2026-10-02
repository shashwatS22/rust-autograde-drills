fn main() {
    { let mut row = String::new(); let mut bit = 1; for j in 0..1 { if j > 0 { row.push(' '); } row.push(char::from_digit(bit as u32, 10).unwrap()); bit = 1 - bit; } println!("{row}"); }
    { let mut row = String::new(); let mut bit = 1; for j in 0..2 { if j > 0 { row.push(' '); } row.push(char::from_digit(bit as u32, 10).unwrap()); bit = 1 - bit; } println!("{row}"); }
    { let mut row = String::new(); let mut bit = 1; for j in 0..3 { if j > 0 { row.push(' '); } row.push(char::from_digit(bit as u32, 10).unwrap()); bit = 1 - bit; } println!("{row}"); }
    { let mut row = String::new(); let mut bit = 1; for j in 0..4 { if j > 0 { row.push(' '); } row.push(char::from_digit(bit as u32, 10).unwrap()); bit = 1 - bit; } println!("{row}"); }
    { let mut row = String::new(); let mut bit = 1; for j in 0..5 { if j > 0 { row.push(' '); } row.push(char::from_digit(bit as u32, 10).unwrap()); bit = 1 - bit; } println!("{row}"); }
}
