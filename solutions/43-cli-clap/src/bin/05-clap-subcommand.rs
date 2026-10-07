use clap::{Parser, Subcommand};
#[derive(Parser)]
struct Cli { #[command(subcommand)] cmd: Commands }
#[derive(Subcommand)]
enum Commands { List, Add { id: u32 } }
fn sub_name(args: &[&str]) -> String { match Cli::parse_from(args).cmd { Commands::List => "list".into(), Commands::Add { .. } => "add".into() } }

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/43-cli-clap/checks/05-clap-subcommand.rs"]
mod tests;
