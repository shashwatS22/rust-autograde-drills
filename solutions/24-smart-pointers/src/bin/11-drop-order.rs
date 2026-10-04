struct D(i32);
impl Drop for D { fn drop(&mut self) {} }
fn val() -> i32 { D(7).0 }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/24-smart-pointers/checks/11-drop-order.rs"]
mod tests;
