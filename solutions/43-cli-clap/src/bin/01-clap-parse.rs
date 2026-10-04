use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(long)] n: i32 }
fn parse_n(args: &[&str]) -> i32 { Cli::parse_from(args).n }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/43-cli-clap/checks/01-clap-parse.rs"]
mod tests;
