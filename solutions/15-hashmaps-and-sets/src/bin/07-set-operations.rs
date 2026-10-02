use std::collections::HashSet;
fn main() {
    let a: HashSet<i32> = vec![1, 2, 3, 4].into_iter().collect();
    let b: HashSet<i32> = vec![3, 4, 5].into_iter().collect();
    let mut union: Vec<i32> = a.union(&b).cloned().collect();
    union.sort();
    println!("{}", union.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" "));
    let mut inter: Vec<i32> = a.intersection(&b).cloned().collect();
    inter.sort();
    println!("{}", inter.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" "));
}
