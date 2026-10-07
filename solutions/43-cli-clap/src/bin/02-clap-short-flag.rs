use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(short = 'c')] count: u32 }
fn parse_count(args: &[&str]) -> u32 { Cli::parse_from(args).count }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/43-cli-clap/checks/02-clap-short-flag.rs"]
mod tests;
