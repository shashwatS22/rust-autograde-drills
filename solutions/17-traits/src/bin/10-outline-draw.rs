trait Outline { fn draw(&self) -> &'static str; }
struct Dot;
impl Outline for Dot { fn draw(&self) -> &'static str { "." } }
fn shapes() -> String { Dot.draw().into() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/10-outline-draw.rs"]
mod tests;
