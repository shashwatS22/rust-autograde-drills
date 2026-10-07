use super::*;
#[test]
fn graded() {
    assert_eq!(parse_n(&["app", "--n", "7"]), 7);
}
