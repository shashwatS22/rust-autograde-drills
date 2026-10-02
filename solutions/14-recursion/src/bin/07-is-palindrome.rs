fn is_palindrome(s: &str) -> bool {
    let b = s.as_bytes();
    fn helper(b: &[u8], l: usize, r: usize) -> bool {
        if l >= r { true } else if b[l] != b[r] { false } else { helper(b, l + 1, r - 1) }
    }
    helper(b, 0, b.len().saturating_sub(1))
}
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/14-recursion/checks/07-is-palindrome.rs"]
mod tests;
