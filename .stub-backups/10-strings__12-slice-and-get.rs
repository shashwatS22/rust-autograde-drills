//! 10-strings / 12-slice-and-get
//!
//! TASK
//! GIVEN `s = "abcdefgh"`. Print `&s[2..5]`, `&s[5..]`, and `s.get(2..5)` with `{:?}`. The README must explain why slicing is by **byte** index and what happens with a non-ASCII string.
//!
//! CONCEPT
//! String indexing uses byte offsets. get(range) returns Option because bad slices would panic with [..].
//!
//! EXPECTED OUTPUT
//! `cde
//! fgh
//! Some("cde")`

fn main() {
    // Your code below
}