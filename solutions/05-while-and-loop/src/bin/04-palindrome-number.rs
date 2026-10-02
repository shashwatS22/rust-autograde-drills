fn main() {
    let n: u32 = 12321;
    let mut rev = 0;
    let mut x = n;
    while x > 0 {
        rev = rev * 10 + x % 10;
        x /= 10;
    }
    if rev == n {
        println!("palindrome");
    } else {
        println!("not palindrome");
    }
}
