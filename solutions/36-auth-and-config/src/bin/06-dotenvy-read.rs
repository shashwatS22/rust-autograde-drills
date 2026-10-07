fn load_api_key(config: &str) -> String {
    unsafe { std::env::remove_var("DRILL_API_KEY") };
    dotenvy::from_read(config.as_bytes()).ok();
    std::env::var("DRILL_API_KEY").unwrap_or_default()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/36-auth-and-config/checks/06-dotenvy-read.rs"]
mod tests;
