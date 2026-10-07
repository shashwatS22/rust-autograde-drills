use std::mem::ManuallyDrop;
fn no_double_free() -> String {
    let s = ManuallyDrop::new(String::from("keep"));
    let clone = (*s).clone();
    // INVARIANT: we never drop `s` — only the clone is returned
    clone
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/08-manually-drop.rs"]
mod tests;
