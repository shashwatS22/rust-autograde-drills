use std::error::Error;
fn err() -> Box<dyn Error> { Box::new(std::io::Error::new(std::io::ErrorKind::Other, "x")) }
fn has() -> bool { err().source().is_none() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/25-error-design/checks/05-source-chain.rs"]
mod tests;
