fn main() {
    struct Address { city: String }
    struct User { address: Address }
    let user = User { address: Address { city: String::from("Bareilly") } };
    println!("{}", user.address.city);
}
