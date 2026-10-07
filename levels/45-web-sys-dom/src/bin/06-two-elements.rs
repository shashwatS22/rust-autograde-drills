//! 45-web-sys-dom / 06-two-elements
//!
//! TASK
//! Create two elements and distinguish tags.
//!
//! SIGNATURE
//! fn tags() -> (String, String)
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
#[derive(Clone, Debug)]
struct MiniNode { tag: String, text: String, children: Vec<usize> }
struct MiniDocument { nodes: Vec<MiniNode> }
impl MiniDocument {
    fn new() -> Self { Self { nodes: Vec::new() } }
    fn create_element(&mut self, tag: &str) -> usize {
        let id = self.nodes.len();
        self.nodes.push(MiniNode { tag: tag.into(), text: String::new(), children: Vec::new() });
        id
    }
    fn set_text_content(&mut self, id: usize, text: &str) { self.nodes[id].text = text.into(); }
    fn append_child(&mut self, parent: usize, child: usize) { self.nodes[parent].children.push(child); }
    fn text_of_first(&self, tag: &str) -> Option<String> {
        self.nodes.iter().find(|n| n.tag == tag).map(|n| n.text.clone())
    }
    fn remove_last_child(&mut self, parent: usize) -> bool { self.nodes[parent].children.pop().is_some() }
}
fn tags() -> (String, String) { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-two-elements.rs"]
mod tests;
