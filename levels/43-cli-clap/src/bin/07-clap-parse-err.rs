//! 43-cli-clap / 07-clap-parse-err
//!
//! TASK
//! `try_parse_from` returns `Err` on bad input.
//!
//! SIGNATURE
//! fn bad_args(args: &[&str]) -> bool
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(long)] n: i32 }
fn bad_args(args: &[&str]) -> bool { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/07-clap-parse-err.rs"]
mod tests;
