fn opt() -> Option<i32> { Some(1).and_then(|x| Some(x + 1)) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/09-option-ok.rs"]
mod tests;
