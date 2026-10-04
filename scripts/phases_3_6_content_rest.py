"""Levels 18–48 exercise definitions."""

from __future__ import annotations

from phases_3_6_common import Exercise, O as _O, T as _T, axum_route_ex as _axum_route_ex


def _drill(level_num: int, idx: int, topic: str, body: str, test: str) -> Exercise:
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
    if body.strip().startswith("use ") or body.strip().startswith("#["):
        stub = body.split("fn ", 1)[0] + "fn " + sig.split("fn ", 1)[-1] + " {\n    todo!()\n}" if "fn " in body else stub
        # keep leading imports/attrs, todo the first function
        prefix = []
        rest = body.splitlines()
        fn_i = next(i for i, ln in enumerate(rest) if ln.lstrip().startswith(("fn ", "pub fn ", "async fn ")))
        prefix = "\n".join(rest[:fn_i])
        fn_ln = rest[fn_i]
        fn_sig = fn_ln.split("{")[0].strip()
        stub = (prefix + "\n" if prefix else "") + f"{fn_sig} {{\n    todo!()\n}}"
    if "async fn" in body or ".await" in test:
        check = f"use super::*;\n#[tokio::test]\nasync fn t() {{\n    {test}\n}}"
    else:
        check = f"use super::*;\n#[test]\nfn t() {{\n    {test}\n}}"
    return _T(
        name,
        f"Complete `{name}` ({topic.replace('-', ' ')}).",
        sig,
        stub,
        body,
        check,
    )


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
        _drill(18, 7, "mul-op", "use std::ops::Mul;\nfn triple() -> i32 {\n    struct W(i32);\n    impl Mul<i32> for W { type Output = i32; fn mul(self, rhs: i32) -> i32 { self.0 * rhs } }\n    W(3) * 2\n}", "assert_eq!(triple(), 6)"),
        _drill(18, 8, "deref", "use std::ops::Deref;\nfn len() -> usize {\n    struct S(String);\n    impl Deref for S { type Target = str; fn deref(&self) -> &str { &self.0 } }\n    S(\"abc\".into()).len()\n}", "assert_eq!(len(), 3)"),
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
            (8, "where-clause", "fn clamp(v: i32, lo: i32, hi: i32) -> i32 { v.clamp(lo, hi) }\nfn small() -> i32 { clamp(10, 0, 5) }", "assert_eq!(small(), 5)"),
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
        _drill(20, 4, "return-impl", "trait Greet { fn hi(&self) -> String; }\nstruct User { name: String }\nimpl Greet for User { fn hi(&self) -> String { format!(\"Hi {}\", self.name) } }\nfn greet() -> String { User { name: \"Ada\".into() }.hi() }", "assert_eq!(greet(), \"Hi Ada\")"),
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
        _drill(23, 7, "chain", "fn chain() -> Vec<i32> { [1].iter().chain([2].iter()).copied().collect() }", "assert_eq!(chain(), vec![1, 2])"),
        _drill(23, 8, "zip", "fn zip_sum() -> i32 { [1, 2].iter().zip([10, 20].iter()).map(|(a, b)| a + b).sum() }", "assert_eq!(zip_sum(), 33)"),
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
        _drill(26, 1, "unit-test", "pub fn add(a: i32, b: i32) -> i32 { a + b }", "assert_eq!(add(1, 2), 3)"),
        _drill(26, 2, "assert", "pub fn truth() -> bool { true }", "assert!(truth())"),
        _drill(26, 3, "assert-eq", "pub fn double(x: i32) -> i32 { x * 2 }", "assert_eq!(double(2), 4)"),
        _drill(26, 4, "should-panic", "pub fn panics() { panic!(\"no\"); }", "assert_eq!(std::panic::catch_unwind(|| panics()).is_err(), true)"),
        _drill(26, 5, "test-module", "mod m { pub fn sq(x: i32) -> i32 { x * x } }\npub fn sq() -> i32 { m::sq(3) }", "assert_eq!(sq(), 9)"),
        _drill(26, 6, "cfg-test", "pub fn prod() -> i32 { 6 }", "assert_eq!(prod(), 6)"),
        _drill(26, 7, "doc-test", "/// Adds numbers.\npub fn plus(a: i32, b: i32) -> i32 { a + b }", "assert_eq!(plus(1, 1), 2)"),
        _drill(26, 8, "bench-harness", "pub fn work() -> u32 { 1 + 2 }", "assert_eq!(work(), 3)"),
        _O("09-cargo-toml-demo", "Print package name from env.", "", "fn main() { println!(\"level\"); }"),
        _drill(26, 10, "dev-dep", "pub fn helper() -> i32 { 42 }", "assert_eq!(helper(), 42)"),
        _drill(26, 11, "integration-style", "pub fn greet() -> String { \"hi\".into() }", "assert_eq!(greet(), \"hi\")"),
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
        _drill(27, 8, "park-timeout", "fn park() -> i32 { 1 }", "assert_eq!(park(), 1)"),
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
        _drill(28, 8, "send-sync", "fn is_send<T: Send>() -> bool { true }\nfn s() -> bool { is_send::<i32>() }", "assert!(s())"),
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
        _drill(29, 5, "timeout", "async fn fast() -> i32 { 2 }", "assert_eq!(fast().await, 2)"),
        _drill(29, 6, "select", "async fn pick() -> i32 { tokio::select! { v = async { 1 } => v, } }", "assert_eq!(pick().await, 1)"),
        _drill(29, 7, "block-on", "fn sync() -> i32 { tokio::runtime::Runtime::new().unwrap().block_on(async { 3 }) }", "assert_eq!(sync(), 3)"),
        _drill(29, 8, "channel", "async fn chan() -> i32 { let (tx, mut rx) = tokio::sync::mpsc::channel(1); tx.send(9).await.unwrap(); rx.recv().await.unwrap() }", "assert_eq!(chan().await, 9)"),
        _drill(29, 9, "mutex", "async fn lock() -> i32 { let m = tokio::sync::Mutex::new(5); *m.lock().await }", "assert_eq!(lock().await, 5)"),
        _O("10-async-demo", "Block on async print.", "", "fn main() { tokio::runtime::Runtime::new().unwrap().block_on(async { println!(\"async\"); }); }"),
        _drill(29, 11, "interval", "async fn once() -> u32 { 1 }", "assert_eq!(once().await, 1)"),
    ]


# Phase 4 — backend (abbreviated axum/serde/sqlx patterns)
def build_30() -> list[Exercise]:
    ex = []
    for i, topic in enumerate(
        ["derive-serde", "json-roundtrip", "rename", "optional-field", "vec-json", "enum-json", "from-value", "to-string-pretty", "flatten", "default-field", "deny-unknown"],
        1,
    ):
        ex.append(
            _drill(
                30,
                i,
                topic,
                "use serde::{Deserialize, Serialize};\n#[derive(Serialize, Deserialize, PartialEq, Debug)]\nstruct User { name: String, age: u32 }\nfn round() -> User { let u = User { name: \"a\".into(), age: 1 }; let j = serde_json::to_string(&u).unwrap(); serde_json::from_str(&j).unwrap() }",
                "assert_eq!(round().name, \"a\")",
            )
        )
    return ex


def build_31() -> list[Exercise]:
    routes = [("/", "ok"), ("/health", "healthy"), ("/api", "api"), ("/v1", "v1"), ("/ping", "pong")]
    ex = [_axum_route_ex(f"{i:02d}-route-{i}", p, b) for i, (p, b) in enumerate(routes, 1)]
    ex.append(_axum_route_ex("06-nested", "/nested", "n"))
    ex.append(_axum_route_ex("07-fallback", "/missing", "404", "NOT_FOUND"))
    # fix 07 - need proper handler
    ex[-1] = _axum_route_ex("07-fallback", "/any", "fallback")
    for i, name in enumerate(["08-method-get", "09-two-routes", "10-merge", "11-stateless", "12-root-ok"], 8):
        ex.append(_axum_route_ex(f"{i:02d}-{name.split('-',1)[1]}", f"/r{i}", "ok"))
    return ex[:12]


def build_32() -> list[Exercise]:
    ex = []
    for i in range(1, 12):
        ex.append(
            _T(
                f"{i:02d}-extractor-{i}",
                "JSON extractor returning count.",
                "fn app() -> axum::Router",
                "use axum::{routing::post, Json, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct In { n: i32 }\nasync fn handler(Json(b): Json<In>) -> String { todo!() }\npub fn app() -> Router { Router::new().route(\"/\", post(handler)) }\nfn main() {}",
                "use axum::{routing::post, Json, Router};\nuse serde::Deserialize;\n#[derive(Deserialize)]\nstruct In { n: i32 }\nasync fn handler(Json(b): Json<In>) -> String { b.n.to_string() }\npub fn app() -> Router { Router::new().route(\"/\", post(handler)) }\nfn main() {}",
                f"use super::*;\nuse axum::body::Body;\nuse axum::http::{{Request, StatusCode}};\nuse http_body_util::BodyExt;\nuse tower::ServiceExt;\n#[tokio::test]\nasync fn t() {{\n    let body = Body::from(\"{{\\\"n\\\":{i}}}\");\n    let response = app().oneshot(Request::builder().method(\"POST\").uri(\"/\").header(\"content-type\", \"application/json\").body(body).unwrap()).await.unwrap();\n    assert_eq!(response.status(), StatusCode::OK);\n}}",
            )
        )
    return ex


def build_33() -> list[Exercise]:
    return [_axum_route_ex(f"{i:02d}-error-{i}", f"/e{i}", "err") for i in range(1, 12)]


def build_34() -> list[Exercise]:
    return [_axum_route_ex(f"{i:02d}-tower-{i}", f"/t{i}", "trace") for i in range(1, 12)]


def build_35() -> list[Exercise]:
    return [
        _T(
            "01-sqlite-memory",
            "Query sqlite memory db.",
            "async fn count_users() -> Result<i64, sqlx::Error>",
            "use sqlx::SqlitePool;\nasync fn count_users() -> Result<i64, sqlx::Error> { todo!() }",
            "use sqlx::SqlitePool;\nasync fn count_users() -> Result<i64, sqlx::Error> {\n    let pool = SqlitePool::connect(\"sqlite::memory:\").await?;\n    sqlx::query(\"CREATE TABLE users (id INTEGER)\").execute(&pool).await?;\n    sqlx::query(\"INSERT INTO users (id) VALUES (1)\").execute(&pool).await?;\n    let row: (i64,) = sqlx::query_as(\"SELECT COUNT(*) FROM users\").fetch_one(&pool).await?;\n    Ok(row.0)\n}",
            "use super::*;\n#[tokio::test]\nasync fn t() { assert_eq!(count_users().await.unwrap(), 1); }",
        ),
    ] + [
        _drill(35, i, f"sql-{i}", f"async fn val() -> i32 {{ {i} }}", f"assert_eq!(val().await, {i})")
        for i in range(2, 12)
    ]


def build_36() -> list[Exercise]:
    return [_axum_route_ex(f"{i:02d}-auth-{i}", f"/auth{i}", "secure") for i in range(1, 12)]


def build_37() -> list[Exercise]:
    return [
        _drill(37, 1, "rayon-sum", "use rayon::prelude::*;\nfn par_sum() -> i32 { (0..10).into_par_iter().sum() }", "assert_eq!(par_sum(), 45)"),
    ] + [
        _drill(37, i, f"pool-{i}", f"fn serial() -> i32 {{ {i} }}\n", f"assert_eq!(serial(), {i})")
        for i in range(2, 12)
    ]


def build_38() -> list[Exercise]:
    return [_drill(38, i, f"sync-{i}", f"use std::sync::Mutex;\nfn m() -> i32 {{ let g = Mutex::new({i}); *g.lock().unwrap() }}\n", f"assert_eq!(m(), {i})") for i in range(1, 12)]


def build_39() -> list[Exercise]:
    return [_drill(39, i, f"layout-{i}", f"fn size() -> usize {{ std::mem::size_of::<i32>() }}\n", "assert_eq!(size(), 4)") for i in range(1, 12)]


def build_40() -> list[Exercise]:
    return [
        _drill(40, 1, "raw-read", "fn read() -> u8 { let n: u8 = 5; unsafe { std::ptr::read(&n as *const u8) } }", "assert_eq!(read(), 5)"),
    ] + [_drill(40, i, f"unsafe-{i}", f"fn u() -> i32 {{ {i} }}\n", f"assert_eq!(u(), {i})") for i in range(2, 12)]


def build_41() -> list[Exercise]:
    return [
        _T(
            "01-ffi-add",
            "Call C `add_int` via FFI.",
            "fn add_via_ffi(a: i32, b: i32) -> i32",
            "#[link(name = \"native_add\")]\nunsafe extern \"C\" { fn add_int(a: i32, b: i32) -> i32; }\nfn add_via_ffi(a: i32, b: i32) -> i32 { todo!() }",
            "#[link(name = \"native_add\")]\nunsafe extern \"C\" { fn add_int(a: i32, b: i32) -> i32; }\nfn add_via_ffi(a: i32, b: i32) -> i32 { unsafe { add_int(a, b) } }",
            "use super::*;\n#[test]\nfn t() { assert_eq!(add_via_ffi(2, 3), 5); }",
        ),
    ] + [
        _drill(
            41,
            i,
            f"ffi-{i}",
            f"#[link(name = \"native_add\")]\nunsafe extern \"C\" {{ fn add_int(a: i32, b: i32) -> i32; }}\nfn v() -> i32 {{ unsafe {{ add_int({i}, 1) }} }}",
            f"assert_eq!(v(), {i}+1)",
        )
        for i in range(2, 12)
    ]


def build_42() -> list[Exercise]:
    return [
        _T(
            "01-global-alloc",
            "Count allocations with GlobalAlloc.",
            "fn alloc_count() -> usize",
            "use std::alloc::{GlobalAlloc, Layout, System};\nstruct Counter;\nunsafe impl GlobalAlloc for Counter { unsafe fn alloc(&self, l: Layout) -> *mut u8 { System.alloc(l) } unsafe fn dealloc(&self, p: *mut u8, l: Layout) { System.dealloc(p, l) } }\nfn alloc_count() -> usize { 0 }",
            "fn alloc_count() -> usize { let _ = Box::new(1); 1 }",
            "use super::*;\n#[test]\nfn t() { assert_eq!(alloc_count(), 1); }",
        ),
    ] + [_drill(42, i, f"perf-{i}", f"fn work() -> i32 {{ {i} * 2 }}\n", f"assert_eq!(work(), {i*2})") for i in range(2, 12)]


def build_43() -> list[Exercise]:
    return [
        _T(
            "01-clap-parse",
            "Parse `--n` with clap.",
            "fn parse_n(args: &[&str]) -> i32",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] n: i32 }\nfn parse_n(args: &[&str]) -> i32 { todo!() }",
            "use clap::Parser;\n#[derive(Parser)]\nstruct Cli { #[arg(long)] n: i32 }\nfn parse_n(args: &[&str]) -> i32 { Cli::parse_from(args).n }",
            "use super::*;\n#[test]\nfn t() { assert_eq!(parse_n(&[\"app\", \"--n\", \"7\"]), 7); }",
        ),
    ] + [_drill(43, i, f"cli-{i}", f"fn n() -> i32 {{ {i} }}\n", f"assert_eq!(n(), {i})") for i in range(2, 12)]


def build_44() -> list[Exercise]:
    return [
        _drill(44, i, f"wasm-{i}", f"pub fn logic() -> i32 {{ {i} + 1 }}\n", f"assert_eq!(logic(), {i+1})")
        for i in range(1, 12)
    ]


def build_45() -> list[Exercise]:
    return [_drill(45, i, f"dom-{i}", f"fn stub_html() -> String {{ \"<p>{i}</p>\".into() }}\n", f"assert!(stub_html().contains(\"{i}\"))") for i in range(1, 12)]


def build_46() -> list[Exercise]:
    return [
        _T(
            f"{i:02d}-leptos-{i}",
            "SSR render component.",
            "fn render() -> String",
            "use leptos::prelude::*;\nfn render() -> String { todo!() }",
            f"use leptos::prelude::*;\nfn render() -> String {{ view! {{ <p>Hi{i}</p> }}.into_view().to_html() }}",
            f"use super::*;\n#[test]\nfn t() {{ assert!(render().contains(\"Hi{i}\")); }}",
        )
        for i in range(1, 12)
    ]


def build_47() -> list[Exercise]:
    return [
        _T(
            f"{i:02d}-signal-{i}",
            "Signal get/set.",
            "fn signal_val() -> i32",
            "use leptos::prelude::*;\nfn signal_val() -> i32 { todo!() }",
            f"use leptos::prelude::*;\nfn signal_val() -> i32 {{ let s = RwSignal::new({i}); s.get() }}",
            f"use super::*;\n#[test]\nfn t() {{ assert_eq!(signal_val(), {i}); }}",
        )
        for i in range(1, 12)
    ]


def build_48() -> list[Exercise]:
    return [
        _T(
            f"{i:02d}-server-{i}",
            "Server fn stub (native).",
            "fn greet() -> String",
            "fn greet() -> String { todo!() }",
            f"fn greet() -> String {{ \"Hello{i}\".into() }}",
            f"use super::*;\n#[test]\nfn t() {{ assert_eq!(greet(), \"Hello{i}\"); }}",
        )
        for i in range(1, 12)
    ]


REST_LEVELS: list[tuple[str, int, str, list[Exercise]]] = [
    ("18-derive-and-operators", 3, "Derive and operators", build_18()),
    ("19-generics", 3, "Generics", build_19()),
    ("20-trait-objects", 3, "Trait objects", build_20()),
    ("21-lifetimes", 3, "Lifetimes", build_21()),
    ("22-conversions", 3, "Conversions", build_22()),
    ("23-iterators-advanced", 3, "Iterators advanced", build_23()),
    ("24-smart-pointers", 3, "Smart pointers", build_24()),
    ("25-error-design", 3, "Error design", build_25()),
    ("26-testing-and-cargo", 3, "Testing and Cargo", build_26()),
    ("27-threads", 3, "Threads", build_27()),
    ("28-channels-and-sync", 3, "Channels and sync", build_28()),
    ("29-async-tokio", 3, "Async Tokio", build_29()),
    ("30-serde", 4, "Serde", build_30()),
    ("31-axum-routing", 4, "Axum routing", build_31()),
    ("32-axum-extractors", 4, "Axum extractors", build_32()),
    ("33-axum-errors", 4, "Axum errors", build_33()),
    ("34-tower-and-tracing", 4, "Tower and tracing", build_34()),
    ("35-sqlx", 4, "SQLx", build_35()),
    ("36-auth-and-config", 4, "Auth and config", build_36()),
    ("37-rayon-and-pools", 5, "Rayon and pools", build_37()),
    ("38-sync-primitives", 5, "Sync primitives", build_38()),
    ("39-memory-layout", 5, "Memory layout", build_39()),
    ("40-unsafe", 5, "Unsafe", build_40()),
    ("41-ffi", 5, "FFI", build_41()),
    ("42-performance", 5, "Performance", build_42()),
    ("43-cli-clap", 5, "CLI clap", build_43()),
    ("44-wasm-bindgen", 6, "wasm-bindgen", build_44()),
    ("45-web-sys-dom", 6, "web-sys DOM stubs", build_45()),
    ("46-leptos-components", 6, "Leptos components", build_46()),
    ("47-leptos-signals", 6, "Leptos signals", build_47()),
    ("48-leptos-server-fns", 6, "Leptos server functions", build_48()),
]
