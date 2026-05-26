#!/usr/bin/env python3
"""Copy deployable static site files into docs/ for GitHub Pages."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

COPY_FILES = ["index.html", "reader.html", "chapters.json", ".nojekyll"]
COPY_DIRS = [
    "第1章-核心套路篇",
    "第2章-动态规划系列",
    "第3章-数据结构系列",
    "第4章-算法思维系列",
    "第5章-高频面试系列",
    "pictures",
]


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()

    for name in COPY_FILES:
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, DOCS / name)

    for name in COPY_DIRS:
        src = ROOT / name
        if src.is_dir():
            shutil.copytree(src, DOCS / name)

    print(f"Prepared {DOCS} for GitHub Pages (/docs folder)")


if __name__ == "__main__":
    main()
