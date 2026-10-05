use sqlx::SqlitePool;
async fn count_users() -> Result<i64, sqlx::Error> {
    let pool = sqlx::SqlitePool::connect("sqlite::memory:").await?;
    sqlx::query("CREATE TABLE users (id INTEGER)").execute(&pool).await?;
    sqlx::query("INSERT INTO users (id) VALUES (1)").execute(&pool).await?;
    let row: (i64,) = sqlx::query_as("SELECT COUNT(*) FROM users").fetch_one(&pool).await?;
    Ok(row.0)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/35-sqlx/checks/01-sqlite-count.rs"]
mod tests;
