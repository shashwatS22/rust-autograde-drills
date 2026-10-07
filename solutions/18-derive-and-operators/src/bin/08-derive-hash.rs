#[derive(Hash, Eq, PartialEq)]
struct Key(i32);
use std::collections::HashSet;
fn uniq_keys() -> usize { let s: HashSet<Key> = [Key(1), Key(1), Key(2)].into_iter().collect(); s.len() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/18-derive-and-operators/checks/08-derive-hash.rs"]
mod tests;
