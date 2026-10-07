use clap::{CommandFactory, Parser};
#[derive(Parser)]
#[command(name = "mytool")]
struct Cli {}
fn prog_name() -> String { Cli::command().get_name().to_string() }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/43-cli-clap/checks/08-clap-help-name.rs"]
mod tests;
