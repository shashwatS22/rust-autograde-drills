#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
fn add_via_ffi(a: i32, b: i32) -> i32 { unsafe { add_int(a, b) } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/41-ffi/checks/01-ffi-add.rs"]
mod tests;
