#!/usr/bin/env python3
"""Find remaining non-Python code blocks in markdown articles."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JAVA_CPP = re.compile(
    r"\b(void|int\[\]|HashMap|LinkedList|LinkedHashMap|TreeNode\*|nullptr|"
    r"INT_MIN|INT_MAX|public class|#include|vector<|std::|\.begin\(\)|\.end\(\))\b"
)
BLOCK_RE = re.compile(r"^```(\S*)\s*\n(.*?)^```", re.MULTILINE | re.DOTALL)

def main():
    issues = []
    for md in sorted(ROOT.rglob("*.md")):
        if md.name == "README.md":
            continue
        text = md.read_text(encoding="utf-8")
        for lang, block in BLOCK_RE.findall(text):
            lang = lang or "(untagged)"
            if lang.lower() in ("python", "py"):
                continue
            if lang.lower() in ("java", "cpp", "c++"):
                issues.append((str(md.relative_to(ROOT)), lang, "non-python fence"))
                continue
            if JAVA_CPP.search(block):
                issues.append((str(md.relative_to(ROOT)), lang, block[:100].replace("\n", " ")))

    print(f"Issues: {len(issues)}")
    for item in issues[:30]:
        print(" | ".join(item))

if __name__ == "__main__":
    main()
