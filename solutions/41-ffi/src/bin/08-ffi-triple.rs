#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn triple(n: i32) -> i32 { unsafe { add_int(add_int(n, n), n) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/41-ffi/checks/08-ffi-triple.rs"]
mod tests;
