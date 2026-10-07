use std::mem::MaybeUninit;
fn init_on_stack() -> i32 {
    let mut slot = MaybeUninit::<i32>::uninit();
    // INVARIANT: write once before assume_init
    unsafe { slot.as_mut_ptr().write(42); }
    unsafe { slot.assume_init() }
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/07-maybe-uninit.rs"]
mod tests;
