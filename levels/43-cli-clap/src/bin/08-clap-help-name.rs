//! 43-cli-clap / 08-clap-help-name
//!
//! TASK
//! Program name from `CommandFactory`.
//!
//! SIGNATURE
//! fn prog_name() -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use clap::{CommandFactory, Parser};
#[derive(Parser)]
#[command(name = "mytool")]
struct Cli {}
fn prog_name() -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/08-clap-help-name.rs"]
mod tests;
