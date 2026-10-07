use clap::Parser;
#[derive(Parser)]
struct Cli { label: Option<String> }
fn parse_label(args: &[&str]) -> Option<String> { Cli::parse_from(args).label }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/43-cli-clap/checks/06-clap-optional.rs"]
mod tests;
