use sqlx::SqlitePool;
async fn after_delete() -> Result<i64, sqlx::Error> {
    let pool = sqlx::SqlitePool::connect("sqlite::memory:").await?;
    sqlx::query("CREATE TABLE ids (id INTEGER)").execute(&pool).await?;
    sqlx::query("INSERT INTO ids (id) VALUES (1),(2)").execute(&pool).await?;
    sqlx::query("DELETE FROM ids WHERE id = 1").execute(&pool).await?;
    let row: (i64,) = sqlx::query_as("SELECT COUNT(*) FROM ids").fetch_one(&pool).await?;
    Ok(row.0)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/35-sqlx/checks/06-delete-row.rs"]
mod tests;
