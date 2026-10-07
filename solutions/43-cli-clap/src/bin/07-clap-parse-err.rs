use clap::Parser;
#[derive(Parser)]
struct Cli { #[arg(long)] n: i32 }
fn bad_args(args: &[&str]) -> bool { Cli::try_parse_from(args).is_err() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/43-cli-clap/checks/07-clap-parse-err.rs"]
mod tests;
