#!/usr/bin/env python3
"""Check relative links and heading anchors in tracked Markdown files.

External URLs are not fetched. Exits with status 1 if a link is broken.
"""
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")


def slug(text):
    """GitHub-style anchor for a heading."""
    text = re.sub(r"[`*_]|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        found, in_code = set(), False
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.lstrip().startswith("```"):
                in_code = not in_code
            elif not in_code and (m := HEADING.match(line)):
                found.add(slug(m.group(1)))
        cache[path] = found
    return cache[path]


def markdown_files():
    out = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
                         cwd=REPO, capture_output=True, text=True, check=True).stdout
    return [REPO / p for p in out.splitlines() if (REPO / p).exists()]


def main():
    broken = []
    for path in markdown_files():
        in_code = False
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            for target in LINK.findall(line):
                if re.match(r"[a-z][a-z0-9+.-]*:", target):
                    continue
                file_part, _, anchor = target.partition("#")
                dest = (path.parent / file_part).resolve() if file_part else path
                where = f"{path.relative_to(REPO)}:{number}"
                if not dest.exists():
                    broken.append(f"{where}: missing {target}")
                elif anchor and dest.suffix == ".md" and anchor not in anchors(dest):
                    broken.append(f"{where}: no heading for #{anchor} in {file_part or path.name}")
    for item in broken:
        print(item)
    print(f"{len(broken)} broken link(s)" if broken else "All relative links resolve.")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
