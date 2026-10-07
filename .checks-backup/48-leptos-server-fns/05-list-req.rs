use super::*;
#[test]
fn graded() {
    assert_eq!(total(SumReq { values: vec![1, 2, 3] }).total, 6);
}
