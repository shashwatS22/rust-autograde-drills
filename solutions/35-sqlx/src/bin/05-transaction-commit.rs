use sqlx::SqlitePool;
async fn tx_count() -> Result<i64, sqlx::Error> {
    let pool = sqlx::SqlitePool::connect("sqlite::memory:").await?;
    sqlx::query("CREATE TABLE pairs (a INTEGER, b INTEGER)").execute(&pool).await?;
    let mut tx = pool.begin().await?;
    sqlx::query("INSERT INTO pairs (a,b) VALUES (1,2)").execute(&mut *tx).await?;
    sqlx::query("INSERT INTO pairs (a,b) VALUES (3,4)").execute(&mut *tx).await?;
    tx.commit().await?;
    let row: (i64,) = sqlx::query_as("SELECT COUNT(*) FROM pairs").fetch_one(&pool).await?;
    Ok(row.0)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/35-sqlx/checks/05-transaction-commit.rs"]
mod tests;
