//! 43-cli-clap / 05-clap-subcommand
//!
//! TASK
//! Parse a subcommand enum.
//!
//! SIGNATURE
//! fn sub_name(args: &[&str]) -> String
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use clap::{Parser, Subcommand};
#[derive(Parser)]
struct Cli { #[command(subcommand)] cmd: Commands }
#[derive(Subcommand)]
enum Commands { List, Add { id: u32 } }
fn sub_name(args: &[&str]) -> String { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/05-clap-subcommand.rs"]
mod tests;
