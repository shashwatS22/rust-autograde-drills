//! 42-performance / 01-global-alloc
//!
//! TASK
//! Count allocations with GlobalAlloc.
//!
//! SIGNATURE
//! fn alloc_count() -> usize
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use std::alloc::{GlobalAlloc, Layout, System};
struct Counter;
unsafe impl GlobalAlloc for Counter { unsafe fn alloc(&self, l: Layout) -> *mut u8 { System.alloc(l) } unsafe fn dealloc(&self, p: *mut u8, l: Layout) { System.dealloc(p, l) } }
fn alloc_count() -> usize { 0 }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-global-alloc.rs"]
mod tests;
