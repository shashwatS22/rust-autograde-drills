//! 24-smart-pointers / 04-rc-refcell
//!
//! TASK
//! Implement `rc refcell` as described in the stub.
//!
//! CONCEPT
//! Rc<RefCell<T>> combines shared ownership with interior mutability.
//!
//! SIGNATURE
//! fn combo() -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::rc::Rc;
use std::cell::RefCell;
fn combo() -> i32 {
    todo!()
}

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-rc-refcell.rs"]
mod tests;