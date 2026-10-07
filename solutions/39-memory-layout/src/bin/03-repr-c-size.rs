fn c_layout() -> usize {
    #[repr(C)]
    struct Pair { a: u8, b: u32 }
    std::mem::size_of::<Pair>()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/39-memory-layout/checks/03-repr-c-size.rs"]
mod tests;
