use super::*;
#[test]
fn graded() {
    assert!(parse_verbose(&["app", "--verbose"]));
}
