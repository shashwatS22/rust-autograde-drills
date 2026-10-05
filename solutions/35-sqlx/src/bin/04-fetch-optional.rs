use sqlx::SqlitePool;
async fn maybe_one() -> Result<Option<i64>, sqlx::Error> {
    let pool = sqlx::SqlitePool::connect("sqlite::memory:").await?;
    sqlx::query("CREATE TABLE t (v INTEGER)").execute(&pool).await?;
    let empty: Option<(i64,)> = sqlx::query_as("SELECT v FROM t LIMIT 1").fetch_optional(&pool).await?;
    sqlx::query("INSERT INTO t (v) VALUES (9)").execute(&pool).await?;
    let some: Option<(i64,)> = sqlx::query_as("SELECT v FROM t LIMIT 1").fetch_optional(&pool).await?;
    Ok(some.map(|r| r.0).or(empty.map(|r| r.0)))
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/35-sqlx/checks/04-fetch-optional.rs"]
mod tests;
