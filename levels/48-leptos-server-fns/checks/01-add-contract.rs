use super::*;
#[test]
fn graded() {
    assert_eq!(handle(AddReq { a: 2, b: 3 }).sum, 5);
}
