#!/usr/bin/env python3
"""Restore Phase 1 exercise //! headers from reference/CURSOR-BUILD-SPEC.md §9."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "reference" / "CURSOR-BUILD-SPEC.md"


def parse_spec() -> list[tuple[str, str, str, str, bool]]:
    text = SPEC.read_text(encoding="utf-8")
    start = text.find("## 9. The exercise bank")
    if start < 0:
        raise SystemExit("§9 not found in spec")
    text = text[start:]
    rows: list[tuple[str, str, str, str, bool]] = []
    level_dir: str | None = None
    for line in text.splitlines():
        m_level = re.match(
            r"^### Level \d+ — `([0-9]{2}-[^`]+)`",
            line,
        )
        if m_level:
            level_dir = m_level.group(1)
            continue
        if not level_dir or not line.startswith("|"):
            continue
        if line.startswith("| #") or line.startswith("|---"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 5:
            continue
        _num, file_cell, task, expected = parts[1:5]
        if not file_cell.startswith("`"):
            continue
        m_file = re.search(r"`([^`]+)`", file_cell)
        if not m_file:
            continue
        name = m_file.group(1).strip()
        test_graded = "[T]" in file_cell or "[T]" in task or expected.strip() in ("checks", "**[T]**", "[T]")
        if test_graded:
            expected = task if task.startswith("`fn") or task.startswith("fn ") else expected
            expected = expected.strip("`")
        elif expected.strip() in ("checks", "**[T]**", "[T]"):
            expected = "→ checks"
        expected = expected.replace("⏎", "\n")
        rows.append((level_dir, name, task, expected, test_graded))
    return rows


def build_header(
    level_dir: str, name: str, task: str, expected: str, test_graded: bool
) -> list[str]:
    lines = [
        f"//! {level_dir} / {name}",
        "//!",
        "//! TASK",
        f"//! {task}",
        "//!",
    ]
    if test_graded:
        sig = expected.split(".", 1)[0] if expected.startswith("fn ") else expected
        lines.extend(
            [
                "//! SIGNATURE",
                f"//! {sig}",
                "//!",
                "//! This exercise is graded by the checks at the bottom of the file, not by",
                "//! printed output. Leave `main` empty.",
                "//!",
            ]
        )
    else:
        lines.append("//! EXPECTED OUTPUT")
        for el in expected.split("\n"):
            lines.append(f"//! {el}")
        lines.append("")
    return lines


def patch_stub(path: Path, header_lines: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("//!"):
        raise SystemExit(f"unexpected stub format: {path}")
    rest_start = 0
    for i, line in enumerate(text.splitlines()):
        if not line.startswith("//!") and line.strip():
            rest_start = i
            break
    else:
        rest_start = len(text.splitlines())
    rest = "\n".join(text.splitlines()[rest_start:])
    if rest and not rest.startswith("\n"):
        rest = "\n" + rest
    path.write_text("\n".join(header_lines) + rest, encoding="utf-8")


def main() -> int:
    rows = parse_spec()
    backup = ROOT / ".stub-backups"
    backup.mkdir(parents=True, exist_ok=True)
    for level_dir, name, task, expected, test_graded in rows:
        stub = ROOT / "levels" / level_dir / "src" / "bin" / f"{name}.rs"
        if not stub.exists():
            print(f"skip missing {stub}")
            continue
        header = build_header(level_dir, name, task, expected, test_graded)
        patch_stub(stub, header)
        dest = backup / f"{level_dir}__{name}.rs"
        shutil.copy2(stub, dest)
    print(f"Updated {len(rows)} Phase 1 stubs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
