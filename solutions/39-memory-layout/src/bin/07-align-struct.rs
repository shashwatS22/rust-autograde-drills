fn align_struct() -> usize {
    struct S { x: u64 }
    std::mem::align_of::<S>()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/39-memory-layout/checks/07-align-struct.rs"]
mod tests;
