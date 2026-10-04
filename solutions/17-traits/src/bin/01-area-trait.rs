trait Area { fn area(&self) -> f64; }
struct Circle { r: f64 }
impl Area for Circle { fn area(&self) -> f64 { std::f64::consts::PI * self.r * self.r } }
fn circle_area(r: f64) -> f64 { Circle { r }.area() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/17-traits/checks/01-area-trait.rs"]
mod tests;
