#[link(name = "native_add")]
unsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }
type DoubleFn = extern "C" fn(i32) -> i32;
#[unsafe(no_mangle)]
pub extern "C" fn double_in_rust(n: i32) -> i32 { n * 2 }
fn call_rust_double() -> i32 {
    let f: DoubleFn = double_in_rust;
    f(21)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/41-ffi/checks/05-rust-export-c.rs"]
mod tests;
