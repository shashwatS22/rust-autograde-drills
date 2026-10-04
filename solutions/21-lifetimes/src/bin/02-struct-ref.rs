struct Ex<'a> { s: &'a str }
fn first_word(s: &str) -> Ex { Ex { s: s.split_whitespace().next().unwrap_or("") } }
fn w() -> &'static str { first_word("rust lang").s }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/21-lifetimes/checks/02-struct-ref.rs"]
mod tests;
