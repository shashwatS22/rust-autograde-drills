fn main() {
    { let mut row = String::new(); for _ in 0..5 { row.push('*'); } println!("{row}"); }
    { let mut row = String::new(); row.push('*'); for _ in 0..3 { row.push(' '); } row.push('*'); println!("{row}"); }
    { let mut row = String::new(); row.push('*'); for _ in 0..3 { row.push(' '); } row.push('*'); println!("{row}"); }
    { let mut row = String::new(); row.push('*'); for _ in 0..3 { row.push(' '); } row.push('*'); println!("{row}"); }
    { let mut row = String::new(); for _ in 0..5 { row.push('*'); } println!("{row}"); }
}
