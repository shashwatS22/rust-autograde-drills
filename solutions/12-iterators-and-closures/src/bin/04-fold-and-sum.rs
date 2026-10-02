fn main() {
    let v = vec![5, 10, 15];
    let fold_sum = v.iter().fold(0, |acc, x| acc + *x);
    println!("{fold_sum}");
    println!("{}", v.iter().sum::<i32>());
}
