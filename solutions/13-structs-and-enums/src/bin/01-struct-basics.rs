fn main() {
    struct User { name: String, age: u32 }
    let u = User { name: String::from("Ada"), age: 36 };
    println!("{}", u.name);
    println!("{}", u.age);
}
