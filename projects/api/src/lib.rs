//! REST API capstone — implement milestones in README.md; gate: `cargo test -p api`.

pub fn placeholder() -> &'static str {
    "capstone-not-started"
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn scaffold_compiles() {
        assert_eq!(placeholder(), "capstone-not-started");
    }
}
