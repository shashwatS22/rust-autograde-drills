fn main() {

    #[derive(Debug)]
    struct Person { name: String, age: u32, city: String }
    let people = vec![
        Person { name: "Ada".into(), age: 36, city: "London".into() },
        Person { name: "Raman".into(), age: 42, city: "Kolkata".into() },
        Person { name: "Meera".into(), age: 29, city: "Pune".into() },
    ];

    match people.iter().find(|p| p.name == "Ada") {
        Some(p) => println!("{}", p.name),
        None => println!("none"),
    }
    match people.iter().find(|p| p.name == "Zara") {
        Some(p) => println!("{}", p.name),
        None => println!("none"),
    }
}
