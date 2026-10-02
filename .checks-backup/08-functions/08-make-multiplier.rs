use super::*;

#[test]
fn multiplier() {
    let triple = make_multiplier(3);
    assert_eq!(triple(4), 12);
    assert_eq!(triple(0), 0);
}
