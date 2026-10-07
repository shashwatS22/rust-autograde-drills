"""Levels 18–48 exercise definitions."""

from __future__ import annotations

from textwrap import dedent

from phases_3_6_common import Exercise, O as _O, T as _T, axum_route_ex as _axum_route_ex, check_block


def _drill(
    level_num: int,
    idx: int,
    topic: str,
    body: str,
    test: str,
    test2: str | None = None,
    test3: str | None = None,
    task: str | None = None,
    contract: str = "",
) -> Exercise:
    name = f"{idx:02d}-{topic}"
    sig_line = next(
        (
            ln
            for ln in body.splitlines()
            if ln.lstrip().startswith(("fn ", "pub fn ", "async fn ", "pub async fn "))
        ),
        "fn value() -> i32",
    )
    sig = sig_line.split("{")[0].strip()
    stub = f"{sig} {{\n    todo!()\n}}"
    if body.strip().startswith(("use ", "#[")):
        rest = body.splitlines()
        fn_i = next(
            i
            for i, ln in enumerate(rest)
            if ln.lstrip().startswith(("fn ", "pub fn ", "async fn ", "pub async fn "))
        )
        prefix = "\n".join(rest[:fn_i])
        fn_sig = rest[fn_i].split("{")[0].strip()
        stub = (prefix + "\n" if prefix else "") + f"{fn_sig} {{\n    todo!()\n}}"
    t2 = test2 if test2 is not None else test
    t3 = test3 if test3 is not None else "assert!(true)"
    async_test = "async fn" in body or ".await" in test or ".await" in (test2 or "")
    check = check_block(test, t2, t3, async_test=async_test)
    desc = task or f"Implement `{topic.replace('-', ' ')}` as described in the stub."
    ex = _T(name, desc, sig, stub, body, check)
    ex.checks_contract = contract or f"{test}; edge via {t3[:40]}"
    return ex


def _eight(exercises: list[Exercise]) -> list[Exercise]:
    return exercises[:8]


def _topics(level: str, stems: list[str]) -> list[str]:
    return stems


def build_18() -> list[Exercise]:
    return [
        _drill(18, 1, "derive-debug", "fn show() -> String {\n    #[derive(Debug)]\n    enum C { Red }\n    format!(\"{:?}\", C::Red)\n}", "assert_eq!(show(), \"Red\")"),
        _drill(18, 2, "derive-clone", "fn cloned() -> i32 {\n    #[derive(Clone, Copy)]\n    struct P { v: i32 }\n    let a = P { v: 3 };\n    a.clone().v\n}", "assert_eq!(cloned(), 3)"),
        _drill(18, 3, "derive-eq", "fn eq_ok() -> bool {\n    #[derive(PartialEq)]\n    struct P { v: i32 }\n    P { v: 1 } == P { v: 1 }\n}", "assert!(eq_ok())"),
        _drill(18, 4, "derive-ord", "fn sorted() -> Vec<i32> {\n    #[derive(Ord, PartialOrd, Eq, PartialEq, Clone)]\n    struct S { v: i32 }\n    let mut v = vec![S { v: 2 }, S { v: 1 }];\n    v.sort();\n    v.into_iter().map(|s| s.v).collect()\n}", "assert_eq!(sorted(), vec![1, 2])"),
        _drill(18, 5, "add-assign", "use std::ops::AddAssign;\nfn bump() -> i32 {\n    struct C { n: i32 }\n    impl AddAssign for C { fn add_assign(&mut self, rhs: Self) { self.n += rhs.n } }\n    let mut c = C { n: 1 };\n    c += C { n: 2 };\n    c.n\n}", "assert_eq!(bump(), 3)"),
        _drill(18, 6, "index-struct", "use std::ops::Index;\nfn second() -> i32 {\n    struct Pair(i32, i32);\n    impl Index<usize> for Pair { type Output = i32; fn index(&self, i: usize) -> &i32 { if i == 0 { &self.0 } else { &self.1 } } }\n    Pair(1, 9)[1]\n}", "assert_eq!(second(), 9)"),
        _drill(
            18,
            7,
            "default-override",
            "struct Config { retries: u32, timeout_ms: u32 }\nimpl Default for Config {\n    fn default() -> Self { Self { retries: 3, timeout_ms: 1000 } }\n}\nfn default_retries() -> u32 { Config::default().retries }",
            "assert_eq!(default_retries(), 3);",
            "assert_eq!(Config::default().timeout_ms, 1000);",
            "assert!(default_retries() > 0);",
            task="Implement `Default` with non-zero field values.",
        ),
        _drill(
            18,
            8,
            "derive-hash",
            "#[derive(Hash, Eq, PartialEq)]\nstruct Key(i32);\nuse std::collections::HashSet;\nfn uniq_keys() -> usize { let s: HashSet<Key> = [Key(1), Key(1), Key(2)].into_iter().collect(); s.len() }",
            "assert_eq!(uniq_keys(), 2);",
            "assert!(uniq_keys() >= 1);",
            "assert_ne!(uniq_keys(), 3);",
            task="Derive `Hash` and collect into a `HashSet`.",
        ),
        _drill(18, 9, "bitand", "fn mask() -> u8 { 0b1100u8 & 0b1010u8 }", "assert_eq!(mask(), 0b1000)"),
        _drill(18, 10, "default", "fn age() -> u32 {\n    #[derive(Default)]\n    struct P { age: u32 }\n    P::default().age\n}", "assert_eq!(age(), 0)"),
        _drill(18, 11, "hash-set", "use std::collections::HashSet;\nfn uniq() -> usize {\n    let s: HashSet<i32> = [1, 1, 2].into_iter().collect();\n    s.len()\n}", "assert_eq!(uniq(), 2)"),
    ]


def build_19() -> list[Exercise]:
    return [
        _drill(19, i, t, b, c)
        for i, t, b, c in [
            (1, "generic-max", "fn max_i32(a: i32, b: i32) -> i32 { if a > b { a } else { b } }", "assert_eq!(max_i32(1, 4), 4)"),
            (2, "generic-min", "fn min_i32(a: i32, b: i32) -> i32 { if a < b { a } else { b } }", "assert_eq!(min_i32(4, 1), 1)"),
            (3, "pair", "struct Pair<T>(pub T, pub T);\nfn first() -> i32 { Pair(7, 8).0 }", "assert_eq!(first(), 7)"),
            (4, "identity", "fn id<T>(x: T) -> T { x }\nfn id_i32() -> i32 { id(5) }", "assert_eq!(id_i32(), 5)"),
            (5, "swap", "fn swap<T>(a: T, b: T) -> (T, T) { (b, a) }\nfn swapped() -> (i32, i32) { swap(1, 2) }", "assert_eq!(swapped(), (2, 1))"),
            (6, "count", "fn count<T>(v: &[T]) -> usize { v.len() }\nfn three() -> usize { count(&[1, 2, 3]) }", "assert_eq!(three(), 3)"),
            (7, "first", "fn first<T: Copy>(v: &[T]) -> Option<T> { v.first().copied() }\nfn got() -> i32 { first(&[9, 1]).unwrap() }", "assert_eq!(got(), 9)"),
            (
                8,
                "where-clause",
                "fn largest<T>(a: T, b: T) -> T\nwhere\n    T: PartialOrd,\n{\n    if a > b { a } else { b }\n}\nfn pick() -> i32 { largest(3, 9) }",
                "assert_eq!(pick(), 9);",
            ),
            (9, "collect", "fn doubled() -> Vec<i32> { vec![1, 2].into_iter().map(|x| x * 2).collect() }", "assert_eq!(doubled(), vec![2, 4])"),
            (10, "option-map", "fn inc() -> Option<i32> { Some(2).map(|x| x + 1) }", "assert_eq!(inc(), Some(3))"),
            (11, "result-map", "fn ok() -> Result<i32, ()> { Ok(3).map(|x| x + 1) }", "assert_eq!(ok(), Ok(4))"),
        ]
    ]


def build_20() -> list[Exercise]:
    return [
        _T(
            "01-trait-object",
            "Return `Box<dyn Displayable>`.",
            "fn boxed() -> String",
            "trait Displayable { fn show(&self) -> String; }\nstruct Item { t: String }\nimpl Displayable for Item { fn show(&self) -> String { self.t.clone() } }\nfn boxed() -> String { let b: Box<dyn Displayable> = Box::new(Item { t: \"hi\".into() }); b.show() }",
            "trait Displayable { fn show(&self) -> String; }\nstruct Item { t: String }\nimpl Displayable for Item { fn show(&self) -> String { self.t.clone() } }\nfn boxed() -> String { let b: Box<dyn Displayable> = Box::new(Item { t: \"hi\".into() }); b.show() }",
            "use super::*;\n#[test]\nfn t() { assert_eq!(boxed(), \"hi\"); }",
        ),
        _drill(20, 2, "vec-dyn", "trait Draw { fn draw(&self) -> char; }\nstruct A;\nimpl Draw for A { fn draw(&self) -> char { 'A' } }\nfn chars() -> String { let v: Vec<Box<dyn Draw>> = vec![Box::new(A)]; v.iter().map(|d| d.draw()).collect() }", "assert_eq!(chars(), \"A\")"),
        _drill(20, 3, "impl-trait-arg", "trait Speak { fn speak(&self) -> &str; }\nstruct Dog;\nimpl Speak for Dog { fn speak(&self) -> &str { \"woof\" } }\nfn talk(s: &dyn Speak) -> &str { s.speak() }\nfn dog() -> &'static str { talk(&Dog) }", "assert_eq!(dog(), \"woof\")"),
        _drill(
            20,
            4,
            "return-impl",
            "trait Greet { fn hi(&self) -> String; }\nstruct User { name: String }\nimpl Greet for User { fn hi(&self) -> String { format!(\"Hi {}\", self.name) } }\nfn make_greeter() -> impl Greet { User { name: \"Ada\".into() } }\nfn greet() -> String { make_greeter().hi() }",
            "assert_eq!(greet(), \"Hi Ada\");",
            "assert!(greet().contains(\"Ada\"));",
            "assert!(!greet().is_empty());",
            task="Return `impl Greet` from a factory function.",
        ),
        _drill(20, 5, "enum-dispatch", "enum Pet { Cat, Dog }\nfn sound(p: Pet) -> &'static str { match p { Pet::Cat => \"meow\", Pet::Dog => \"woof\" } }\nfn cat() -> &'static str { sound(Pet::Cat) }", "assert_eq!(cat(), \"meow\")"),
        _drill(20, 6, "count-dyn", "trait Id { fn id(&self) -> u32; }\nstruct X(u32);\nimpl Id for X { fn id(&self) -> u32 { self.0 } }\nfn sum(v: &[Box<dyn Id>]) -> u32 { v.iter().map(|x| x.id()).sum() }\nfn two() -> u32 { sum(&[Box::new(X(1)), Box::new(X(2))]) }", "assert_eq!(two(), 3)"),
        _drill(20, 7, "filter-trait", "trait Even { fn is_even(&self) -> bool; }\nimpl Even for i32 { fn is_even(&self) -> bool { *self % 2 == 0 } }\nfn count(v: &[i32]) -> usize { v.iter().filter(|x| x.is_even()).count() }\nfn evens() -> usize { count(&[1, 2, 3, 4]) }", "assert_eq!(evens(), 2)"),
        _drill(20, 8, "box-string", "fn boxed_str() -> String { (*Box::new(\"rust\".to_string())).clone() }", "assert_eq!(boxed_str(), \"rust\")"),
        _drill(20, 9, "clone-dyn", "trait Cloneable: Clone { fn val(&self) -> i32; }\n#[derive(Clone)]\nstruct N(i32);\nimpl Cloneable for N { fn val(&self) -> i32 { self.0 } }\nfn dup(n: &N) -> i32 { n.clone().val() }\nfn v() -> i32 { dup(&N(4)) }", "assert_eq!(v(), 4)"),
        _drill(20, 10, "sort-area", "trait Area { fn area(&self) -> i32; }\nstruct S { s: i32 }\nimpl Area for S { fn area(&self) -> i32 { self.s * self.s } }\nfn biggest(v: &[S]) -> i32 { v.iter().map(|s| s.area()).max().unwrap() }", "assert_eq!(biggest(&[S { s: 2 }, S { s: 3 }]), 9)"),
        _drill(20, 11, "mixed-vec", "fn mix() -> usize { let v: Vec<Box<dyn std::fmt::Debug>> = vec![Box::new(1i32), Box::new(\"a\")]; v.len() }", "assert_eq!(mix(), 2)"),
    ]


def build_21() -> list[Exercise]:
    return [
        _drill(21, 1, "longest", "fn longest<'a>(a: &'a str, b: &'a str) -> &'a str { if a.len() > b.len() { a } else { b } }\nfn pick() -> &'static str { longest(\"hi\", \"hello\") }", "assert_eq!(pick(), \"hello\")"),
        _drill(21, 2, "struct-ref", "struct Ex<'a> { s: &'a str }\nfn first_word(s: &str) -> Ex { Ex { s: s.split_whitespace().next().unwrap_or(\"\") } }\nfn w() -> &'static str { first_word(\"rust lang\").s }", "assert_eq!(w(), \"rust\")"),
        _drill(21, 3, "explicit", "fn identity<'a>(x: &'a str) -> &'a str { x }\nfn id() -> &'static str { identity(\"ok\") }", "assert_eq!(id(), \"ok\")"),
        _drill(21, 4, "static-str", "fn msg() -> &'static str { \"static\" }", "assert_eq!(msg(), \"static\")"),
        _drill(21, 5, "elision", "fn first(s: &str) -> &str { &s[0..1] }\nfn f() -> &'static str { first(\"abc\") }", "assert_eq!(f(), \"a\")"),
        _drill(21, 6, "method", "struct S<'a> { t: &'a str }\nimpl<'a> S<'a> { fn get(&self) -> &str { self.t } }\nfn g() -> &'static str { S { t: \"x\" }.get() }", "assert_eq!(g(), \"x\")"),
        _drill(21, 7, "both-refs", "fn both<'a>(a: &'a str, b: &'a str) -> (&'a str, &'a str) { (a, b) }\nfn p() -> (&'static str, &'static str) { both(\"a\", \"b\") }", "assert_eq!(p().0, \"a\")"),
        _drill(21, 8, "outlives", "fn choose<'a>(flag: bool, a: &'a str, b: &'a str) -> &'a str { if flag { a } else { b } }\nfn c() -> &'static str { choose(true, \"y\", \"n\") }", "assert_eq!(c(), \"y\")"),
        _drill(21, 9, "struct-field", "struct Holder { value: i32 }\nfn get() -> i32 { Holder { value: 5 }.value }", "assert_eq!(get(), 5)"),
        _drill(21, 10, "slice", "fn head(s: &str) -> &str { &s[..2] }\nfn h() -> &'static str { head(\"rust\") }", "assert_eq!(h(), \"ru\")"),
        _O("11-lifetime-demo", "Print two string lengths.", "let a = \"short\";\nlet b = \"longer\";", "fn main() {\n    let a = \"short\";\n    let b = \"longer\";\n    println!(\"{} {}\", a.len(), b.len());\n}"),
    ]


def build_22() -> list[Exercise]:
    return [
        _drill(22, 1, "from-into", "struct Wrapper(i32);\nimpl From<i32> for Wrapper { fn from(v: i32) -> Self { Wrapper(v) } }\nfn wrap() -> i32 { Wrapper::from(3).0 }", "assert_eq!(wrap(), 3)"),
        _drill(22, 2, "into", "struct Meters(u32);\nimpl From<u32> for Meters { fn from(v: u32) -> Self { Meters(v) } }\nfn m() -> u32 { let m: Meters = 5.into(); m.0 }", "assert_eq!(m(), 5)"),
        _drill(22, 3, "try-from", "fn parse() -> Result<i32, std::num::TryFromIntError> { i32::try_from(42i64) }", "assert_eq!(parse(), Ok(42))"),
        _drill(22, 4, "as-ref", "fn len(s: impl AsRef<str>) -> usize { s.as_ref().len() }\nfn l() -> usize { len(\"abc\") }", "assert_eq!(l(), 3)"),
        _drill(22, 5, "deref-coerce", "use std::ops::Deref;\nstruct S(String);\nimpl Deref for S { type Target = str; fn deref(&self) -> &str { &self.0 } }\nfn upper(s: &str) -> String { s.to_uppercase() }\nfn u() -> String { upper(&S(\"hi\".into())) }", "assert_eq!(u(), \"HI\")"),
        _drill(22, 6, "to-string", "fn s() -> String { 42.to_string() }", "assert_eq!(s(), \"42\")"),
        _drill(22, 7, "parse", "fn p() -> i32 { \"7\".parse().unwrap() }", "assert_eq!(p(), 7)"),
        _drill(22, 8, "try-parse", "fn bad() -> Result<i32, ()> { \"x\".parse::<i32>().map_err(|_| ()) }", "assert!(bad().is_err())"),
        _drill(22, 9, "collect-str", "fn joined() -> String { [\"a\", \"b\"].iter().cloned().collect::<String>() }", "assert_eq!(joined(), \"ab\")"),
        _drill(22, 10, "from-str", "use std::str::FromStr;\nfn froms() -> i32 { i32::from_str(\"9\").unwrap() }", "assert_eq!(froms(), 9)"),
        _O("11-conversions-demo", "Print `From`/`Into` example.", "", "fn main() {\n    let s: String = \"hi\".into();\n    println!(\"{}\", s);\n}"),
    ]


def build_23() -> list[Exercise]:
    return [
        _drill(23, 1, "iter-sum", "fn sum(v: &[i32]) -> i32 { v.iter().sum() }\nfn ten() -> i32 { sum(&[1, 2, 3, 4]) }", "assert_eq!(ten(), 10)"),
        _drill(23, 2, "map-collect", "fn double(v: &[i32]) -> Vec<i32> { v.iter().map(|x| x * 2).collect() }\nfn d() -> Vec<i32> { double(&[1, 2]) }", "assert_eq!(d(), vec![2, 4])"),
        _drill(23, 3, "filter", "fn evens(v: &[i32]) -> Vec<i32> { v.iter().filter(|x| *x % 2 == 0).copied().collect() }\nfn e() -> Vec<i32> { evens(&[1, 2, 3, 4]) }", "assert_eq!(e(), vec![2, 4])"),
        _drill(23, 4, "fold", "fn fold_sum(v: &[i32]) -> i32 { v.iter().fold(0, |a, b| a + *b) }\nfn f() -> i32 { fold_sum(&[1, 2, 3]) }", "assert_eq!(f(), 6)"),
        _drill(23, 5, "find", "fn find(v: &[i32]) -> Option<i32> { v.iter().copied().find(|x| *x > 2) }\nfn g() -> Option<i32> { find(&[1, 3, 2]) }", "assert_eq!(g(), Some(3))"),
        _drill(23, 6, "any-all", "fn all_pos(v: &[i32]) -> bool { v.iter().all(|x| *x > 0) }\nfn a() -> bool { all_pos(&[1, 2]) }", "assert!(a())"),
        _drill(
            23,
            7,
            "custom-iter",
            "struct Counter { n: u32 }\nimpl Iterator for Counter { type Item = u32; fn next(&mut self) -> Option<Self::Item> { if self.n < 3 { let c = self.n; self.n += 1; Some(c) } else { None } } }\nfn collect_counter() -> Vec<u32> { Counter { n: 0 }.collect() }",
            "assert_eq!(collect_counter(), vec![0, 1, 2]);",
            "assert_eq!(collect_counter().len(), 3);",
            "assert_eq!(collect_counter()[0], 0);",
            task="Implement `Iterator` by hand for a small counter.",
        ),
        _drill(
            23,
            8,
            "collect-result",
            "fn parse_all(v: &[&str]) -> Result<Vec<i32>, std::num::ParseIntError> { v.iter().map(|s| s.parse()).collect() }\nfn ok() -> Result<Vec<i32>, std::num::ParseIntError> { parse_all(&[\"1\", \"2\"]) }\nfn bad() -> Result<Vec<i32>, std::num::ParseIntError> { parse_all(&[\"1\", \"x\"]) }",
            "assert_eq!(ok(), Ok(vec![1, 2]));",
            "assert!(bad().is_err());",
            "assert_eq!(ok().unwrap().len(), 2);",
            task="Use `collect` to build a `Result<Vec<_>, _>`.",
        ),
        _drill(23, 9, "enumerate", "fn idx() -> usize { [\"a\", \"b\"].iter().enumerate().find(|(i, _)| *i == 1).map(|(_, s)| s.len()).unwrap_or(0) }", "assert_eq!(idx(), 1)"),
        _drill(23, 10, "custom-iter", "struct Counter { n: u32 }\nimpl Iterator for Counter { type Item = u32; fn next(&mut self) -> Option<Self::Item> { if self.n < 3 { let c = self.n; self.n += 1; Some(c) } else { None } } }\nfn collect() -> Vec<u32> { Counter { n: 0 }.collect() }", "assert_eq!(collect(), vec![0, 1, 2])"),
        _drill(23, 11, "collect-result", "fn parse_all(v: &[&str]) -> Result<Vec<i32>, std::num::ParseIntError> { v.iter().map(|s| s.parse()).collect() }\nfn ok() -> Result<Vec<i32>, std::num::ParseIntError> { parse_all(&[\"1\", \"2\"]) }", "assert_eq!(ok(), Ok(vec![1, 2]))"),
    ]


def build_24() -> list[Exercise]:
    return [
        _drill(24, 1, "box-heap", "fn boxed() -> i32 { let b = Box::new(5); *b }", "assert_eq!(boxed(), 5)"),
        _drill(24, 2, "rc-share", "use std::rc::Rc;\nfn shared() -> i32 { let a = Rc::new(3); let b = Rc::clone(&a); *a + *b }", "assert_eq!(shared(), 6)"),
        _drill(24, 3, "refcell", "use std::cell::RefCell;\nfn mutate() -> i32 { let c = RefCell::new(1); *c.borrow_mut() += 2; *c.borrow() }", "assert_eq!(mutate(), 3)"),
        _drill(24, 4, "rc-refcell", "use std::rc::Rc;\nuse std::cell::RefCell;\nfn combo() -> i32 { let v = Rc::new(RefCell::new(2)); *v.borrow() * 2 }", "assert_eq!(combo(), 4)"),
        _drill(24, 5, "box-recursive", "enum List { Cons(i32, Box<List>), Nil }\nfn head() -> i32 { match List::Cons(1, Box::new(List::Nil)) { List::Cons(h, _) => h, List::Nil => 0 } }", "assert_eq!(head(), 1)"),
        _drill(24, 6, "deref-box", "use std::ops::Deref;\nfn len() -> usize { Box::new(\"abc\".to_string()).len() }", "assert_eq!(len(), 3)"),
        _drill(24, 7, "cow", "use std::borrow::Cow;\nfn cow() -> usize { Cow::from(\"hi\").len() }", "assert_eq!(cow(), 2)"),
        _drill(24, 8, "weak-count", "use std::rc::{Rc, Weak};\nfn weak() -> bool { let r = Rc::new(1); let w: Weak<_> = Rc::downgrade(&r); w.upgrade().is_some() }", "assert!(weak())"),
        _drill(24, 9, "cell", "use std::cell::Cell;\nfn cell() -> i32 { let c = Cell::new(1); c.set(4); c.get() }", "assert_eq!(cell(), 4)"),
        _O("10-smart-ptr-demo", "Print box value.", "let b = Box::new(42);", "fn main() {\n    let b = Box::new(42);\n    println!(\"{}\", *b);\n}"),
        _drill(24, 11, "drop-order", "struct D(i32);\nimpl Drop for D { fn drop(&mut self) {} }\nfn val() -> i32 { D(7).0 }", "assert_eq!(val(), 7)"),
    ]


def build_25() -> list[Exercise]:
    return [
        _T(
            "01-thiserror",
            "Define `AppError` with thiserror.",
            "fn parse_port(s: &str) -> Result<u16, AppError>",
            "use thiserror::Error;\n#[derive(Debug, Error)]\nenum AppError { #[error(\"bad port\")] BadPort }\nfn parse_port(s: &str) -> Result<u16, AppError> { s.parse().map_err(|_| AppError::BadPort) }",
            "use thiserror::Error;\n#[derive(Debug, Error)]\nenum AppError { #[error(\"bad port\")] BadPort }\nfn parse_port(s: &str) -> Result<u16, AppError> { s.parse().map_err(|_| AppError::BadPort) }",
            "use super::*;\n#[test]\nfn t() { assert!(parse_port(\"80\").is_ok()); assert!(parse_port(\"x\").is_err()); }",
        ),
        _T(
            "02-anyhow",
            "Use anyhow::Result.",
            "fn read_num(s: &str) -> anyhow::Result<i32>",
            "fn read_num(s: &str) -> anyhow::Result<i32> { todo!() }",
            "fn read_num(s: &str) -> anyhow::Result<i32> { Ok(s.parse()?)}",
            "use super::*;\n#[test]\nfn t() { assert_eq!(read_num(\"3\").unwrap(), 3); }",
        ),
        _drill(25, 3, "map-err", "fn wrap(s: &str) -> Result<i32, String> { s.parse::<i32>().map_err(|e| e.to_string()) }\nfn w() -> Result<i32, String> { wrap(\"2\") }", "assert_eq!(w(), Ok(2))"),
        _drill(25, 4, "context", "use anyhow::Context;\nfn ctx(s: &str) -> anyhow::Result<i32> { s.parse().context(\"parse\") }\nfn c() -> anyhow::Result<i32> { ctx(\"1\") }", "assert_eq!(c().unwrap(), 1)"),
        _drill(25, 5, "source-chain", "use std::error::Error;\nfn err() -> Box<dyn Error> { Box::new(std::io::Error::new(std::io::ErrorKind::Other, \"x\")) }\nfn has() -> bool { err().source().is_none() }", "assert!(has())"),
        _drill(25, 6, "display-err", "use thiserror::Error;\n#[derive(Error, Debug)]\n#[error(\"code {0}\")]\nstruct E(u32);\nfn msg() -> String { E(5).to_string() }", "assert_eq!(msg(), \"code 5\")"),
        _drill(25, 7, "question", "fn div(a: i32, b: i32) -> Result<i32, &'static str> { if b == 0 { Err(\"zero\") } else { Ok(a / b) } }\nfn d() -> Result<i32, &'static str> { div(10, 2) }", "assert_eq!(d(), Ok(5))"),
        _drill(25, 8, "combine", "fn both(a: Result<i32, ()>, b: Result<i32, ()>) -> Result<i32, ()> { a.and_then(|x| b.map(|y| x + y)) }\nfn b() -> Result<i32, ()> { both(Ok(1), Ok(2)) }", "assert_eq!(b(), Ok(3))"),
        _drill(25, 9, "option-ok", "fn opt() -> Option<i32> { Some(1).and_then(|x| Some(x + 1)) }", "assert_eq!(opt(), Some(2))"),
        _drill(25, 10, "from-err", "fn from() -> Result<(), std::num::ParseIntError> { \"1\".parse::<i32>().map(|_| ()) }", "assert!(from().is_ok())"),
        _O("11-error-demo", "Print Result with anyhow.", "", "fn main() {\n    let r: anyhow::Result<i32> = Ok(1);\n    println!(\"{:?}\", r);\n}"),
    ]


def build_26() -> list[Exercise]:
    return [
        _T(
            "01-assert-eq",
            "Function graded with `assert_eq!` in checks.",
            "pub fn add(a: i32, b: i32) -> i32",
            "pub fn add(a: i32, b: i32) -> i32 { todo!() }",
            "pub fn add(a: i32, b: i32) -> i32 { a + b }",
            check_block("assert_eq!(add(1, 2), 3);", "assert_eq!(add(0, 0), 0);", "assert_eq!(add(-1, 1), 0);"),
        ),
        _T(
            "02-assert-bool",
            "Use `assert!` on a predicate.",
            "pub fn is_positive(n: i32) -> bool",
            "pub fn is_positive(n: i32) -> bool { todo!() }",
            "pub fn is_positive(n: i32) -> bool { n > 0 }",
            check_block("assert!(is_positive(3));", "assert!(!is_positive(0));", "assert!(!is_positive(-2));"),
        ),
        _T(
            "03-assert-ne",
            "Use `assert_ne!` for inequality.",
            "pub fn not_zero(n: i32) -> bool",
            "pub fn not_zero(n: i32) -> bool { todo!() }",
            "pub fn not_zero(n: i32) -> bool { n != 0 }",
            check_block("assert_ne!(not_zero(1), false);", "assert_eq!(not_zero(0), false);", "assert!(not_zero(5));"),
        ),
        _T(
            "04-should-panic",
            "Function that panics on invalid input; check uses `catch_unwind`.",
            "pub fn divide(a: i32, b: i32) -> i32",
            "pub fn divide(a: i32, b: i32) -> i32 { todo!() }",
            "pub fn divide(a: i32, b: i32) -> i32 { if b == 0 { panic!(\"zero\"); } a / b }",
            check_block(
                "assert_eq!(divide(10, 2), 5);",
                "assert!(std::panic::catch_unwind(|| divide(1, 0)).is_err());",
                "assert_eq!(divide(9, 3), 3);",
            ),
        ),
        _T(
            "05-test-module",
            "Keep helpers in a private module, expose one function.",
            "pub fn sq() -> i32",
            "mod math { pub fn sq(x: i32) -> i32 { todo!() } }\npub fn sq() -> i32 { math::sq(3) }",
            "mod math { pub fn sq(x: i32) -> i32 { x * x } }\npub fn sq() -> i32 { math::sq(3) }",
            check_block("assert_eq!(sq(), 9);", "assert_eq!(sq(), 3 * 3);", "assert_ne!(sq(), 8);"),
        ),
        _T(
            "06-result-ok",
            "Return `Result` and test with `is_ok` / `unwrap`.",
            "pub fn parse_one(s: &str) -> Result<i32, ()>",
            "pub fn parse_one(s: &str) -> Result<i32, ()> { todo!() }",
            "pub fn parse_one(s: &str) -> Result<i32, ()> { s.parse().map_err(|_| ()) }",
            check_block(
                "assert_eq!(parse_one(\"7\").unwrap(), 7);",
                "assert!(parse_one(\"x\").is_err());",
                "assert!(parse_one(\"0\").is_ok());",
            ),
        ),
        _T(
            "07-doc-comment",
            "Document a public API with `///` (rustdoc reads it).",
            "pub fn triple(x: i32) -> i32",
            "/// Returns three times `x`.\npub fn triple(x: i32) -> i32 { todo!() }",
            "/// Returns three times `x`.\npub fn triple(x: i32) -> i32 { x * 3 }",
            check_block("assert_eq!(triple(2), 6);", "assert_eq!(triple(0), 0);", "assert_eq!(triple(-1), -3);"),
        ),
        _T(
            "08-test-helper",
            "Combine assertions in one graded test.",
            "pub fn greet(name: &str) -> String",
            "pub fn greet(name: &str) -> String { todo!() }",
            "pub fn greet(name: &str) -> String { format!(\"Hello, {name}!\") }",
            check_block(
                "assert_eq!(greet(\"Ada\"), \"Hello, Ada!\");",
                "assert!(greet(\"x\").starts_with(\"Hello\"));",
                "assert!(greet(\"\").ends_with('!'));",
            ),
        ),
    ]


def build_27() -> list[Exercise]:
    return [
        _drill(27, 1, "spawn-join", "use std::thread;\nfn doubled() -> i32 { let h = thread::spawn(|| 21); h.join().unwrap() * 2 }", "assert_eq!(doubled(), 42)"),
        _drill(27, 2, "move-closure", "use std::thread;\nfn moved() -> i32 { let v = vec![1, 2]; let h = thread::spawn(move || v.len()); h.join().unwrap() as i32 }", "assert_eq!(moved(), 2)"),
        _drill(27, 3, "scoped", "fn sum() -> i32 { std::thread::scope(|s| { let h = s.spawn(|| 3); h.join().unwrap() }) }", "assert_eq!(sum(), 3)"),
        _drill(27, 4, "sleep-ms", "use std::thread;\nuse std::time::Duration;\nfn ok() -> bool { thread::sleep(Duration::from_millis(1)); true }", "assert!(ok())"),
        _drill(27, 5, "yield", "fn ids() -> usize { std::thread::available_parallelism().map(|n| n.get()).unwrap_or(1).max(1) }", "assert!(ids() >= 1)"),
        _drill(27, 6, "panic-catch", "fn caught() -> bool { std::panic::catch_unwind(|| panic!(\"x\")).is_err() }", "assert!(caught())"),
        _drill(27, 7, "thread-name", "fn named() -> bool { std::thread::Builder::new().name(\"t\".into()).spawn(|| 1).unwrap().join().unwrap() == 1 }", "assert!(named())"),
        _drill(
            27,
            8,
            "atomic-two-threads",
            "use std::sync::atomic::{AtomicUsize, Ordering};\nuse std::sync::Arc;\nuse std::thread;\nfn two_thread_inc() -> usize {\n    let c = Arc::new(AtomicUsize::new(0));\n    let a = Arc::clone(&c);\n    let b = Arc::clone(&c);\n    let h1 = thread::spawn(move || { a.fetch_add(1, Ordering::SeqCst); });\n    let h2 = thread::spawn(move || { b.fetch_add(1, Ordering::SeqCst); });\n    h1.join().unwrap();\n    h2.join().unwrap();\n    c.load(Ordering::SeqCst)\n}",
            "assert_eq!(two_thread_inc(), 2);",
            "assert!(two_thread_inc() >= 2);",
            "assert_ne!(two_thread_inc(), 0);",
            task="Increment an `AtomicUsize` from two threads.",
        ),
        _drill(27, 9, "atomic-inc", "use std::sync::atomic::{AtomicUsize, Ordering};\nfn inc() -> usize { let a = AtomicUsize::new(0); a.fetch_add(1, Ordering::SeqCst); a.load(Ordering::SeqCst) }", "assert_eq!(inc(), 1)"),
        _O("10-thread-demo", "Spawn thread printing id.", "", "use std::thread;\nfn main() { let _ = thread::spawn(|| println!(\"thread\")).join(); }"),
        _drill(27, 11, "join-all", "use std::thread;\nfn total() -> i32 { let hs = vec![thread::spawn(|| 1), thread::spawn(|| 2)]; hs.into_iter().map(|h| h.join().unwrap()).sum() }", "assert_eq!(total(), 3)"),
    ]


def build_28() -> list[Exercise]:
    return [
        _drill(28, 1, "mpsc", "use std::sync::mpsc;\nfn send_recv() -> i32 { let (tx, rx) = mpsc::channel(); tx.send(5).unwrap(); rx.recv().unwrap() }", "assert_eq!(send_recv(), 5)"),
        _drill(28, 2, "arc-mutex", "use std::sync::{Arc, Mutex};\nuse std::thread;\nfn shared() -> i32 { let m = Arc::new(Mutex::new(0)); let mut h = vec![]; for _ in 0..2 { let c = Arc::clone(&m); h.push(thread::spawn(move || { *c.lock().unwrap() += 1; })); } for j in h { j.join().unwrap(); } *m.lock().unwrap() }", "assert_eq!(shared(), 2)"),
        _drill(28, 3, "condvar", "use std::sync::{Arc, Mutex, Condvar};\nfn signal() -> i32 { let pair = Arc::new((Mutex::new(false), Condvar::new())); let (lock, cv) = &*pair; let mut started = lock.lock().unwrap(); *started = true; cv.notify_one(); 1 }", "assert_eq!(signal(), 1)"),
        _drill(28, 4, "barrier", "use std::sync::{Arc, Barrier};\nuse std::thread;\nfn wait() -> usize { let b = Arc::new(Barrier::new(2)); let b2 = Arc::clone(&b); let h = thread::spawn(move || { b2.wait(); 1 }); b.wait(); h.join().unwrap() }", "assert_eq!(wait(), 1)"),
        _drill(28, 5, "rwlock", "use std::sync::RwLock;\nfn read() -> i32 { let l = RwLock::new(3); *l.read().unwrap() }", "assert_eq!(read(), 3)"),
        _drill(28, 6, "once", "use std::sync::OnceLock;\nfn once() -> &'static str { static O: OnceLock<String> = OnceLock::new(); O.get_or_init(|| \"ok\".into()) }", "assert_eq!(once(), \"ok\")"),
        _drill(28, 7, "try-lock", "use std::sync::Mutex;\nfn tryl() -> bool { let m = Mutex::new(1); m.try_lock().is_ok() }", "assert!(tryl())"),
        _drill(
            28,
            8,
            "arc-cross-thread",
            "use std::sync::Arc;\nuse std::thread;\nfn arc_value() -> i32 {\n    let v = Arc::new(42i32);\n    let c = Arc::clone(&v);\n    let h = thread::spawn(move || *c);\n    h.join().unwrap()\n}",
            "assert_eq!(arc_value(), 42);",
            "assert!(arc_value() > 0);",
            "assert_ne!(arc_value(), 0);",
            task="Share `Arc<i32>` with another thread (requires `Send + Sync`).",
        ),
        _drill(28, 9, "sync-bound", "fn is_sync<T: Sync>() -> bool { true }\nfn s() -> bool { is_sync::<i32>() }", "assert!(s())"),
        _O("10-channel-demo", "Print channel result.", "", "use std::sync::mpsc;\nfn main() { let (tx, rx) = mpsc::channel(); tx.send(1).unwrap(); println!(\"{}\", rx.recv().unwrap()); }"),
        _drill(28, 11, "drop-sender", "use std::sync::mpsc;\nfn closed() -> bool { let (tx, rx) = mpsc::channel::<i32>(); drop(tx); rx.recv().is_err() }", "assert!(closed())"),
    ]


def build_29() -> list[Exercise]:
    return [
        _T(
            "01-async-fn",
            "Async fn returning 7.",
            "async fn seven() -> i32",
            "async fn seven() -> i32 { todo!() }",
            "async fn seven() -> i32 { 7 }",
            "use super::*;\n#[tokio::test]\nasync fn t() { assert_eq!(seven().await, 7); }",
        ),
        _T(
            "02-sleep-pause",
            "Use tokio::time::pause in test.",
            "async fn delayed() -> i32",
            "async fn delayed() -> i32 { tokio::time::sleep(std::time::Duration::from_secs(60)).await; 1 }",
            "async fn delayed() -> i32 { tokio::time::sleep(std::time::Duration::from_secs(60)).await; 1 }",
            "use super::*;\n#[tokio::test]\nasync fn t() { tokio::time::pause(); let h = tokio::spawn(delayed()); tokio::time::advance(std::time::Duration::from_secs(60)).await; assert_eq!(h.await.unwrap(), 1); }",
        ),
        _drill(29, 3, "join", "async fn both() -> (i32, i32) { tokio::join!(async { 1 }, async { 2 }) }", "assert_eq!(both().await, (1, 2))"),
        _drill(29, 4, "spawn", "async fn spawned() -> i32 { let h = tokio::spawn(async { 4 }); h.await.unwrap() }", "assert_eq!(spawned().await, 4)"),
        _T(
            "05-timeout",
            "Use `tokio::time::timeout`; test with `pause` + `advance`.",
            "async fn timeout_fires() -> bool",
            "async fn timeout_fires() -> bool { todo!() }",
            "async fn timeout_fires() -> bool {\n    let inner = async {\n        tokio::time::sleep(std::time::Duration::from_secs(60)).await;\n        1i32\n    };\n    tokio::time::timeout(std::time::Duration::from_secs(1), inner).await.is_err()\n}",
            check_block(
                "tokio::time::pause();",
                "let h = tokio::spawn(timeout_fires());",
                "tokio::time::advance(std::time::Duration::from_secs(1)).await;",
                "assert!(h.await.unwrap());",
                async_test=True,
            ),
        ),
        _drill(29, 6, "select", "async fn pick() -> i32 { tokio::select! { v = async { 1 } => v, } }", "assert_eq!(pick().await, 1)"),
        _drill(29, 7, "block-on", "fn sync() -> i32 { tokio::runtime::Runtime::new().unwrap().block_on(async { 3 }) }", "assert_eq!(sync(), 3)"),
        _drill(29, 8, "channel", "async fn chan() -> i32 { let (tx, mut rx) = tokio::sync::mpsc::channel(1); tx.send(9).await.unwrap(); rx.recv().await.unwrap() }", "assert_eq!(chan().await, 9)"),
        _drill(29, 9, "mutex", "async fn lock() -> i32 { let m = tokio::sync::Mutex::new(5); *m.lock().await }", "assert_eq!(lock().await, 5)"),
        _O("10-async-demo", "Block on async print.", "", "fn main() { tokio::runtime::Runtime::new().unwrap().block_on(async { println!(\"async\"); }); }"),
        _drill(29, 11, "interval", "async fn once() -> u32 { 1 }", "assert_eq!(once().await, 1)"),
    ]


# Phase 4 — serde (distinct attributes per exercise)
def build_30() -> list[Exercise]:
    return [
        _T(
            "01-json-roundtrip",
            "Derive Serialize/Deserialize and round-trip JSON.",
            "fn round() -> String",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize, PartialEq, Debug)]\nstruct User { name: String }\nfn round() -> String { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize, PartialEq, Debug)]\nstruct User { name: String }\nfn round() -> String { let u = User { name: \"a\".into() }; serde_json::to_string(&u).unwrap() }",
            check_block(
                "assert_eq!(round(), r#\"{\"name\":\"a\"}\"#);",
                "let back: User = serde_json::from_str(&round()).unwrap();",
                "assert_eq!(back.name, \"a\");",
            ),
        ),
        _T(
            "02-rename-field",
            "Use `#[serde(rename = \"...\")]` on one field.",
            "fn json_key() -> String",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct User { #[serde(rename = \"user_name\")] name: String }\nfn json_key() -> String { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct User { #[serde(rename = \"user_name\")] name: String }\nfn json_key() -> String { serde_json::to_string(&User { name: \"x\".into() }).unwrap() }",
            check_block(
                "assert!(json_key().contains(\"user_name\"));",
                "assert!(!json_key().contains(\"\\\"name\\\"\"));",
                "assert_eq!(serde_json::from_str::<User>(&json_key()).unwrap().name, \"x\");",
            ),
        ),
        _T(
            "03-rename-all",
            "Use `#[serde(rename_all = \"camelCase\")]`.",
            "fn camel() -> String",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\n#[serde(rename_all = \"camelCase\")]\nstruct User { first_name: String }\nfn camel() -> String { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\n#[serde(rename_all = \"camelCase\")]\nstruct User { first_name: String }\nfn camel() -> String { serde_json::to_string(&User { first_name: \"a\".into() }).unwrap() }",
            check_block(
                "assert!(camel().contains(\"firstName\"));",
                "assert!(!camel().contains(\"first_name\"));",
                "assert_eq!(serde_json::from_str::<User>(&camel()).unwrap().first_name, \"a\");",
            ),
        ),
        _T(
            "04-option-absent",
            "Deserialize missing optional field as `None`.",
            "fn nick() -> Option<String>",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct User { name: String, nick: Option<String> }\nfn nick() -> Option<String> { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct User { name: String, nick: Option<String> }\nfn nick() -> Option<String> { serde_json::from_str::<User>(r#\"{\"name\":\"a\"}\"#).unwrap().nick }",
            check_block(
                "assert_eq!(nick(), None);",
                "let with: User = serde_json::from_str(r#\"{\"name\":\"a\",\"nick\":\"z\"}\"#).unwrap();",
                "assert_eq!(with.nick.as_deref(), Some(\"z\"));",
            ),
        ),
        _T(
            "05-vec-json",
            "Serialize a `Vec` field.",
            "fn tags_len() -> usize",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct Post { tags: Vec<String> }\nfn tags_len() -> usize { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct Post { tags: Vec<String> }\nfn tags_len() -> usize { serde_json::from_str::<Post>(\"{\\\"tags\\\":[\\\"a\\\",\\\"b\\\"]}\").unwrap().tags.len() }",
            check_block("assert_eq!(tags_len(), 2);", "assert_eq!(tags_len(), 2);", "assert!(tags_len() > 0);"),
        ),
        _T(
            "06-enum-json",
            "Externally tagged enum in JSON.",
            "fn kind() -> String",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize, Debug, PartialEq)]\nenum Msg { Ping, Pong }\nfn kind() -> String { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize, Debug, PartialEq)]\nenum Msg { Ping, Pong }\nfn kind() -> String { serde_json::to_string(&Msg::Ping).unwrap() }",
            check_block(
                "assert!(kind().contains(\"Ping\"));",
                "let pong = serde_json::to_string(&Msg::Pong).unwrap();",
                "assert_eq!(serde_json::from_str::<Msg>(&pong).unwrap(), Msg::Pong);",
            ),
        ),
        _T(
            "07-default-field",
            "Fill missing fields with `#[serde(default)]`.",
            "fn score_default() -> u32",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct Score { #[serde(default)] points: u32 }\nfn score_default() -> u32 { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct Score { #[serde(default)] points: u32 }\nfn score_default() -> u32 { serde_json::from_str::<Score>(\"{}\").unwrap().points }",
            check_block("assert_eq!(score_default(), 0);", "assert_eq!(score_default(), 0);", "assert!(score_default() == 0);"),
        ),
        _T(
            "08-deny-unknown",
            "Reject unknown JSON keys with `deny_unknown_fields`.",
            "fn strict_err() -> bool",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\n#[serde(deny_unknown_fields)]\nstruct User { name: String }\nfn strict_err() -> bool { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\n#[serde(deny_unknown_fields)]\nstruct User { name: String }\nfn strict_err() -> bool { serde_json::from_str::<User>(r#\"{\"name\":\"a\",\"extra\":1}\"#).is_err() }",
            check_block(
                "assert!(strict_err());",
                "assert!(serde_json::from_str::<User>(r#\"{\"name\":\"a\"}\"#).is_ok());",
                "assert!(strict_err());",
            ),
        ),
    ]


def build_31() -> list[Exercise]:
    routes = [
        ("01-root-ok", "/", "ok"),
        ("02-health", "/health", "healthy"),
        ("03-ping", "/ping", "pong"),
        ("04-api", "/api", "api"),
        ("05-v1", "/v1", "v1"),
        ("06-nested", "/nested", "n"),
        ("07-fallback", "/any", "fallback"),
        ("08-method-get", "/get", "ok"),
    ]
    return [_axum_route_ex(name, path, body) for name, path, body in routes]


def build_32() -> list[Exercise]:
    ax = """
use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode};
use http_body_util::BodyExt;
use tower::ServiceExt;
"""
    return [
        _T(
            "01-path-id",
            "Extract `{id}` with `Path`.",
            "fn app() -> axum::Router",
            "use axum::{extract::Path, routing::get, Router};\nasync fn user(Path(id): Path<u32>) -> String { todo!() }\npub fn app() -> Router { Router::new().route(\"/users/{id}\", get(user)) }\nfn main() {}",
            "use axum::{extract::Path, routing::get, Router};\nasync fn user(Path(id): Path<u32>) -> String { id.to_string() }\npub fn app() -> Router { Router::new().route(\"/users/{id}\", get(user)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/users/42\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::OK);\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"42\");\n}",
        ),
        _T(
            "02-query-page",
            "Extract query string with `Query`.",
            "fn app() -> axum::Router",
            "use axum::{extract::Query, routing::get, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct Q { page: u32 }\nasync fn list(Query(q): Query<Q>) -> String { todo!() }\npub fn app() -> Router { Router::new().route(\"/list\", get(list)) }\nfn main() {}",
            "use axum::{extract::Query, routing::get, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct Q { page: u32 }\nasync fn list(Query(q): Query<Q>) -> String { q.page.to_string() }\npub fn app() -> Router { Router::new().route(\"/list\", get(list)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/list?page=3\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"3\");\n}",
        ),
        _T(
            "03-json-body",
            "Parse JSON body with `Json`.",
            "fn app() -> axum::Router",
            "use axum::{routing::post, Json, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct In { n: i32 }\nasync fn handler(Json(b): Json<In>) -> String { todo!() }\npub fn app() -> Router { Router::new().route(\"/\", post(handler)) }\nfn main() {}",
            "use axum::{routing::post, Json, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct In { n: i32 }\nasync fn handler(Json(b): Json<In>) -> String { b.n.to_string() }\npub fn app() -> Router { Router::new().route(\"/\", post(handler)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().method(\"POST\").uri(\"/\").header(\"content-type\", \"application/json\").body(Body::from(\"{\\\"n\\\":7}\")).unwrap()).await.unwrap();\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"7\");\n}",
        ),
        _T(
            "04-json-bad",
            "Invalid JSON yields 400 Bad Request.",
            "fn app() -> axum::Router",
            "use axum::{routing::post, Json, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct In { n: i32 }\nasync fn handler(Json(_): Json<In>) -> &'static str { \"ok\" }\npub fn app() -> Router { Router::new().route(\"/\", post(handler)) }\nfn main() {}",
            "use axum::{routing::post, Json, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct In { n: i32 }\nasync fn handler(Json(_): Json<In>) -> &'static str { \"ok\" }\npub fn app() -> Router { Router::new().route(\"/\", post(handler)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().method(\"POST\").uri(\"/\").header(\"content-type\", \"application/json\").body(Body::from(\"not-json\")).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::BAD_REQUEST);\n}",
        ),
        _T(
            "05-state-counter",
            "Share handler state with `State`.",
            "fn app() -> axum::Router",
            "use axum::{extract::State, routing::get, Router};\nuse std::sync::Arc;\nasync fn count(State(n): State<Arc<i32>>) -> String { todo!() }\npub fn app() -> Router { Router::new().route(\"/\", get(count)).with_state(Arc::new(5i32)) }\nfn main() {}",
            "use axum::{extract::State, routing::get, Router};\nuse std::sync::Arc;\nasync fn count(State(n): State<Arc<i32>>) -> String { n.to_string() }\npub fn app() -> Router { Router::new().route(\"/\", get(count)).with_state(Arc::new(5i32)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"5\");\n}",
        ),
        _T(
            "06-header-map",
            "Read a request header.",
            "fn app() -> axum::Router",
            "use axum::{http::HeaderMap, routing::get, Router};\nasync fn echo(headers: HeaderMap) -> String { todo!() }\npub fn app() -> Router { Router::new().route(\"/\", get(echo)) }\nfn main() {}",
            "use axum::{http::HeaderMap, routing::get, Router};\nasync fn echo(headers: HeaderMap) -> String { headers.get(\"x-token\").and_then(|v| v.to_str().ok()).unwrap_or(\"\").into() }\npub fn app() -> Router { Router::new().route(\"/\", get(echo)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/\").header(\"x-token\", \"abc\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"abc\");\n}",
        ),
        _T(
            "07-missing-field",
            "Missing JSON field yields 422.",
            "fn app() -> axum::Router",
            "use axum::{routing::post, Json, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct In { n: i32, m: i32 }\nasync fn handler(Json(_): Json<In>) -> &'static str { \"ok\" }\npub fn app() -> Router { Router::new().route(\"/\", post(handler)) }\nfn main() {}",
            "use axum::{routing::post, Json, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct In { n: i32, m: i32 }\nasync fn handler(Json(_): Json<In>) -> &'static str { \"ok\" }\npub fn app() -> Router { Router::new().route(\"/\", post(handler)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().method(\"POST\").uri(\"/\").header(\"content-type\", \"application/json\").body(Body::from(\"{\\\"n\\\":1}\")).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::UNPROCESSABLE_ENTITY);\n}",
        ),
        _T(
            "08-path-and-query",
            "Combine `Path` and `Query`.",
            "fn app() -> axum::Router",
            "use axum::{extract::{Path, Query}, routing::get, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct Q { verbose: bool }\nasync fn show(Path(id): Path<u32>, Query(q): Query<Q>) -> String { todo!() }\npub fn app() -> Router { Router::new().route(\"/items/{id}\", get(show)) }\nfn main() {}",
            "use axum::{extract::{Path, Query}, routing::get, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct Q { verbose: bool }\nasync fn show(Path(id): Path<u32>, Query(q): Query<Q>) -> String { format!(\"{}:{}\", id, q.verbose) }\npub fn app() -> Router { Router::new().route(\"/items/{id}\", get(show)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/items/9?verbose=true\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"9:true\");\n}",
        ),
    ]


def build_33() -> list[Exercise]:
    err_enum = dedent(
        """
        use axum::http::StatusCode;
        use axum::response::{IntoResponse, Response};

        #[derive(Debug)]
        enum AppError {
            NotFound,
            BadRequest,
        }

        impl IntoResponse for AppError {
            fn into_response(self) -> Response {
                match self {
                    AppError::NotFound => (StatusCode::NOT_FOUND, "not found").into_response(),
                    AppError::BadRequest => (StatusCode::BAD_REQUEST, "bad request").into_response(),
                }
            }
        }
        """
    ).strip()
    ax = """
use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode};
use http_body_util::BodyExt;
use tower::ServiceExt;
"""
    return [
        _T(
            "01-not-found",
            "Return `AppError::NotFound` as 404 via `IntoResponse`.",
            "fn app() -> axum::Router",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn missing() -> Result<&'static str, AppError> {{ Err(AppError::NotFound) }}\npub fn app() -> Router {{ todo!() }}\nfn main() {{}}",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn missing() -> Result<&'static str, AppError> {{ Err(AppError::NotFound) }}\npub fn app() -> Router {{ Router::new().route(\"/missing\", get(missing)) }}\nfn main() {{}}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/missing\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::NOT_FOUND);\n}",
        ),
        _T(
            "02-bad-request",
            "Return `AppError::BadRequest` as 400.",
            "fn app() -> axum::Router",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn bad() -> Result<&'static str, AppError> {{ Err(AppError::BadRequest) }}\npub fn app() -> Router {{ todo!() }}\nfn main() {{}}",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn bad() -> Result<&'static str, AppError> {{ Err(AppError::BadRequest) }}\npub fn app() -> Router {{ Router::new().route(\"/bad\", get(bad)) }}\nfn main() {{}}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/bad\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::BAD_REQUEST);\n}",
        ),
        _T(
            "03-ok-route",
            "Return `Ok` from a `Result` handler (200).",
            "fn app() -> axum::Router",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn ok() -> Result<&'static str, AppError> {{ Ok(\"ok\") }}\npub fn app() -> Router {{ todo!() }}\nfn main() {{}}",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn ok() -> Result<&'static str, AppError> {{ Ok(\"ok\") }}\npub fn app() -> Router {{ Router::new().route(\"/ok\", get(ok)) }}\nfn main() {{}}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/ok\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::OK);\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"ok\");\n}",
        ),
        _T(
            "04-status-only",
            "Use `(StatusCode, &str)` as `IntoResponse` without a custom enum.",
            "fn app() -> axum::Router",
            "use axum::{http::StatusCode, response::IntoResponse, routing::get, Router};\nasync fn gone() -> impl IntoResponse { todo!() }\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{http::StatusCode, response::IntoResponse, routing::get, Router};\nasync fn gone() -> impl IntoResponse { (StatusCode::GONE, \"gone\") }\npub fn app() -> Router { Router::new().route(\"/gone\", get(gone)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/gone\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::GONE);\n}",
        ),
        _T(
            "05-json-error-body",
            "Return JSON error body with `(StatusCode, Json<_>)`.",
            "fn app() -> axum::Router",
            "use axum::{http::StatusCode, response::IntoResponse, routing::get, Json, Router};\nuse serde::Serialize;\n#[derive(Serialize)]\nstruct ErrBody { msg: &'static str }\nasync fn fail() -> impl IntoResponse { todo!() }\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{http::StatusCode, response::IntoResponse, routing::get, Json, Router};\nuse serde::Serialize;\n#[derive(Serialize)]\nstruct ErrBody { msg: &'static str }\nasync fn fail() -> impl IntoResponse { (StatusCode::UNPROCESSABLE_ENTITY, Json(ErrBody { msg: \"nope\" })) }\npub fn app() -> Router { Router::new().route(\"/fail\", get(fail)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/fail\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::UNPROCESSABLE_ENTITY);\n    assert!(r.into_body().collect().await.unwrap().to_bytes().windows(4).any(|w| w == b\"nope\"));\n}",
        ),
        _T(
            "06-branch-error",
            "Pick error variant from a path parameter.",
            "fn app() -> axum::Router",
            f"{err_enum}\nuse axum::{{extract::Path, routing::get, Router}};\nasync fn pick(Path(code): Path<u16>) -> Result<&'static str, AppError> {{ todo!() }}\npub fn app() -> Router {{ todo!() }}\nfn main() {{}}",
            f"{err_enum}\nuse axum::{{extract::Path, routing::get, Router}};\nasync fn pick(Path(code): Path<u16>) -> Result<&'static str, AppError> {{\n    if code == 404 {{ Err(AppError::NotFound) }} else if code == 400 {{ Err(AppError::BadRequest) }} else {{ Ok(\"fine\") }}\n}}\npub fn app() -> Router {{ Router::new().route(\"/code/{{code}}\", get(pick)) }}\nfn main() {{}}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/code/404\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::NOT_FOUND);\n}",
        ),
        _T(
            "07-empty-body-404",
            "404 response body is readable in tests.",
            "fn app() -> axum::Router",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn nowhere() -> Result<(), AppError> {{ Err(AppError::NotFound) }}\npub fn app() -> Router {{ todo!() }}\nfn main() {{}}",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn nowhere() -> Result<(), AppError> {{ Err(AppError::NotFound) }}\npub fn app() -> Router {{ Router::new().route(\"/\", get(nowhere)) }}\nfn main() {{}}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::NOT_FOUND);\n    assert!(!r.into_body().collect().await.unwrap().to_bytes().is_empty());\n}",
        ),
        _T(
            "08-map-to-response",
            "Map `Result` to response with `match` and `into_response()`.",
            "fn app() -> axum::Router",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn wrapped(flag: bool) -> axum::response::Response {{\n    let r: Result<&str, AppError> = if flag {{ Ok(\"yes\") }} else {{ Err(AppError::BadRequest) }};\n    todo!()\n}}\npub fn app() -> Router {{ todo!() }}\nfn main() {{}}",
            f"{err_enum}\nuse axum::{{routing::get, Router}};\nasync fn wrapped(flag: bool) -> axum::response::Response {{\n    let r: Result<&str, AppError> = if flag {{ Ok(\"yes\") }} else {{ Err(AppError::BadRequest) }};\n    match r {{ Ok(v) => v.into_response(), Err(e) => e.into_response() }}\n}}\nasync fn yes() -> axum::response::Response {{ wrapped(true).await }}\npub fn app() -> Router {{ Router::new().route(\"/yes\", get(yes)) }}\nfn main() {{}}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/yes\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::OK);\n}",
        ),
    ]


def build_34() -> list[Exercise]:
    ax = """
use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode, HeaderValue};
use http_body_util::BodyExt;
use tower::ServiceExt;
"""
    return [
        _T(
            "01-response-header-layer",
            "Add a response header with `tower::util::MapResponseLayer`.",
            "fn app() -> axum::Router",
            "use axum::{routing::get, Router};\nuse tower::util::MapResponseLayer;\nuse axum::response::Response;\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{routing::get, Router};\nuse tower::util::MapResponseLayer;\nuse axum::response::Response;\nuse axum::http::HeaderValue;\npub fn app() -> Router {\n    Router::new().route(\"/\", get(|| async { \"hi\" })).layer(MapResponseLayer::new(|mut res: Response| {\n        res.headers_mut().insert(\"x-drill\", HeaderValue::from_static(\"1\"));\n        res\n    }))\n}\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.headers().get(\"x-drill\").unwrap(), \"1\");\n}",
        ),
        _T(
            "02-cors-allow-origin",
            "Allow any origin with `tower_http::cors::CorsLayer`.",
            "fn app() -> axum::Router",
            "use axum::{routing::get, Router};\nuse tower_http::cors::{Any, CorsLayer};\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{routing::get, Router};\nuse tower_http::cors::{Any, CorsLayer};\npub fn app() -> Router {\n    Router::new().route(\"/\", get(|| async { \"ok\" })).layer(CorsLayer::new().allow_origin(Any))\n}\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/\").header(\"origin\", \"http://example.com\").body(Body::empty()).unwrap()).await.unwrap();\n    assert!(r.headers().get(\"access-control-allow-origin\").is_some());\n}",
        ),
        _T(
            "03-cors-preflight",
            "Answer an OPTIONS preflight with CORS headers.",
            "fn app() -> axum::Router",
            "use axum::{routing::get, Router};\nuse tower_http::cors::{Any, CorsLayer};\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{routing::get, Router};\nuse tower_http::cors::{Any, CorsLayer};\npub fn app() -> Router {\n    Router::new().route(\"/\", get(|| async { \"ok\" })).layer(CorsLayer::new().allow_origin(Any).allow_methods(Any))\n}\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().method(\"OPTIONS\").uri(\"/\").header(\"origin\", \"http://a.com\").header(\"access-control-request-method\", \"GET\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.status(), StatusCode::OK);\n    assert!(r.headers().get(\"access-control-allow-origin\").is_some());\n}",
        ),
        _T(
            "04-trace-layer",
            "Wrap the router with `tower_http::trace::TraceLayer`.",
            "fn app() -> axum::Router",
            "use axum::{routing::get, Router};\nuse tower_http::trace::TraceLayer;\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{routing::get, Router};\nuse tower_http::trace::TraceLayer;\npub fn app() -> Router {\n    Router::new().route(\"/ping\", get(|| async { \"pong\" })).layer(TraceLayer::new_for_http())\n}\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/ping\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"pong\");\n}",
        ),
        _T(
            "05-tracing-span",
            "Enter a `tracing` span inside a handler.",
            "fn app() -> axum::Router",
            "use axum::{routing::get, Router};\nasync fn traced() -> &'static str { todo!() }\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{routing::get, Router};\nasync fn traced() -> &'static str {\n    let span = tracing::info_span!(\"handler\", item = \"book\");\n    let _enter = span.enter();\n    \"traced\"\n}\npub fn app() -> Router { Router::new().route(\"/\", get(traced)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"traced\");\n}",
        ),
        _T(
            "06-layer-stack",
            "Stack CORS and a custom response header layer.",
            "fn app() -> axum::Router",
            "use axum::{routing::get, Router};\nuse tower::util::MapResponseLayer;\nuse tower_http::cors::{Any, CorsLayer};\nuse axum::response::Response;\nuse axum::http::HeaderValue;\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{routing::get, Router};\nuse tower::util::MapResponseLayer;\nuse tower_http::cors::{Any, CorsLayer};\nuse axum::response::Response;\nuse axum::http::HeaderValue;\npub fn app() -> Router {\n    Router::new().route(\"/\", get(|| async { \"x\" }))\n        .layer(CorsLayer::new().allow_origin(Any))\n        .layer(MapResponseLayer::new(|mut res: Response| { res.headers_mut().insert(\"x-stack\", HeaderValue::from_static(\"yes\")); res }))\n}\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/\").header(\"origin\", \"http://b.com\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.headers().get(\"x-stack\").unwrap(), \"yes\");\n}",
        ),
        _T(
            "07-request-id-header",
            "Echo `x-request-id` after layers are applied.",
            "fn app() -> axum::Router",
            "use axum::{http::HeaderMap, routing::get, Router};\nasync fn echo(headers: HeaderMap) -> String { todo!() }\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{http::HeaderMap, routing::get, Router};\nasync fn echo(headers: HeaderMap) -> String { headers.get(\"x-request-id\").and_then(|v| v.to_str().ok()).unwrap_or(\"\").into() }\npub fn app() -> Router { Router::new().route(\"/\", get(echo)) }\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/\").header(\"x-request-id\", \"abc-9\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.into_body().collect().await.unwrap().to_bytes(), \"abc-9\");\n}",
        ),
        _T(
            "08-nest-with-layer",
            "Nest a router and apply a layer only to the nested routes.",
            "fn app() -> axum::Router",
            "use axum::{routing::get, Router};\nuse tower::util::MapResponseLayer;\nuse axum::response::Response;\nuse axum::http::HeaderValue;\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{routing::get, Router};\nuse tower::util::MapResponseLayer;\nuse axum::response::Response;\nuse axum::http::HeaderValue;\npub fn app() -> Router {\n    let api = Router::new().route(\"/inner\", get(|| async { \"in\" })).layer(MapResponseLayer::new(|mut res: Response| {\n        res.headers_mut().insert(\"x-nested\", HeaderValue::from_static(\"1\")); res\n    }));\n    Router::new().nest(\"/api\", api)\n}\nfn main() {}",
            ax
            + "#[tokio::test]\nasync fn graded() {\n    let r = app().oneshot(Request::builder().uri(\"/api/inner\").body(Body::empty()).unwrap()).await.unwrap();\n    assert_eq!(r.headers().get(\"x-nested\").unwrap(), \"1\");\n}",
        ),
    ]


def build_35() -> list[Exercise]:
    async_pool = "let pool = sqlx::SqlitePool::connect(\"sqlite::memory:\").await?;"
    return [
        _T(
            "01-sqlite-count",
            "Create an in-memory SQLite table `users`, insert one row, and return `COUNT(*)`.",
            "async fn count_users() -> Result<i64, sqlx::Error>",
            "use sqlx::SqlitePool;\nasync fn count_users() -> Result<i64, sqlx::Error> { todo!() }",
            f"use sqlx::SqlitePool;\nasync fn count_users() -> Result<i64, sqlx::Error> {{\n    {async_pool}\n    sqlx::query(\"CREATE TABLE users (id INTEGER)\").execute(&pool).await?;\n    sqlx::query(\"INSERT INTO users (id) VALUES (1)\").execute(&pool).await?;\n    let row: (i64,) = sqlx::query_as(\"SELECT COUNT(*) FROM users\").fetch_one(&pool).await?;\n    Ok(row.0)\n}}",
            check_block(
                "assert_eq!(count_users().await.unwrap(), 1);",
                "assert_eq!(count_users().await.unwrap(), 1);",
                "assert!(count_users().await.is_ok());",
                async_test=True,
            ),
        ),
        _T(
            "02-insert-select",
            "Insert name into `items` and read it back with a bound parameter.",
            "async fn item_name() -> Result<String, sqlx::Error>",
            "use sqlx::SqlitePool;\nasync fn item_name() -> Result<String, sqlx::Error> { todo!() }",
            f"use sqlx::SqlitePool;\nasync fn item_name() -> Result<String, sqlx::Error> {{\n    {async_pool}\n    sqlx::query(\"CREATE TABLE items (name TEXT)\").execute(&pool).await?;\n    sqlx::query(\"INSERT INTO items (name) VALUES (?)\").bind(\"pen\").execute(&pool).await?;\n    let row: (String,) = sqlx::query_as(\"SELECT name FROM items WHERE name = ?\").bind(\"pen\").fetch_one(&pool).await?;\n    Ok(row.0)\n}}",
            check_block(
                "assert_eq!(item_name().await.unwrap(), \"pen\");",
                "assert_ne!(item_name().await.unwrap(), \"\");",
                "assert!(item_name().await.is_ok());",
                async_test=True,
            ),
        ),
        _T(
            "03-sum-column",
            "Store integers in `nums` and return their SQL `SUM`.",
            "async fn sum_nums() -> Result<i64, sqlx::Error>",
            "use sqlx::SqlitePool;\nasync fn sum_nums() -> Result<i64, sqlx::Error> { todo!() }",
            f"use sqlx::SqlitePool;\nasync fn sum_nums() -> Result<i64, sqlx::Error> {{\n    {async_pool}\n    sqlx::query(\"CREATE TABLE nums (v INTEGER)\").execute(&pool).await?;\n    for v in [1, 2, 3] {{ sqlx::query(\"INSERT INTO nums (v) VALUES (?)\").bind(v).execute(&pool).await?; }}\n    let row: (i64,) = sqlx::query_as(\"SELECT SUM(v) FROM nums\").fetch_one(&pool).await?;\n    Ok(row.0)\n}}",
            check_block(
                "assert_eq!(sum_nums().await.unwrap(), 6);",
                "assert!(sum_nums().await.unwrap() > 0);",
                "assert!(sum_nums().await.is_ok());",
                async_test=True,
            ),
        ),
        _T(
            "04-fetch-optional",
            "Return `Some` when a row exists and `None` when the table is empty.",
            "async fn maybe_one() -> Result<Option<i64>, sqlx::Error>",
            "use sqlx::SqlitePool;\nasync fn maybe_one() -> Result<Option<i64>, sqlx::Error> { todo!() }",
            f"use sqlx::SqlitePool;\nasync fn maybe_one() -> Result<Option<i64>, sqlx::Error> {{\n    {async_pool}\n    sqlx::query(\"CREATE TABLE t (v INTEGER)\").execute(&pool).await?;\n    let empty: Option<(i64,)> = sqlx::query_as(\"SELECT v FROM t LIMIT 1\").fetch_optional(&pool).await?;\n    sqlx::query(\"INSERT INTO t (v) VALUES (9)\").execute(&pool).await?;\n    let some: Option<(i64,)> = sqlx::query_as(\"SELECT v FROM t LIMIT 1\").fetch_optional(&pool).await?;\n    Ok(some.map(|r| r.0).or(empty.map(|r| r.0)))\n}}",
            check_block(
                "assert_eq!(maybe_one().await.unwrap(), Some(9));",
                "assert!(maybe_one().await.unwrap().is_some());",
                "assert!(maybe_one().await.is_ok());",
                async_test=True,
            ),
        ),
        _T(
            "05-transaction-commit",
            "Use a transaction to insert two rows; both must be visible after commit.",
            "async fn tx_count() -> Result<i64, sqlx::Error>",
            "use sqlx::SqlitePool;\nasync fn tx_count() -> Result<i64, sqlx::Error> { todo!() }",
            f"use sqlx::SqlitePool;\nasync fn tx_count() -> Result<i64, sqlx::Error> {{\n    {async_pool}\n    sqlx::query(\"CREATE TABLE pairs (a INTEGER, b INTEGER)\").execute(&pool).await?;\n    let mut tx = pool.begin().await?;\n    sqlx::query(\"INSERT INTO pairs (a,b) VALUES (1,2)\").execute(&mut *tx).await?;\n    sqlx::query(\"INSERT INTO pairs (a,b) VALUES (3,4)\").execute(&mut *tx).await?;\n    tx.commit().await?;\n    let row: (i64,) = sqlx::query_as(\"SELECT COUNT(*) FROM pairs\").fetch_one(&pool).await?;\n    Ok(row.0)\n}}",
            check_block(
                "assert_eq!(tx_count().await.unwrap(), 2);",
                "assert!(tx_count().await.unwrap() >= 2);",
                "assert!(tx_count().await.is_ok());",
                async_test=True,
            ),
        ),
        _T(
            "06-delete-row",
            "Delete a row by id and return remaining count.",
            "async fn after_delete() -> Result<i64, sqlx::Error>",
            "use sqlx::SqlitePool;\nasync fn after_delete() -> Result<i64, sqlx::Error> { todo!() }",
            f"use sqlx::SqlitePool;\nasync fn after_delete() -> Result<i64, sqlx::Error> {{\n    {async_pool}\n    sqlx::query(\"CREATE TABLE ids (id INTEGER)\").execute(&pool).await?;\n    sqlx::query(\"INSERT INTO ids (id) VALUES (1),(2)\").execute(&pool).await?;\n    sqlx::query(\"DELETE FROM ids WHERE id = 1\").execute(&pool).await?;\n    let row: (i64,) = sqlx::query_as(\"SELECT COUNT(*) FROM ids\").fetch_one(&pool).await?;\n    Ok(row.0)\n}}",
            check_block(
                "assert_eq!(after_delete().await.unwrap(), 1);",
                "assert_ne!(after_delete().await.unwrap(), 2);",
                "assert!(after_delete().await.is_ok());",
                async_test=True,
            ),
        ),
        _T(
            "07-update-row",
            "Update a column value and read it back.",
            "async fn updated() -> Result<i32, sqlx::Error>",
            "use sqlx::SqlitePool;\nasync fn updated() -> Result<i32, sqlx::Error> { todo!() }",
            f"use sqlx::SqlitePool;\nasync fn updated() -> Result<i32, sqlx::Error> {{\n    {async_pool}\n    sqlx::query(\"CREATE TABLE scores (n INTEGER)\").execute(&pool).await?;\n    sqlx::query(\"INSERT INTO scores (n) VALUES (1)\").execute(&pool).await?;\n    sqlx::query(\"UPDATE scores SET n = 10 WHERE n = 1\").execute(&pool).await?;\n    let row: (i32,) = sqlx::query_as(\"SELECT n FROM scores\").fetch_one(&pool).await?;\n    Ok(row.0)\n}}",
            check_block(
                "assert_eq!(updated().await.unwrap(), 10);",
                "assert!(updated().await.unwrap() > 1);",
                "assert!(updated().await.is_ok());",
                async_test=True,
            ),
        ),
        _T(
            "08-max-value",
            "Return the maximum value in a column via SQL.",
            "async fn max_val() -> Result<i32, sqlx::Error>",
            "use sqlx::SqlitePool;\nasync fn max_val() -> Result<i32, sqlx::Error> { todo!() }",
            f"use sqlx::SqlitePool;\nasync fn max_val() -> Result<i32, sqlx::Error> {{\n    {async_pool}\n    sqlx::query(\"CREATE TABLE vals (v INTEGER)\").execute(&pool).await?;\n    for v in [3, 7, 2] {{ sqlx::query(\"INSERT INTO vals (v) VALUES (?)\").bind(v).execute(&pool).await?; }}\n    let row: (i32,) = sqlx::query_as(\"SELECT MAX(v) FROM vals\").fetch_one(&pool).await?;\n    Ok(row.0)\n}}",
            check_block(
                "assert_eq!(max_val().await.unwrap(), 7);",
                "assert!(max_val().await.unwrap() > 3);",
                "assert!(max_val().await.is_ok());",
                async_test=True,
            ),
        ),
    ]


def build_36() -> list[Exercise]:
    return [
        _T(
            "01-argon2-hash",
            "Hash a password with `argon2`.",
            "fn hash_password(pwd: &str) -> String",
            "use argon2::{Argon2, PasswordHasher};\nuse argon2::password_hash::SaltString;\nfn hash_password(pwd: &str) -> String { todo!() }",
            "use argon2::{Argon2, PasswordHasher};\nuse argon2::password_hash::SaltString;\nfn hash_password(pwd: &str) -> String {\n    let salt = SaltString::encode_b64(b\"unique16bytesalt\").unwrap();\n    Argon2::default().hash_password(pwd.as_bytes(), &salt).unwrap().to_string()\n}",
            check_block(
                "let h = hash_password(\"secret\");",
                "assert!(h.starts_with(\"$argon2\"));",
                "assert!(hash_password(\"x\").contains(\"argon2\"));",
            ),
        ),
        _T(
            "02-argon2-verify-ok",
            "Verify a password against an argon2 hash.",
            "fn verify_ok(pwd: &str, hash: &str) -> bool",
            "use argon2::{Argon2, PasswordHasher, PasswordVerifier};\nuse argon2::password_hash::{PasswordHash, SaltString};\nfn verify_ok(pwd: &str, hash: &str) -> bool { todo!() }",
            "use argon2::{Argon2, PasswordHasher, PasswordVerifier};\nuse argon2::password_hash::{PasswordHash, SaltString};\nfn verify_ok(pwd: &str, hash: &str) -> bool {\n    let parsed = PasswordHash::new(hash).unwrap();\n    Argon2::default().verify_password(pwd.as_bytes(), &parsed).is_ok()\n}\nfn make_hash(pwd: &str) -> String {\n    let salt = SaltString::encode_b64(b\"unique16bytesalt\").unwrap();\n    Argon2::default().hash_password(pwd.as_bytes(), &salt).unwrap().to_string()\n}",
            check_block(
                "let h = make_hash(\"pw\");",
                "assert!(verify_ok(\"pw\", &h));",
                "assert!(verify_ok(\"pw\", &make_hash(\"pw\")));",
            ),
        ),
        _T(
            "03-argon2-verify-fail",
            "Wrong password fails verification.",
            "fn verify_bad(pwd: &str, hash: &str) -> bool",
            "use argon2::{Argon2, PasswordHasher, PasswordVerifier};\nuse argon2::password_hash::{PasswordHash, SaltString};\nfn verify_bad(pwd: &str, hash: &str) -> bool { todo!() }",
            "use argon2::{Argon2, PasswordHasher, PasswordVerifier};\nuse argon2::password_hash::{PasswordHash, SaltString};\nfn verify_bad(pwd: &str, hash: &str) -> bool {\n    let parsed = PasswordHash::new(hash).unwrap();\n    Argon2::default().verify_password(pwd.as_bytes(), &parsed).is_err()\n}\nfn make_hash(pwd: &str) -> String {\n    let salt = SaltString::encode_b64(b\"unique16bytesalt\").unwrap();\n    Argon2::default().hash_password(pwd.as_bytes(), &salt).unwrap().to_string()\n}",
            check_block(
                "let h = make_hash(\"right\");",
                "assert!(verify_bad(\"wrong\", &h));",
                "assert!(!verify_bad(\"right\", &h));",
            ),
        ),
        _T(
            "04-jwt-sign",
            "Sign a JWT with `jsonwebtoken`.",
            "fn sign_token(sub: &str, secret: &[u8]) -> String",
            "use jsonwebtoken::{encode, Header, EncodingKey};\nuse serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct Claims { sub: String, exp: usize }\nfn sign_token(sub: &str, secret: &[u8]) -> String { todo!() }",
            "use jsonwebtoken::{encode, Header, EncodingKey};\nuse serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct Claims { sub: String, exp: usize }\nfn sign_token(sub: &str, secret: &[u8]) -> String {\n    let claims = Claims { sub: sub.into(), exp: 9_999_999_999 };\n    encode(&Header::default(), &claims, &EncodingKey::from_secret(secret)).unwrap()\n}",
            check_block(
                "let t = sign_token(\"ada\", b\"sekrit\");",
                "assert_eq!(t.split('.').count(), 3);",
                "assert!(!sign_token(\"x\", b\"k\").is_empty());",
            ),
        ),
        _T(
            "05-jwt-reject",
            "Reject a token signed with a different secret.",
            "fn decode_fails(token: &str, secret: &[u8]) -> bool",
            "use jsonwebtoken::{decode, DecodingKey, Validation, encode, Header, EncodingKey};\nuse serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct Claims { sub: String, exp: usize }\nfn decode_fails(token: &str, secret: &[u8]) -> bool { todo!() }",
            "use jsonwebtoken::{decode, DecodingKey, Validation, encode, Header, EncodingKey};\nuse serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct Claims { sub: String, exp: usize }\nfn decode_fails(token: &str, secret: &[u8]) -> bool {\n    decode::<Claims>(token, &DecodingKey::from_secret(secret), &Validation::default()).is_err()\n}\nfn mint(secret: &[u8]) -> String {\n    encode(&Header::default(), &Claims { sub: \"u\".into(), exp: 9_999_999_999 }, &EncodingKey::from_secret(b\"other\")).unwrap()\n}",
            check_block(
                "let t = mint(b\"ignored\");",
                "assert!(decode_fails(&t, b\"sekrit\"));",
                "assert!(decode_fails(&t, b\"nope\"));",
            ),
        ),
        _T(
            "06-dotenvy-read",
            "Load key/value pairs from a string with `dotenvy::from_read`.",
            "fn load_api_key(config: &str) -> String",
            "fn load_api_key(config: &str) -> String { todo!() }",
            "fn load_api_key(config: &str) -> String {\n    unsafe { std::env::remove_var(\"DRILL_API_KEY\") };\n    dotenvy::from_read(config.as_bytes()).ok();\n    std::env::var(\"DRILL_API_KEY\").unwrap_or_default()\n}",
            check_block(
                "assert_eq!(load_api_key(\"DRILL_API_KEY=hello\\n\"), \"hello\");",
                "assert_eq!(load_api_key(\"DRILL_API_KEY=zz\\n\"), \"zz\");",
                "assert!(!load_api_key(\"DRILL_API_KEY=1\\n\").is_empty());",
            ),
        ),
        _T(
            "07-auth-header-ok",
            "Axum route accepts a Bearer token header.",
            "fn app() -> axum::Router",
            "use axum::{http::HeaderMap, routing::get, Router};\nasync fn me(headers: HeaderMap) -> Result<&'static str, axum::http::StatusCode> { todo!() }\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{http::HeaderMap, routing::get, Router};\nasync fn me(headers: HeaderMap) -> Result<&'static str, axum::http::StatusCode> {\n    match headers.get(\"authorization\").and_then(|v| v.to_str().ok()) {\n        Some(\"Bearer ok-token\") => Ok(\"user\"),\n        _ => Err(axum::http::StatusCode::UNAUTHORIZED),\n    }\n}\npub fn app() -> Router { Router::new().route(\"/me\", get(me)) }\nfn main() {}",
            """
use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode};
use tower::ServiceExt;
#[tokio::test]
async fn graded() {
    let r = app().oneshot(Request::builder().uri("/me").header("authorization", "Bearer ok-token").body(Body::empty()).unwrap()).await.unwrap();
    assert_eq!(r.status(), StatusCode::OK);
}
""".strip(),
        ),
        _T(
            "08-auth-header-missing",
            "Missing `Authorization` returns 401.",
            "fn app() -> axum::Router",
            "use axum::{http::HeaderMap, routing::get, Router};\nasync fn me(headers: HeaderMap) -> Result<&'static str, axum::http::StatusCode> { todo!() }\npub fn app() -> Router { todo!() }\nfn main() {}",
            "use axum::{http::HeaderMap, routing::get, Router};\nasync fn me(headers: HeaderMap) -> Result<&'static str, axum::http::StatusCode> {\n    match headers.get(\"authorization\").and_then(|v| v.to_str().ok()) {\n        Some(\"Bearer ok-token\") => Ok(\"user\"),\n        _ => Err(axum::http::StatusCode::UNAUTHORIZED),\n    }\n}\npub fn app() -> Router { Router::new().route(\"/me\", get(me)) }\nfn main() {}",
            """
use super::*;
use axum::body::Body;
use axum::http::{Request, StatusCode};
use tower::ServiceExt;
#[tokio::test]
async fn graded() {
    let r = app().oneshot(Request::builder().uri("/me").body(Body::empty()).unwrap()).await.unwrap();
    assert_eq!(r.status(), StatusCode::UNAUTHORIZED);
}
""".strip(),
        ),
    ]


def build_37() -> list[Exercise]:
    return [
        _drill(
            37,
            1,
            "par-sum",
            "use rayon::prelude::*;\nfn par_sum() -> i32 { (0..10).into_par_iter().sum() }",
            "assert_eq!(par_sum(), 45);",
            "assert_eq!(par_sum(), 45);",
            "assert!(par_sum() > 0);",
            task="Sum 0..10 with `into_par_iter()`.",
        ),
        _drill(
            37,
            2,
            "par-map",
            "use rayon::prelude::*;\nfn doubled() -> Vec<i32> { (1..4).into_par_iter().map(|x| x * 2).collect() }",
            "assert_eq!(doubled(), vec![2, 4, 6]);",
            "assert_eq!(doubled().len(), 3);",
            "assert_eq!(doubled()[0], 2);",
            task="Double each element in parallel with `map`.",
        ),
        _drill(
            37,
            3,
            "par-filter",
            "use rayon::prelude::*;\nfn evens() -> Vec<i32> { (1..=6).into_par_iter().filter(|x| x % 2 == 0).collect() }",
            "assert_eq!(evens(), vec![2, 4, 6]);",
            "assert!(!evens().contains(&1));",
            "assert_eq!(evens().len(), 3);",
            task="Collect even numbers using `filter` on a parallel range.",
        ),
        _drill(
            37,
            4,
            "par-fold",
            "use rayon::prelude::*;\nfn par_product() -> i32 { [1, 2, 3, 4].par_iter().copied().reduce(|| 1, |a, b| a * b) }",
            "assert_eq!(par_product(), 24);",
            "assert!(par_product() > 1);",
            "assert_ne!(par_product(), 0);",
            task="Multiply slice elements with `par_iter().reduce`.",
        ),
        _drill(
            37,
            5,
            "par-sort",
            "use rayon::prelude::*;\nfn sorted() -> Vec<i32> { let mut v: Vec<i32> = (0..5).rev().collect(); v.par_sort(); v }",
            "assert_eq!(sorted(), vec![0, 1, 2, 3, 4]);",
            "assert_eq!(sorted().first(), Some(&0));",
            "assert_eq!(sorted().last(), Some(&4));",
            task="Sort a vector in parallel with `par_sort`.",
        ),
        _drill(
            37,
            6,
            "par-chunks",
            "use rayon::prelude::*;\nfn chunk_sum() -> i32 { [1, 2, 3, 4].par_chunks(2).map(|c| c.iter().sum::<i32>()).sum() }",
            "assert_eq!(chunk_sum(), 10);",
            "assert!(chunk_sum() > 4);",
            "assert_eq!(chunk_sum(), 1 + 2 + 3 + 4);",
            task="Sum each parallel chunk of two elements.",
        ),
        _drill(
            37,
            7,
            "par-find-any",
            "use rayon::prelude::*;\nfn has_seven() -> bool { (1..=10).into_par_iter().any(|x| x == 7) }",
            "assert!(has_seven());",
            "assert_eq!(has_seven(), true);",
            "assert!(!(1..=6).any(|x| x == 7));",
            task="Use parallel `any` to search for 7.",
        ),
        _drill(
            37,
            8,
            "par-len",
            "use rayon::prelude::*;\nfn par_len() -> usize { (0..100).into_par_iter().count() }",
            "assert_eq!(par_len(), 100);",
            "assert!(par_len() > 50);",
            "assert_ne!(par_len(), 0);",
            task="Count a parallel range with `into_par_iter`.",
        ),
    ]


def build_38() -> list[Exercise]:
    return [
        _drill(
            38,
            1,
            "atomic-fetch-two",
            "use std::sync::atomic::{AtomicUsize, Ordering};\nuse std::sync::Arc;\nuse std::thread;\nfn parallel_add() -> usize {\n    let n = Arc::new(AtomicUsize::new(0));\n    let a = Arc::clone(&n);\n    let b = Arc::clone(&n);\n    let h1 = thread::spawn(move || { a.fetch_add(10, Ordering::SeqCst); });\n    let h2 = thread::spawn(move || { b.fetch_add(5, Ordering::SeqCst); });\n    h1.join().unwrap(); h2.join().unwrap();\n    n.load(Ordering::SeqCst)\n}",
            "assert_eq!(parallel_add(), 15);",
            task="Two threads `fetch_add` into one `AtomicUsize`.",
        ),
        _drill(
            38,
            2,
            "rwlock-readers",
            "use std::sync::RwLock;\nfn many_reads() -> i32 {\n    let lock = RwLock::new(4);\n    let r1 = lock.read().unwrap();\n    let r2 = lock.read().unwrap();\n    *r1 + *r2\n}",
            "assert_eq!(many_reads(), 8);",
            task="Hold two read guards at once.",
        ),
        _drill(
            38,
            3,
            "rwlock-write",
            "use std::sync::RwLock;\nfn write_bump() -> i32 {\n    let lock = RwLock::new(1);\n    { *lock.write().unwrap() += 2; }\n    *lock.read().unwrap()\n}",
            "assert_eq!(write_bump(), 3);",
            task="Take a write lock, then read the new value.",
        ),
        _drill(
            38,
            4,
            "condvar-pair",
            "use std::sync::{Arc, Condvar, Mutex};\nuse std::thread;\nfn worker_wakes() -> i32 {\n    let pair = Arc::new((Mutex::new(0i32), Condvar::new()));\n    let pair2 = Arc::clone(&pair);\n    let h = thread::spawn(move || {\n        let (lock, cv) = &*pair2;\n        let mut v = lock.lock().unwrap();\n        *v = 7;\n        cv.notify_one();\n    });\n    let (lock, cv) = &*pair;\n    let mut v = lock.lock().unwrap();\n    while *v == 0 { v = cv.wait(v).unwrap(); }\n    h.join().unwrap();\n    *v\n}",
            "assert_eq!(worker_wakes(), 7);",
            task="Wait on a `Condvar` until another thread updates data.",
        ),
        _drill(
            38,
            5,
            "ordering-relaxed",
            "use std::sync::atomic::{AtomicUsize, Ordering};\nfn relaxed_inc() -> usize {\n    let a = AtomicUsize::new(0);\n    a.fetch_add(1, Ordering::Relaxed);\n    a.load(Ordering::Relaxed)\n}",
            "assert_eq!(relaxed_inc(), 1);",
            task="Increment with `Ordering::Relaxed`.",
        ),
        _drill(
            38,
            6,
            "ordering-seq_cst",
            "use std::sync::atomic::{AtomicBool, Ordering};\nfn flag_seen() -> bool {\n    let flag = AtomicBool::new(false);\n    flag.store(true, Ordering::SeqCst);\n    flag.load(Ordering::SeqCst)\n}",
            "assert!(flag_seen());",
            task="Publish a flag with `SeqCst` store/load.",
        ),
        _drill(
            38,
            7,
            "mutex-poison-recover",
            "use std::sync::Mutex;\nfn into_inner() -> i32 {\n    let m = Mutex::new(5);\n    let guard = m.lock().unwrap();\n    *guard + 1\n}",
            "assert_eq!(into_inner(), 6);",
            task="Use a `Mutex` guard to mutate in place.",
        ),
        _drill(
            38,
            8,
            "barrier-two",
            "use std::sync::{Arc, Barrier};\nuse std::thread;\nfn both_ready() -> usize {\n    let b = Arc::new(Barrier::new(2));\n    let b2 = Arc::clone(&b);\n    let h = thread::spawn(move || { b2.wait(); 1 });\n    b.wait();\n    h.join().unwrap()\n}",
            "assert_eq!(both_ready(), 1);",
            task="Synchronize two threads with `Barrier`.",
        ),
        _drill(38, 9, "sync-extra", "use std::sync::OnceLock;\nfn once_num() -> i32 { static N: OnceLock<i32> = OnceLock::new(); *N.get_or_init(|| 2) }", "assert_eq!(once_num(), 2)"),
        _drill(38, 10, "sync-extra2", "use std::sync::atomic::{AtomicI32, Ordering};\nfn swap() -> i32 { let a = AtomicI32::new(1); a.swap(9, Ordering::SeqCst) }", "assert_eq!(swap(), 1)"),
        _drill(38, 11, "sync-extra3", "use std::sync::Mutex;\nfn drop_guard() -> i32 { let m = Mutex::new(0); { let mut g = m.lock().unwrap(); *g = 3; } *m.lock().unwrap() }", "assert_eq!(drop_guard(), 3)"),
    ]


def build_39() -> list[Exercise]:
    return [
        _drill(
            39,
            1,
            "size-padding",
            "fn padded_size() -> usize {\n    struct Padded { a: u8, b: u32 }\n    std::mem::size_of::<Padded>()\n}",
            "assert_eq!(padded_size(), 8);",
            "assert!(padded_size() > 5);",
            "assert_ne!(padded_size(), 5);",
            task="Struct size includes alignment padding.",
        ),
        _drill(
            39,
            2,
            "align-of",
            "fn align_u32() -> usize { std::mem::align_of::<u32>() }",
            "assert_eq!(align_u32(), 4);",
            task="Read alignment with `align_of`.",
        ),
        _drill(
            39,
            3,
            "repr-c-size",
            "fn c_layout() -> usize {\n    #[repr(C)]\n    struct Pair { a: u8, b: u32 }\n    std::mem::size_of::<Pair>()\n}",
            "assert_eq!(c_layout(), 8);",
            task="`#[repr(C)]` fixes field order for FFI-style layout.",
        ),
        _drill(
            39,
            4,
            "niche-option",
            "use std::num::NonZeroU8;\nfn niche_one_byte() -> usize { std::mem::size_of::<Option<NonZeroU8>>() }",
            "assert_eq!(niche_one_byte(), 1);",
            task="`Option<NonZeroU8>` uses a niche (size 1).",
        ),
        _drill(
            39,
            5,
            "box-size",
            "fn box_size() -> usize { std::mem::size_of::<Box<i32>>() }",
            "assert_eq!(box_size(), std::mem::size_of::<usize>());",
            task="`Box<T>` is pointer-sized on the stack.",
        ),
        _drill(
            39,
            6,
            "field-sum-not-size",
            "fn fields_vs_struct() -> (usize, usize) {\n    struct S { a: u8, b: u16 }\n    (std::mem::size_of_val(&S { a: 0, b: 0 }), std::mem::size_of::<u8>() as usize + std::mem::size_of::<u16>() as usize)\n}",
            "assert_eq!(fields_vs_struct().0, 4);",
            "assert!(fields_vs_struct().0 >= fields_vs_struct().1);",
            "assert_eq!(fields_vs_struct().1, 3);",
            task="Sum of field sizes can be less than struct size.",
        ),
        _drill(
            39,
            7,
            "align-struct",
            "fn align_struct() -> usize {\n    struct S { x: u64 }\n    std::mem::align_of::<S>()\n}",
            "assert_eq!(align_struct(), 8);",
            task="Struct alignment follows its largest field.",
        ),
        _drill(
            39,
            8,
            "array-size",
            "fn arr() -> usize { std::mem::size_of::<[u8; 16]>() }",
            "assert_eq!(arr(), 16);",
            task="Array size is element size times length.",
        ),
        _drill(39, 9, "layout-extra", "fn zst() -> usize { struct Z; std::mem::size_of::<Z>() }", "assert_eq!(zst(), 0)"),
        _drill(39, 10, "layout-extra2", "fn tuple_size() -> usize { std::mem::size_of::<(u8, u32)>() }", "assert_eq!(tuple_size(), 8)"),
        _drill(39, 11, "layout-extra3", "fn ref_size() -> usize { std::mem::size_of::<&i32>() }", "assert_eq!(ref_size(), std::mem::size_of::<usize>())"),
    ]


def build_40() -> list[Exercise]:
    return [
        _drill(
            40,
            1,
            "ptr-read",
            "fn read_byte() -> u8 { let n: u8 = 5; // INVARIANT: `n` lives while pointer is used\n unsafe { std::ptr::read(&n as *const u8) } }",
            "assert_eq!(read_byte(), 5);",
            "assert_ne!(read_byte(), 0);",
            "assert!(read_byte() <= 255);",
            task="Read a `u8` through a raw pointer (stack value must stay valid).",
        ),
        _drill(
            40,
            2,
            "ptr-write",
            "fn write_seven() -> i32 { let mut n = 0i32; // INVARIANT: exclusive mutable access\n unsafe { std::ptr::write(&mut n as *mut i32, 7); } n }",
            "assert_eq!(write_seven(), 7);",
            "assert_ne!(write_seven(), 0);",
            "assert!(write_seven() > 0);",
            task="Write through `*mut i32` then return the variable.",
        ),
        _drill(
            40,
            3,
            "slice-from-raw",
            "fn first_of_three() -> i32 { let v = [10i32, 20, 30]; // INVARIANT: slice length matches allocation\n unsafe { std::slice::from_raw_parts(v.as_ptr(), 3)[0] } }",
            "assert_eq!(first_of_three(), 10);",
            "assert_ne!(first_of_three(), 20);",
            "assert!(first_of_three() > 0);",
            task="Build a slice from raw parts for a fixed array.",
        ),
        _drill(
            40,
            4,
            "str-from-utf8",
            "fn parse_ascii() -> &'static str { let bytes: &[u8] = b\"rust\"; // INVARIANT: valid UTF-8\n unsafe { std::str::from_utf8_unchecked(bytes) } }",
            "assert_eq!(parse_ascii(), \"rust\");",
            "assert_eq!(parse_ascii().len(), 4);",
            "assert!(!parse_ascii().is_empty());",
            task="Use `from_utf8_unchecked` on known-valid ASCII bytes.",
        ),
        _drill(
            40,
            5,
            "unsafe-stack",
            "struct Stack2 { data: [i32; 2], len: usize }\nimpl Stack2 {\n    // INVARIANT: len <= 2 and only slots < len are initialized\n    unsafe fn push(&mut self, v: i32) { *self.data.get_unchecked_mut(self.len) = v; self.len += 1; }\n    unsafe fn pop(&mut self) -> i32 { self.len -= 1; *self.data.get_unchecked(self.len) }\n}\nfn stack_ops() -> (i32, i32) {\n    let mut s = Stack2 { data: [0, 0], len: 0 };\n    unsafe { s.push(1); s.push(2); }\n    unsafe { (s.pop(), s.pop()) }\n}",
            "assert_eq!(stack_ops(), (2, 1));",
            "assert_ne!(stack_ops().0, 0);",
            "assert_eq!(stack_ops().1, 1);",
            task="Two-slot stack with `unsafe` push/pop and a documented invariant.",
        ),
        _drill(
            40,
            6,
            "copy-nonoverlapping",
            "fn copy_two() -> [i32; 2] { let src = [1, 2]; let mut dst = [0i32; 2]; // INVARIANT: dst has room for 2 elements\n unsafe { std::ptr::copy_nonoverlapping(src.as_ptr(), dst.as_mut_ptr(), 2); } dst }",
            "assert_eq!(copy_two(), [1, 2]);",
            "assert_ne!(copy_two(), [0, 0]);",
            "assert_eq!(copy_two()[1], 2);",
            task="Copy two `i32` values with `copy_nonoverlapping`.",
        ),
        _drill(
            40,
            7,
            "maybe-uninit",
            "use std::mem::MaybeUninit;\nfn init_on_stack() -> i32 {\n    let mut slot = MaybeUninit::<i32>::uninit();\n    // INVARIANT: write once before assume_init\n    unsafe { slot.as_mut_ptr().write(42); }\n    unsafe { slot.assume_init() }\n}",
            "assert_eq!(init_on_stack(), 42);",
            "assert_ne!(init_on_stack(), 0);",
            "assert!(init_on_stack() > 0);",
            task="Write into `MaybeUninit` then `assume_init`.",
        ),
        _drill(
            40,
            8,
            "manually-drop",
            "use std::mem::ManuallyDrop;\nfn no_double_free() -> String {\n    let s = ManuallyDrop::new(String::from(\"keep\"));\n    let clone = (*s).clone();\n    // INVARIANT: we never drop `s` — only the clone is returned\n    clone\n}",
            "assert_eq!(no_double_free(), \"keep\");",
            "assert_eq!(no_double_free().len(), 4);",
            "assert!(!no_double_free().is_empty());",
            task="Use `ManuallyDrop` to control drop order.",
        ),
    ]


def build_41() -> list[Exercise]:
    link = '#[link(name = "native_add")]\nunsafe extern "C" { fn add_int(a: i32, b: i32) -> i32; }'
    return [
        _T(
            "01-ffi-add",
            "Call C `add_int` from `native/add.c` via FFI.",
            "fn add_via_ffi(a: i32, b: i32) -> i32",
            f"{link}\nfn add_via_ffi(a: i32, b: i32) -> i32 {{ todo!() }}",
            f"{link}\nfn add_via_ffi(a: i32, b: i32) -> i32 {{ unsafe {{ add_int(a, b) }} }}",
            check_block(
                "assert_eq!(add_via_ffi(2, 3), 5);",
                "assert_eq!(add_via_ffi(0, 0), 0);",
                "assert_eq!(add_via_ffi(-1, 1), 0);",
            ),
        ),
        _drill(
            41,
            2,
            "ffi-double",
            f"{link}\nfn double_via_ffi(n: i32) -> i32 {{ unsafe {{ add_int(n, n) }} }}",
            "assert_eq!(double_via_ffi(4), 8);",
            "assert_eq!(double_via_ffi(0), 0);",
            "assert_eq!(double_via_ffi(-2), -4);",
            task="Double an integer by adding it to itself in C.",
        ),
        _drill(
            41,
            3,
            "ffi-increment",
            f"{link}\nfn inc_via_ffi(n: i32) -> i32 {{ unsafe {{ add_int(n, 1) }} }}",
            "assert_eq!(inc_via_ffi(9), 10);",
            "assert_eq!(inc_via_ffi(-1), 0);",
            "assert_eq!(inc_via_ffi(0), 1);",
            task="Increment by one using `add_int(n, 1)`.",
        ),
        _drill(
            41,
            4,
            "ffi-sum-three",
            f"{link}\nfn sum3(a: i32, b: i32, c: i32) -> i32 {{ unsafe {{ add_int(add_int(a, b), c) }} }}",
            "assert_eq!(sum3(1, 2, 3), 6);",
            "assert_eq!(sum3(0, 0, 0), 0);",
            "assert_eq!(sum3(-1, 2, 1), 2);",
            task="Chain two C calls to add three numbers.",
        ),
        _T(
            "05-rust-export-c",
            "Export `double_in_rust` with `#[no_mangle]` for C callbacks.",
            "fn call_rust_double() -> i32",
            f"{link}\n#[unsafe(no_mangle)]\npub extern \"C\" fn double_in_rust(n: i32) -> i32 {{ n * 2 }}\nfn call_rust_double() -> i32 {{ todo!() }}",
            f"{link}\ntype DoubleFn = extern \"C\" fn(i32) -> i32;\n#[unsafe(no_mangle)]\npub extern \"C\" fn double_in_rust(n: i32) -> i32 {{ n * 2 }}\nfn call_rust_double() -> i32 {{\n    let f: DoubleFn = double_in_rust;\n    f(21)\n}}",
            check_block(
                "assert_eq!(call_rust_double(), 42);",
                "assert_eq!(double_in_rust(0), 0);",
                "assert_eq!(double_in_rust(3), 6);",
            ),
        ),
        _drill(
            41,
            6,
            "ffi-wrap",
            f"{link}\nfn wrap_add(a: i32, b: i32) -> Option<i32> {{ if a > 1_000_000 {{ None }} else {{ Some(unsafe {{ add_int(a, b) }}) }} }}",
            "assert_eq!(wrap_add(2, 2), Some(4));",
            "assert_eq!(wrap_add(2_000_000, 1), None);",
            "assert!(wrap_add(0, 0).is_some());",
            task="Guard huge inputs before calling FFI.",
        ),
        _drill(
            41,
            7,
            "ffi-abs-diff",
            f"{link}\nfn abs_diff(a: i32, b: i32) -> i32 {{ if a >= b {{ unsafe {{ add_int(a, -b) }} }} else {{ unsafe {{ add_int(b, -a) }} }} }}",
            "assert_eq!(abs_diff(5, 3), 2);",
            "assert_eq!(abs_diff(3, 5), 2);",
            "assert_eq!(abs_diff(0, 0), 0);",
            task="Compute absolute difference using `add_int` with negation.",
        ),
        _drill(
            41,
            8,
            "ffi-triple",
            f"{link}\nfn triple(n: i32) -> i32 {{ unsafe {{ add_int(add_int(n, n), n) }} }}",
            "assert_eq!(triple(3), 9);",
            "assert_eq!(triple(0), 0);",
            "assert_eq!(triple(-2), -6);",
            task="Multiply by three using only `add_int`.",
        ),
    ]


def build_42() -> list[Exercise]:
    return [
        _drill(
            42,
            1,
            "vec-with-capacity",
            "fn cap_len() -> usize { let v: Vec<i32> = Vec::with_capacity(100); v.capacity() }",
            "assert_eq!(cap_len(), 100);",
            task="Preallocate with `Vec::with_capacity`.",
        ),
        _drill(
            42,
            2,
            "vec-push-growth",
            "fn after_push() -> usize { let mut v = Vec::new(); v.push(1); v.push(2); v.len() }",
            "assert_eq!(after_push(), 2);",
            task="Growing a vec without setting capacity first.",
        ),
        _drill(
            42,
            3,
            "string-clone-allocs",
            "fn clone_count_hint() -> usize { let a = String::from(\"hi\"); let b = a.clone(); a.len() + b.len() }",
            "assert_eq!(clone_count_hint(), 4);",
            task="Cloning a `String` duplicates heap data.",
        ),
        _drill(
            42,
            4,
            "no-collect-sum",
            "fn sum_iter() -> i32 { (0..5).map(|x| x).sum() }",
            "assert_eq!(sum_iter(), 10);",
            task="Sum an iterator without an intermediate `collect`.",
        ),
        _drill(
            42,
            5,
            "extend-vs-push",
            "fn extend_len() -> usize { let mut v = vec![1]; v.extend([2, 3]); v.len() }",
            "assert_eq!(extend_len(), 3);",
            task="Bulk append with `extend`.",
        ),
        _drill(
            42,
            6,
            "reserve-more",
            "fn reserved() -> usize { let mut v = vec![1, 2]; v.reserve(10); v.capacity() }",
            "assert!(reserved() >= 12);",
            task="Reserve extra space before more pushes.",
        ),
        _drill(
            42,
            7,
            "drain-reuse",
            "fn drain_sum() -> i32 { let mut v = vec![1, 2, 3]; v.drain(..).sum() }",
            "assert_eq!(drain_sum(), 6);",
            task="Drain elements without allocating a new vec.",
        ),
        _drill(
            42,
            8,
            "into-iter-owned",
            "fn consume() -> i32 { vec![1, 2].into_iter().sum() }",
            "assert_eq!(consume(), 3);",
            task="Use `into_iter` to consume owned values.",
        ),
        _drill(42, 9, "perf-extra", "fn shrink() -> usize { let mut v = Vec::with_capacity(50); v.push(1); v.shrink_to_fit(); v.capacity() }", "assert!(shrink() >= 1)"),
        _drill(42, 10, "perf-extra2", "fn clear_len() -> usize { let mut v = vec![1, 2, 3]; v.clear(); v.len() }", "assert_eq!(clear_len(), 0)"),
        _drill(42, 11, "perf-extra3", "fn retain() -> Vec<i32> { let mut v = vec![1, 2, 3, 4]; v.retain(|x| x % 2 == 0); v }", "assert_eq!(retain(), vec![2, 4])"),
    ]


def build_43() -> list[Exercise]:
    return [
        _T(
            "01-clap-parse",
            "Parse `--n` with clap.",
            "fn parse_n(args: &[&str]) -> i32",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] n: i32 }\nfn parse_n(args: &[&str]) -> i32 { todo!() }",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] n: i32 }\nfn parse_n(args: &[&str]) -> i32 { Cli::parse_from(args).n }",
            check_block("assert_eq!(parse_n(&[\"app\", \"--n\", \"7\"]), 7);"),
        ),
        _T(
            "02-clap-short-flag",
            "Short flag `-c`.",
            "fn parse_count(args: &[&str]) -> u32",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(short = 'c')] count: u32 }\nfn parse_count(args: &[&str]) -> u32 { todo!() }",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(short = 'c')] count: u32 }\nfn parse_count(args: &[&str]) -> u32 { Cli::parse_from(args).count }",
            check_block("assert_eq!(parse_count(&[\"app\", \"-c\", \"3\"]), 3);"),
        ),
        _T(
            "03-clap-bool-flag",
            "Boolean `--verbose` flag.",
            "fn parse_verbose(args: &[&str]) -> bool",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] verbose: bool }\nfn parse_verbose(args: &[&str]) -> bool { todo!() }",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] verbose: bool }\nfn parse_verbose(args: &[&str]) -> bool { Cli::parse_from(args).verbose }",
            check_block("assert!(parse_verbose(&[\"app\", \"--verbose\"]));"),
        ),
        _T(
            "04-clap-default",
            "Default value for an optional field.",
            "fn parse_port(args: &[&str]) -> u16",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long, default_value_t = 8080)] port: u16 }\nfn parse_port(args: &[&str]) -> u16 { todo!() }",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long, default_value_t = 8080)] port: u16 }\nfn parse_port(args: &[&str]) -> u16 { Cli::parse_from(args).port }",
            check_block("assert_eq!(parse_port(&[\"app\"]), 8080);"),
        ),
        _T(
            "05-clap-subcommand",
            "Parse a subcommand enum.",
            "fn sub_name(args: &[&str]) -> String",
            "use clap::{Parser, Subcommand};\n#[derive(Parser)]\nstruct Cli { #[command(subcommand)] cmd: Commands }\n#[derive(Subcommand)]\nenum Commands { List, Add { id: u32 } }\nfn sub_name(args: &[&str]) -> String { todo!() }",
            "use clap::{Parser, Subcommand};\n#[derive(Parser)]\nstruct Cli { #[command(subcommand)] cmd: Commands }\n#[derive(Subcommand)]\nenum Commands { List, Add { id: u32 } }\nfn sub_name(args: &[&str]) -> String { match Cli::parse_from(args).cmd { Commands::List => \"list\".into(), Commands::Add { .. } => \"add\".into() } }",
            check_block(
                "assert_eq!(sub_name(&[\"app\", \"list\"]), \"list\");",
                "assert_eq!(sub_name(&[\"app\", \"add\", \"1\"]), \"add\");",
                "assert_ne!(sub_name(&[\"app\", \"list\"]), \"add\");",
            ),
        ),
        _T(
            "06-clap-optional",
            "Optional positional argument.",
            "fn parse_label(args: &[&str]) -> Option<String>",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { label: Option<String> }\nfn parse_label(args: &[&str]) -> Option<String> { todo!() }",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { label: Option<String> }\nfn parse_label(args: &[&str]) -> Option<String> { Cli::parse_from(args).label }",
            check_block(
                "assert_eq!(parse_label(&[\"app\", \"x\"]), Some(\"x\".into()));",
                "assert_eq!(parse_label(&[\"app\"]), None);",
                "assert!(parse_label(&[\"app\", \"a\"]).is_some());",
            ),
        ),
        _T(
            "07-clap-parse-err",
            "`try_parse_from` returns `Err` on bad input.",
            "fn bad_args(args: &[&str]) -> bool",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] n: i32 }\nfn bad_args(args: &[&str]) -> bool { todo!() }",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] n: i32 }\nfn bad_args(args: &[&str]) -> bool { Cli::try_parse_from(args).is_err() }",
            check_block(
                "assert!(bad_args(&[\"app\", \"--n\", \"not-int\"]));",
                "assert!(!bad_args(&[\"app\", \"--n\", \"1\"]));",
                "assert!(bad_args(&[\"app\", \"--n\"]));",
            ),
        ),
        _T(
            "08-clap-help-name",
            "Program name from `CommandFactory`.",
            "fn prog_name() -> String",
            "use clap::{CommandFactory, Parser};\n#[derive(Parser)]\n#[command(name = \"mytool\")]\nstruct Cli {}\nfn prog_name() -> String { todo!() }",
            "use clap::{CommandFactory, Parser};\n#[derive(Parser)]\n#[command(name = \"mytool\")]\nstruct Cli {}\nfn prog_name() -> String { Cli::command().get_name().to_string() }",
            check_block(
                "assert_eq!(prog_name(), \"mytool\");",
                "assert_eq!(prog_name(), \"mytool\");",
                "assert!(!prog_name().is_empty());",
            ),
        ),
        _drill(43, 9, "cli-extra", "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] x: i32 }\nfn x() -> i32 { Cli::parse_from([\"a\", \"--x\", \"2\"]).x }", "assert_eq!(x(), 2)"),
        _drill(43, 10, "cli-extra2", "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] x: i32 }\nfn x() -> i32 { Cli::parse_from([\"a\", \"--x\", \"-1\"]).x }", "assert_eq!(x(), -1)"),
        _drill(43, 11, "cli-extra3", "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] x: i32 }\nfn x() -> i32 { Cli::parse_from([\"a\", \"--x\", \"0\"]).x }", "assert_eq!(x(), 0)"),
    ]


def build_44() -> list[Exercise]:
    return [
        _T(
            "01-wasm-add",
            "Expose `wasm_add` with `#[wasm_bindgen]`; test via a native wrapper.",
            "fn run_add() -> i32",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_add(a: i32, b: i32) -> i32 { todo!() }\nfn run_add() -> i32 { wasm_add(2, 3) }",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_add(a: i32, b: i32) -> i32 { a + b }\nfn run_add() -> i32 { wasm_add(2, 3) }",
            check_block(
                "assert_eq!(run_add(), 5);",
                "assert_eq!(wasm_add(0, 0), 0);",
                "assert_eq!(wasm_add(-1, 1), 0);",
            ),
        ),
        _T(
            "02-wasm-greet",
            "Return a greeting string from a `#[wasm_bindgen]` function.",
            "fn greeting_len() -> usize",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_greet(name: &str) -> String { todo!() }\nfn greeting_len() -> usize { wasm_greet(\"Ada\").len() }",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_greet(name: &str) -> String { format!(\"Hello, {}!\", name) }\nfn greeting_len() -> usize { wasm_greet(\"Ada\").len() }",
            check_block(
                "assert_eq!(greeting_len(), 11);",
                "assert!(wasm_greet(\"\").starts_with(\"Hello\"));",
                "assert!(wasm_greet(\"x\").contains('x'));",
            ),
        ),
        _T(
            "03-wasm-double",
            "Double a number in a bindgen-exported function.",
            "fn doubled() -> i32",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_double(n: i32) -> i32 { todo!() }\nfn doubled() -> i32 { wasm_double(4) }",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_double(n: i32) -> i32 { n * 2 }\nfn doubled() -> i32 { wasm_double(4) }",
            check_block(
                "assert_eq!(doubled(), 8);",
                "assert_eq!(wasm_double(0), 0);",
                "assert_eq!(wasm_double(-3), -6);",
            ),
        ),
        _T(
            "04-wasm-abs",
            "Absolute value via wasm_bindgen (graded natively).",
            "fn abs_val() -> i32",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_abs(n: i32) -> i32 { todo!() }\nfn abs_val() -> i32 { wasm_abs(-7) }",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_abs(n: i32) -> i32 { n.abs() }\nfn abs_val() -> i32 { wasm_abs(-7) }",
            check_block(
                "assert_eq!(abs_val(), 7);",
                "assert_eq!(wasm_abs(0), 0);",
                "assert_eq!(wasm_abs(5), 5);",
            ),
        ),
        _T(
            "05-wasm-max",
            "Return the larger of two i32 values.",
            "fn max_pair() -> i32",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_max(a: i32, b: i32) -> i32 { todo!() }\nfn max_pair() -> i32 { wasm_max(3, 9) }",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_max(a: i32, b: i32) -> i32 { if a > b { a } else { b } }\nfn max_pair() -> i32 { wasm_max(3, 9) }",
            check_block(
                "assert_eq!(max_pair(), 9);",
                "assert_eq!(wasm_max(9, 3), 9);",
                "assert_eq!(wasm_max(4, 4), 4);",
            ),
        ),
        _T(
            "06-wasm-fizz",
            "Fizz helper: return true when n divisible by 3.",
            "fn is_fizz() -> bool",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_fizz(n: u32) -> bool { todo!() }\nfn is_fizz() -> bool { wasm_fizz(9) }",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_fizz(n: u32) -> bool { n % 3 == 0 }\nfn is_fizz() -> bool { wasm_fizz(9) }",
            check_block(
                "assert!(is_fizz());",
                "assert!(!wasm_fizz(10));",
                "assert!(wasm_fizz(0));",
            ),
        ),
        _T(
            "07-wasm-sum-slice",
            "Sum a slice passed to wasm_bindgen (native test uses a fixed slice).",
            "fn sum_three() -> i32",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_sum_slice(vals: &[i32]) -> i32 { todo!() }\nfn sum_three() -> i32 { wasm_sum_slice(&[1, 2, 3]) }",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_sum_slice(vals: &[i32]) -> i32 { vals.iter().sum() }\nfn sum_three() -> i32 { wasm_sum_slice(&[1, 2, 3]) }",
            check_block(
                "assert_eq!(sum_three(), 6);",
                "assert_eq!(wasm_sum_slice(&[]), 0);",
                "assert_eq!(wasm_sum_slice(&[-1, 1]), 0);",
            ),
        ),
        _T(
            "08-wasm-reverse-string",
            "Reverse a string in a bindgen function.",
            "fn rev() -> String",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_reverse(s: &str) -> String { todo!() }\nfn rev() -> String { wasm_reverse(\"rust\") }",
            "use wasm_bindgen::prelude::*;\n#[wasm_bindgen]\npub fn wasm_reverse(s: &str) -> String { s.chars().rev().collect() }\nfn rev() -> String { wasm_reverse(\"rust\") }",
            check_block(
                "assert_eq!(rev(), \"tsur\");",
                "assert_eq!(wasm_reverse(\"\"), \"\");",
                "assert_eq!(wasm_reverse(\"a\"), \"a\");",
            ),
        ),
    ]


def build_45() -> list[Exercise]:
    dom_types = dedent(
        """
        #[derive(Clone, Debug)]
        struct MiniNode { tag: String, text: String, children: Vec<usize> }
        struct MiniDocument { nodes: Vec<MiniNode> }
        impl MiniDocument {
            fn new() -> Self { Self { nodes: Vec::new() } }
            fn create_element(&mut self, tag: &str) -> usize {
                let id = self.nodes.len();
                self.nodes.push(MiniNode { tag: tag.into(), text: String::new(), children: Vec::new() });
                id
            }
            fn set_text_content(&mut self, id: usize, text: &str) { self.nodes[id].text = text.into(); }
            fn append_child(&mut self, parent: usize, child: usize) { self.nodes[parent].children.push(child); }
            fn text_of_first(&self, tag: &str) -> Option<String> {
                self.nodes.iter().find(|n| n.tag == tag).map(|n| n.text.clone())
            }
            fn remove_last_child(&mut self, parent: usize) -> bool { self.nodes[parent].children.pop().is_some() }
        }
        """
    ).strip()
    return [
        _T(
            "01-create-element",
            "In-memory `create_element` (maps to `web_sys`).",
            "fn tag_name() -> String",
            f"{dom_types}\nfn tag_name() -> String {{ todo!() }}",
            f"{dom_types}\nfn tag_name() -> String {{ let mut doc = MiniDocument::new(); let id = doc.create_element(\"p\"); doc.nodes[id].tag.clone() }}",
            check_block("assert_eq!(tag_name(), \"p\");"),
        ),
        _T(
            "02-set-text",
            "Set text content on a node.",
            "fn text() -> String",
            f"{dom_types}\nfn text() -> String {{ todo!() }}",
            f"{dom_types}\nfn text() -> String {{ let mut doc = MiniDocument::new(); let id = doc.create_element(\"p\"); doc.set_text_content(id, \"hi\"); doc.nodes[id].text.clone() }}",
            check_block("assert_eq!(text(), \"hi\");"),
        ),
        _T(
            "03-query-text",
            "Find first node by tag and read text.",
            "fn find_text() -> Option<String>",
            f"{dom_types}\nfn find_text() -> Option<String> {{ todo!() }}",
            f"{dom_types}\nfn find_text() -> Option<String> {{ let mut doc = MiniDocument::new(); let id = doc.create_element(\"span\"); doc.set_text_content(id, \"x\"); doc.text_of_first(\"span\") }}",
            check_block("assert_eq!(find_text(), Some(\"x\".into()));"),
        ),
        _T(
            "04-append-child",
            "Append a child index under a parent.",
            "fn child_count() -> usize",
            f"{dom_types}\nfn child_count() -> usize {{ todo!() }}",
            f"{dom_types}\nfn child_count() -> usize {{ let mut doc = MiniDocument::new(); let p = doc.create_element(\"div\"); let c = doc.create_element(\"p\"); doc.append_child(p, c); doc.nodes[p].children.len() }}",
            check_block("assert_eq!(child_count(), 1);"),
        ),
        _T(
            "05-remove-child",
            "Remove the last child from a parent.",
            "fn after_remove() -> usize",
            f"{dom_types}\nfn after_remove() -> usize {{ todo!() }}",
            f"{dom_types}\nfn after_remove() -> usize {{ let mut doc = MiniDocument::new(); let p = doc.create_element(\"div\"); let c = doc.create_element(\"p\"); doc.append_child(p, c); doc.remove_last_child(p); doc.nodes[p].children.len() }}",
            check_block("assert_eq!(after_remove(), 0);"),
        ),
        _T(
            "06-two-elements",
            "Create two elements and distinguish tags.",
            "fn tags() -> (String, String)",
            f"{dom_types}\nfn tags() -> (String, String) {{ todo!() }}",
            f"{dom_types}\nfn tags() -> (String, String) {{ let mut doc = MiniDocument::new(); let a = doc.create_element(\"p\"); let b = doc.create_element(\"div\"); (doc.nodes[a].tag.clone(), doc.nodes[b].tag.clone()) }}",
            check_block("assert_eq!(tags(), (\"p\".into(), \"div\".into()));"),
        ),
        _T(
            "07-nested-text",
            "Parent with child; read child text via index.",
            "fn nested() -> String",
            f"{dom_types}\nfn nested() -> String {{ todo!() }}",
            f"{dom_types}\nfn nested() -> String {{ let mut doc = MiniDocument::new(); let p = doc.create_element(\"div\"); let c = doc.create_element(\"p\"); doc.set_text_content(c, \"inner\"); doc.append_child(p, c); doc.nodes[c].text.clone() }}",
            check_block("assert_eq!(nested(), \"inner\");"),
        ),
        _T(
            "08-document-len",
            "Track how many nodes exist in the mini document.",
            "fn node_count() -> usize",
            f"{dom_types}\nfn node_count() -> usize {{ todo!() }}",
            f"{dom_types}\nfn node_count() -> usize {{ let mut doc = MiniDocument::new(); doc.create_element(\"a\"); doc.create_element(\"b\"); doc.nodes.len() }}",
            check_block("assert_eq!(node_count(), 2);"),
        ),
        _drill(45, 9, "dom-extra", f"{dom_types}\nfn one() -> usize {{ let mut d = MiniDocument::new(); d.create_element(\"x\"); 1 }}", "assert_eq!(one(), 1)"),
        _drill(45, 10, "dom-extra2", f"{dom_types}\nfn zero() -> usize {{ MiniDocument::new().nodes.len() }}", "assert_eq!(zero(), 0)"),
        _drill(45, 11, "dom-extra3", f"{dom_types}\nfn id() -> usize {{ let mut d = MiniDocument::new(); d.create_element(\"z\") }}", "assert_eq!(id(), 0)"),
    ]


def build_46() -> list[Exercise]:
    return [
        _T(
            "01-prop-greet",
            "Component with a prop (function argument).",
            "fn render() -> String",
            "use leptos::prelude::*;\n#[component]\nfn Greet(name: &'static str) -> impl IntoView { todo!() }\nfn render() -> String { todo!() }",
            "use leptos::prelude::*;\n#[component]\nfn Greet(name: &'static str) -> impl IntoView { view! { <p>{name}</p> } }\nfn render() -> String { view! { <Greet name=\"Ada\"/> }.into_view().to_html() }",
            check_block("assert!(render().contains(\"Ada\"));"),
        ),
        _T(
            "02-list-map",
            "Render a list from a `Vec`.",
            "fn render() -> String",
            "use leptos::prelude::*;\nfn render() -> String { todo!() }",
            "use leptos::prelude::*;\nfn render() -> String { let items = vec![1, 2]; view! { <ul>{items.into_iter().map(|n| view! { <li>{n}</li> }).collect_view()}</ul> }.into_view().to_html() }",
            check_block("assert!(render().contains(\"1\"));", "assert!(render().contains(\"2\"));", "assert!(render().contains(\"li\"));"),
        ),
        _T(
            "03-show-when",
            "Conditional UI with `Show`.",
            "fn render(show: bool) -> String",
            "use leptos::prelude::*;\nfn render(show: bool) -> String { todo!() }",
            "use leptos::prelude::*;\nfn render(show: bool) -> String { view! { <Show when=move || show fallback=|| view! { <p>no</p> }><p>yes</p></Show> }.into_view().to_html() }",
            check_block("assert!(render(true).contains(\"yes\"));", "assert!(render(false).contains(\"no\"));", "assert!(!render(false).contains(\"yes\"));"),
        ),
        _T(
            "04-nested-components",
            "Nest two components.",
            "fn render() -> String",
            "use leptos::prelude::*;\n#[component]\nfn Inner() -> impl IntoView { todo!() }\n#[component]\nfn Outer() -> impl IntoView { view! { <Inner/> } }\nfn render() -> String { view! { <Outer/> }.into_view().to_html() }",
            "use leptos::prelude::*;\n#[component]\nfn Inner() -> impl IntoView { view! { <span>in</span> } }\n#[component]\nfn Outer() -> impl IntoView { view! { <div><Inner/></div> } }\nfn render() -> String { view! { <Outer/> }.into_view().to_html() }",
            check_block("assert!(render().contains(\"in\"));", "assert!(render().contains(\"div\"));", "assert!(render().contains(\"span\"));"),
        ),
        _T(
            "05-fragment-style",
            "Sibling elements in one view.",
            "fn render() -> String",
            "use leptos::prelude::*;\nfn render() -> String { todo!() }",
            "use leptos::prelude::*;\nfn render() -> String { view! { <p>a</p><p>b</p> }.into_view().to_html() }",
            check_block("assert!(render().contains(\"a\"));", "assert!(render().contains(\"b\"));", "assert!(render().matches('p').count() >= 2);"),
        ),
        _T(
            "06-dynamic-tag-text",
            "Interpolate a number in markup.",
            "fn render(n: i32) -> String",
            "use leptos::prelude::*;\nfn render(n: i32) -> String { todo!() }",
            "use leptos::prelude::*;\nfn render(n: i32) -> String { view! { <p>{n}</p> }.into_view().to_html() }",
            check_block("assert!(render(7).contains(\"7\"));", "assert!(render(0).contains(\"0\"));", "assert!(!render(7).is_empty());"),
        ),
        _T(
            "07-child-prop",
            "Pass a numeric prop to a child component.",
            "fn render() -> String",
            "use leptos::prelude::*;\n#[component]\nfn N(n: i32) -> impl IntoView { view! { <em>{n}</em> } }\nfn render() -> String { todo!() }",
            "use leptos::prelude::*;\n#[component]\nfn N(n: i32) -> impl IntoView { view! { <em>{n}</em> } }\nfn render() -> String { view! { <N n=3/> }.into_view().to_html() }",
            check_block("assert!(render().contains(\"3\"));", "assert!(render().contains(\"em\"));", "assert!(!render().is_empty());"),
        ),
        _T(
            "08-wrapper-class",
            "Wrapper component adds a CSS class name in markup.",
            "fn render() -> String",
            "use leptos::prelude::*;\n#[component]\nfn Card() -> impl IntoView { view! { <div class=\"card\">ok</div> } }\nfn render() -> String { todo!() }",
            "use leptos::prelude::*;\n#[component]\nfn Card() -> impl IntoView { view! { <div class=\"card\">ok</div> } }\nfn render() -> String { view! { <Card/> }.into_view().to_html() }",
            check_block("assert!(render().contains(\"card\"));", "assert!(render().contains(\"ok\"));", "assert!(render().contains(\"div\"));"),
        ),
        _drill(46, 9, "leptos-extra", "use leptos::prelude::*;\nfn r() -> String { view! { <p>x</p> }.into_view().to_html() }", "assert!(r().contains(\"x\"))"),
        _drill(46, 10, "leptos-extra2", "use leptos::prelude::*;\nfn r() -> String { view! { <p>y</p> }.into_view().to_html() }", "assert!(r().contains(\"y\"))"),
        _drill(46, 11, "leptos-extra3", "use leptos::prelude::*;\nfn r() -> String { view! { <p>z</p> }.into_view().to_html() }", "assert!(r().contains(\"z\"))"),
    ]


def build_47() -> list[Exercise]:
    return [
        _T(
            "01-signal-set",
            "Create a signal and `set` a new value.",
            "fn after_set() -> i32",
            "use leptos::prelude::*;\nfn after_set() -> i32 { todo!() }",
            "use leptos::prelude::*;\nfn after_set() -> i32 { let s = RwSignal::new(1); s.set(5); s.get() }",
            check_block("assert_eq!(after_set(), 5);"),
        ),
        _T(
            "02-signal-update",
            "Use `update` to mutate in place.",
            "fn after_update() -> i32",
            "use leptos::prelude::*;\nfn after_update() -> i32 { todo!() }",
            "use leptos::prelude::*;\nfn after_update() -> i32 { let s = RwSignal::new(2); s.update(|n| *n += 3); s.get() }",
            check_block("assert_eq!(after_update(), 5);"),
        ),
        _T(
            "03-derived-memo",
            "Derived value with `Memo`.",
            "fn doubled() -> i32",
            "use leptos::prelude::*;\nfn doubled() -> i32 { todo!() }",
            "use leptos::prelude::*;\nfn doubled() -> i32 { let n = RwSignal::new(4); let d = Memo::new(move |_| n.get() * 2); d.get() }",
            check_block("assert_eq!(doubled(), 8);"),
        ),
        _T(
            "04-memo-tracks-set",
            "Memo updates after `set`.",
            "fn after_change() -> i32",
            "use leptos::prelude::*;\nfn after_change() -> i32 { todo!() }",
            "use leptos::prelude::*;\nfn after_change() -> i32 { let n = RwSignal::new(1); let d = Memo::new(move |_| n.get() + 10); n.set(2); d.get() }",
            check_block("assert_eq!(after_change(), 12);"),
        ),
        _T(
            "05-write-from-signal",
            "Write a second signal from the first.",
            "fn synced() -> i32",
            "use leptos::prelude::*;\nfn synced() -> i32 { todo!() }",
            "use leptos::prelude::*;\nfn synced() -> i32 { let a = RwSignal::new(3); let b = RwSignal::new(0); b.set(a.get()); a.set(9); b.get() + a.get() }",
            check_block("assert_eq!(synced(), 12);"),
        ),
        _T(
            "06-signal-string",
            "Signal holding a `String`.",
            "fn label() -> String",
            "use leptos::prelude::*;\nfn label() -> String { todo!() }",
            "use leptos::prelude::*;\nfn label() -> String { let s = RwSignal::new(\"a\".to_string()); s.set(\"b\".into()); s.get() }",
            check_block("assert_eq!(label(), \"b\");"),
        ),
        _T(
            "07-update-string",
            "Mutate string signal with `update`.",
            "fn len() -> usize",
            "use leptos::prelude::*;\nfn len() -> usize { todo!() }",
            "use leptos::prelude::*;\nfn len() -> usize { let s = RwSignal::new(String::new()); s.update(|t| t.push_str(\"hi\")); s.get().len() }",
            check_block("assert_eq!(len(), 2);"),
        ),
        _T(
            "08-memo-sum",
            "Memo combining two reads.",
            "fn sum() -> i32",
            "use leptos::prelude::*;\nfn sum() -> i32 { todo!() }",
            "use leptos::prelude::*;\nfn sum() -> i32 { let a = RwSignal::new(1); let b = RwSignal::new(2); let m = Memo::new(move |_| a.get() + b.get()); m.get() }",
            check_block("assert_eq!(sum(), 3);"),
        ),
        _drill(47, 9, "sig-extra", "use leptos::prelude::*;\nfn v() -> i32 { RwSignal::new(0).get() }", "assert_eq!(v(), 0)"),
        _drill(47, 10, "sig-extra2", "use leptos::prelude::*;\nfn v() -> i32 { let s = RwSignal::new(1); s.set(2); s.get() }", "assert_eq!(v(), 2)"),
        _drill(47, 11, "sig-extra3", "use leptos::prelude::*;\nfn v() -> i32 { Memo::new(|_| 3).get() }", "assert_eq!(v(), 3)"),
    ]


def build_48() -> list[Exercise]:
    return [
        _T(
            "01-add-contract",
            "Serde request/response pair (server-fn shape).",
            "fn handle(req: AddReq) -> AddResp",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct AddReq { a: i32, b: i32 }\n#[derive(Serialize, Deserialize)]\nstruct AddResp { sum: i32 }\nfn handle(req: AddReq) -> AddResp { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct AddReq { a: i32, b: i32 }\n#[derive(Serialize, Deserialize)]\nstruct AddResp { sum: i32 }\nfn handle(req: AddReq) -> AddResp { AddResp { sum: req.a + req.b } }",
            check_block("assert_eq!(handle(AddReq { a: 2, b: 3 }).sum, 5);"),
        ),
        _T(
            "02-greet-contract",
            "String in, string out.",
            "fn greet(req: GreetReq) -> GreetResp",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct GreetReq { name: String }\n#[derive(Serialize, Deserialize)]\nstruct GreetResp { msg: String }\nfn greet(req: GreetReq) -> GreetResp { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct GreetReq { name: String }\n#[derive(Serialize, Deserialize)]\nstruct GreetResp { msg: String }\nfn greet(req: GreetReq) -> GreetResp { GreetResp { msg: format!(\"Hello, {}!\", req.name) } }",
            check_block("assert_eq!(greet(GreetReq { name: \"Ada\".into() }).msg, \"Hello, Ada!\");"),
        ),
        _T(
            "03-json-roundtrip",
            "Round-trip the request type through JSON.",
            "fn round_json() -> String",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct PingReq { n: u32 }\nfn round_json() -> String { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct PingReq { n: u32 }\nfn round_json() -> String { serde_json::to_string(&PingReq { n: 1 }).unwrap() }",
            check_block("assert!(round_json().contains(\"n\"));", "assert_eq!(serde_json::from_str::<PingReq>(&round_json()).unwrap().n, 1);", "assert!(!round_json().is_empty());"),
        ),
        _T(
            "04-error-flag",
            "Response includes success flag.",
            "fn auth(req: AuthReq) -> AuthResp",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct AuthReq { token: String }\n#[derive(Serialize, Deserialize)]\nstruct AuthResp { ok: bool }\nfn auth(req: AuthReq) -> AuthResp { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct AuthReq { token: String }\n#[derive(Serialize, Deserialize)]\nstruct AuthResp { ok: bool }\nfn auth(req: AuthReq) -> AuthResp { AuthResp { ok: req.token == \"good\" } }",
            check_block("assert!(auth(AuthReq { token: \"good\".into() }).ok);", "assert!(!auth(AuthReq { token: \"bad\".into() }).ok);", "assert!(auth(AuthReq { token: \"good\".into() }).ok);"),
        ),
        _T(
            "05-list-req",
            "Request carries a `Vec`.",
            "fn total(req: SumReq) -> SumResp",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct SumReq { values: Vec<i32> }\n#[derive(Serialize, Deserialize)]\nstruct SumResp { total: i32 }\nfn total(req: SumReq) -> SumResp { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct SumReq { values: Vec<i32> }\n#[derive(Serialize, Deserialize)]\nstruct SumResp { total: i32 }\nfn total(req: SumReq) -> SumResp { SumResp { total: req.values.iter().sum() } }",
            check_block("assert_eq!(total(SumReq { values: vec![1, 2, 3] }).total, 6);"),
        ),
        _T(
            "06-option-field",
            "Optional field in request.",
            "fn echo(req: EchoReq) -> EchoResp",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct EchoReq { msg: Option<String> }\n#[derive(Serialize, Deserialize)]\nstruct EchoResp { msg: String }\nfn echo(req: EchoReq) -> EchoResp { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct EchoReq { msg: Option<String> }\n#[derive(Serialize, Deserialize)]\nstruct EchoResp { msg: String }\nfn echo(req: EchoReq) -> EchoResp { EchoResp { msg: req.msg.unwrap_or_else(|| \"none\".into()) } }",
            check_block("assert_eq!(echo(EchoReq { msg: None }).msg, \"none\");", "assert_eq!(echo(EchoReq { msg: Some(\"x\".into()) }).msg, \"x\");", "assert_eq!(echo(EchoReq { msg: None }).msg, \"none\");"),
        ),
        _T(
            "07-deserialize-resp",
            "Deserialize response JSON.",
            "fn parse_resp() -> i32",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct CountResp { n: i32 }\nfn parse_resp() -> i32 { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct CountResp { n: i32 }\nfn parse_resp() -> i32 { serde_json::from_str::<CountResp>(\"{\\\"n\\\":9}\").unwrap().n }",
            check_block("assert_eq!(parse_resp(), 9);"),
        ),
        _T(
            "08-wire-format",
            "Serialize response for wire format.",
            "fn wire() -> String",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct OkResp { ok: bool }\nfn wire() -> String { todo!() }",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct OkResp { ok: bool }\nfn wire() -> String { serde_json::to_string(&OkResp { ok: true }).unwrap() }",
            check_block("assert!(wire().contains(\"true\"));", "assert!(serde_json::from_str::<OkResp>(&wire()).unwrap().ok);", "assert!(!wire().is_empty());"),
        ),
        _drill(
            48,
            9,
            "srv-extra",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct R { v: i32 }\nfn v() -> i32 { serde_json::from_str::<R>(\"{\\\"v\\\":1}\").unwrap().v }",
            "assert_eq!(v(), 1)",
        ),
        _drill(
            48,
            10,
            "srv-extra2",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct R { v: i32 }\nfn v() -> i32 { R { v: 2 }.v }",
            "assert_eq!(v(), 2)",
        ),
        _drill(
            48,
            11,
            "srv-extra3",
            "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize)]\nstruct R { v: i32 }\nfn v() -> i32 { R { v: 3 }.v }",
            "assert_eq!(v(), 3)",
        ),
    ]


REST_LEVELS: list[tuple[str, int, str, list[Exercise]]] = [
    ("18-derive-and-operators", 3, "Derive and operators", _eight(build_18())),
    ("19-generics", 3, "Generics", _eight(build_19())),
    ("20-trait-objects", 3, "Trait objects", _eight(build_20())),
    ("21-lifetimes", 3, "Lifetimes", _eight(build_21())),
    ("22-conversions", 3, "Conversions", _eight(build_22())),
    ("23-iterators-advanced", 3, "Iterators advanced", _eight(build_23())),
    ("24-smart-pointers", 3, "Smart pointers", _eight(build_24())),
    ("25-error-design", 3, "Error design", _eight(build_25())),
    ("26-testing-and-cargo", 3, "Testing and Cargo", _eight(build_26())),
    ("27-threads", 3, "Threads", _eight(build_27())),
    ("28-channels-and-sync", 3, "Channels and sync", _eight(build_28())),
    ("29-async-tokio", 3, "Async Tokio", _eight(build_29())),
    ("30-serde", 4, "Serde", _eight(build_30())),
    ("31-axum-routing", 4, "Axum routing", _eight(build_31())),
    ("32-axum-extractors", 4, "Axum extractors", _eight(build_32())),
    ("33-axum-errors", 4, "Axum errors", _eight(build_33())),
    ("34-tower-and-tracing", 4, "Tower and tracing", _eight(build_34())),
    ("35-sqlx", 4, "SQLx", build_35()),
    ("36-auth-and-config", 4, "Auth and config", _eight(build_36())),
    ("37-rayon-and-pools", 5, "Rayon and pools", build_37()),
    ("38-sync-primitives", 5, "Sync primitives", _eight(build_38())),
    ("39-memory-layout", 5, "Memory layout", _eight(build_39())),
    ("40-unsafe", 5, "Unsafe", build_40()),
    ("41-ffi", 5, "FFI", build_41()),
    ("42-performance", 5, "Performance", _eight(build_42())),
    ("43-cli-clap", 5, "CLI clap", _eight(build_43())),
    ("44-wasm-bindgen", 6, "wasm-bindgen", build_44()),
    ("45-web-sys-dom", 6, "web-sys DOM stubs", _eight(build_45())),
    ("46-leptos-components", 6, "Leptos components", _eight(build_46())),
    ("47-leptos-signals", 6, "Leptos signals", _eight(build_47())),
    ("48-leptos-server-fns", 6, "Leptos server functions", _eight(build_48())),
]
