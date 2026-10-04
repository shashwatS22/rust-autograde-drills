enum List { Cons(i32, Box<List>), Nil }
fn head() -> i32 { match List::Cons(1, Box::new(List::Nil)) { List::Cons(h, _) => h, List::Nil => 0 } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/05-box-recursive.rs"]
mod tests;
