use super::*;
#[test]
fn t() { assert!((circle_area(1.0) - std::f64::consts::PI).abs() < 1e-6); }
