#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn inc_via_ffi(n: i32) -> i32 { unsafe { add_int(n, 1) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/41-ffi/checks/03-ffi-increment.rs"]
mod tests;
