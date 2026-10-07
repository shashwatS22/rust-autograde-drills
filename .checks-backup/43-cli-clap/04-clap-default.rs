use super::*;
#[test]
fn graded() {
    assert_eq!(parse_port(&["app"]), 8080);
}
