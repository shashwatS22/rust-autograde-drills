trait Summary { fn summarize(&self) -> String; }
struct Note { text: String }
impl Summary for Note { fn summarize(&self) -> String { self.text.clone() } }
fn announce_text(n: &Note) -> String { n.summarize() }
fn announce(s: &str) -> String { announce_text(&Note { text: s.into() }) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/07-trait-param.rs"]
mod tests;
