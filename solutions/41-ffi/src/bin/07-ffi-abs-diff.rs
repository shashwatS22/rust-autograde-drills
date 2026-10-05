#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn abs_diff(a: i32, b: i32) -> i32 { if a >= b { unsafe { add_int(a, -b) } } else { unsafe { add_int(b, -a) } } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/41-ffi/checks/07-ffi-abs-diff.rs"]
mod tests;
