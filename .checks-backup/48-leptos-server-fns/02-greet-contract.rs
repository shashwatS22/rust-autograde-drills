use super::*;
#[test]
fn graded() {
    assert_eq!(greet(GreetReq { name: "Ada".into() }).msg, "Hello, Ada!");
}
