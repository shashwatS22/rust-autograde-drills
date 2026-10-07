use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(long, default_value_t = 8080)] port: u16 }
fn parse_port(args: &[&str]) -> u16 { Cli::parse_from(args).port }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/43-cli-clap/checks/04-clap-default.rs"]
mod tests;
