use super::*;
#[test]
fn t() {
    assert_eq!(std::panic::catch_unwind(|| panics()).is_err(), true)
}
