use super::*;
    #[test]
    fn graded() {
        assert!((circle_area(1.0) - std::f64::consts::PI).abs() < 1e-6);
assert!((circle_area(0.0)).abs() < 1e-9);
assert!(circle_area(2.0) > circle_area(1.0));
    }
