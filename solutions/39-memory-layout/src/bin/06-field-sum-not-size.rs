fn fields_vs_struct() -> (usize, usize) {
    struct S { a: u8, b: u16 }
    (std::mem::size_of_val(&S { a: 0, b: 0 }), std::mem::size_of::<u8>() as usize + std::mem::size_of::<u16>() as usize)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/39-memory-layout/checks/06-field-sum-not-size.rs"]
mod tests;
