fn parse_ascii() -> &'static str { let bytes: &[u8] = b"rust"; // INVARIANT: valid UTF-8
 unsafe { std::str::from_utf8_unchecked(bytes) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/04-str-from-utf8.rs"]
mod tests;
