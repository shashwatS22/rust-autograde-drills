fn main() {
    { let mut row = String::new(); for k in 0..1 { if k > 0 { row.push(' '); } row.push((b'A' + k as u8) as char); } println!("{row}"); }
    { let mut row = String::new(); for k in 0..2 { if k > 0 { row.push(' '); } row.push((b'A' + k as u8) as char); } println!("{row}"); }
    { let mut row = String::new(); for k in 0..3 { if k > 0 { row.push(' '); } row.push((b'A' + k as u8) as char); } println!("{row}"); }
    { let mut row = String::new(); for k in 0..4 { if k > 0 { row.push(' '); } row.push((b'A' + k as u8) as char); } println!("{row}"); }
    { let mut row = String::new(); for k in 0..5 { if k > 0 { row.push(' '); } row.push((b'A' + k as u8) as char); } println!("{row}"); }
}
