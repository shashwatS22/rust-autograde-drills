fn main() {
    { let mut row = String::new(); for j in 1..=5 { row.push_str(&format!("{:>4}", 1 * j)); } println!("{row}"); }
    { let mut row = String::new(); for j in 1..=5 { row.push_str(&format!("{:>4}", 2 * j)); } println!("{row}"); }
    { let mut row = String::new(); for j in 1..=5 { row.push_str(&format!("{:>4}", 3 * j)); } println!("{row}"); }
    { let mut row = String::new(); for j in 1..=5 { row.push_str(&format!("{:>4}", 4 * j)); } println!("{row}"); }
    { let mut row = String::new(); for j in 1..=5 { row.push_str(&format!("{:>4}", 5 * j)); } println!("{row}"); }
}
