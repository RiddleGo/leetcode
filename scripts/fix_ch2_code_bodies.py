#!/usr/bin/env python3
"""Fix Python-fenced blocks that still contain C++/Java syntax."""
from pathlib import Path

CH = Path(r"d:\leetcode\fucking-algorithm-book\第2章-动态规划系列")

# (filename, old, new) — old/new without fence lines
REPLACEMENTS: list[tuple[str, str, str]] = [
    (
        "2.8-状态压缩：对动态规划进行降维打击.md",
        """int longestPalindromeSubseq(string s) {
    int n = s.size();
    // dp 数组全部初始化为 0
    vector<vector<int>> dp(n, vector<int>(n, 0));
    // base case
    for (int i = 0; i < n; i++)
        dp[i][i] = 1;
    // 反着遍历保证正确的状态转移
    for (int i = n - 2; i >= 0; i--) {
        for (int j = i + 1; j < n; j++) {
            // 状态转移方程
            if (s[i] == s[j])
                dp[i][j] = dp[i + 1][j - 1] + 2;
            else
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
        }
    }
    // 整个 s 的最长回文子串长度
    return dp[0][n - 1];
}""",
        """class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]""",
    ),
    (
        "2.8-状态压缩：对动态规划进行降维打击.md",
        """for (int i = n - 2; i >= 0; i--) {
    for (int j = i + 1; j < n; j++) {
        // 状态转移方程
        if (s[i] == s[j])
            dp[i][j] = dp[i + 1][j - 1] + 2;
        else
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
    }
}""",
        """for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            dp[i][j] = dp[i + 1][j - 1] + 2
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])""",
    ),
    (
        "2.8-状态压缩：对动态规划进行降维打击.md",
        """for (int i = n - 2; i >= 0; i--) {
    for (int j = i + 1; j < n; j++) {
        // 在这里，一维 dp 数组中的数是什么？
        if (s[i] == s[j])
            dp[j] = dp[j - 1] + 2;
        else
            dp[j] = max(dp[j], dp[j - 1]);
    }
}""",
        """for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            dp[j] = dp[j - 1] + 2
        else:
            dp[j] = max(dp[j], dp[j - 1])""",
    ),
    (
        "2.8-状态压缩：对动态规划进行降维打击.md",
        """for (int i = n - 2; i >= 0; i--) {
    for (int j = i + 1; j < n; j++) {
        if (s[i] == s[j])
            // dp[i][j] = dp[i+1][j-1] + 2;
            dp[j] = ?? + 2;
        else
            // dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
            dp[j] = max(dp[j], dp[j - 1]);
    }
}""",
        """for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            dp[j] = pre + 2  # dp[i+1][j-1] + 2
        else:
            dp[j] = max(dp[j], dp[j - 1])""",
    ),
    (
        "2.8-状态压缩：对动态规划进行降维打击.md",
        """for (int i = n - 2; i >= 0; i--) {
    // 存储 dp[i+1][j-1] 的变量
    int pre = 0;
    for (int j = i + 1; j < n; j++) {
        int temp = dp[j];
        if (s[i] == s[j])
            // dp[i][j] = dp[i+1][j-1] + 2;
            dp[j] = pre + 2;
        else
            dp[j] = max(dp[j], dp[j - 1]);
        // 到下一轮循环，pre 就是 dp[i+1][j-1] 了
        pre = temp;
    }
}""",
        """for i in range(n - 2, -1, -1):
    pre = 0
    for j in range(i + 1, n):
        temp = dp[j]
        if s[i] == s[j]:
            dp[j] = pre + 2
        else:
            dp[j] = max(dp[j], dp[j - 1])
        pre = temp""",
    ),
    (
        "2.8-状态压缩：对动态规划进行降维打击.md",
        """if (s[5] == s[7])
    // dp[5][7] = dp[i+1][j-1] + 2;
    dp[7] = pre + 2;""",
        """if s[5] == s[7]:
    dp[7] = pre + 2  # dp[i+1][j-1] + 2""",
    ),
    (
        "2.8-状态压缩：对动态规划进行降维打击.md",
        """// dp 数组全部初始化为 0
vector<vector<int>> dp(n, vector<int>(n, 0));
// base case
for (int i = 0; i < n; i++)
    dp[i][i] = 1;""",
        """dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1""",
    ),
    (
        "2.8-状态压缩：对动态规划进行降维打击.md",
        """// 一维 dp 数组全部初始化为 1
vector<int> dp(n, 1);""",
        """dp = [1] * n""",
    ),
    (
        "2.8-状态压缩：对动态规划进行降维打击.md",
        """int longestPalindromeSubseq(string s) {
    int n = s.size();
    // base case：一维 dp 数组全部初始化为 0
    vector<int> dp(n, 1);

    for (int i = n - 2; i >= 0; i--) {
        int pre = 0;
        for (int j = i + 1; j < n; j++) {
            int temp = dp[j];
            // 状态转移方程
            if (s[i] == s[j])
                dp[j] = pre + 2;
            else
                dp[j] = max(dp[j], dp[j - 1]);
            pre = temp;
        }
    }
    return dp[n - 1];
}""",
        """class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            pre = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                pre = temp
        return dp[n - 1]""",
    ),
]


def main():
    from collections import defaultdict
    by_file: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for fname, old, new in REPLACEMENTS:
        by_file[fname].append((old, new))

    for fname, pairs in by_file.items():
        path = CH / fname
        text = path.read_text(encoding="utf-8")
        for old, new in pairs:
            if old not in text:
                print(f"MISSING in {fname}: {old[:60]}...")
                continue
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")
        print(f"fixed {fname}")


if __name__ == "__main__":
    main()
