fn all_pos(v: &[i32]) -> bool { v.iter().all(|x| *x > 0) }
fn a() -> bool { all_pos(&[1, 2]) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/23-iterators-advanced/checks/06-any-all.rs"]
mod tests;
