fn main() {

    #[derive(Debug)]
    struct Person { name: String, age: u32, city: String }
    let people = vec![
        Person { name: "Ada".into(), age: 36, city: "London".into() },
        Person { name: "Raman".into(), age: 42, city: "Kolkata".into() },
        Person { name: "Meera".into(), age: 29, city: "Pune".into() },
    ];

    let names: Vec<String> = people.iter().filter(|p| p.age > 30).map(|p| p.name.clone()).collect();
    println!("{}", names.join(", "));
}
