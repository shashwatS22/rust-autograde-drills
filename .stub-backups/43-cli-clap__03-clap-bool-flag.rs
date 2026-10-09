//! 43-cli-clap / 03-clap-bool-flag
//!
//! TASK
//! Boolean `--verbose` flag.
//!
//! SIGNATURE
//! fn parse_verbose(args: &[&str]) -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(long)] verbose: bool }
fn parse_verbose(args: &[&str]) -> bool { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/03-clap-bool-flag.rs"]
mod tests;