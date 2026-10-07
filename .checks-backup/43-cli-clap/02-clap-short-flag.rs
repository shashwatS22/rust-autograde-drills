use super::*;
#[test]
fn graded() {
    assert_eq!(parse_count(&["app", "-c", "3"]), 3);
}
