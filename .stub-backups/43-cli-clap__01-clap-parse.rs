//! 43-cli-clap / 01-clap-parse
//!
//! TASK
//! Parse `--n` with clap.
//!
//! SIGNATURE
//! fn parse_n(args: &[&str]) -> i32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(long)] n: i32 }
fn parse_n(args: &[&str]) -> i32 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/01-clap-parse.rs"]
mod tests;
