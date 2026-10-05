"""Levels 18–48 exercise definitions."""

from __future__ import annotations

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
    return [_axum_route_ex(f"{i:02d}-auth-{i}", f"/auth{i}", "secure") for i in range(1, 12)]


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
    return [_drill(38, i, f"sync-{i}", f"use std::sync::Mutex;\nfn m() -> i32 {{ let g = Mutex::new({i}); *g.lock().unwrap() }}\n", f"assert_eq!(m(), {i})") for i in range(1, 12)]


def build_39() -> list[Exercise]:
    return [_drill(39, i, f"layout-{i}", f"fn size() -> usize {{ std::mem::size_of::<i32>() }}\n", "assert_eq!(size(), 4)") for i in range(1, 12)]


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
            "transmute-size",
            "fn bool_from_u8() -> bool { let b: u8 = 1; // INVARIANT: only 0/1 used as bool here\n unsafe { std::mem::transmute::<u8, bool>(b) } }",
            "assert!(bool_from_u8());",
            "assert_eq!(bool_from_u8() as u8, 1);",
            "assert_ne!(bool_from_u8() as u8, 0);",
            task="Transmute `u8` 1 to `bool` (document the invariant).",
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
            "read-volatile",
            "fn read_volatile() -> i32 { let x = 99i32; // INVARIANT: `x` is not mutated concurrently\n unsafe { std::ptr::read_volatile(&x as *const i32) } }",
            "assert_eq!(read_volatile(), 99);",
            "assert_ne!(read_volatile(), 0);",
            "assert!(read_volatile() > 50);",
            task="Read an `i32` with `read_volatile` (document why).",
        ),
        _drill(
            40,
            8,
            "static-mut-counter",
            "static mut COUNT: u32 = 0;\nfn bump_unsafe() -> u32 { // INVARIANT: single-threaded test only\n unsafe { COUNT += 1; COUNT } }",
            "assert_eq!(bump_unsafe(), 1);",
            "assert_eq!(bump_unsafe(), 2);",
            "assert!(bump_unsafe() >= 3);",
            task="Increment a `static mut` counter inside `unsafe` (tests run serially).",
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
        _drill(
            41,
            5,
            "ffi-ten",
            f"{link}\nfn ten() -> i32 {{ unsafe {{ add_int(7, 3) }} }}",
            "assert_eq!(ten(), 10);",
            "assert!(ten() > 0);",
            "assert_ne!(ten(), 0);",
            task="Return 10 from `add_int(7, 3)`.",
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
