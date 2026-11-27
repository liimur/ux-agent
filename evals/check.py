#!/usr/bin/env python3
"""Deterministic checks for the manual evaluations.

Checks only what a script can decide: input fixtures are unchanged, expected
output files exist and are not empty, DESIGN.md lints (optional), and no
sentence makes a forbidden claim. Design quality is judged by a person with
the rubric. Usage:

    python3 evals/check.py start
    python3 evals/check.py all --root examples/task-board/output
    python3 evals/check.py system --lint
"""
import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INPUT = "evals/task-board/input"

# case: (output directory name, expected files, rubric)
CASES = {
    "start": ("eval-start", ["brief.md"], "start.md"),
    "system": ("eval-system", ["DESIGN.md", "*.md"], "design-system.md"),
    "design": ("eval-design", ["design.md"], "design.md"),
    "review": ("eval-review", ["review.md"], "review.md"),
    "hil-direction": ("eval-hil-direction", ["brief.md"], "hil-direction.md"),
    "hil-conflict": ("eval-hil-conflict", ["DESIGN.md", "*.md"], "hil-conflict.md"),
    "review-control": ("eval-review-control", ["review.md"], "review-control.md"),
    "design-rules": ("eval-design-rules", ["design.md"], "design-rules.md"),
    "interview": ("eval-interview", ["designer-rules.md"], "interview.md"),
    "research": ("eval-research", ["plan.md"], "research.md"),
    "prototype": ("eval-prototype", ["*.html", "PROTOTYPE.md"], "prototype.md"),
}

# Affirmative claims the harness forbids without evidence. A match is flagged
# for a person to read in context; negated sentences are skipped.
CLAIMS = [
    r"соответству\w* (?:требованиям )?WCAG",
    r"(?:conforms?|compliant|complies) (?:to|with) WCAG",
    r"WCAG[- ]compliant",
    r"meets WCAG",
    r"полностью доступ\w*",
    r"fully accessible",
    r"протестирова\w* (?:с|на) (?:пользовател|участник)",
    r"tested with (?:users|participants)",
]
NEGATION = re.compile(r"\b(?:не|нет|без|not|no|never|cannot|unverified|непровер)\w*", re.I)


def run(cmd):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)


def check_inputs():
    """Compare fixtures with evals/task-board/input.sha256.

    After an intentional fixture change, regenerate the manifest:
    (cd evals/task-board/input && shasum -a 256 * > ../input.sha256)
    """
    manifest = REPO / "evals/task-board/input.sha256"
    expected = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, name = line.split(maxsplit=1)
        expected[name.lstrip("*")] = digest
    actual = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in (REPO / INPUT).iterdir() if p.is_file()}
    problems = [f"modified {n}" for n in expected if n in actual and actual[n] != expected[n]]
    problems += [f"missing {n}" for n in expected if n not in actual]
    problems += [f"unexpected {n}" for n in actual if n not in expected]
    if problems:
        return "FAIL", "input fixtures differ from input.sha256: " + ", ".join(problems)
    return "PASS", "input fixtures match input.sha256"


def check_outputs(directory, patterns):
    results = []
    for pattern in patterns:
        found = [p for p in directory.glob(pattern) if p.is_file() and p.stat().st_size > 0]
        if found:
            results.append(("PASS", f"{pattern}: " + ", ".join(p.name for p in found)))
        else:
            results.append(("FAIL", f"{pattern}: missing or empty in {directory}"))
    return results


def check_claims(directory):
    results = []
    for path in sorted(directory.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".html", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for sentence in re.split(r"(?<=[.!?])\s+|\n", text):
            for claim in CLAIMS:
                if re.search(claim, sentence, re.I) and not NEGATION.search(sentence):
                    results.append(("FLAG", f"{path.name}: possible unsupported claim: {sentence.strip()[:160]}"))
    return results or [("PASS", "no affirmative conformance or testing claims found")]


def check_lint(directory):
    design = directory / "DESIGN.md"
    if not design.exists():
        return [("SKIP", "no DESIGN.md to lint")]
    try:
        res = run(["npx", "--yes", "@google/design.md", "lint", str(design)])
    except FileNotFoundError:
        return [("SKIP", "npx not available")]
    status = "PASS" if res.returncode == 0 else "FAIL"
    lines = (res.stdout or res.stderr).strip().splitlines()
    return [(status, "design.md lint: " + (lines[-1] if lines else "no output"))]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("case", choices=[*CASES, "all"])
    parser.add_argument("--root", default="projects", help="directory containing eval-<case> outputs")
    parser.add_argument("--lint", action="store_true", help="run the DESIGN.md linter through npx")
    args = parser.parse_args()

    cases = list(CASES) if args.case == "all" else [args.case]
    root = (REPO / args.root).resolve()
    failed = False
    status, message = check_inputs()
    print(f"[{status}] {message}")
    failed |= status == "FAIL"

    for case in cases:
        dirname, patterns, rubric = CASES[case]
        directory = root / dirname
        print(f"\n== {case} ({directory.relative_to(REPO) if directory.is_relative_to(REPO) else directory})")
        if not directory.is_dir():
            print("[SKIP] output directory not found")
            if args.case != "all":
                failed = True
            continue
        results = check_outputs(directory, patterns) + check_claims(directory)
        if args.lint:
            results += check_lint(directory)
        for status, message in results:
            print(f"[{status}] {message}")
            failed |= status == "FAIL"
        print(f"Judge the rest with evals/task-board/rubrics/{rubric}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
