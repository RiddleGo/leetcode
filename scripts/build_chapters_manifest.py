#!/usr/bin/env python3
"""Scan chapter markdown files and generate chapters.json + index.html."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_BASE = "https://riddlego.github.io/leetcode"
HUB_URL = "https://riddlego.github.io/interview-hub/index.html"
REPO_URL = "https://github.com/RiddleGo/leetcode"
HUB_REPO = "https://github.com/RiddleGo/interview-hub"

CHAPTER_ORDER = [
    "第1章-核心套路篇",
    "第2章-动态规划系列",
    "第3章-数据结构系列",
    "第4章-算法思维系列",
    "第5章-高频面试系列",
]

CHAPTER_LABELS = {
    "第1章-核心套路篇": "第1章 核心套路篇",
    "第2章-动态规划系列": "第2章 动态规划系列",
    "第3章-数据结构系列": "第3章 数据结构系列",
    "第4章-算法思维系列": "第4章 算法思维系列",
    "第5章-高频面试系列": "第5章 高频面试系列",
}


def title_from_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    stem = path.stem
    if "-" in stem:
        return stem.split("-", 1)[1]
    return stem


def md_to_reader_path(rel: str) -> str:
    return f"reader.html?path={rel.replace(chr(92), '/')}"


def collect_chapters() -> list[dict]:
    chapters = []
    for folder_name in CHAPTER_ORDER:
        folder = ROOT / folder_name
        if not folder.is_dir():
            continue
        articles = []
        for md in sorted(folder.glob("*.md")):
            if md.stat().st_size == 0:
                continue
            rel = md.relative_to(ROOT).as_posix()
            reader_path = md_to_reader_path(rel)
            articles.append(
                {
                    "title": title_from_file(md),
                    "path": rel,
                    "html": reader_path,
                    "url": f"{PAGES_BASE}/{reader_path}",
                }
            )
        chapters.append(
            {
                "id": folder_name,
                "label": CHAPTER_LABELS.get(folder_name, folder_name),
                "articles": articles,
            }
        )
    return chapters


INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>学习总入口 · 算法小抄与面经</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --bg: #0c0e14;
      --card: #151922;
      --border: rgba(255,255,255,.08);
      --text: #eef2f8;
      --muted: #8b95a8;
      --a: #3ee0c9;
      --b: #a78bfa;
      --radius: 16px;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      font-family: "DM Sans", "PingFang SC", "Microsoft YaHei", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      background-image:
        radial-gradient(ellipse 100% 80% at 100% 0%, rgba(62,224,201,.12), transparent 50%),
        radial-gradient(ellipse 70% 50% at 0% 100%, rgba(167,139,250,.1), transparent 45%);
    }}
    .wrap {{ max-width: 960px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem; }}
    header {{ text-align: center; margin-bottom: 2.75rem; }}
    header h1 {{
      font-size: clamp(1.6rem, 4vw, 2.1rem);
      font-weight: 700;
      letter-spacing: -0.03em;
      margin: 0 0 .5rem;
      background: linear-gradient(120deg, var(--text), var(--a));
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    header p {{ color: var(--muted); margin: 0; font-size: .95rem; }}
    header .motto {{
      margin: 1rem 0 0;
      font-size: .88rem;
      font-style: italic;
      color: rgba(167,139,250,.85);
    }}
    .grid {{
      display: grid;
      gap: 1.1rem;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    }}
    article {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.35rem 1.25rem 1.25rem;
      display: flex;
      flex-direction: column;
      gap: .75rem;
      transition: border-color .2s, box-shadow .2s;
    }}
    article:hover {{
      border-color: rgba(62,224,201,.25);
      box-shadow: 0 12px 40px rgba(0,0,0,.35);
    }}
    article.featured {{ grid-column: 1 / -1; border-color: rgba(167,139,250,.35); }}
    article h2 {{ margin: 0; font-size: 1.05rem; font-weight: 700; letter-spacing: -0.02em; }}
    article .meta {{ font-size: .78rem; color: var(--muted); }}
    article p.desc {{ margin: 0; flex: 1; font-size: .875rem; color: #b8c0d0; }}
    .actions {{ display: flex; flex-wrap: wrap; gap: .5rem; margin-top: .25rem; }}
    a.btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: .45rem .85rem;
      border-radius: 10px;
      font-size: .8rem;
      font-weight: 600;
      text-decoration: none;
      border: 1px solid var(--border);
      color: var(--text);
      background: rgba(255,255,255,.04);
      transition: border-color .15s, color .15s, background .15s;
    }}
    a.btn:hover {{ border-color: var(--a); color: var(--a); background: rgba(62,224,201,.08); }}
    a.btn.primary {{
      border-color: rgba(62,224,201,.35);
      color: var(--a);
      background: rgba(62,224,201,.1);
    }}
    a.btn.primary:hover {{ background: rgba(62,224,201,.18); }}
    .section-label {{
      text-align: center;
      font-size: 0.82rem;
      color: var(--muted);
      margin: 0.5rem 0 0.75rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      grid-column: 1 / -1;
    }}
    .chapter-block {{ grid-column: 1 / -1; }}
    .chapter-block h3 {{
      margin: 1.5rem 0 0.75rem;
      font-size: 1rem;
      color: var(--b);
      font-weight: 700;
    }}
    .article-list {{
      display: grid;
      gap: 0.5rem;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .article-list a {{
      display: block;
      padding: 0.55rem 0.75rem;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: rgba(255,255,255,.03);
      color: var(--text);
      text-decoration: none;
      font-size: 0.85rem;
      transition: border-color .15s, color .15s;
    }}
    .article-list a:hover {{ border-color: var(--a); color: var(--a); }}
    footer {{
      margin-top: 3rem;
      text-align: center;
      font-size: .8rem;
      color: var(--muted);
    }}
    footer a {{ color: var(--a); text-decoration: none; }}
    footer a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>学习总入口</h1>
      <p>labuladong 算法小抄（Python 版）+ 面经导航（Agent / AI Infra / 自动驾驶 / 搜广推）</p>
      <p class="motto">你最终会成为你自己</p>
    </header>
    <div class="grid" id="cards">
      <article class="featured">
        <h2>面经导航 · interview-hub</h2>
        <div class="meta">300+ 题 · 四方向面经 + AI 系统教材</div>
        <p class="desc">Agent 算法、AI Infra、自动驾驶、搜广推四大题库单页学习，以及《人工智能系统》教材在线阅读。</p>
        <div class="actions">
          <a class="btn primary" href="{hub_url}">打开面经导航</a>
          <a class="btn" href="{hub_repo}">GitHub 仓库</a>
        </div>
      </article>
      <p class="section-label">算法小抄 · Python 版（{article_count} 篇）</p>
    </div>
    <div id="chapters"></div>
    <footer>
      <a href="{repo_url}">@RiddleGo/leetcode</a>
      · 示例代码已全部转换为 Python
    </footer>
  </div>
  <script>
    const CHAPTERS = {chapters_json};
    const root = document.getElementById("chapters");
    CHAPTERS.forEach(ch => {{
      const block = document.createElement("div");
      block.className = "chapter-block";
      block.innerHTML = `<h3>${{ch.label}}（${{ch.articles.length}} 篇）</h3>`;
      const ul = document.createElement("ul");
      ul.className = "article-list";
      ch.articles.forEach(a => {{
        const li = document.createElement("li");
        const link = document.createElement("a");
        link.href = "reader.html?path=" + encodeURIComponent(a.path);
        link.textContent = a.title;
        li.appendChild(link);
        ul.appendChild(li);
      }});
      block.appendChild(ul);
      root.appendChild(block);
    }});
  </script>
</body>
</html>
"""


def write_outputs(chapters: list[dict]) -> int:
    article_count = sum(len(c["articles"]) for c in chapters)
    chapters_json = json.dumps(chapters, ensure_ascii=False, indent=2)

    (ROOT / "chapters.json").write_text(chapters_json + "\n", encoding="utf-8")

    index_html = INDEX_TEMPLATE.format(
        hub_url=HUB_URL,
        hub_repo=HUB_REPO,
        repo_url=REPO_URL,
        article_count=article_count,
        chapters_json=chapters_json,
    )
    (ROOT / "index.html").write_text(index_html, encoding="utf-8")
    return article_count


def update_readme(chapters: list[dict]) -> None:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    online = (
        "## 在线访问\n\n"
        "- **学习总入口（推荐）**：https://riddlego.github.io/leetcode/\n"
        "- **面经导航**：https://riddlego.github.io/interview-hub/index.html\n"
    )
    if "## 在线访问" not in text:
        marker = "> **说明：**"
        if marker in text:
            idx = text.index("\n", text.index(marker)) + 1
            text = text[:idx] + "\n" + online + text[idx:]
        else:
            text = online + "\n" + text

    toc_lines = ["# 目录", ""]
    for ch in chapters:
        toc_lines.append(f"* {ch['label']}")
        for a in ch["articles"]:
            toc_lines.append(f"  * [{a['title']}]({a['html']})")
            if a["path"].endswith("2.17-经典动态规划：完全背包问题.md"):
                toc_lines.append("  * 2.18 题目千百变，套路不会变（原文缺失，上游仓库未收录）")
        toc_lines.append("")
    new_toc = "\n".join(toc_lines)

    if "# 目录" in text:
        start = text.index("# 目录")
        text = text[:start] + new_toc
    else:
        text = text.rstrip() + "\n\n" + new_toc

    readme.write_text(text, encoding="utf-8")


def main() -> None:
    chapters = collect_chapters()
    count = write_outputs(chapters)
    update_readme(chapters)
    print(f"Generated chapters.json, index.html, README TOC ({count} articles, {len(chapters)} chapters)")


if __name__ == "__main__":
    main()
