struct Article { title: String, author: String }
trait Summary { fn summarize(&self) -> String; }
impl Summary for Article { fn summarize(&self) -> String { format!("{} by {}", self.title, self.author) } }
fn blurb() -> String { Article { title: "Rust".into(), author: "Ada".into() }.summarize() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/03-summary-trait.rs"]
mod tests;
