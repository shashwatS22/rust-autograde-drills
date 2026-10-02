#[derive(Debug, Clone)]
pub struct DiffLine {
    pub line_no: usize,
    pub expected: String,
    pub actual: String,
    pub is_first_diff: bool,
}

#[derive(Debug, Clone)]
pub struct Diff {
    pub lines: Vec<DiffLine>,
    pub truncated: usize,
}

pub fn normalize(s: &str) -> String {
    s.replace("\r\n", "\n")
        .lines()
        .map(str::trim_end)
        .collect::<Vec<_>>()
        .join("\n")
        .trim_end()
        .to_string()
}

pub fn compare(expected: &str, actual: &str) -> bool {
    normalize(expected) == normalize(actual)
}

pub fn build_diff(expected: &str, actual: &str, max_lines: usize) -> Diff {
    let exp_norm = normalize(expected);
    let act_norm = normalize(actual);
    let exp_lines: Vec<&str> = exp_norm.lines().collect();
    let act_lines: Vec<&str> = act_norm.lines().collect();
    let max_len = exp_lines.len().max(act_lines.len());
    let mut first_diff: Option<usize> = None;
    let mut lines = Vec::new();

    for i in 0..max_len {
        let e = exp_lines.get(i).copied().unwrap_or("");
        let a = act_lines.get(i).copied().unwrap_or("");
        if first_diff.is_none() && e != a {
            first_diff = Some(i + 1);
        }
        if lines.len() < max_lines {
            lines.push(DiffLine {
                line_no: i + 1,
                expected: if e.is_empty() {
                    "(nothing)".into()
                } else {
                    e.into()
                },
                actual: if a.is_empty() {
                    "(nothing)".into()
                } else {
                    a.into()
                },
                is_first_diff: first_diff == Some(i + 1),
            });
        }
    }

    let truncated = max_len.saturating_sub(max_lines);
    Diff { lines, truncated }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn exact_match() {
        assert!(compare("a\nb", "a\nb"));
    }

    #[test]
    fn trailing_whitespace() {
        assert!(compare("a  \nb", "a\nb"));
    }

    #[test]
    fn crlf() {
        assert!(compare("a\r\nb", "a\nb"));
    }

    #[test]
    fn trailing_newlines() {
        assert!(compare("a\nb\n\n", "a\nb"));
    }

    #[test]
    fn empty_actual() {
        assert!(!compare("a", ""));
    }

    #[test]
    fn actual_longer() {
        assert!(!compare("a", "a\nextra"));
    }
}
