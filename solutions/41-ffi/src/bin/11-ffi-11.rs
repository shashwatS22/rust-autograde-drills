#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn v() -> i32 { unsafe { add_int(11, 1) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/41-ffi/checks/11-ffi-11.rs"]
mod tests;
