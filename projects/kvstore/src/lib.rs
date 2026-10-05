use std::collections::HashMap;
use std::path::Path;
use std::sync::{Arc, Mutex};

use thiserror::Error;

#[derive(Debug, Error, PartialEq, Eq)]
pub enum StoreError {
    #[error("key not found")]
    NotFound,
    #[error("io error")]
    Io,
}

pub trait KvStore {
    fn get(&self, key: &str) -> Result<Option<String>, StoreError>;
    fn set(&mut self, key: &str, value: &str) -> Result<(), StoreError>;
    fn delete(&mut self, key: &str) -> Result<bool, StoreError>;
}

pub struct MemoryStore {
    map: HashMap<String, String>,
}

impl MemoryStore {
    pub fn new() -> Self {
        Self {
            map: HashMap::new(),
        }
    }
}

impl KvStore for MemoryStore {
    fn get(&self, key: &str) -> Result<Option<String>, StoreError> {
        todo!()
    }

    fn set(&mut self, key: &str, value: &str) -> Result<(), StoreError> {
        todo!()
    }

    fn delete(&mut self, key: &str) -> Result<bool, StoreError> {
        todo!()
    }
}

pub struct FileStore {
    path: std::path::PathBuf,
}

impl FileStore {
    pub fn open(path: impl AsRef<Path>) -> Result<Self, StoreError> {
        todo!()
    }
}

impl KvStore for FileStore {
    fn get(&self, key: &str) -> Result<Option<String>, StoreError> {
        todo!()
    }

    fn set(&mut self, key: &str, value: &str) -> Result<(), StoreError> {
        todo!()
    }

    fn delete(&mut self, key: &str) -> Result<bool, StoreError> {
        todo!()
    }
}

pub struct ThreadSafeStore {
    inner: Arc<Mutex<MemoryStore>>,
}

impl ThreadSafeStore {
    pub fn new() -> Self {
        Self {
            inner: Arc::new(Mutex::new(MemoryStore::new())),
        }
    }
}

impl KvStore for ThreadSafeStore {
    fn get(&self, key: &str) -> Result<Option<String>, StoreError> {
        todo!()
    }

    fn set(&mut self, key: &str, value: &str) -> Result<(), StoreError> {
        todo!()
    }

    fn delete(&mut self, key: &str) -> Result<bool, StoreError> {
        todo!()
    }
}

#[async_trait::async_trait]
pub trait AsyncKvStore {
    async fn get(&self, key: &str) -> Result<Option<String>, StoreError>;
    async fn set(&self, key: &str, value: &str) -> Result<(), StoreError>;
}

pub struct TokioMemoryStore {
    inner: tokio::sync::Mutex<MemoryStore>,
}

impl TokioMemoryStore {
    pub fn new() -> Self {
        Self {
            inner: tokio::sync::Mutex::new(MemoryStore::new()),
        }
    }
}

#[async_trait::async_trait]
impl AsyncKvStore for TokioMemoryStore {
    async fn get(&self, key: &str) -> Result<Option<String>, StoreError> {
        todo!()
    }

    async fn set(&self, key: &str, value: &str) -> Result<(), StoreError> {
        todo!()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[ignore]
    fn memory_roundtrip() {
        let mut s = MemoryStore::new();
        s.set("a", "1").unwrap();
        assert_eq!(s.get("a").unwrap(), Some("1".into()));
        assert!(s.delete("a").unwrap());
        assert_eq!(s.get("a").unwrap(), None);
    }

    #[test]
    #[ignore]
    fn file_persists() {
        let path = std::env::temp_dir().join("kvstore-test.json");
        let mut s = FileStore::open(&path).unwrap();
        s.set("k", "v").unwrap();
        drop(s);
        let s2 = FileStore::open(&path).unwrap();
        assert_eq!(s2.get("k").unwrap(), Some("v".into()));
        let _ = std::fs::remove_file(path);
    }

    #[test]
    #[ignore]
    fn thread_safe_shared() {
        use std::thread;
        let store = Arc::new(Mutex::new(MemoryStore::new()));
        store.lock().unwrap().set("x", "1").unwrap();
        let reader = Arc::clone(&store);
        let handle = thread::spawn(move || reader.lock().unwrap().get("x").unwrap());
        assert_eq!(handle.join().unwrap(), Some("1".into()));
    }

    #[tokio::test]
    #[ignore]
    async fn async_store() {
        let s = TokioMemoryStore::new();
        s.set("z", "9").await.unwrap();
        assert_eq!(s.get("z").await.unwrap(), Some("9".into()));
    }
}
