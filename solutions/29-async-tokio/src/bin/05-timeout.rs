async fn timeout_fires() -> bool {
    let inner = async {
        tokio::time::sleep(std::time::Duration::from_secs(60)).await;
        1i32
    };
    tokio::time::timeout(std::time::Duration::from_secs(1), inner).await.is_err()
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/29-async-tokio/checks/05-timeout.rs"]
mod tests;
