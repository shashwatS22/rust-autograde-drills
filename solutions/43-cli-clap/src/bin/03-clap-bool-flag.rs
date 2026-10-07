use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(long)] verbose: bool }
fn parse_verbose(args: &[&str]) -> bool { Cli::parse_from(args).verbose }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/43-cli-clap/checks/03-clap-bool-flag.rs"]
mod tests;
