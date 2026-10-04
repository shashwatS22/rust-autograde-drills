//! Leptos full-stack capstone — see README.md (wasm-pack + deploy milestones).

pub fn placeholder() -> &'static str {
    "web-capstone-not-started"
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn scaffold_compiles() {
        assert!(placeholder().contains("capstone"));
    }
}
