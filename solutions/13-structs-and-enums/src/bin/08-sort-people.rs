fn main() {
    #[derive(Debug, Clone)]
    struct Person { name: String, age: u32, city: String }
    let people = vec![
        Person { name: "Ada".into(), age: 36, city: "London".into() },
        Person { name: "Raman".into(), age: 42, city: "Kolkata".into() },
        Person { name: "Meera".into(), age: 29, city: "Pune".into() },
    ];
    let mut sorted = people.clone();
    sorted.sort_by_key(|p| p.age);
    let names: Vec<String> = sorted.iter().map(|p| p.name.clone()).collect();
    println!("{}", names.join(" "));
}
