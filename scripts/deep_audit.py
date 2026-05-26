#!/usr/bin/env python3
"""Deep audit: untagged blocks, broken fences, Java/C++ residue in prose."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK_RE = re.compile(r"^```(\S*)\s*\n(.*?)^```", re.MULTILINE | re.DOTALL)
JAVA_CPP_IN_BLOCK = re.compile(
    r"\b(void\s+\w+\(|int\[\]|HashMap|LinkedList|LinkedHashMap|TreeNode\*|"
    r"nullptr|INT_MIN|INT_MAX|public\s+class|#include|vector<|std::|"
    r"\.begin\(\)|\.end\(\)|new\s+TreeNode|\.addLast\(|\.removeLast\(\))\b"
)

def main():
    untagged = []
    suspicious_untagged = []
    non_python_langs = []
    empty_blocks = []
    files_with_issues = set()

    for md in sorted(ROOT.rglob("*.md")):
        if md.name == "README.md":
            continue
        text = md.read_text(encoding="utf-8")
        rel = str(md.relative_to(ROOT))

        if not text.strip() and md.name.endswith(".md"):
            empty_blocks.append(rel)

        for lang, block in BLOCK_RE.findall(text):
            lang_key = lang or "(untagged)"
            if lang.lower() in ("java", "cpp", "c++", "javascript", "go"):
                non_python_langs.append((rel, lang_key))
                files_with_issues.add(rel)
            elif lang_key == "(untagged)":
                untagged.append((rel, block[:60].replace("\n", " ")))
                if JAVA_CPP_IN_BLOCK.search(block):
                    suspicious_untagged.append((rel, block[:80].replace("\n", " ")))
                    files_with_issues.add(rel)

        # count fences
        opens = len(re.findall(r"^```", text, re.MULTILINE))
        if opens % 2 != 0:
            files_with_issues.add(rel + " [broken fence count]")

    print("=== EMPTY ARTICLES ===")
    for f in empty_blocks:
        print(f"  {f}")

    print(f"\n=== NON-PYTHON FENCE TAGS: {len(non_python_langs)} ===")
    for item in non_python_langs[:20]:
        print(f"  {item[0]}: {item[1]}")

    print(f"\n=== UNTAGGED BLOCKS: {len(untagged)} ===")
    print(f"=== SUSPICIOUS UNTAGGED (Java/C++ syntax): {len(suspicious_untagged)} ===")
    for item in suspicious_untagged[:25]:
        print(f"  {item[0]}: {item[1]}")

    print(f"\n=== ARTICLES WITH ISSUES: {len(files_with_issues)} ===")
    for f in sorted(files_with_issues):
        print(f"  {f}")

    ok = (
        not non_python_langs
        and not suspicious_untagged
        and len(empty_blocks) <= 1  # 2.18 expected
    )
    print(f"\nOVERALL: {'PASS' if ok else 'NEEDS FIX'}")

if __name__ == "__main__":
    main()
