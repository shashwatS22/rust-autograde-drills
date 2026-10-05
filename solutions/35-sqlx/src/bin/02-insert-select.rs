use sqlx::SqlitePool;
async fn item_name() -> Result<String, sqlx::Error> {
    let pool = sqlx::SqlitePool::connect("sqlite::memory:").await?;
    sqlx::query("CREATE TABLE items (name TEXT)").execute(&pool).await?;
    sqlx::query("INSERT INTO items (name) VALUES (?)").bind("pen").execute(&pool).await?;
    let row: (String,) = sqlx::query_as("SELECT name FROM items WHERE name = ?").bind("pen").fetch_one(&pool).await?;
    Ok(row.0)
}

fn main() {}


// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/35-sqlx/checks/02-insert-select.rs"]
mod tests;
