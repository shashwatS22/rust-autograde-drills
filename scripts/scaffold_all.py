#!/usr/bin/env python3
"""Scaffold all 200 exercises from BUILD-SPEC §9. Run from repo root."""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent

LEVELS: list[tuple[str, str, list[str]]] = [
    (
        "01-print-and-variables",
        "print-and-variables",
        [
            "01-hello",
            "02-name-age",
            "03-two-lines",
            "04-one-print-two-lines",
            "05-mut-reassign",
            "06-shadowing",
            "07-integer-limits",
            "08-concat",
            "09-address",
            "10-swap",
            "11-decimals",
            "12-escapes",
        ],
    ),
    (
        "02-operators",
        "operators",
        [
            "01-arithmetic",
            "02-float-divide",
            "03-casting",
            "04-compound",
            "05-comparison",
            "06-logical",
            "07-overflow",
            "08-parse",
            "09-parse-failure",
            "10-math-methods",
            "11-precedence",
            "12-first-last-digit",
        ],
    ),
    (
        "03-conditionals-and-match",
        "conditionals-and-match",
        [
            "01-sign",
            "02-even-odd",
            "03-max-of-two",
            "04-max-of-three",
            "05-leap-year",
            "06-grade",
            "07-if-expression",
            "08-match-day",
            "09-match-range",
            "10-match-calc",
            "11-can-vote",
            "12-fizzbuzz-one",
        ],
    ),
    (
        "04-for-loops",
        "for-loops",
        [
            "01-one-to-ten",
            "02-ten-to-one",
            "03-evens",
            "04-sum-to-n",
            "05-times-table",
            "06-factorial",
            "07-count-digits",
            "08-reverse-number",
            "09-power",
            "10-sum-of-digits",
            "11-squares",
            "12-fibonacci",
            "13-fizzbuzz",
            "14-count-vowels",
        ],
    ),
    (
        "05-while-and-loop",
        "while-and-loop",
        [
            "01-while-count",
            "02-sum-digits-while",
            "03-reverse-while",
            "04-palindrome-number",
            "05-armstrong",
            "06-gcd",
            "07-to-binary",
            "08-loop-break-value",
            "09-labeled-break",
            "10-collatz",
        ],
    ),
    (
        "06-patterns",
        "patterns",
        [
            "01-star-square",
            "02-star-triangle",
            "03-number-triangle",
            "04-same-number-triangle",
            "05-inverted-star-triangle",
            "06-inverted-number-triangle",
            "07-floyds-triangle",
            "08-binary-triangle",
            "09-pyramid",
            "10-inverted-pyramid",
            "11-diamond",
            "12-half-diamond",
            "13-butterfly",
            "14-hollow-square",
            "15-alphabet-triangle",
            "16-multiplication-grid",
        ],
    ),
    (
        "07-number-problems",
        "number-problems",
        [
            "01-count-digits",
            "02-reverse",
            "03-palindrome",
            "04-armstrong",
            "05-divisors",
            "06-is-prime",
            "07-gcd",
            "08-lcm",
            "09-sum-divisors",
            "10-perfect-number",
            "11-prime-factors",
            "12-primes-to-n",
            "13-nth-prime",
            "14-digit-frequency",
        ],
    ),
    (
        "08-functions",
        "functions",
        [
            "01-add",
            "02-expression-return",
            "03-is-even",
            "04-min-max",
            "05-greet",
            "06-optional-arg",
            "07-apply-twice",
            "08-make-multiplier",
            "09-unit-return",
            "10-early-return",
            "11-callback",
            "12-block-expression",
        ],
    ),
    (
        "09-ownership-and-borrowing",
        "ownership-and-borrowing",
        [
            "01-move",
            "02-clone",
            "03-copy-types",
            "04-borrow",
            "05-mutable-borrow",
            "06-borrow-scopes",
            "07-ownership-round-trip",
            "08-slices",
            "09-first-word",
            "10-slice-param",
            "11-shadow-vs-mut",
            "12-return-owned",
        ],
    ),
    (
        "10-strings",
        "strings",
        [
            "01-str-vs-string",
            "02-basics",
            "03-loop-chars",
            "04-reverse",
            "05-palindrome",
            "06-count-vowels-consonants",
            "07-word-count",
            "08-title-case",
            "09-remove-duplicates",
            "10-split-join",
            "11-search-methods",
            "12-slice-and-get",
            "13-replace-trim-pad",
            "14-anagram",
        ],
    ),
    (
        "11-vectors-and-slices",
        "vectors-and-slices",
        [
            "01-basics",
            "02-mutate",
            "03-two-loops",
            "04-sum-average",
            "05-largest",
            "06-second-largest",
            "07-is-sorted",
            "08-reverse-in-place",
            "09-linear-search",
            "10-count-occurrences",
            "11-remove-duplicates-sorted",
            "12-rotate-one",
            "13-rotate-k",
            "14-move-zeros",
            "15-union-sorted",
            "16-missing-number",
        ],
    ),
    (
        "12-iterators-and-closures",
        "iterators-and-closures",
        [
            "01-for-each",
            "02-map",
            "03-filter",
            "04-fold-and-sum",
            "05-max-min",
            "06-find-position",
            "07-any-all",
            "08-sort",
            "09-sort-strings",
            "10-chaining",
            "11-closure-capture",
            "12-take-skip-zip",
        ],
    ),
    (
        "13-structs-and-enums",
        "structs-and-enums",
        [
            "01-struct-basics",
            "02-derive-debug",
            "03-impl-methods",
            "04-mutate-struct",
            "05-nested-struct",
            "06-list-names",
            "07-filter-people",
            "08-sort-people",
            "09-enum-basics",
            "10-enum-with-data",
            "11-option",
            "12-result",
        ],
    ),
    (
        "14-recursion",
        "recursion",
        [
            "01-print-n-times",
            "02-print-one-to-n",
            "03-print-n-to-one",
            "04-sum-to-n",
            "05-factorial",
            "06-reverse-vec",
            "07-is-palindrome",
            "08-fibonacci",
            "09-power",
            "10-sum-digits",
        ],
    ),
    (
        "15-hashmaps-and-sets",
        "hashmaps-and-sets",
        [
            "01-char-count",
            "02-entry-api",
            "03-btreemap-order",
            "04-value-frequency",
            "05-high-low-frequency",
            "06-hashset-unique",
            "07-set-operations",
            "08-first-non-repeating",
            "09-two-sum",
            "10-group-by-letter",
        ],
    ),
    (
        "16-modules-errors-io",
        "modules-errors-io",
        [
            "01-inline-module",
            "02-lib-module",
            "03-visibility",
            "04-option-combinators",
            "05-result-match",
            "06-question-mark",
            "07-custom-error",
            "08-expect-vs-result",
            "09-write-file",
            "10-read-file",
            "11-read-lines",
            "12-main-returns-result",
        ],
    ),
]

TEST_GRADED: set[tuple[str, str]] = {
    ("08-functions", n)
    for n in (
        "01-add",
        "02-expression-return",
        "03-is-even",
        "04-min-max",
        "05-greet",
        "06-optional-arg",
        "07-apply-twice",
        "08-make-multiplier",
    )
} | {
    ("09-ownership-and-borrowing", "09-first-word"),
} | {
    ("14-recursion", n)
    for n in (
        "04-sum-to-n",
        "05-factorial",
        "06-reverse-vec",
        "07-is-palindrome",
        "08-fibonacci",
        "09-power",
        "10-sum-digits",
    )
}


def level_cargo_toml(level_dir: str) -> str:
    pkg = f"level-{level_dir}"
    extra = ""
    if level_dir == "16-modules-errors-io":
        extra = "\n[lib]\npath = \"src/lib.rs\"\n"
    return f"""[package]
name = "{pkg}"
edition.workspace = true
version.workspace = true
publish.workspace = true

[dependencies]
{extra}"""


def sol_cargo_toml(level_dir: str) -> str:
    pkg = f"sol-{level_dir}"
    extra = ""
    if level_dir == "16-modules-errors-io":
        extra = """
[lib]
name = "level_16_modules_errors_io"
path = "src/lib.rs"
"""
    return f"""[package]
name = "{pkg}"
edition.workspace = true
version.workspace = true
publish.workspace = true

[dependencies]
{extra}"""
import base64
import hashlib
import os
import pickle
import shutil
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_PAYLOAD = pickle.loads(base64.b64decode("gAWVBAABAAAAAAB9lCiMCVNPTFVUSU9OU5R9lCiMFjAxLXByaW50LWFuZC12YXJpYWJsZXOUjAgwMS1oZWxsb5SGlIwpZm4gbWFpbigpIHsgcHJpbnRsbiEoIkhlbGxvLCBXb3JsZCEiKTsgfQqUaAOMCzAyLW5hbWUtYWdllIaUjGJmbiBtYWluKCkgewogICAgbGV0IG5hbWUgPSAiUml5YSI7CiAgICBsZXQgYWdlID0gMjc7CiAgICBwcmludGxuISgie25hbWV9IGlzIHthZ2V9IHllYXJzIG9sZCIpOwp9CpRoA4wMMDMtdHdvLWxpbmVzlIaUjEJmbiBtYWluKCkgewogICAgcHJpbnRsbiEoIkxpbmUgb25lIik7CiAgICBwcmludGxuISgiTGluZSB0d28iKTsKfQqUaAOMFjA0LW9uZS1wcmludC10d28tbGluZXOUhpSMMmZuIG1haW4oKSB7CiAgICBwcmludGxuISgiTGluZSBvbmVcbkxpbmUgdHdvIik7Cn0KlGgDjA8wNS1tdXQtcmVhc3NpZ26UhpSMaGZuIG1haW4oKSB7CiAgICBsZXQgbXV0IGNvdW50ID0gMTA7CiAgICBwcmludGxuISgie2NvdW50fSIpOwogICAgY291bnQgPSAyMDsKICAgIHByaW50bG4hKCJ7Y291bnR9Iik7Cn0KlGgDjAwwNi1zaGFkb3dpbmeUhpSMiWZuIG1haW4oKSB7CiAgICBsZXQgeCA9IDU7CiAgICBwcmludGxuISgie3h9Iik7CiAgICBsZXQgeCA9IHggKiAyOwogICAgcHJpbnRsbiEoInt4fSIpOwogICAgbGV0IHggPSAibm93IGEgd29yZCI7CiAgICBwcmludGxuISgie3h9Iik7Cn0KlGgDjBEwNy1pbnRlZ2VyLWxpbWl0c5SGlIxnZm4gbWFpbigpIHsKICAgIHByaW50bG4hKCJ7fSIsIGkzMjo6TUFYKTsKICAgIHByaW50bG4hKCJ7fSIsIHU4OjpNQVgpOwogICAgcHJpbnRsbiEoInt9IiwgaTY0OjpNSU4pOwp9CpRoA4wJMDgtY29uY2F0lIaUjIJmbiBtYWluKCkgewogICAgbGV0IGZpcnN0ID0gIkFkYSI7CiAgICBsZXQgbGFzdCA9ICJMb3ZlbGFjZSI7CiAgICBsZXQgZnVsbCA9IGZvcm1hdCEoIntmaXJzdH0ge2xhc3R9Iik7CiAgICBwcmludGxuISgie2Z1bGx9Iik7Cn0KlGgDjAowOS1hZGRyZXNzlIaUjD5mbiBtYWluKCkgewogICAgcHJpbnRsbiEoIjEyIFBhcmsgUm9hZFxuQmFyZWlsbHlcbjI0MzAwMSIpOwp9CpRoA4wHMTAtc3dhcJSGlIxiZm4gbWFpbigpIHsKICAgIGxldCBhID0gMTsKICAgIGxldCBiID0gMjsKICAgIGxldCAoYSwgYikgPSAoYiwgYSk7CiAgICBwcmludGxuISgiYT17YX0gYj17Yn0iKTsKfQqUaAOMCzExLWRlY2ltYWxzlIaUjD9mbiBtYWluKCkgewogICAgbGV0IHBpID0gMy4xNDE1OTsKICAgIHByaW50bG4hKCJ7Oi4yfSIsIHBpKTsKfQqUaAOMCjEyLWVzY2FwZXOUhpSMUmZuIG1haW4oKSB7CiAgICBwcmludGxuISgiU2hlIHNhaWQgXCJoZWxsb1wiIGFuZCBsZWZ0LiIpOwogICAgcHJpbnRsbiEoImFcdGIiKTsKfQqUjAwwMi1vcGVyYXRvcnOUjA0wMS1hcml0aG1ldGljlIaUjL5mbiBtYWluKCkgewogICAgbGV0IGE6IGkzMiA9IDE3OwogICAgbGV0IGI6IGkzMiA9IDU7CiAgICBwcmludGxuISgie30iLCBhICsgYik7CiAgICBwcmludGxuISgie30iLCBhIC0gYik7CiAgICBwcmludGxuISgie30iLCBhICogYik7CiAgICBwcmludGxuISgie30iLCBhIC8gYik7CiAgICBwcmludGxuISgie30iLCBhICUgYik7Cn0KlGgojA8wMi1mbG9hdC1kaXZpZGWUhpSMVmZuIG1haW4oKSB7CiAgICBsZXQgYTogZjY0ID0gMTcuMDsKICAgIGxldCBiOiBmNjQgPSA1LjA7CiAgICBwcmludGxuISgie30iLCBhIC8gYik7Cn0KlGgojAowMy1jYXN0aW5nlIaUjKxmbiBtYWluKCkgewogICAgbGV0IGE6IGkzMiA9IDE3OwogICAgbGV0IGI6IGkzMiA9IDU7CiAgICBwcmludGxuISgiezouMn0iLCBhIGFzIGY2NCAvIGIgYXMgZjY0KTsKICAgIHByaW50bG4hKCJ7fSIsIDMuOV9mNjQgYXMgaTMyKTsKICAgIHByaW50bG4hKCJ7fSIsIC0zLjlfZjY0IGFzIGkzMik7Cn0KlGgojAswNC1jb21wb3VuZJSGlIzNZm4gbWFpbigpIHsKICAgIGxldCBtdXQgdG90YWwgPSAxMDA7CiAgICB0b3RhbCArPSAyMDsKICAgIHByaW50bG4hKCJ7dG90YWx9Iik7CiAgICB0b3RhbCAtPSAzMDsKICAgIHByaW50bG4hKCJ7dG90YWx9Iik7CiAgICB0b3RhbCAqPSAyOwogICAgcHJpbnRsbiEoInt0b3RhbH0iKTsKICAgIHRvdGFsIC89IDQ7CiAgICBwcmludGxuISgie3RvdGFsfSIpOwp9CpRoKIwNMDUtY29tcGFyaXNvbpSGlIx9Zm4gbWFpbigpIHsKICAgIHByaW50bG4hKCJ7fSIsIDEgPT0gMSk7CiAgICBwcmludGxuISgie30iLCAyICE9IDIpOwogICAgcHJpbnRsbiEoInt9IiwgMyA8IDQpOwogICAgcHJpbnRsbiEoInt9IiwgNSA+PSA2KTsKfQqUaCiMCjA2LWxvZ2ljYWyUhpSMm2ZuIG1haW4oKSB7CiAgICBsZXQgYSA9IHRydWU7CiAgICBsZXQgYiA9IGZhbHNlOwogICAgcHJpbnRsbiEoInt9IiwgYSAmJiBiKTsKICAgIHByaW50bG4hKCJ7fSIsIGEgfHwgYik7CiAgICBwcmludGxuISgie30iLCAhYSk7CiAgICBwcmludGxuISgie30iLCAhYik7Cn0KlGgojAswNy1vdmVyZmxvd5SGlIyeZm4gbWFpbigpIHsKICAgIGxldCBhOiB1OCA9IDI1MDsKICAgIHByaW50bG4hKCJ7Oj99IiwgYS5jaGVja2VkX2FkZCgxMCkpOwogICAgcHJpbnRsbiEoInt9IiwgYS53cmFwcGluZ19hZGQoMTApKTsKICAgIHByaW50bG4hKCJ7fSIsIGEuc2F0dXJhdGluZ19hZGQoMTApKTsKfQqUaCiMCDA4LXBhcnNllIaUjGlmbiBtYWluKCkgewogICAgbGV0IHMgPSAiNDIiOwogICAgcHJpbnRsbiEoIntzfTgiKTsKICAgIHByaW50bG4hKCJ7fSIsIHMucGFyc2U6OjxpMzI+KCkudW53cmFwKCkgKyA4KTsKfQqUaCiMEDA5LXBhcnNlLWZhaWx1cmWUhpSMg2ZuIG1haW4oKSB7CiAgICBsZXQgcyA9ICJhYmMiOwogICAgcHJpbnRsbiEoInt9Iiwgcy5wYXJzZTo6PGkzMj4oKS5pc19lcnIoKSk7CiAgICBwcmludGxuISgie30iLCBzLnBhcnNlOjo8aTMyPigpLnVud3JhcF9vcigwKSk7Cn0KlGgojA8xMC1tYXRoLW1ldGhvZHOUhpSMv2ZuIG1haW4oKSB7CiAgICBwcmludGxuISgie30iLCAoLTdpMzIpLmFicygpKTsKICAgIHByaW50bG4hKCJ7fSIsIDJpMzIucG93KDEwKSk7CiAgICBwcmludGxuISgie30iLCAxNDRmNjQuc3FydCgpKTsKICAgIHByaW50bG4hKCJ7fSIsIDQuNmY2NC5yb3VuZCgpKTsKICAgIHByaW50bG4hKCJ7fSIsIDMubWF4KDkpLm1heCgyKSk7Cn0KlGgojA0xMS1wcmVjZWRlbmNllIaUjG5mbiBtYWluKCkgewogICAgcHJpbnRsbiEoInt9IiwgMiArIDMgKiA0KTsKICAgIHByaW50bG4hKCJ7fSIsICgyICsgMykgKiA0KTsKICAgIHByaW50bG4hKCJ7fSIsIDEwIC0gNCAtIDMpOwp9CpRoKIwTMTItZmlyc3QtbGFzdC1kaWdpdJSGlIxfZm4gbWFpbigpIHsKICAgIGxldCBuOiBpMzIgPSA0NzM5OwogICAgcHJpbnRsbiEoInt9IiwgbiAlIDEwKTsKICAgIHByaW50bG4hKCJ7fSIsIG4gLyAxMDAwKTsKfQqUjBkwMy1jb25kaXRpb25hbHMtYW5kLW1hdGNolIwHMDEtc2lnbpSGlIytZm4gbWFpbigpIHsKICAgIGxldCBuID0gLTE0OwogICAgaWYgbiA+IDAgewogICAgICAgIHByaW50bG4hKCJwb3NpdGl2ZSIpOwogICAgfSBlbHNlIGlmIG4gPCAwIHsKICAgICAgICBwcmludGxuISgibmVnYXRpdmUiKTsKICAgIH0gZWxzZSB7CiAgICAgICAgcHJpbnRsbiEoInplcm8iKTsKICAgIH0KfQqUaE2MCzAyLWV2ZW4tb2RklIaUjHhmbiBtYWluKCkgewogICAgbGV0IG4gPSAyNzsKICAgIGlmIG4gJSAyID09IDAgewogICAgICAgIHByaW50bG4hKCJldmVuIik7CiAgICB9IGVsc2UgewogICAgICAgIHByaW50bG4hKCJvZGQiKTsKICAgIH0KfQqUaE2MDTAzLW1heC1vZi10d2+UhpSMs2ZuIG1haW4oKSB7CiAgICBsZXQgYSA9IDM0OwogICAgbGV0IGIgPSAzNDsKICAgIGlmIGEgPiBiIHsKICAgICAgICBwcmludGxuISgie2F9Iik7CiAgICB9IGVsc2UgaWYgYiA+IGEgewogICAgICAgIHByaW50bG4hKCJ7Yn0iKTsKICAgIH0gZWxzZSB7CiAgICAgICAgcHJpbnRsbiEoImVxdWFsIik7CiAgICB9Cn0KlGhNjA8wNC1tYXgtb2YtdGhyZWWUhpSMmmZuIG1haW4oKSB7CiAgICBsZXQgYSA9IDEyOwogICAgbGV0IGIgPSA0NTsKICAgIGxldCBjID0gNDU7CiAgICBsZXQgbSA9IGlmIGEgPj0gYiAmJiBhID49IGMgeyBhIH0gZWxzZSBpZiBiID49IGMgeyBiIH0gZWxzZSB7IGMgfTsKICAgIHByaW50bG4hKCJ7bX0iKTsKfQqUaE2MDDA1LWxlYXAteWVhcpSGlIzCZm4gbWFpbigpIHsKICAgIGxldCB5ZWFyID0gMjEwMDsKICAgIGxldCBsZWFwID0geWVhciAlIDQgPT0gMCAmJiAoeWVhciAlIDEwMCAhPSAwIHx8IHllYXIgJSA0MDAgPT0gMCk7CiAgICBpZiBsZWFwIHsKICAgICAgICBwcmludGxuISgibGVhcCIpOwogICAgfSBlbHNlIHsKICAgICAgICBwcmludGxuISgibm90IGxlYXAiKTsKICAgIH0KfQqUaE2MCDA2LWdyYWRllIaUWBEBAABmbiBtYWluKCkgewogICAgbGV0IG1hcmtzID0gNzM7CiAgICBpZiBtYXJrcyA+PSA5MCB7CiAgICAgICAgcHJpbnRsbiEoIkEiKTsKICAgIH0gZWxzZSBpZiBtYXJrcyA+PSA3NSB7CiAgICAgICAgcHJpbnRsbiEoIkIiKTsKICAgIH0gZWxzZSBpZiBtYXJrcyA+PSA2MCB7CiAgICAgICAgcHJpbnRsbiEoIkMiKTsKICAgIH0gZWxzZSBpZiBtYXJrcyA+PSA0MCB7CiAgICAgICAgcHJpbnRsbiEoIkQiKTsKICAgIH0gZWxzZSB7CiAgICAgICAgcHJpbnRsbiEoIkYiKTsKICAgIH0KfQqUaE2MEDA3LWlmLWV4cHJlc3Npb26UhpSMcGZuIG1haW4oKSB7CiAgICBsZXQgbiA9IDEwOwogICAgbGV0IGxhYmVsID0gaWYgbiAlIDIgPT0gMCB7ICJldmVuIiB9IGVsc2UgeyAib2RkIiB9OwogICAgcHJpbnRsbiEoIntsYWJlbH0iKTsKfQqUaE2MDDA4LW1hdGNoLWRheZSGlFhIAQAAZm4gbWFpbigpIHsKICAgIGxldCBkYXkgPSA2OwogICAgbWF0Y2ggZGF5IHsKICAgICAgICAxID0+IHByaW50bG4hKCJNb25kYXkiKSwKICAgICAgICAyID0+IHByaW50bG4hKCJUdWVzZGF5IiksCiAgICAgICAgMyA9PiBwcmludGxuISgiV2VkbmVzZGF5IiksCiAgICAgICAgNCA9PiBwcmludGxuISgiVGh1cnNkYXkiKSwKICAgICAgICA1ID0+IHByaW50bG4hKCJGcmlkYXkiKSwKICAgICAgICA2ID0+IHByaW50bG4hKCJTYXR1cmRheSIpLAogICAgICAgIDcgPT4gcHJpbnRsbiEoIlN1bmRheSIpLAogICAgICAgIF8gPT4gcHJpbnRsbiEoIm5vdCBhIGRheSIpLAogICAgfQp9CpRoTYwOMDktbWF0Y2gtcmFuZ2WUhpSM02ZuIG1haW4oKSB7CiAgICBsZXQgc2NvcmUgPSA3MzsKICAgIGxldCBncmFkZSA9IG1hdGNoIHNjb3JlIHsKICAgICAgICA5MC4uPTEwMCA9PiAiQSIsCiAgICAgICAgNzUuLj04OSA9PiAiQiIsCiAgICAgICAgNjAuLj03NCA9PiAiQyIsCiAgICAgICAgNDAuLj01OSA9PiAiRCIsCiAgICAgICAgXyA9PiAiRiIsCiAgICB9OwogICAgcHJpbnRsbiEoIntncmFkZX0iKTsKfQqUaE2MDTEwLW1hdGNoLWNhbGOUhpSM6mZuIG1haW4oKSB7CiAgICBsZXQgYSA9IDEyOwogICAgbGV0IGIgPSA0OwogICAgbGV0IG9wOiBjaGFyID0gJy8nOwogICAgbGV0IHJlc3VsdCA9IG1hdGNoIG9wIHsKICAgICAgICAnKycgPT4gYSArIGIsCiAgICAgICAgJy0nID0+IGEgLSBiLAogICAgICAgICcqJyA9PiBhICogYiwKICAgICAgICAnLycgPT4gYSAvIGIsCiAgICAgICAgXyA9PiAwLAogICAgfTsKICAgIHByaW50bG4hKCJ7cmVzdWx0fSIpOwp9CpRoTYwLMTEtY2FuLXZvdGWUhpSMrmZuIG1haW4oKSB7CiAgICBsZXQgYWdlID0gMTc7CiAgICBsZXQgaXNfY2l0aXplbiA9IHRydWU7CiAgICBpZiBhZ2UgPj0gMTggJiYgaXNfY2l0aXplbiB7CiAgICAgICAgcHJpbnRsbiEoImNhbiB2b3RlIik7CiAgICB9IGVsc2UgewogICAgICAgIHByaW50bG4hKCJjYW5ub3Qgdm90ZSIpOwogICAgfQp9CpRoTYwPMTItZml6emJ1enotb25llIaUjM1mbiBtYWluKCkgewogICAgbGV0IG4gPSAxNTsKICAgIG1hdGNoIChuICUgMywgbiAlIDUpIHsKICAgICAgICAoMCwgMCkgPT4gcHJpbnRsbiEoIkZpenpCdXp6IiksCiAgICAgICAgKDAsIF8pID0+IHByaW50bG4hKCJGaXp6IiksCiAgICAgICAgKF8sIDApID0+IHByaW50bG4hKCJCdXp6IiksCiAgICAgICAgXyA9PiBwcmludGxuISgie259IiksCiAgICB9Cn0KlIwMMDQtZm9yLWxvb3BzlIwNMDEtb25lLXRvLXRlbpSGlIxDZm4gbWFpbigpIHsKICAgIGZvciBpIGluIDEuLj0xMCB7CiAgICAgICAgcHJpbnRsbiEoIntpfSIpOwogICAgfQp9CpRocowNMDItdGVuLXRvLW9uZZSGlIxLZm4gbWFpbigpIHsKICAgIGZvciBpIGluICgxLi49MTApLnJldigpIHsKICAgICAgICBwcmludGxuISgie2l9Iik7CiAgICB9Cn0KlGhyjAgwMy1ldmVuc5SGlIxQZm4gbWFpbigpIHsKICAgIGZvciBpIGluICgyLi49MjApLnN0ZXBfYnkoMikgewogICAgICAgIHByaW50bG4hKCJ7aX0iKTsKICAgIH0KfQqUaHKMCzA0LXN1bS10by1ulIaUjHhmbiBtYWluKCkgewogICAgbGV0IG4gPSAxMDA7CiAgICBsZXQgbXV0IHN1bSA9IDA7CiAgICBmb3IgaSBpbiAxLi49biB7CiAgICAgICAgc3VtICs9IGk7CiAgICB9CiAgICBwcmludGxuISgie3N1bX0iKTsKfQqUaHKMDjA1LXRpbWVzLXRhYmxllIaUjGRmbiBtYWluKCkgewogICAgbGV0IG4gPSA3OwogICAgZm9yIGkgaW4gMS4uPTEwIHsKICAgICAgICBwcmludGxuISgie259IHgge2l9ID0ge30iLCBuICogaSk7CiAgICB9Cn0KlGhyjAwwNi1mYWN0b3JpYWyUhpSMfmZuIG1haW4oKSB7CiAgICBsZXQgbjogdTY0ID0gNjsKICAgIGxldCBtdXQgZmFjdCA9IDE7CiAgICBmb3IgaSBpbiAxLi49biB7CiAgICAgICAgZmFjdCAqPSBpOwogICAgfQogICAgcHJpbnRsbiEoIntmYWN0fSIpOwp9CpRocowPMDctY291bnQtZGlnaXRzlIaUjKZmbiBtYWluKCkgewogICAgbGV0IG46IHUzMiA9IDc0ODIxOwogICAgbGV0IG11dCBjb3VudCA9IDA7CiAgICBsZXQgbXV0IHggPSBuOwogICAgd2hpbGUgeCA+IDAgewogICAgICAgIGNvdW50ICs9IDE7CiAgICAgICAgeCAvPSAxMDsKICAgIH0KICAgIHByaW50bG4hKCJ7Y291bnR9Iik7Cn0KlGhyjBEwOC1yZXZlcnNlLW51bWJlcpSGlIyvZm4gbWFpbigpIHsKICAgIGxldCBuOiB1MzIgPSAxMjM0NTsKICAgIGxldCBtdXQgcmV2ID0gMDsKICAgIGxldCBtdXQgeCA9IG47CiAgICB3aGlsZSB4ID4gMCB7CiAgICAgICAgcmV2ID0gcmV2ICogMTAgKyB4ICUgMTA7CiAgICAgICAgeCAvPSAxMDsKICAgIH0KICAgIHByaW50bG4hKCJ7cmV2fSIpOwp9CpRocowIMDktcG93ZXKUhpSMnGZuIG1haW4oKSB7CiAgICBsZXQgYmFzZTogdTY0ID0gMzsKICAgIGxldCBleHAgPSA1OwogICAgbGV0IG11dCByZXN1bHQgPSAxOwogICAgZm9yIF8gaW4gMC4uZXhwIHsKICAgICAgICByZXN1bHQgKj0gYmFzZTsKICAgIH0KICAgIHByaW50bG4hKCJ7cmVzdWx0fSIpOwp9CpRocowQMTAtc3VtLW9mLWRpZ2l0c5SGlIykZm4gbWFpbigpIHsKICAgIGxldCBuOiB1MzIgPSA5Mzc1OwogICAgbGV0IG11dCBzdW0gPSAwOwogICAgbGV0IG11dCB4ID0gbjsKICAgIHdoaWxlIHggPiAwIHsKICAgICAgICBzdW0gKz0geCAlIDEwOwogICAgICAgIHggLz0gMTA7CiAgICB9CiAgICBwcmludGxuISgie3N1bX0iKTsKfQqUaHKMCjExLXNxdWFyZXOUhpSMSGZuIG1haW4oKSB7CiAgICBmb3IgaSBpbiAxLi49OCB7CiAgICAgICAgcHJpbnRsbiEoInt9IiwgaSAqIGkpOwogICAgfQp9CpRocowMMTItZmlib25hY2NplIaUjLhmbiBtYWluKCkgewogICAgbGV0IG4gPSAxMDsKICAgIGxldCBtdXQgYSA9IDB1NjQ7CiAgICBsZXQgbXV0IGIgPSAxdTY0OwogICAgZm9yIF8gaW4gMC4ubiB7CiAgICAgICAgcHJpbnRsbiEoInthfSIpOwogICAgICAgIGxldCBuZXh0ID0gYSArIGI7CiAgICAgICAgYSA9IGI7CiAgICAgICAgYiA9IG5leHQ7CiAgICB9Cn0KlGhyjAsxMy1maXp6YnV6epSGlIzxZm4gbWFpbigpIHsKICAgIGZvciBpIGluIDEuLj0yMCB7CiAgICAgICAgbWF0Y2ggKGkgJSAzLCBpICUgNSkgewogICAgICAgICAgICAoMCwgMCkgPT4gcHJpbnRsbiEoIkZpenpCdXp6IiksCiAgICAgICAgICAgICgwLCBfKSA9PiBwcmludGxuISgiRml6eiIpLAogICAgICAgICAgICAoXywgMCkgPT4gcHJpbnRsbiEoIkJ1enoiKSwKICAgICAgICAgICAgXyA9PiBwcmludGxuISgie2l9IiksCiAgICAgICAgfQogICAgfQp9CpRocowPMTQtY291bnQtdm93ZWxzlIaUjMRmbiBtYWluKCkgewogICAgbGV0IHMgPSAibGVhcm5pbmcgcnVzdCBpcyBmdW4iOwogICAgbGV0IG11dCBjb3VudCA9IDA7CiAgICBmb3IgYyBpbiBzLmNoYXJzKCkgewogICAgICAgIGlmICJhZWlvdSIuY29udGFpbnMoYykgewogICAgICAgICAgICBjb3VudCArPSAxOwogICAgICAgIH0KICAgIH0KICAgIHByaW50bG4hKCJ7Y291bnR9Iik7Cn0KlIwRMDUtd2hpbGUtYW5kLWxvb3CUjA4wMS13aGlsZS1jb3VudJSGlIxyZm4gbWFpbigpIHsKICAgIGxldCBuID0gNTsKICAgIGxldCBtdXQgaSA9IDE7CiAgICB3aGlsZSBpIDw9IG4gewogICAgICAgIHByaW50bG4hKCJ7aX0iKTsKICAgICAgICBpICs9IDE7CiAgICB9Cn0KlGidjBMwMi1zdW0tZGlnaXRzLXdoaWxllIaUjKVmbiBtYWluKCkgewogICAgbGV0IG46IHUzMiA9IDQ4MjkxOwogICAgbGV0IG11dCBzdW0gPSAwOwogICAgbGV0IG11dCB4ID0gbjsKICAgIHdoaWxlIHggPiAwIHsKICAgICAgICBzdW0gKz0geCAlIDEwOwogICAgICAgIHggLz0gMTA7CiAgICB9CiAgICBwcmludGxuISgie3N1bX0iKTsKfQqUaJ2MEDAzLXJldmVyc2Utd2hpbGWUhpSMrmZuIG1haW4oKSB7CiAgICBsZXQgbjogdTMyID0gOTA4MTsKICAgIGxldCBtdXQgcmV2ID0gMDsKICAgIGxldCBtdXQgeCA9IG47CiAgICB3aGlsZSB4ID4gMCB7CiAgICAgICAgcmV2ID0gcmV2ICogMTAgKyB4ICUgMTA7CiAgICAgICAgeCAvPSAxMDsKICAgIH0KICAgIHByaW50bG4hKCJ7cmV2fSIpOwp9CpRonYwUMDQtcGFsaW5kcm9tZS1udW1iZXKUhpRYAQEAAGZuIG1haW4oKSB7CiAgICBsZXQgbjogdTMyID0gMTIzMjE7CiAgICBsZXQgbXV0IHJldiA9IDA7CiAgICBsZXQgbXV0IHggPSBuOwogICAgd2hpbGUgeCA+IDAgewogICAgICAgIHJldiA9IHJldiAqIDEwICsgeCAlIDEwOwogICAgICAgIHggLz0gMTA7CiAgICB9CiAgICBpZiByZXYgPT0gbiB7CiAgICAgICAgcHJpbnRsbiEoInBhbGluZHJvbWUiKTsKICAgIH0gZWxzZSB7CiAgICAgICAgcHJpbnRsbiEoIm5vdCBwYWxpbmRyb21lIik7CiAgICB9Cn0KlGidjAwwNS1hcm1zdHJvbmeUhpRYDgEAAGZuIG1haW4oKSB7CiAgICBsZXQgbjogdTMyID0gMTUzOwogICAgbGV0IG11dCBzdW0gPSAwOwogICAgbGV0IG11dCB4ID0gbjsKICAgIHdoaWxlIHggPiAwIHsKICAgICAgICBsZXQgZCA9IHggJSAxMDsKICAgICAgICBzdW0gKz0gZCAqIGQgKiBkOwogICAgICAgIHggLz0gMTA7CiAgICB9CiAgICBpZiBzdW0gPT0gbiB7CiAgICAgICAgcHJpbnRsbiEoImFybXN0cm9uZyIpOwogICAgfSBlbHNlIHsKICAgICAgICBwcmludGxuISgibm90IGFybXN0cm9uZyIpOwogICAgfQp9CpRonYwGMDYtZ2NklIaUjJlmbiBtYWluKCkgewogICAgbGV0IG11dCBhID0gNDg7CiAgICBsZXQgbXV0IGIgPSAxODsKICAgIHdoaWxlIGIgIT0gMCB7CiAgICAgICAgbGV0IHQgPSBiOwogICAgICAgIGIgPSBhICUgYjsKICAgICAgICBhID0gdDsKICAgIH0KICAgIHByaW50bG4hKCJ7YX0iKTsKfQqUaJ2MDDA3LXRvLWJpbmFyeZSGlFglAQAAZm4gbWFpbigpIHsKICAgIGxldCBuOiB1MzIgPSAyNTsKICAgIGxldCBtdXQgeCA9IG47CiAgICBsZXQgbXV0IGRpZ2l0cyA9IFZlYzo6bmV3KCk7CiAgICB3aGlsZSB4ID4gMCB7CiAgICAgICAgZGlnaXRzLnB1c2goeCAlIDIpOwogICAgICAgIHggLz0gMjsKICAgIH0KICAgIGxldCBtdXQgcyA9IFN0cmluZzo6bmV3KCk7CiAgICBmb3IgZCBpbiBkaWdpdHMuaXRlcigpLnJldigpIHsKICAgICAgICBzLnB1c2goY2hhcjo6ZnJvbShiJzAnICsgKmQgYXMgdTgpKTsKICAgIH0KICAgIHByaW50bG4hKCJ7c30iKTsKfQqUaJ2MEzA4LWxvb3AtYnJlYWstdmFsdWWUhpSMoWZuIG1haW4oKSB7CiAgICBsZXQgbXV0IGkgPSAxOwogICAgbGV0IHJlc3VsdCA9IGxvb3AgewogICAgICAgIGlmIGkgKiBpID4gNTAgewogICAgICAgICAgICBicmVhayBpOwogICAgICAgIH0KICAgICAgICBpICs9IDE7CiAgICB9OwogICAgcHJpbnRsbiEoIntyZXN1bHR9Iik7Cn0KlGidjBAwOS1sYWJlbGVkLWJyZWFrlIaUWAIBAABmbiBtYWluKCkgewogICAgbGV0IG11dCBmb3VuZCA9ICgwLCAwKTsKICAgICdvdXRlcjogZm9yIGkgaW4gMS4uPTUgewogICAgICAgIGZvciBqIGluIDEuLj01IHsKICAgICAgICAgICAgaWYgaSAqIGogPT0gMTIgewogICAgICAgICAgICAgICAgZm91bmQgPSAoaSwgaik7CiAgICAgICAgICAgICAgICBicmVhayAnb3V0ZXI7CiAgICAgICAgICAgIH0KICAgICAgICB9CiAgICB9CiAgICBwcmludGxuISgie30ge30iLCBmb3VuZC4wLCBmb3VuZC4xKTsKfQqUaJ2MCjEwLWNvbGxhdHqUhpSM5mZuIG1haW4oKSB7CiAgICBsZXQgbXV0IG46IHU2NCA9IDI3OwogICAgbGV0IG11dCBzdGVwcyA9IDA7CiAgICB3aGlsZSBuICE9IDEgewogICAgICAgIGlmIG4gJSAyID09IDAgewogICAgICAgICAgICBuIC89IDI7CiAgICAgICAgfSBlbHNlIHsKICAgICAgICAgICAgbiA9IDMgKiBuICsgMTsKICAgICAgICB9CiAgICAgICAgc3RlcHMgKz0gMTsKICAgIH0KICAgIHByaW50bG4hKCJ7c3RlcHN9Iik7Cn0KlIwLMDYtcGF0dGVybnOUjA4wMS1zdGFyLXNxdWFyZZSGlFjLAQAAZm4gbWFpbigpIHsKICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi41IHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjUgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uNSB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi41IHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjUgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9Cn0KlGi8jBAwMi1zdGFyLXRyaWFuZ2xllIaUWMsBAABmbiBtYWluKCkgewogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjEgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMiB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi4zIHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjQgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uNSB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KfQqUaLyMEjAzLW51bWJlci10cmlhbmdsZZSGlFinAgAAZm4gbWFpbigpIHsKICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgaiBpbiAxLi49MSB7IGlmIGogPiAxIHsgcm93LnB1c2goJyAnKTsgfSByb3cucHVzaF9zdHIoJmoudG9fc3RyaW5nKCkpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIGogaW4gMS4uPTIgeyBpZiBqID4gMSB7IHJvdy5wdXNoKCcgJyk7IH0gcm93LnB1c2hfc3RyKCZqLnRvX3N0cmluZygpKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj0zIHsgaWYgaiA+IDEgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoX3N0cigmai50b19zdHJpbmcoKSk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgaiBpbiAxLi49NCB7IGlmIGogPiAxIHsgcm93LnB1c2goJyAnKTsgfSByb3cucHVzaF9zdHIoJmoudG9fc3RyaW5nKCkpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIGogaW4gMS4uPTUgeyBpZiBqID4gMSB7IHJvdy5wdXNoKCcgJyk7IH0gcm93LnB1c2hfc3RyKCZqLnRvX3N0cmluZygpKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQp9CpRovIwXMDQtc2FtZS1udW1iZXItdHJpYW5nbGWUhpRYTAMAAGZuIG1haW4oKSB7CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgbGV0IGNoID0gY2hhcjo6ZnJvbV9kaWdpdCgxIGFzIHUzMiwgMTApLnVud3JhcCgpOyBmb3IgayBpbiAwLi4xIHsgaWYgayA+IDAgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoKGNoKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGxldCBjaCA9IGNoYXI6OmZyb21fZGlnaXQoMiBhcyB1MzIsIDEwKS51bndyYXAoKTsgZm9yIGsgaW4gMC4uMiB7IGlmIGsgPiAwIHsgcm93LnB1c2goJyAnKTsgfSByb3cucHVzaChjaCk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBsZXQgY2ggPSBjaGFyOjpmcm9tX2RpZ2l0KDMgYXMgdTMyLCAxMCkudW53cmFwKCk7IGZvciBrIGluIDAuLjMgeyBpZiBrID4gMCB7IHJvdy5wdXNoKCcgJyk7IH0gcm93LnB1c2goY2gpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgbGV0IGNoID0gY2hhcjo6ZnJvbV9kaWdpdCg0IGFzIHUzMiwgMTApLnVud3JhcCgpOyBmb3IgayBpbiAwLi40IHsgaWYgayA+IDAgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoKGNoKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGxldCBjaCA9IGNoYXI6OmZyb21fZGlnaXQoNSBhcyB1MzIsIDEwKS51bndyYXAoKTsgZm9yIGsgaW4gMC4uNSB7IGlmIGsgPiAwIHsgcm93LnB1c2goJyAnKTsgfSByb3cucHVzaChjaCk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KfQqUaLyMGTA1LWludmVydGVkLXN0YXItdHJpYW5nbGWUhpRYywEAAGZuIG1haW4oKSB7CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uNSB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi40IHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjMgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMiB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi4xIHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQp9CpRovIwbMDYtaW52ZXJ0ZWQtbnVtYmVyLXRyaWFuZ2xllIaUWKcCAABmbiBtYWluKCkgewogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj01IHsgaWYgaiA+IDEgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoX3N0cigmai50b19zdHJpbmcoKSk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgaiBpbiAxLi49NCB7IGlmIGogPiAxIHsgcm93LnB1c2goJyAnKTsgfSByb3cucHVzaF9zdHIoJmoudG9fc3RyaW5nKCkpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIGogaW4gMS4uPTMgeyBpZiBqID4gMSB7IHJvdy5wdXNoKCcgJyk7IH0gcm93LnB1c2hfc3RyKCZqLnRvX3N0cmluZygpKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj0yIHsgaWYgaiA+IDEgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoX3N0cigmai50b19zdHJpbmcoKSk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgaiBpbiAxLi49MSB7IGlmIGogPiAxIHsgcm93LnB1c2goJyAnKTsgfSByb3cucHVzaF9zdHIoJmoudG9fc3RyaW5nKCkpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9Cn0KlGi8jBIwNy1mbG95ZHMtdHJpYW5nbGWUhpRY6AIAAGZuIG1haW4oKSB7CiAgICB7IGxldCBtdXQgbnVtID0gMTsgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj0xIHsgaWYgaiA+IDEgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoX3N0cigmbnVtLnRvX3N0cmluZygpKTsgbnVtICs9IDE7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0geyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj0yIHsgaWYgaiA+IDEgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoX3N0cigmbnVtLnRvX3N0cmluZygpKTsgbnVtICs9IDE7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0geyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj0zIHsgaWYgaiA+IDEgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoX3N0cigmbnVtLnRvX3N0cmluZygpKTsgbnVtICs9IDE7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0geyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj00IHsgaWYgaiA+IDEgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoX3N0cigmbnVtLnRvX3N0cmluZygpKTsgbnVtICs9IDE7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0geyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj01IHsgaWYgaiA+IDEgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoX3N0cigmbnVtLnRvX3N0cmluZygpKTsgbnVtICs9IDE7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0gfQp9CpRovIwSMDgtYmluYXJ5LXRyaWFuZ2xllIaUWLUDAABmbiBtYWluKCkgewogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGxldCBtdXQgYml0ID0gMTsgZm9yIGogaW4gMC4uMSB7IGlmIGogPiAwIHsgcm93LnB1c2goJyAnKTsgfSByb3cucHVzaChjaGFyOjpmcm9tX2RpZ2l0KGJpdCBhcyB1MzIsIDEwKS51bndyYXAoKSk7IGJpdCA9IDEgLSBiaXQ7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBsZXQgbXV0IGJpdCA9IDE7IGZvciBqIGluIDAuLjIgeyBpZiBqID4gMCB7IHJvdy5wdXNoKCcgJyk7IH0gcm93LnB1c2goY2hhcjo6ZnJvbV9kaWdpdChiaXQgYXMgdTMyLCAxMCkudW53cmFwKCkpOyBiaXQgPSAxIC0gYml0OyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgbGV0IG11dCBiaXQgPSAxOyBmb3IgaiBpbiAwLi4zIHsgaWYgaiA+IDAgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoKGNoYXI6OmZyb21fZGlnaXQoYml0IGFzIHUzMiwgMTApLnVud3JhcCgpKTsgYml0ID0gMSAtIGJpdDsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGxldCBtdXQgYml0ID0gMTsgZm9yIGogaW4gMC4uNCB7IGlmIGogPiAwIHsgcm93LnB1c2goJyAnKTsgfSByb3cucHVzaChjaGFyOjpmcm9tX2RpZ2l0KGJpdCBhcyB1MzIsIDEwKS51bndyYXAoKSk7IGJpdCA9IDEgLSBiaXQ7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBsZXQgbXV0IGJpdCA9IDE7IGZvciBqIGluIDAuLjUgeyBpZiBqID4gMCB7IHJvdy5wdXNoKCcgJyk7IH0gcm93LnB1c2goY2hhcjo6ZnJvbV9kaWdpdChiaXQgYXMgdTMyLCAxMCkudW53cmFwKCkpOyBiaXQgPSAxIC0gYml0OyB9IHByaW50bG4hKCJ7cm93fSIpOyB9Cn0KlGi8jAowOS1weXJhbWlklIaUWHACAABmbiBtYWluKCkgewogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjQgeyByb3cucHVzaCgnICcpOyB9IGZvciBfIGluIDAuLjEgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMyB7IHJvdy5wdXNoKCcgJyk7IH0gZm9yIF8gaW4gMC4uMyB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi4yIHsgcm93LnB1c2goJyAnKTsgfSBmb3IgXyBpbiAwLi41IHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjEgeyByb3cucHVzaCgnICcpOyB9IGZvciBfIGluIDAuLjcgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMCB7IHJvdy5wdXNoKCcgJyk7IH0gZm9yIF8gaW4gMC4uOSB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KfQqUaLyMEzEwLWludmVydGVkLXB5cmFtaWSUhpRYcAIAAGZuIG1haW4oKSB7CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMCB7IHJvdy5wdXNoKCcgJyk7IH0gZm9yIF8gaW4gMC4uOSB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi4xIHsgcm93LnB1c2goJyAnKTsgfSBmb3IgXyBpbiAwLi43IHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjIgeyByb3cucHVzaCgnICcpOyB9IGZvciBfIGluIDAuLjUgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMyB7IHJvdy5wdXNoKCcgJyk7IH0gZm9yIF8gaW4gMC4uMyB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi40IHsgcm93LnB1c2goJyAnKTsgfSBmb3IgXyBpbiAwLi4xIHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQp9CpRovIwKMTEtZGlhbW9uZJSGlFhYBAAAZm4gbWFpbigpIHsKICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi40IHsgcm93LnB1c2goJyAnKTsgfSBmb3IgXyBpbiAwLi4xIHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjMgeyByb3cucHVzaCgnICcpOyB9IGZvciBfIGluIDAuLjMgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMiB7IHJvdy5wdXNoKCcgJyk7IH0gZm9yIF8gaW4gMC4uNSB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi4xIHsgcm93LnB1c2goJyAnKTsgfSBmb3IgXyBpbiAwLi43IHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjAgeyByb3cucHVzaCgnICcpOyB9IGZvciBfIGluIDAuLjkgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMSB7IHJvdy5wdXNoKCcgJyk7IH0gZm9yIF8gaW4gMC4uNyB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi4yIHsgcm93LnB1c2goJyAnKTsgfSBmb3IgXyBpbiAwLi41IHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjMgeyByb3cucHVzaCgnICcpOyB9IGZvciBfIGluIDAuLjMgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uNCB7IHJvdy5wdXNoKCcgJyk7IH0gZm9yIF8gaW4gMC4uMSB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KfQqUaLyMDzEyLWhhbGYtZGlhbW9uZJSGlFgvAwAAZm4gbWFpbigpIHsKICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi4xIHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjIgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMyB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi40IHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjUgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uNCB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi4zIHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjIgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIF8gaW4gMC4uMSB7IHJvdy5wdXNoKCcqJyk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KfQqUaLyMDDEzLWJ1dHRlcmZseZSGlFi+AwAAZm4gbWFpbigpIHsKICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyByb3cucHVzaF9zdHIoIioiKTsgcm93LnB1c2hfc3RyKCIgICAgICAiKTsgcm93LnB1c2hfc3RyKCIqIik7IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgcm93LnB1c2hfc3RyKCIqKiIpOyByb3cucHVzaF9zdHIoIiAgICAiKTsgcm93LnB1c2hfc3RyKCIqKiIpOyBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IHJvdy5wdXNoX3N0cigiKioqIik7IHJvdy5wdXNoX3N0cigiICAiKTsgcm93LnB1c2hfc3RyKCIqKioiKTsgcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyByb3cucHVzaF9zdHIoIioqKioiKTsgcm93LnB1c2hfc3RyKCIiKTsgcm93LnB1c2hfc3RyKCIqKioqIik7IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgcm93LnB1c2hfc3RyKCIqKioqIik7IHJvdy5wdXNoX3N0cigiIik7IHJvdy5wdXNoX3N0cigiKioqKiIpOyBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IHJvdy5wdXNoX3N0cigiKioqIik7IHJvdy5wdXNoX3N0cigiICAiKTsgcm93LnB1c2hfc3RyKCIqKioiKTsgcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyByb3cucHVzaF9zdHIoIioqIik7IHJvdy5wdXNoX3N0cigiICAgICIpOyByb3cucHVzaF9zdHIoIioqIik7IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgcm93LnB1c2hfc3RyKCIqIik7IHJvdy5wdXNoX3N0cigiICAgICAgIik7IHJvdy5wdXNoX3N0cigiKiIpOyBwcmludGxuISgie3Jvd30iKTsgfQp9CpRovIwQMTQtaG9sbG93LXNxdWFyZZSGlFglAgAAZm4gbWFpbigpIHsKICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgXyBpbiAwLi41IHsgcm93LnB1c2goJyonKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IHJvdy5wdXNoKCcqJyk7IGZvciBfIGluIDAuLjMgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoKCcqJyk7IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgcm93LnB1c2goJyonKTsgZm9yIF8gaW4gMC4uMyB7IHJvdy5wdXNoKCcgJyk7IH0gcm93LnB1c2goJyonKTsgcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyByb3cucHVzaCgnKicpOyBmb3IgXyBpbiAwLi4zIHsgcm93LnB1c2goJyAnKTsgfSByb3cucHVzaCgnKicpOyBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBfIGluIDAuLjUgeyByb3cucHVzaCgnKicpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9Cn0KlGi8jBQxNS1hbHBoYWJldC10cmlhbmdsZZSGlFjAAgAAZm4gbWFpbigpIHsKICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgayBpbiAwLi4xIHsgaWYgayA+IDAgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoKChiJ0EnICsgayBhcyB1OCkgYXMgY2hhcik7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgayBpbiAwLi4yIHsgaWYgayA+IDAgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoKChiJ0EnICsgayBhcyB1OCkgYXMgY2hhcik7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgayBpbiAwLi4zIHsgaWYgayA+IDAgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoKChiJ0EnICsgayBhcyB1OCkgYXMgY2hhcik7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgayBpbiAwLi40IHsgaWYgayA+IDAgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoKChiJ0EnICsgayBhcyB1OCkgYXMgY2hhcik7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgayBpbiAwLi41IHsgaWYgayA+IDAgeyByb3cucHVzaCgnICcpOyB9IHJvdy5wdXNoKChiJ0EnICsgayBhcyB1OCkgYXMgY2hhcik7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KfQqUaLyMFjE2LW11bHRpcGxpY2F0aW9uLWdyaWSUhpRYTQIAAGZuIG1haW4oKSB7CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIGogaW4gMS4uPTUgeyByb3cucHVzaF9zdHIoJmZvcm1hdCEoIns6PjR9IiwgMSAqIGopKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj01IHsgcm93LnB1c2hfc3RyKCZmb3JtYXQhKCJ7Oj40fSIsIDIgKiBqKSk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KICAgIHsgbGV0IG11dCByb3cgPSBTdHJpbmc6Om5ldygpOyBmb3IgaiBpbiAxLi49NSB7IHJvdy5wdXNoX3N0cigmZm9ybWF0ISgiezo+NH0iLCAzICogaikpOyB9IHByaW50bG4hKCJ7cm93fSIpOyB9CiAgICB7IGxldCBtdXQgcm93ID0gU3RyaW5nOjpuZXcoKTsgZm9yIGogaW4gMS4uPTUgeyByb3cucHVzaF9zdHIoJmZvcm1hdCEoIns6PjR9IiwgNCAqIGopKTsgfSBwcmludGxuISgie3Jvd30iKTsgfQogICAgeyBsZXQgbXV0IHJvdyA9IFN0cmluZzo6bmV3KCk7IGZvciBqIGluIDEuLj01IHsgcm93LnB1c2hfc3RyKCZmb3JtYXQhKCJ7Oj40fSIsIDUgKiBqKSk7IH0gcHJpbnRsbiEoIntyb3d9Iik7IH0KfQqUjBIwNy1udW1iZXItcHJvYmxlbXOUjA8wMS1jb3VudC1kaWdpdHOUhpSMh2ZuIG1haW4oKSB7CiAgICBsZXQgbjogdTMyID0gOTQ2MjEzOwogICAgbGV0IG11dCBjID0gMDsKICAgIGxldCBtdXQgeCA9IG47CiAgICB3aGlsZSB4ID4gMCB7IGMgKz0gMTsgeCAvPSAxMDsgfQogICAgcHJpbnRsbiEoIntjfSIpOwp9CpRo7YwKMDItcmV2ZXJzZZSGlIyZZm4gbWFpbigpIHsKICAgIGxldCBuOiB1MzIgPSA3MDA7CiAgICBsZXQgbXV0IHJldiA9IDA7CiAgICBsZXQgbXV0IHggPSBuOwogICAgd2hpbGUgeCA+IDAgeyByZXYgPSByZXYgKiAxMCArIHggJSAxMDsgeCAvPSAxMDsgfQogICAgcHJpbnRsbiEoIntyZXZ9Iik7Cn0KlGjtjA0wMy1wYWxpbmRyb21llIaUjKFmbiBtYWluKCkgewogICAgbGV0IG46IHUzMiA9IDEyMjE7CiAgICBsZXQgbXV0IHJldiA9IDA7CiAgICBsZXQgbXV0IHggPSBuOwogICAgd2hpbGUgeCA+IDAgeyByZXYgPSByZXYgKiAxMCArIHggJSAxMDsgeCAvPSAxMDsgfQogICAgcHJpbnRsbiEoInt9IiwgcmV2ID09IG4pOwp9CpRo7YwMMDQtYXJtc3Ryb25nlIaUjMVmbiBtYWluKCkgewogICAgbGV0IG46IHUzMiA9IDM3MTsKICAgIGxldCBtdXQgc3VtID0gMDsKICAgIGxldCBtdXQgeCA9IG47CiAgICB3aGlsZSB4ID4gMCB7CiAgICAgICAgbGV0IGQgPSB4ICUgMTA7CiAgICAgICAgc3VtICs9IGQgKiBkICogZDsKICAgICAgICB4IC89IDEwOwogICAgfQogICAgcHJpbnRsbiEoInt9Iiwgc3VtID09IG4pOwp9CpRo7YwLMDUtZGl2aXNvcnOUhpSMuGZuIG1haW4oKSB7CiAgICBsZXQgbjogdTMyID0gMzY7CiAgICBsZXQgbXV0IHBhcnRzID0gVmVjOjpuZXcoKTsKICAgIGZvciBpIGluIDEuLj1uIHsKICAgICAgICBpZiBuICUgaSA9PSAwIHsgcGFydHMucHVzaChpLnRvX3N0cmluZygpKTsgfQogICAgfQogICAgcHJpbnRsbiEoInt9IiwgcGFydHMuam9pbigiICIpKTsKfQqUaO2MCzA2LWlzLXByaW1llIaUjO1mbiBtYWluKCkgewogICAgbGV0IG46IHUzMiA9IDk3OwogICAgbGV0IG11dCBwcmltZSA9IG4gPiAxOwogICAgbGV0IG11dCBpID0gMjsKICAgIHdoaWxlIGkgKiBpIDw9IG4gewogICAgICAgIGlmIG4gJSBpID09IDAgeyBwcmltZSA9IGZhbHNlOyBicmVhazsgfQogICAgICAgIGkgKz0gMTsKICAgIH0KICAgIHByaW50bG4hKCJ7fSIsIGlmIHByaW1lIHsgInByaW1lIiB9IGVsc2UgeyAibm90IHByaW1lIiB9KTsKfQqUaO2MBjA3LWdjZJSGlIx+Zm4gbWFpbigpIHsKICAgIGxldCBtdXQgYSA9IDEyMDsKICAgIGxldCBtdXQgYiA9IDQ1OwogICAgd2hpbGUgYiAhPSAwIHsgbGV0IHQgPSBiOyBiID0gYSAlIGI7IGEgPSB0OyB9CiAgICBwcmludGxuISgie2F9Iik7Cn0KlGjtjAYwOC1sY22UhpSMuGZuIG1haW4oKSB7CiAgICBsZXQgYSA9IDEyOwogICAgbGV0IGIgPSAxODsKICAgIGxldCBtdXQgeCA9IGE7CiAgICBsZXQgbXV0IHkgPSBiOwogICAgd2hpbGUgeSAhPSAwIHsgbGV0IHQgPSB5OyB5ID0geCAlIHk7IHggPSB0OyB9CiAgICBsZXQgZ2NkID0geDsKICAgIHByaW50bG4hKCJ7fSIsIGEgKiBiIC8gZ2NkKTsKfQqUaO2MDzA5LXN1bS1kaXZpc29yc5SGlIyCZm4gbWFpbigpIHsKICAgIGxldCBuOiB1MzIgPSAyODsKICAgIGxldCBtdXQgc3VtID0gMDsKICAgIGZvciBpIGluIDEuLj1uIHsgaWYgbiAlIGkgPT0gMCB7IHN1bSArPSBpOyB9IH0KICAgIHByaW50bG4hKCJ7c3VtfSIpOwp9CpRo7YwRMTAtcGVyZmVjdC1udW1iZXKUhpSMtmZuIG1haW4oKSB7CiAgICBsZXQgbjogdTMyID0gNDk2OwogICAgbGV0IG11dCBzdW0gPSAwOwogICAgZm9yIGkgaW4gMS4ubiB7IGlmIG4gJSBpID09IDAgeyBzdW0gKz0gaTsgfSB9CiAgICBpZiBzdW0gPT0gbiB7IHByaW50bG4hKCJwZXJmZWN0Iik7IH0gZWxzZSB7IHByaW50bG4hKCJub3QgcGVyZmVjdCIpOyB9Cn0KlGjtjBAxMS1wcmltZS1mYWN0b3JzlIaUWBkBAABmbiBtYWluKCkgewogICAgbGV0IG11dCBuOiB1MzIgPSAzNjA7CiAgICBsZXQgbXV0IHBhcnRzID0gVmVjOjpuZXcoKTsKICAgIGxldCBtdXQgZCA9IDI7CiAgICB3aGlsZSBkICogZCA8PSBuIHsKICAgICAgICB3aGlsZSBuICUgZCA9PSAwIHsgcGFydHMucHVzaChkLnRvX3N0cmluZygpKTsgbiAvPSBkOyB9CiAgICAgICAgZCArPSAxOwogICAgfQogICAgaWYgbiA+IDEgeyBwYXJ0cy5wdXNoKG4udG9fc3RyaW5nKCkpOyB9CiAgICBwcmludGxuISgie30iLCBwYXJ0cy5qb2luKCIgIikpOwp9CpRo7YwOMTItcHJpbWVzLXRvLW6UhpRYVQEAAGZuIG1haW4oKSB7CiAgICBsZXQgbjogdTMyID0gMzA7CiAgICBsZXQgbXV0IHBhcnRzID0gVmVjOjpuZXcoKTsKICAgIGZvciBwIGluIDIuLj1uIHsKICAgICAgICBsZXQgbXV0IHByaW1lID0gdHJ1ZTsKICAgICAgICBsZXQgbXV0IGkgPSAyOwogICAgICAgIHdoaWxlIGkgKiBpIDw9IHAgewogICAgICAgICAgICBpZiBwICUgaSA9PSAwIHsgcHJpbWUgPSBmYWxzZTsgYnJlYWs7IH0KICAgICAgICAgICAgaSArPSAxOwogICAgICAgIH0KICAgICAgICBpZiBwcmltZSB7IHBhcnRzLnB1c2gocC50b19zdHJpbmcoKSk7IH0KICAgIH0KICAgIHByaW50bG4hKCJ7fSIsIHBhcnRzLmpvaW4oIiAiKSk7Cn0KlGjtjAwxMy1udGgtcHJpbWWUhpRYYgEAAGZuIG1haW4oKSB7CiAgICBsZXQgayA9IDIwOwogICAgbGV0IG11dCBjb3VudCA9IDA7CiAgICBsZXQgbXV0IHAgPSAyOwogICAgd2hpbGUgY291bnQgPCBrIHsKICAgICAgICBsZXQgbXV0IHByaW1lID0gdHJ1ZTsKICAgICAgICBsZXQgbXV0IGkgPSAyOwogICAgICAgIHdoaWxlIGkgKiBpIDw9IHAgewogICAgICAgICAgICBpZiBwICUgaSA9PSAwIHsgcHJpbWUgPSBm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bXV0IHYgPSB2ZWMhWzEsIDIsIDMsIDQsIDVdOwogICAgaWYgIXYuaXNfZW1wdHkoKSB7CiAgICAgICAgbGV0IGZpcnN0ID0gdi5yZW1vdmUoMCk7CiAgICAgICAgdi5wdXNoKGZpcnN0KTsKICAgIH0KICAgIGxldCBwYXJ0czogVmVjPFN0cmluZz4gPSB2Lml0ZXIoKS5tYXAofHh8IHgudG9fc3RyaW5nKCkpLmNvbGxlY3QoKTsKICAgIHByaW50bG4hKCJ7fSIsIHBhcnRzLmpvaW4oIiAiKSk7Cn0KlGqNAQAAjAsxMy1yb3RhdGUta5SGlFgyAQAAZm4gbWFpbigpIHsKICAgIGxldCB2ID0gdmVjIVsxLCAyLCAzLCA0LCA1LCA2LCA3XTsKICAgIGxldCBrID0gMzsKICAgIGxldCBuID0gdi5sZW4oKTsKICAgIGxldCBrID0gayAlIG47CiAgICBsZXQgcm90YXRlZCA9IHZbay4uXS5pdGVyKCkuY2hhaW4odlsuLmtdLml0ZXIoKSkuY2xvbmVkKCkuY29sbGVjdDo6PFZlYzxfPj4oKTsKICAgIGxldCBwYXJ0czogVmVjPFN0cmluZz4gPSByb3RhdGVkLml0ZXIoKS5tYXAofHh8IHgudG9fc3RyaW5nKCkpLmNvbGxlY3QoKTsKICAgIHByaW50bG4hKCJ7fSIsIHBhcnRzLmpvaW4oIiAiKSk7Cn0KlGqNAQAAjA0xNC1tb3ZlLXplcm9zlIaUWEsBAABmbiBtYWluKCkgewogICAgbGV0IHYgPSB2ZWMhWzAsIDEsIDAsIDMsIDEyXTsKICAgIGxldCBtdXQgb3V0OiBWZWM8aTMyPiA9IHYuaXRlcigpLmZpbHRlcih8Jnh8ICp4ICE9IDApLmNsb25lZCgpLmNvbGxlY3QoKTsKICAgIGxldCB6ZXJvcyA9IHYuaXRlcigpLmZpbHRlcih8Jnh8ICp4ID09IDApLmNvdW50KCk7CiAgICBmb3IgXyBpbiAwLi56ZXJvcyB7IG91dC5wdXNoKDApOyB9CiAgICBsZXQgcGFydHM6IFZlYzxTdHJpbmc+ID0gb3V0Lml0ZXIoKS5tYXAofHh8IHgudG9fc3RyaW5nKCkpLmNvbGxlY3QoKTsKICAgIHByaW50bG4hKCJ7fSIsIHBh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CTExLW9wdGlvbpSGlFhlAgAAZm4gbWFpbigpIHsKCiAgICAjW2Rlcml2ZShEZWJ1ZyldCiAgICBzdHJ1Y3QgUGVyc29uIHsgbmFtZTogU3RyaW5nLCBhZ2U6IHUzMiwgY2l0eTogU3RyaW5nIH0KICAgIGxldCBwZW9wbGUgPSB2ZWMhWwogICAgICAgIFBlcnNvbiB7IG5hbWU6ICJBZGEiLmludG8oKSwgYWdlOiAzNiwgY2l0eTogIkxvbmRvbiIuaW50bygpIH0sCiAgICAgICAgUGVyc29uIHsgbmFtZTogIlJhbWFuIi5pbnRvKCksIGFnZTogNDIsIGNpdHk6ICJLb2xrYXRhIi5pbnRvKCkgfSwKICAgICAgICBQZXJzb24geyBuYW1lOiAiTWVlcmEiLmludG8oKSwgYWdlOiAyOSwgY2l0eTogIlB1bmUiLmludG8oKSB9LAogICAgXTsKCiAgICBtYXRjaCBwZW9wbGUuaXRlcigpLmZpbmQofHB8IHAubmFtZSA9PSAiQWRhIikgewogICAgICAgIFNvbWUocCkgPT4gcHJpbnRsbiEoInt9IiwgcC5uYW1lKSwKICAgICAgICBOb25lID0+IHByaW50bG4hKCJub25lIiksCiAgICB9CiAgICBtYXRjaCBwZW9wbGUuaXRlcigpLmZpbmQofHB8IHAubmFtZSA9PSAiWmFyYSIpIHsKICAgICAgICBTb21lKHApID0+IHByaW50bG4hKCJ7fSIsIHAubmFtZSksCiAgICAgICAgTm9uZSA9PiBwcmludGxuISgibm9uZSIpLAogICAgfQp9CpRq4wEAAIwJMTItcmVzdWx0lIaUWDQBAABmbiBkaXZpZGUoYTogaTMyLCBiOiBpMzIpIC0+IFJlc3VsdDxpMzIsIFN0cmluZz4gewogICAgaWYgYiA9PSAwIHsgRXJyKFN0cmluZzo6ZnJvbSgiQ2Fubm90IGRpdmlkZSBieSB6ZXJvIikpIH0gZWxzZSB7IE9rKGEgLyBiKSB9Cn0KZm4gbWFpbigpIHsKICAgIG1hdGNoIGRpdmlkZSgxMiwgNCkgeyBPayh2KSA9PiBwcmludGxuISgie3Z9IiksIEVycihlKSA9PiBwcmludGxuISgie2V9IiksIH0KICAgIG1hdGNoIGRpdmlkZSgx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b24uc29ydCgpOwogICAgcHJpbnRsbiEoInt9IiwgdW5pb24uaXRlcigpLm1hcCh8eHwgeC50b19zdHJpbmcoKSkuY29sbGVjdDo6PFZlYzxfPj4oKS5qb2luKCIgIikpOwogICAgbGV0IG11dCBpbnRlcjogVmVjPGkzMj4gPSBhLmludGVyc2VjdGlvbigmYikuY2xvbmVkKCkuY29sbGVjdCgpOwogICAgaW50ZXIuc29ydCgpOwogICAgcHJpbnRsbiEoInt9IiwgaW50ZXIuaXRlcigpLm1hcCh8eHwgeC50b19zdHJpbmcoKSkuY29sbGVjdDo6PFZlYzxfPj4oKS5qb2luKCIgIikpOwp9CpRqJQIAAIwWMDgtZmlyc3Qtbm9uLXJlcGVhdGluZ5SGlFg+AQAAdXNlIHN0ZDo6Y29sbGVjdGlvbnM6Okhhc2hNYXA7CmZuIG1haW4oKSB7CiAgICBsZXQgcyA9ICJzd2lzcyI7CiAgICBsZXQgbXV0IG1hcDogSGFzaE1hcDxjaGFyLCB1MzI+ID0gSGFzaE1hcDo6bmV3KCk7CiAgICBmb3IgYyBpbiBzLmNoYXJzKCkgeyAqbWFwLmVudHJ5KGMpLm9yX2luc2VydCgwKSArPSAxOyB9CiAgICBmb3IgYyBpbiBzLmNoYXJzKCkgewogICAgICAgIGlmIG1hcFsmY10gPT0gMSB7CiAgICAgICAgICAgIHByaW50bG4hKCJ7Y30iKTsKICAgICAgICAgICAgcmV0dXJuOwogICAgICAgIH0KICAgIH0KICAgIHByaW50bG4hKCJub25lIik7Cn0KlGolAgAAjAowOS10d28tc3VtlIaUWGsBAAB1c2Ugc3RkOjpjb2xsZWN0aW9uczo6SGFzaE1hcDsKZm4gbWFpbigpIHsKICAgIGxldCB2ID0gdmVjIVsyLCA3LCAxMSwgMTVdOwogICAgbGV0IHRhcmdldCA9IDk7CiAgICBsZXQgbXV0IG1hcDogSGFzaE1hcDxpMzIsIHVzaXplPiA9IEhhc2hNYXA6Om5ldygpOwogICAgZm9yIChpLCAmeCkgaW4gdi5pdGVyKCkuZW51bWVyYXRlKCkgewogICAgICAgIGxldCBuZWVkID0gdGFyZ2V0IC0geDsKICAgICAgICBpZiBsZXQgU29tZSgm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biEoInt2fSIpLAogICAgICAgIEVycihfKSA9PiBwcmludGxuISgiY291bGQgbm90IHBhcnNlIiksCiAgICB9Cn0KlGpEAgAAjA8wNy1jdXN0b20tZXJyb3KUhpRYJgIAAGVudW0gTWF0aEVycm9yIHsgRGl2aWRlQnlaZXJvIH0KaW1wbCBzdGQ6OmZtdDo6RGlzcGxheSBmb3IgTWF0aEVycm9yIHsKICAgIGZuIGZtdCgmc2VsZiwgZjogJm11dCBzdGQ6OmZtdDo6Rm9ybWF0dGVyPCdfPikgLT4gc3RkOjpmbXQ6OlJlc3VsdCB7CiAgICAgICAgbWF0Y2ggc2VsZiB7IE1hdGhFcnJvcjo6RGl2aWRlQnlaZXJvID0+IHdyaXRlIShmLCAiY2Fubm90IGRpdmlkZSBieSB6ZXJvIikgfQogICAgfQp9CmZuIGNoZWNrZWRfZGl2KGE6IGkzMiwgYjogaTMyKSAtPiBSZXN1bHQ8aTMyLCBNYXRoRXJyb3I+IHsKICAgIGlmIGIgPT0gMCB7IEVycihNYXRoRXJyb3I6OkRpdmlkZUJ5WmVybykgfSBlbHNlIHsgT2soYSAvIGIpIH0KfQpmbiBtYWluKCkgewogICAgbWF0Y2ggY2hlY2tlZF9kaXYoMTAsIDIpIHsgT2sodikgPT4gcHJpbnRsbiEoInt2fSIpLCBFcnIoZSkgPT4gcHJpbnRsbiEoIntlfSIpLCB9CiAgICBtYXRjaCBjaGVja2VkX2RpdigxMCwgMCkgeyBPayh2KSA9PiBwcmludGxuISgie3Z9IiksIEVycihlKSA9PiBwcmludGxuISgie2V9IiksIH0KfQqUakQCAACMEzA4LWV4cGVjdC12cy1yZXN1bHSUhpSM52ZuIG1haW4oKSB7CiAgICBwcmludGxuISgie30iLCAiNDIiLnBhcnNlOjo8aTMyPigpLmV4cGVjdCgidGhlIGNvbmZpZyB2YWx1ZSBtdXN0IGJlIGEgbnVtYmVyIikpOwogICAgbGV0IHJlY292ZXJlZCA9ICJ4Ii5wYXJzZTo6PGkzMj4oKS51bndyYXBfb3JfZWxzZSh8X3wgewogICAgICAgIHByaW50bG4hKCJyZWNvdmVyZWQiKTsKICAgICAgICAwCiAgICB9KTsKICAgIGxldCBfID0gcmVj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"))
SOLUTIONS = _PAYLOAD["SOLUTIONS"]
CHECKS = _PAYLOAD["CHECKS"]
STUBS = _PAYLOAD["STUBS"]
STUB_EXPECTED_INLINE = _PAYLOAD["STUB_EXPECTED_INLINE"]
TEST_SIGNATURES = _PAYLOAD["TEST_SIGNATURES"]
TEST_FN_BODY = _PAYLOAD["TEST_FN_BODY"]
LEVEL_LIST = _PAYLOAD["LEVEL_LIST"]
TEST_GRADED = _PAYLOAD["TEST_GRADED_SET"]
ROOT = _ROOT


def is_test_graded(level_dir: str, name: str) -> bool:
    return (level_dir, name) in TEST_GRADED


def stub_expected_line(level_dir: str, name: str) -> str:
    key = (level_dir, name)
    inline = STUB_EXPECTED_INLINE.get(key)
    if inline is not None:
        if inline == "FROM_SOLUTION":
            return f"See expected/{name}.txt"
        return inline
    if is_test_graded(level_dir, name):
        return ""
    return f"See expected/{name}.txt"


def write_stub(level_dir: str, name: str, path: Path) -> None:
    meta = STUBS.get((level_dir, name))
    if not meta:
        raise KeyError(f"missing stub {level_dir}/{name}")
    task, given, extra_doc, do_not_change = meta
    if str(SCRIPTS) not in sys.path:
        sys.path.insert(0, str(SCRIPTS))
    from concept_header import concept_doc_lines

    lines = [f"//! {level_dir} / {name}", "//!", "//! TASK", f"//! {task}", "//!"]
    lines.extend(concept_doc_lines(level_dir, name))
    if extra_doc:
        lines.extend(["//!", f"//! {extra_doc}", "//!"])
    if do_not_change:
        lines.extend(["//! DO NOT CHANGE the GIVEN values.", "//!"])
    if is_test_graded(level_dir, name):
        sig = TEST_SIGNATURES[(level_dir, name)]
        lines.extend([
            "//! SIGNATURE", f"//! {sig}", "//!",
            "//! This exercise is graded by the checks at the bottom of the file, not by",
            "//! printed output. Leave `main` empty.", "//!",
        ])
    exp = stub_expected_line(level_dir, name)
    if exp:
        lines.extend(["//! EXPECTED OUTPUT", f"//! {exp.replace(chr(10), chr(10) + '//! ')}", ""])
    else:
        lines.append("")
    body = []
    if is_test_graded(level_dir, name):
        body.append(TEST_FN_BODY[(level_dir, name)])
        body.extend(["", "fn main() {}", "", "// ---- CHECKS: DO NOT EDIT ----", "#[cfg(test)]",
                     f'#[path = "../../checks/{name}.rs"]', "mod tests;"])
    else:
        body.append("fn main() {")
        if given:
            body.extend(["    // ---- GIVEN ----", *[f"    {g}" for g in given.split(chr(10))],
                         "    // ---------------", ""])
        body.extend(["    // Your code below", "}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(chr(10).join(lines + body) + chr(10), encoding="utf-8")


def solution_body(level_dir: str, name: str) -> str:
    code = SOLUTIONS[(level_dir, name)]
    if is_test_graded(level_dir, name):
        code = code.rstrip() + f"""

// ---- CHECKS: DO NOT EDIT ----
#[cfg(test)]
#[path = "../../../../levels/{level_dir}/checks/{name}.rs"]
mod tests;
"""
    return code


def backup_checks() -> None:
    backup = ROOT / ".checks-backup"
    backup.mkdir(parents=True, exist_ok=True)
    for lv, _ in LEVEL_LIST:
        checks = ROOT / "levels" / lv / "checks"
        if not checks.is_dir():
            continue
        dest = backup / lv
        dest.mkdir(parents=True, exist_ok=True)
        for f in checks.glob("*.rs"):
            shutil.copy2(f, dest / f.name)


def write_expected_from_solutions() -> None:
    target = ROOT / "target" / "exercises"
    env = os.environ.copy()
    env["CARGO_TARGET_DIR"] = str(target)
    manifest = str(ROOT / "Cargo.toml")
    for lv, names in LEVEL_LIST:
        sol_pkg = f"sol-{lv}"
        for nm in names:
            if (lv, nm) in CHECKS:
                continue
            subprocess.run(
                ["cargo", "build", "--manifest-path", manifest, "-p", sol_pkg, "--bin", nm],
                cwd=ROOT,
                env=env,
                check=True,
            )
            exe = target / "debug" / nm
            if not exe.exists():
                exe = target / "debug" / nm.replace("-", "_")
            proc = subprocess.run(
                [str(exe)],
                cwd=ROOT / "levels" / lv,
                capture_output=True,
                text=True,
                check=True,
            )
            out_path = ROOT / "levels" / lv / "expected" / f"{nm}.txt"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(proc.stdout, encoding="utf-8")


def rebuild_checks_lock() -> None:
    table = {}
    for lv, _ in LEVEL_LIST:
        checks = ROOT / "levels" / lv / "checks"
        if not checks.is_dir():
            continue
        for f in sorted(checks.glob("*.rs")):
            h = hashlib.sha256(f.read_bytes()).hexdigest()
            table[f"{lv}/{f.stem}"] = h
    lines = [f'{k} = "{v}"' for k, v in sorted(table.items())]
    (ROOT / "checks.lock").write_text(chr(10).join(lines) + chr(10), encoding="utf-8")


def main() -> int:
    os.chdir(ROOT)
    for lv, names in LEVEL_LIST:
        (ROOT / "levels" / lv).mkdir(parents=True, exist_ok=True)
        (ROOT / "solutions" / lv).mkdir(parents=True, exist_ok=True)
        (ROOT / "levels" / lv / "Cargo.toml").write_text(level_cargo_toml(lv), encoding="utf-8")
        (ROOT / "solutions" / lv / "Cargo.toml").write_text(sol_cargo_toml(lv), encoding="utf-8")
        for nm in names:
            stub_path = ROOT / "levels" / lv / "src" / "bin" / f"{nm}.rs"
            sol_path = ROOT / "solutions" / lv / "src" / "bin" / f"{nm}.rs"
            write_stub(lv, nm, stub_path)
            sol_path.parent.mkdir(parents=True, exist_ok=True)
            sol_path.write_text(solution_body(lv, nm), encoding="utf-8")
            backup = ROOT / ".stub-backups" / f"{lv}__{nm}.rs"
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(stub_path, backup)
        if (lv, names[0]) in CHECKS or any((lv, n) in CHECKS for n in names):
            checks_dir = ROOT / "levels" / lv / "checks"
            checks_dir.mkdir(parents=True, exist_ok=True)
            for n in names:
                if (lv, n) in CHECKS:
                    (checks_dir / f"{n}.rs").write_text(CHECKS[(lv, n)], encoding="utf-8")
        if lv == "04-for-loops":
            (ROOT / "levels" / lv / "hints.toml").write_text(
                '"12-fibonacci" = "check your loop\'s starting values."\n', encoding="utf-8"
            )
        if lv == "16-modules-errors-io":
            lib_stub = ROOT / "levels" / lv / "src" / "lib.rs"
            lib_stub.parent.mkdir(parents=True, exist_ok=True)
            lib_stub.write_text("// Add `pub mod` declarations here as you create modules.\n", encoding="utf-8")
            data = ROOT / "levels" / lv / "data"
            data.mkdir(parents=True, exist_ok=True)
            (data / "sample.txt").write_text("hello from a file\n", encoding="utf-8")
            (data / "numbers.txt").write_text("3\n1\n4\n1\n5\n", encoding="utf-8")
            (data / ".gitignore").write_text("out.txt\n", encoding="utf-8")
            sol_lib = ROOT / "solutions" / lv / "src" / "lib.rs"
            sol_lib.write_text("pub mod math;\n", encoding="utf-8")
            (ROOT / "solutions" / lv / "src" / "math.rs").write_text(
                "pub fn add(a: i32, b: i32) -> i32 { a + b }\n"
                "pub fn subtract(a: i32, b: i32) -> i32 { a - b }\n",
                encoding="utf-8",
            )
    backup_checks()
    rebuild_checks_lock()
    write_expected_from_solutions()
    subprocess.run(
        ["cargo", "run", "--release", "-p", "runner", "--bin", "cli", "--", "gen-expected"],
        cwd=ROOT,
        check=True,
    )
    proc = subprocess.run(
        ["cargo", "run", "--release", "-p", "runner", "--bin", "cli", "--", "verify"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    print(proc.stdout)
    if proc.stderr:
        print(proc.stderr, file=sys.stderr)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
