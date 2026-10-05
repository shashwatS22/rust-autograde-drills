"""Exercise bank for phases 3–6 (levels 17–48)."""

from __future__ import annotations

from phases_3_6_common import Exercise, O, T, check_block
from phases_3_6_content_rest import REST_LEVELS


def build_level_17() -> list[Exercise]:
    return [
        T(
            "01-area-trait",
            "Trait `Area` for `Circle`.",
            "fn circle_area(r: f64) -> f64",
            "trait Area { fn area(&self) -> f64; }\nstruct Circle { r: f64 }\nimpl Area for Circle { fn area(&self) -> f64 { todo!() } }\nfn circle_area(r: f64) -> f64 { Circle { r }.area() }",
            "trait Area { fn area(&self) -> f64; }\nstruct Circle { r: f64 }\nimpl Area for Circle { fn area(&self) -> f64 { std::f64::consts::PI * self.r * self.r } }\nfn circle_area(r: f64) -> f64 { Circle { r }.area() }",
            check_block(
                "assert!((circle_area(1.0) - std::f64::consts::PI).abs() < 1e-6);",
                "assert!((circle_area(0.0)).abs() < 1e-9);",
                "assert!(circle_area(2.0) > circle_area(1.0));",
            ),
        ),
        T(
            "02-default-greet",
            "Trait with default method.",
            "fn greeting() -> String",
            "trait Greeter { fn name(&self) -> &str; fn greet(&self) -> String { todo!() } }\nstruct Ada;\nimpl Greeter for Ada { fn name(&self) -> &str { \"Ada\" } }\nfn greeting() -> String { Ada.greet() }",
            "trait Greeter { fn name(&self) -> &str; fn greet(&self) -> String { format!(\"Hello, {}!\", self.name()) } }\nstruct Ada;\nimpl Greeter for Ada { fn name(&self) -> &str { \"Ada\" } }\nfn greeting() -> String { Ada.greet() }",
            "use super::*;\n#[test]\nfn t() { assert_eq!(greeting(), \"Hello, Ada!\"); }",
        ),
        T(
            "03-summary-trait",
            "Trait `Summary` for `Article`.",
            "fn blurb() -> String",
            "struct Article { title: String, author: String }\ntrait Summary { fn summarize(&self) -> String; }\nimpl Summary for Article { fn summarize(&self) -> String { todo!() } }\nfn blurb() -> String { Article { title: \"Rust\".into(), author: \"Ada\".into() }.summarize() }",
            "struct Article { title: String, author: String }\ntrait Summary { fn summarize(&self) -> String; }\nimpl Summary for Article { fn summarize(&self) -> String { format!(\"{} by {}\", self.title, self.author) } }\nfn blurb() -> String { Article { title: \"Rust\".into(), author: \"Ada\".into() }.summarize() }",
            "use super::*;\n#[test]\nfn t() { assert_eq!(blurb(), \"Rust by Ada\"); }",
        ),
        T(
            "04-display-user",
            "Implement `Display` for `User`.",
            "fn format_user() -> String",
            "use std::fmt;\nstruct User { name: String, age: u32 }\nimpl fmt::Display for User { fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result { todo!() } }\nfn format_user() -> String { User { name: \"Riya\".into(), age: 27 }.to_string() }",
            "use std::fmt;\nstruct User { name: String, age: u32 }\nimpl fmt::Display for User { fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result { write!(f, \"{} ({})\", self.name, self.age) } }\nfn format_user() -> String { User { name: \"Riya\".into(), age: 27 }.to_string() }",
            "use super::*;\n#[test]\nfn t() { assert_eq!(format_user(), \"Riya (27)\"); }",
        ),
        O(
            "05-debug-print",
            "Derive `Debug` and print `Point`.",
            "struct Point { x: i32, y: i32 }",
            "#[derive(Debug)]\nstruct Point { x: i32, y: i32 }\nfn main() { println!(\"{:?}\", Point { x: 1, y: 2 }); }",
        ),
        T(
            "06-largest",
            "`largest` with trait bound.",
            "fn largest_i32(v: &[i32]) -> i32",
            "fn largest<T: PartialOrd>(list: &[T]) -> &T { todo!() }\nfn largest_i32(v: &[i32]) -> i32 { *largest(v) }",
            "fn largest<T: PartialOrd>(list: &[T]) -> &T { list.iter().max_by(|a, b| a.partial_cmp(b).unwrap()).unwrap() }\nfn largest_i32(v: &[i32]) -> i32 { *largest(v) }",
            "use super::*;\n#[test]\nfn t() { assert_eq!(largest_i32(&[3, 1, 4]), 4); }",
        ),
        T(
            "07-trait-param",
            "Function taking `impl Summary`.",
            "fn announce(s: &str) -> String",
            "trait Summary { fn summarize(&self) -> String; }\nstruct Note { text: String }\nimpl Summary for Note { fn summarize(&self) -> String { self.text.clone() } }\nfn announce_text(n: &Note) -> String { n.summarize() }\nfn announce(s: &str) -> String { announce_text(&Note { text: s.into() }) }",
            "trait Summary { fn summarize(&self) -> String; }\nstruct Note { text: String }\nimpl Summary for Note { fn summarize(&self) -> String { self.text.clone() } }\nfn announce_text(n: &Note) -> String { n.summarize() }\nfn announce(s: &str) -> String { announce_text(&Note { text: s.into() }) }",
            "use super::*;\n#[test]\nfn t() { assert_eq!(announce(\"hi\"), \"hi\"); }",
        ),
        T(
            "08-partial-eq-trait",
            "Trait `Equals` wrapper.",
            "fn same(a: i32, b: i32) -> bool",
            "trait Equals { fn eq(&self, other: &Self) -> bool; }\nimpl Equals for i32 { fn eq(&self, other: &Self) -> bool { todo!() } }\nfn same(a: i32, b: i32) -> bool { Equals::eq(&a, &b) }",
            "trait Equals { fn eq(&self, other: &Self) -> bool; }\nimpl Equals for i32 { fn eq(&self, other: &Self) -> bool { self == other } }\nfn same(a: i32, b: i32) -> bool { Equals::eq(&a, &b) }",
            "use super::*;\n#[test]\nfn t() { assert!(same(2, 2)); }",
        ),
    ][:8]


ALL_LEVELS: list[tuple[str, int, str]] = [("17-traits", 3, "Traits")] + [
    (lv, ph, title) for lv, ph, title, _ in REST_LEVELS
]

LEVELS_WITH_EXERCISES: list[tuple[str, int, str, list[Exercise]]] = [
    ("17-traits", 3, "Traits", build_level_17()),
] + REST_LEVELS
