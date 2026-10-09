"""Build exercise //! headers with optional CONCEPT blocks."""

from __future__ import annotations

from concepts import get_concept


def concept_doc_lines(level_dir: str, name: str) -> list[str]:
    text = get_concept(level_dir, name)
    if not text:
        return []
    out = ["//! CONCEPT"]
    for line in text.strip().split("\n"):
        out.append(f"//! {line.rstrip()}")
    out.append("//!")
    return out


def build_header(
    level_dir: str,
    name: str,
    task: str,
    expected: str,
    test_graded: bool,
) -> list[str]:
    lines = [
        f"//! {level_dir} / {name}",
        "//!",
        "//! TASK",
        f"//! {task}",
        "//!",
    ]
    lines.extend(concept_doc_lines(level_dir, name))
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


def patch_header_only(path, header_lines: list[str]) -> None:
    from pathlib import Path

    path = Path(path)
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
