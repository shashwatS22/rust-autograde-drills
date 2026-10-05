#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn sum3(a: i32, b: i32, c: i32) -> i32 { unsafe { add_int(add_int(a, b), c) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/41-ffi/checks/04-ffi-sum-three.rs"]
mod tests;
