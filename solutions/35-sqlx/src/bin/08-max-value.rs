use sqlx::SqlitePool;
async fn max_val() -> Result<i32, sqlx::Error> {
    let pool = sqlx::SqlitePool::connect("sqlite::memory:").await?;
    sqlx::query("CREATE TABLE vals (v INTEGER)").execute(&pool).await?;
    for v in [3, 7, 2] { sqlx::query("INSERT INTO vals (v) VALUES (?)").bind(v).execute(&pool).await?; }
    let row: (i32,) = sqlx::query_as("SELECT MAX(v) FROM vals").fetch_one(&pool).await?;
    Ok(row.0)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/35-sqlx/checks/08-max-value.rs"]
mod tests;
