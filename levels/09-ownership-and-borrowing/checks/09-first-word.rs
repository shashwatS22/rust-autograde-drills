use super::*;

#[test]
fn finds_first_word() {
    assert_eq!(first_word("hello world"), "hello");
    assert_eq!(first_word("solo"), "solo");
}
