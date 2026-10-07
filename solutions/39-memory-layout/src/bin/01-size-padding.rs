fn padded_size() -> usize {
    struct Padded { a: u8, b: u32 }
    std::mem::size_of::<Padded>()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/39-memory-layout/checks/01-size-padding.rs"]
mod tests;
