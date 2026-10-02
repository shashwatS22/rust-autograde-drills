fn main() {
    { let mut row = String::new(); let ch = char::from_digit(1 as u32, 10).unwrap(); for k in 0..1 { if k > 0 { row.push(' '); } row.push(ch); } println!("{row}"); }
    { let mut row = String::new(); let ch = char::from_digit(2 as u32, 10).unwrap(); for k in 0..2 { if k > 0 { row.push(' '); } row.push(ch); } println!("{row}"); }
    { let mut row = String::new(); let ch = char::from_digit(3 as u32, 10).unwrap(); for k in 0..3 { if k > 0 { row.push(' '); } row.push(ch); } println!("{row}"); }
    { let mut row = String::new(); let ch = char::from_digit(4 as u32, 10).unwrap(); for k in 0..4 { if k > 0 { row.push(' '); } row.push(ch); } println!("{row}"); }
    { let mut row = String::new(); let ch = char::from_digit(5 as u32, 10).unwrap(); for k in 0..5 { if k > 0 { row.push(' '); } row.push(ch); } println!("{row}"); }
}
