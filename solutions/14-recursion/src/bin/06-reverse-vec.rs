fn reverse(v: &[i32]) -> Vec<i32> {
    if v.is_empty() {
        Vec::new()
    } else {
        let mut r = reverse(&v[1..]);
        r.push(v[0]);
        r
    }
}
fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/14-recursion/checks/06-reverse-vec.rs"]
mod tests;
