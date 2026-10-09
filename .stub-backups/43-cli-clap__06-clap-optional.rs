//! 43-cli-clap / 06-clap-optional
//!
//! TASK
//! Optional positional argument.
//!
//! SIGNATURE
//! fn parse_label(args: &[&str]) -> Option<String>
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use clap::Parser;
#[derive(Parser)]
struct Cli { label: Option<String> }
fn parse_label(args: &[&str]) -> Option<String> { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/06-clap-optional.rs"]
mod tests;