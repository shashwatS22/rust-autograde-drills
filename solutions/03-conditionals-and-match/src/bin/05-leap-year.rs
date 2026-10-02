fn main() {
    let year = 2100;
    let leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
    if leap {
        println!("leap");
    } else {
        println!("not leap");
    }
}
