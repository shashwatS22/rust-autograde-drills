use super::*;

#[test]
fn with_greeting() {
    assert_eq!(greet_with("Ada", Some("Hi")), "Hi, Ada!");
    assert_eq!(greet_with("Ada", None), "Hello, Ada!");
}
