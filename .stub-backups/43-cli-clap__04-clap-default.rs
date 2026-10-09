//! 43-cli-clap / 04-clap-default
//!
//! TASK
//! Default value for an optional field.
//!
//! SIGNATURE
//! fn parse_port(args: &[&str]) -> u16
//!
//! This exercise is graded by the checks at the bottom of the file, not by
//! printed output. Leave `main` empty.
//!
use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(long, default_value_t = 8080)] port: u16 }
fn parse_port(args: &[&str]) -> u16 { todo!() }

fn main() {}

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../checks/04-clap-default.rs"]
mod tests;