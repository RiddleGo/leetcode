#!/usr/bin/env python3
"""Convert Chapter 2 markdown code blocks from Java/C++ to Python."""
from __future__ import annotations

import re
from pathlib import Path

CH_DIR = Path(r"d:\leetcode\fucking-algorithm-book\第2章-动态规划系列")

# Remove ==其他语言代码== sections (C++/Java duplicates at end)
OTHER_LANG_SECTION = re.compile(
    r"\n---\n\n==其他语言代码==.*$",
    re.DOTALL,
)
OTHER_LANG_SECTION_ALT = re.compile(
    r"\n---\n\n== 其他语言代码 ==.*$",
    re.DOTALL,
)
# Remove contributor C++/Java blocks after ==其他语言==
CONTRIBUTOR_CPP_JAVA = re.compile(
    r"\n\n\[[^\]]+\]\([^)]+\) 提供 (?:C\+\+|Java) 代码[：:]?\s*\n\n```(?:C\+\+|cpp|java|c\+\+).*?```",
    re.DOTALL | re.IGNORECASE,
)

def normalize_python_fence(match: re.Match) -> str:
    return "```python\n"

def strip_kian_cpp_section(text: str) -> str:
    """Remove [Kian...] C++ block at end of 2.1"""
    return re.sub(
        r"\n\n\[Kian[^\]]*\][^\n]*\n\n```c\+\+.*?```\s*$",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

def convert_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    # Remove other-language sections
    text = OTHER_LANG_SECTION.sub("", text)
    text = OTHER_LANG_SECTION_ALT.sub("", text)
    while True:
        new = CONTRIBUTOR_CPP_JAVA.sub("", text)
        if new == text:
            break
        text = new
    text = strip_kian_cpp_section(text)

    # Normalize python suffix tags
    text = re.sub(r"```python\s+[^\n]+\n", "```python\n", text)

    # Replace fence openers
    text = re.sub(r"```(?:java|cpp|c\+\+|C\+\+)\s*\n", "```python\n", text, flags=re.IGNORECASE)

    # Untagged blocks with Java/C++ keywords -> python (conservative)
    def maybe_convert_untagged(m: re.Match) -> str:
        body = m.group(1)
        if re.search(
            r"\b(public |class Solution|vector<|int\[\]|String |Arrays\.|Math\.|#include|std::)",
            body,
        ):
            return "```python\n" + body + "```"
        return m.group(0)

    text = re.sub(r"```\n(.*?)```", maybe_convert_untagged, text, flags=re.DOTALL)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


if __name__ == "__main__":
    for p in sorted(CH_DIR.glob("*.md")):
        if "2.18" in p.name:
            continue
        changed = convert_file(p)
        print(f"{'UPDATED' if changed else 'unchanged'}: {p.name}")
