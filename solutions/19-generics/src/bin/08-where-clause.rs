fn largest<T>(a: T, b: T) -> T
where
    T: PartialOrd,
{
    if a > b { a } else { b }
}
fn pick() -> i32 { largest(3, 9) }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/19-generics/checks/08-where-clause.rs"]
mod tests;
