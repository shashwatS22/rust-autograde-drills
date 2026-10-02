fn main() {
    let factor = 3;
    let times = |x| x * factor;
    println!("{}", times(5));
    let times2 = move |x| x * factor;
    println!("{}", times2(10));
}
