//! 43-cli-clap / 02-clap-short-flag
//!
//! TASK
//! Short flag `-c`.
//!
//! SIGNATURE
//! fn parse_count(args: &[&str]) -> u32
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(short = 'c')] count: u32 }
fn parse_count(args: &[&str]) -> u32 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/02-clap-short-flag.rs"]
mod tests;