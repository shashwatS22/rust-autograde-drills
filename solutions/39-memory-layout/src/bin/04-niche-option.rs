use std::num::NonZeroU8;
fn niche_one_byte() -> usize { std::mem::size_of::<Option<NonZeroU8>>() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/39-memory-layout/checks/04-niche-option.rs"]
mod tests;
