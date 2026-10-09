#!/usr/bin/env python3
"""Insert //! CONCEPT blocks into exercise headers (levels + .stub-backups)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from concept_header import build_header, patch_header_only  # noqa: E402


def parse_header(text: str) -> tuple[str, str, str, str, bool] | None:
    if not text.startswith("//!"):
        return None
    lines = text.splitlines()
    m = re.match(r"//! (\d{2}-[^/]+) / (\S+)", lines[0])
    if not m:
        return None
    level_dir, name = m.group(1), m.group(2)
    i = 1

    def skip_blank_doc() -> None:
        nonlocal i
        while i < len(lines) and lines[i].strip() == "//!":
            i += 1

    skip_blank_doc()
    if i >= len(lines) or lines[i] != "//! TASK":
        return None
    i += 1
    task_lines: list[str] = []
    while i < len(lines):
        line = lines[i]
        if line.strip() == "//!":
            i += 1
            continue
        if not line.startswith("//! "):
            break
        body = line[4:]
        if body == "CONCEPT":
            i += 1
            while i < len(lines):
                if lines[i].strip() == "//!":
                    i += 1
                    break
                if not lines[i].startswith("//! "):
                    break
                i += 1
            continue
        if body in ("SIGNATURE", "EXPECTED OUTPUT"):
            break
        task_lines.append(body)
        i += 1
    task = " ".join(task_lines).strip()
    skip_blank_doc()
    if i < len(lines) and lines[i] == "//! SIGNATURE":
        test_graded = True
        i += 1
        sig_lines: list[str] = []
        while i < len(lines):
            if lines[i].strip() == "//!":
                break
            if not lines[i].startswith("//! "):
                break
            sig_lines.append(lines[i][4:])
            i += 1
        expected = " ".join(sig_lines).strip()
    elif i < len(lines) and lines[i] == "//! EXPECTED OUTPUT":
        test_graded = False
        i += 1
        exp_lines: list[str] = []
        while i < len(lines):
            if lines[i].strip() == "//!":
                break
            if not lines[i].startswith("//! "):
                break
            exp_lines.append(lines[i][4:])
            i += 1
        expected = "\n".join(exp_lines).strip()
    else:
        return None
    return level_dir, name, task, expected, test_graded


def patch_file(path: Path) -> str | None:
    parsed = parse_header(path.read_text(encoding="utf-8"))
    if not parsed:
        return None
    level_dir, name, task, expected, test_graded = parsed
    header = build_header(level_dir, name, task, expected, test_graded)
    patch_header_only(path, header)
    return level_dir


def main() -> int:
    updated = 0
    for stub in sorted(ROOT.glob("levels/*/src/bin/*.rs")):
        level_dir = patch_file(stub)
        if level_dir:
            updated += 1
            backup = ROOT / ".stub-backups" / f"{level_dir}__{stub.stem}.rs"
            if backup.exists():
                patch_file(backup)
    print(f"Patched headers on {updated} level exercises (backups where present).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
