#!/usr/bin/env python3
"""Scan markdown files for fenced code block languages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG_RE = re.compile(r"^```(\S*)", re.MULTILINE)

def main():
    totals = {}
    checklist = []
    for md in sorted(ROOT.rglob("*.md")):
        if md.name == "README.md":
            continue
        text = md.read_text(encoding="utf-8")
        langs = LANG_RE.findall(text)
        counts = {}
        for lang in langs:
            key = lang if lang else "(untagged)"
            counts[key] = counts.get(key, 0) + 1
            totals[key] = totals.get(key, 0) + 1
        needs = counts.get("java", 0) + counts.get("cpp", 0) + counts.get("c++", 0)
        checklist.append((str(md.relative_to(ROOT)), counts, needs))
    print("=== Per file ===")
    for path, counts, needs in checklist:
        if needs or counts.get("(untagged)", 0):
            print(f"{path}: {counts} -> needs conversion: {needs}")
    print("\n=== Totals ===")
    for k, v in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    print(f"\nFiles: {len(checklist)}")
    print(f"Java+cpp to convert: {totals.get('java',0)+totals.get('cpp',0)+totals.get('c++',0)}")

if __name__ == "__main__":
    main()
