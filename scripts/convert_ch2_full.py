#!/usr/bin/env python3
"""Convert Chapter 2 markdown Java/C++ code blocks to Python."""
import re
from pathlib import Path

CH = Path(r"d:\leetcode\fucking-algorithm-book\第2章-动态规划系列")

SKIP = "2.18"

# Per-file: replace entire old fenced block (with ```lang) by new python block
FILE_BLOCKS: dict[str, list[tuple[str, str]]] = {}

def convert_cpp_java_body(body: str) -> str:
    """Heuristic C++/Java -> Python for common DP patterns."""
    s = body
    # Common replacements
    reps = [
        (r"\bvector<vector<int>>\s+dp\s*\(\s*(\w+)\s*,\s*vector<int>\s*\(\s*\1\s*,\s*0\s*\)\s*\)",
         r"dp = [[0] * \1 for _ in range(\1)]"),
        (r"\bvector<int>\s+dp\s*\(\s*(\w+)\s*,\s*1\s*\)", r"dp = [1] * \1"),
        (r"\bint\s+(\w+)\s*=\s*", r"\1 = "),
        (r"\bfor\s*\(\s*int\s+(\w+)\s*=\s*(\d+)\s*;\s*\1\s*<\s*(\w+)\s*;\s*\1\+\+\s*\)",
         r"for \1 in range(\2, \3)"),
        (r"\bfor\s*\(\s*int\s+(\w+)\s*=\s*(\w+)\s*-\s*2\s*;\s*\1\s*>=\s*0\s*;\s*\1--\s*\)",
         r"for \1 in range(\2 - 2, -1, -1)"),
        (r"\bfor\s*\(\s*int\s+(\w+)\s*=\s*(\w+)\s*-\s*1\s*;\s*\1\s*>=\s*0\s*;\s*\1--\s*\)",
         r"for \1 in range(\2 - 1, -1, -1)"),
        (r"\bMath\.max\b", "max"),
        (r"\bMath\.min\b", "min"),
        (r"\bstring\s+(\w+)", r"\1: str"),
        (r"\bvoid\s+(\w+)", r"def \1"),
        (r"\bbool\s+(\w+)", r"def \1"),
        (r"\breturn\s+false\b", "return False"),
        (r"\breturn\s+true\b", "return True"),
        (r";\s*$", "", re.MULTILINE),
    ]
    for item in reps:
        if len(item) == 3:
            s = re.sub(item[0], item[1], s, flags=item[2])
        else:
            s = re.sub(item[0], item[1], s)
    return s


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    orig = text

    # Remove other-language sections
    text = re.sub(r"\n---\n\n==其他语言代码==.*$", "", text, flags=re.DOTALL)
    text = re.sub(r"\n\n\[[^\]]+\]\([^)]+\) 提供 (?:C\+\+|Java) 代码[：:]?\s*\n\n```(?:C\+\+|cpp|java).*?```",
                  "", text, flags=re.DOTALL | re.IGNORECASE)

    text = re.sub(r"```python\s+[^\n]+\n", "```python\n", text)

    def repl_fence(m: re.Match) -> str:
        lang = m.group(1).lower()
        body = m.group(2)
        if lang in ("java", "cpp", "c++"):
            # Keep if already looks like python-only pseudocode
            if "class Solution" in body and lang == "java":
                pass
            body = convert_cpp_java_body(body)
        return f"```python\n{body}```"

    text = re.sub(
        r"```(java|cpp|c\+\+|C\+\+)\s*\n(.*?)```",
        repl_fence,
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # Untagged blocks with Java/C++
    def repl_untagged(m: re.Match) -> str:
        body = m.group(1)
        if re.search(r"\b(public |class Solution|vector<|int\[\]|String |Arrays\.|#include)", body):
            return f"```python\n{convert_cpp_java_body(body)}```"
        return m.group(0)

    text = re.sub(r"```\n(.*?)```", repl_untagged, text, flags=re.DOTALL)

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return 1
    return 0


def main():
    n = 0
    for p in sorted(CH.glob("*.md")):
        if SKIP in p.name:
            continue
        n += process_file(p)
        print(p.name)
    print(f"updated {n} files")


if __name__ == "__main__":
    main()
