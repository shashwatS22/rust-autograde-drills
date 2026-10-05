use sqlx::SqlitePool;
async fn updated() -> Result<i32, sqlx::Error> {
    let pool = sqlx::SqlitePool::connect("sqlite::memory:").await?;
    sqlx::query("CREATE TABLE scores (n INTEGER)").execute(&pool).await?;
    sqlx::query("INSERT INTO scores (n) VALUES (1)").execute(&pool).await?;
    sqlx::query("UPDATE scores SET n = 10 WHERE n = 1").execute(&pool).await?;
    let row: (i32,) = sqlx::query_as("SELECT n FROM scores").fetch_one(&pool).await?;
    Ok(row.0)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/35-sqlx/checks/07-update-row.rs"]
mod tests;
