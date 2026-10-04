#!/usr/bin/env python3
"""Generate scripts/phases_3_6_content.py. Run once before scaffold_phases_3_6.py."""

from __future__ import annotations

import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

OUT = Path(__file__).resolve().parent / "phases_3_6_content.py"


@dataclass
class Exercise:
    name: str
    task: str
    test_graded: bool
    solution: str
    signature: str = ""
    stub_body: str = ""
    check: str | None = None
    given: str = ""
    expected_hint: str = ""


def T(
    name: str,
    task: str,
    signature: str,
    stub_fn: str,
    solution_fn: str,
    check: str,
) -> Exercise:
    return Exercise(
        name=name,
        task=task,
        test_graded=True,
        signature=signature,
        stub_body=stub_fn.strip(),
        solution=solution_fn.strip(),
        check=check.strip(),
    )


def O(name: str, task: str, given: str, solution: str, hint: str = "→ from solution") -> Exercise:
    return Exercise(
        name=name,
        task=task,
        test_graded=False,
        given=given.strip(),
        solution=solution.strip(),
        expected_hint=hint,
    )


def axum_test(check_body: str) -> str:
    return f"""use super::*;
use axum::body::Body;
use axum::http::{{Request, StatusCode}};
use http_body_util::BodyExt;
use tower::ServiceExt;

#[tokio::test]
async fn axum_check() {{
{check_body}
}}
"""


def level_17() -> list[Exercise]:
    return [
        T(
            "01-area-trait",
            "Implement `trait Area` with `area(&self) -> f64` for `Circle {{ r }}`.",
            "fn circle_area(r: f64) -> f64",
            "trait Area { fn area(&self) -> f64; }\nstruct Circle { r: f64 }\nimpl Area for Circle { fn area(&self) -> f64 { todo!() } }\nfn circle_area(r: f64) -> f64 { Circle { r }.area() }",
            "trait Area { fn area(&self) -> f64; }\nstruct Circle { r: f64 }\nimpl Area for Circle { fn area(&self) -> f64 { std::f64::consts::PI * self.r * self.r } }\nfn circle_area(r: f64) -> f64 { Circle { r }.area() }",
            "use super::*;\n#[test]\nfn area() { assert!((circle_area(2.0) - 12.566).abs() < 0.01); }",
        ),
        T(
            "02-default-greet",
            "Trait `Greeter` with default `greet` returning `Hello, name!`. Override only `name`.",
            "fn greeting() -> String",
            "trait Greeter { fn name(&self) -> &str; fn greet(&self) -> String { todo!() } }\nstruct Ada;\nimpl Greeter for Ada { fn name(&self) -> &str { \"Ada\" } }\nfn greeting() -> String { Ada.greet() }",
            "trait Greeter { fn name(&self) -> &str; fn greet(&self) -> String { format!(\"Hello, {}!\", self.name()) } }\nstruct Ada;\nimpl Greeter for Ada { fn name(&self) -> &str { \"Ada\" } }\nfn greeting() -> String { Ada.greet() }",
            "use super::*;\n#[test]\nfn greet() { assert_eq!(greeting(), \"Hello, Ada!\"); }",
        ),
        T(
            "03-summary",
            "Trait `Summary` with `summarize(&self) -> String`. Implement for `Article`.",
            "fn article_blurb() -> String",
            "struct Article { title: String, author: String }\ntrait Summary { fn summarize(&self) -> String; }\nimpl Summary for Article { fn summarize(&self) -> String { todo!() } }\nfn article_blurb() -> String { Article { title: \"Rust\".into(), author: \"Ada\".into() }.summarize() }",
            "struct Article { title: String, author: String }\ntrait Summary { fn summarize(&self) -> String; }\nimpl Summary for Article { fn summarize(&self) -> String { format!(\"{} by {}\", self.title, self.author) } }\nfn article_blurb() -> String { Article { title: \"Rust\".into(), author: \"Ada\".into() }.summarize() }",
            "use super::*;\n#[test]\nfn blurb() { assert_eq!(article_blurb(), \"Rust by Ada\"); }",
        ),
        T(
            "04-display-user",
            "Implement `Display` for `User {{ name, age }}` as `name (age)`.",
            "fn format_user() -> String",
            "use std::fmt;\nstruct User { name: String, age: u32 }\nimpl fmt::Display for User { fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result { todo!() } }\nfn format_user() -> String { User { name: \"Riya\".into(), age: 27 }.to_string() }",
            "use std::fmt;\nstruct User { name: String, age: u32 }\nimpl fmt::Display for User { fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result { write!(f, \"{} ({})\", self.name, self.age) } }\nfn format_user() -> String { User { name: \"Riya\".into(), age: 27 }.to_string() }",
            "use super::*;\n#[test]\nfn user() { assert_eq!(format_user(), \"Riya (27)\"); }",
        ),
        O(
            "05-debug-demo",
            "Derive `Debug` on `Point` and print with `{:?}`.",
            "struct Point { x: i32, y: i32 }",
            "#[derive(Debug)]\nstruct Point { x: i32, y: i32 }\nfn main() { let p = Point { x: 1, y: 2 }; println!(\"{:?}\", p); }",
        ),
        T(
            "06-largest",
            "Generic `largest<T: PartialOrd>(list: &[T]) -> &T`.",
            "fn largest_i32(v: &[i32]) -> i32",
            "fn largest<T: PartialOrd>(list: &[T]) -> &T { todo!() }\nfn largest_i32(v: &[i32]) -> i32 { *largest(v) }",
            "fn largest<T: PartialOrd>(list: &[T]) -> &T { list.iter().max_by(|a, b| a.partial_cmp(b).unwrap()).unwrap() }\nfn largest_i32(v: &[i32]) -> i32 { *largest(v) }",
            "use super::*;\n#[test]\nfn big() { assert_eq!(largest_i32(&[3, 1, 4]), 4); }",
        ),
        T(
            "07-count-chars",
            "Trait `Countable` with `count(&self) -> usize` for `&str`.",
            "fn count_hello() -> usize",
            "trait Countable { fn count(&self) -> usize; }\nimpl Countable for str { fn count(&self) -> usize { todo!() } }\nfn count_hello() -> usize { \"hello\".count() }",
            "trait Countable { fn count(&self) -> usize { self.len() } }\nimpl Countable for str {}\nfn count_hello() -> usize { \"hello\".count() }",
            "use super::*;\n#[test]\nfn c() { assert_eq!(count_hello(), 5); }",
        ),
        T(
            "08-pair-eq",
            "Trait `Same` with `is_same(&self, other: &Self) -> bool` for `i32`.",
            "fn twins(a: i32, b: i32) -> bool",
            "trait Same { fn is_same(&self, other: &Self) -> bool; }\nimpl Same for i32 { fn is_same(&self, other: &Self) -> bool { todo!() } }\nfn twins(a: i32, b: i32) -> bool { a.is_same(&b) }",
            "trait Same { fn is_same(&self, other: &Self) -> bool { self == other } }\nimpl Same for i32 {}\nfn twins(a: i32, b: i32) -> bool { a.is_same(&b) }",
            "use super::*;\n#[test]\nfn t() { assert!(twins(2, 2)); assert!(!twins(1, 2)); }",
        ),
        T(
            "09-named-summary",
            "Associated function `News::preview()` returning title.",
            "fn preview() -> String",
            "struct News { title: String }\nimpl News { fn preview() -> String { todo!() } }\nfn preview() -> String { News::preview() }",
            "struct News { title: String }\nimpl News { fn preview() -> String { \"Rust 2024\".into() } }\nfn preview() -> String { News::preview() }",
            "use super::*;\n#[test]\nfn p() { assert_eq!(preview(), \"Rust 2024\"); }",
        ),
        T(
            "10-outline",
            "Trait `Outline` with `draw(&self) -> String`. Two shapes.",
            "fn draw_all() -> String",
            "trait Outline { fn draw(&self) -> String; }\nstruct Square;\nimpl Outline for Square { fn draw(&self) -> String { todo!() } }\nstruct Circle;\nimpl Outline for Circle { fn draw(&self) -> String { todo!() } }\nfn draw_all() -> String { format!(\"{} {}\", Square.draw(), Circle.draw()) }",
            "trait Outline { fn draw(&self) -> String; }\nstruct Square;\nimpl Outline for Square { fn draw(&self) -> String { \"[]\".into() } }\nstruct Circle;\nimpl Outline for Circle { fn draw(&self) -> String { \"()\".into() } }\nfn draw_all() -> String { format!(\"{} {}\", Square.draw(), Circle.draw()) }",
            "use super::*;\n#[test]\nfn d() { assert_eq!(draw_all(), \"[] ()\"); }",
        ),
        T(
            "11-trait-chain",
            "Trait `Twice` with `twice(&self) -> i32`.",
            "fn double_five() -> i32",
            "trait Twice { fn twice(&self) -> i32; }\nimpl Twice for i32 { fn twice(&self) -> i32 { todo!() } }\nfn double_five() -> i32 { 5.twice() }",
            "trait Twice { fn twice(&self) -> i32 { *self * 2 } }\nimpl Twice for i32 {}\nfn double_five() -> i32 { 5.twice() }",
            "use super::*;\n#[test]\nfn d() { assert_eq!(double_five(), 10); }",
        ),
    ]


# Additional level builders appended below (generated in same file)
LEVEL_BUILDERS: list[tuple[str, int, str, Callable[[], list[Exercise]]]] = [
    ("17-traits", 3, "Traits", level_17),
]
