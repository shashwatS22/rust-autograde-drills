struct Stack2 { data: [i32; 2], len: usize }
impl Stack2 {
    // INVARIANT: len <= 2 and only slots < len are initialized
    unsafe fn push(&mut self, v: i32) { *self.data.get_unchecked_mut(self.len) = v; self.len += 1; }
    unsafe fn pop(&mut self) -> i32 { self.len -= 1; *self.data.get_unchecked(self.len) }
}
fn stack_ops() -> (i32, i32) {
    let mut s = Stack2 { data: [0, 0], len: 0 };
    unsafe { s.push(1); s.push(2); }
    unsafe { (s.pop(), s.pop()) }
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/40-unsafe/checks/05-unsafe-stack.rs"]
mod tests;
