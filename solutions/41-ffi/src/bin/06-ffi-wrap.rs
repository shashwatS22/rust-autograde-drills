#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn wrap_add(a: i32, b: i32) -> Option<i32> { if a > 1_000_000 { None } else { Some(unsafe { add_int(a, b) }) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/41-ffi/checks/06-ffi-wrap.rs"]
mod tests;
