use super::*;
#[test]
fn t() { assert!(parse_port("80").is_ok()); assert!(parse_port("x").is_err()); }
