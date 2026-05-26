#!/usr/bin/env python3
from pathlib import Path
import re

CH = Path(r"d:\leetcode\fucking-algorithm-book\第2章-动态规划系列")
files = [
    "2.8-状态压缩：对动态规划进行降维打击.md",
    "2.9-以最小插入次数构造回文串.md",
    "2.10-动态规划之正则表达式.md",
    "2.13-经典动态规划：高楼扔鸡蛋（进阶）.md",
    "2.14-经典动态规划：戳气球问题.md",
    "2.16-经典动态规划：子集背包问题.md",
    "2.17-经典动态规划：完全背包问题.md",
    "2.19-动态规划和回溯算法，到底是什么关系.md",
]
for name in files:
    p = CH / name
    t = p.read_text(encoding="utf-8")
    t2 = re.sub(r"```(?:java|cpp|c\+\+|C\+\+)\s*\n", "```python\n", t, flags=re.I)
    t2 = re.sub(r"```\n(int change|int\[\]|bool isMatch|int minInsertions)", r"```python\n\1", t2)
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("updated", name)
