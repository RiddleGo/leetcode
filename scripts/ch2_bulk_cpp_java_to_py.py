#!/usr/bin/env python3
"""Bulk replace cpp/java fences in Chapter 2 with pre-converted Python blocks."""
from pathlib import Path

CH = Path(r"d:\leetcode\fucking-algorithm-book\第2章-动态规划系列")

# file -> list of (old_block_without_fences, new_block_without_fences)
# Blocks matched after normalizing ```lang to content only via unique substrings

REPLACEMENTS: dict[str, list[tuple[str, str]]] = {}

def apply_file(name: str, pairs: list[tuple[str, str]]) -> None:
    path = CH / name
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        old_f = f"```cpp\n{old}\n```"
        new_f = f"```python\n{new}\n```"
        if old_f not in text:
            old_f = f"```java\n{old}\n```"
            new_f = f"```python\n{new}\n```"
        if old_f not in text:
            raise ValueError(f"Block not found in {name}:\n{old[:80]}...")
        text = text.replace(old_f, new_f, 1)
    path.write_text(text, encoding="utf-8")
    print(f"OK {name} ({len(pairs)} blocks)")
