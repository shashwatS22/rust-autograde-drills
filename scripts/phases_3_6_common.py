"""Shared types for phases 3–6 scaffolding."""

from __future__ import annotations

from dataclasses import dataclass
from textwrap import dedent

AXUM_ONESHOT = dedent(
    """
    let response = app()
        .oneshot(Request::builder().uri("{uri}").body(Body::empty()).unwrap())
        .await
        .unwrap();
    assert_eq!(response.status(), StatusCode::{status});
"""
).strip()


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
    checks_contract: str = ""


def _assert_stmt(line: str) -> str:
    s = line.strip()
    if not s:
        return s
    if not s.endswith(";"):
        s += ";"
    return s


def check_block(*assertions: str, async_test: bool = False) -> str:
    body = "\n    ".join(_assert_stmt(a) for a in assertions if a.strip())
    if async_test:
        return dedent(
            f"""
            use super::*;
            #[tokio::test]
            async fn graded() {{
                {body}
            }}
            """
        ).strip()
    return dedent(
        f"""
        use super::*;
        #[test]
        fn graded() {{
            {body}
        }}
        """
    ).strip()


def T(
    name: str,
    task: str,
    signature: str,
    stub: str,
    solution: str,
    check: str,
) -> Exercise:
    return Exercise(
        name=name,
        task=task,
        test_graded=True,
        signature=signature,
        stub_body=dedent(stub).strip(),
        solution=dedent(solution).strip(),
        check=dedent(check).strip(),
    )


def O(name: str, task: str, given: str, solution: str) -> Exercise:
    return Exercise(
        name=name,
        task=task,
        test_graded=False,
        given=dedent(given).strip(),
        solution=dedent(solution).strip(),
        expected_hint="→ from solution",
    )


def axum_route_ex(name: str, path: str, body: str, status: str = "OK") -> Exercise:
    task = f"Build `app()` with GET `{path}` returning `{body}`."
    sig = "fn app() -> axum::Router"
    sol = dedent(
        f"""
        use axum::{{routing::get, Router}};

        pub fn app() -> Router {{
            Router::new().route("{path}", get(|| async {{ "{body}" }}))
        }}
        """
    ).strip()
    stub = sol.replace(f'"{body}"', '"todo"') + "\n\nfn main() {}"
    sol = sol + "\n\nfn main() {}"
    check = dedent(
        f"""
        use super::*;
        use axum::body::Body;
        use axum::http::{{Request, StatusCode}};
        use tower::ServiceExt;

        #[tokio::test]
        async fn route_works() {{
            {AXUM_ONESHOT.format(uri=path, status=status)}
        }}
        """
    ).strip()
    return T(name, task, sig, stub, sol, check)
