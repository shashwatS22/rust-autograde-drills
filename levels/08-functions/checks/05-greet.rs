use super::*;

#[test]
fn greeting() {
    assert_eq!(greet("Ada"), "Hello, Ada!");
    assert_eq!(greet("Riya"), "Hello, Riya!");
}
