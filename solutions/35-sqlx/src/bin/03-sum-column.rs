use sqlx::SqlitePool;
async fn sum_nums() -> Result<i64, sqlx::Error> {
    let pool = sqlx::SqlitePool::connect("sqlite::memory:").await?;
    sqlx::query("CREATE TABLE nums (v INTEGER)").execute(&pool).await?;
    for v in [1, 2, 3] { sqlx::query("INSERT INTO nums (v) VALUES (?)").bind(v).execute(&pool).await?; }
    let row: (i64,) = sqlx::query_as("SELECT SUM(v) FROM nums").fetch_one(&pool).await?;
    Ok(row.0)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/35-sqlx/checks/03-sum-column.rs"]
mod tests;
