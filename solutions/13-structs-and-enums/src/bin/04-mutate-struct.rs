fn main() {
    struct User { name: String, age: u32 }
    let mut u = User { name: String::from("Ada"), age: 36 };
    u.age = 37;
    println!("{}", u.age);
}
