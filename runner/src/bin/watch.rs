use anyhow::Result;
use notify_debouncer_full::{new_debouncer, DebounceEventResult};
use runner::config::{find_workspace_root, Config};
use runner::progress::{first_unfinished_before, record};
use runner::report::{banner, progression_blocked, result};
use runner::resolve::Workspace;
use runner::run_one::run;
use std::path::PathBuf;
use std::sync::{Arc, Mutex};
use std::time::Duration;

fn main() -> Result<()> {
    let root = find_workspace_root()?;
    let cfg = Config::load(&root)?;
    let ws = Workspace::new(root.clone());
    banner(&cfg);

    let running = Arc::new(Mutex::new(false));
    let last_level16: Arc<Mutex<Option<String>>> = Arc::new(Mutex::new(None));

    let ws2 = ws.clone();
    let cfg2 = cfg.clone();
    let running2 = running.clone();
    let last16 = last_level16.clone();

    let mut debouncer = new_debouncer(Duration::from_millis(120), None, move |res: DebounceEventResult| {
        let Ok(events) = res else { return };
        let paths: Vec<PathBuf> = events
            .iter()
            .flat_map(|e| e.event.paths.iter().cloned())
            .collect();
        for path in paths {
            if path.to_string_lossy().contains("/target/") {
                continue;
            }
            if path.extension().is_none_or(|e| e != "rs") {
                continue;
            }

            let id = if let Some(id) = ws2.id_from_path(&path) {
                *last16.lock().unwrap() = Some(id.clone());
                id
            } else if let Some(level) = ws2.is_level_non_bin_source(&path) {
                let fallback = ws2
                    .default_regrade_id(&level)
                    .unwrap_or_else(|| format!("{level}/01-inline-module"));
                let guard = last16.lock().unwrap();
                guard.clone().unwrap_or(fallback)
            } else {
                continue;
            };

            if *running2.lock().unwrap() {
                continue;
            }
            *running2.lock().unwrap() = true;

            if cfg2.strict_progression {
                if let Ok(Some(blocker)) = first_unfinished_before(&ws2, &id) {
                    progression_blocked(&id, &blocker);
                    *running2.lock().unwrap() = false;
                    continue;
                }
            }

            match run(&ws2, &cfg2, &id, false) {
                Ok(outcome) => {
                    let _ = record(&ws2.root, &outcome);
                    result(&cfg2, &ws2, &outcome);
                }
                Err(e) => eprintln!("runner error: {e:?}"),
            }
            *running2.lock().unwrap() = false;
        }
    })?;

    debouncer
        .watch(root.join("levels"), notify::RecursiveMode::Recursive)?;

    println!("Watching levels/ — save any exercise to check it.\n");
    loop {
        std::thread::sleep(Duration::from_secs(3600));
    }
}
