# GitHub Pages 部署说明

本地仓库已初始化并完成首次 commit，远程地址：`https://github.com/RiddleGo/leetcode.git`

## 1. 创建 GitHub 仓库

在浏览器打开 [New repository](https://github.com/new)，创建 **`RiddleGo/leetcode`**（Public，不要勾选 README）。

或使用 CLI（需先 `gh auth login`）：

```powershell
cd d:\leetcode
gh repo create RiddleGo/leetcode --public --source=. --remote=origin --push
```

若仓库已存在，仅推送：

```powershell
cd d:\leetcode
git push -u origin main
```

## 2. 启用 GitHub Pages

仓库 **Settings → Pages**：

- Source: **Deploy from a branch**
- Branch: **`main`** / **`/ (root)`**

或使用 CLI：

```powershell
gh api repos/RiddleGo/leetcode/pages -X POST -f "source[branch]=main" -f "source[path]=/"
```

## 3. 访问地址

部署完成后（约 1–3 分钟）：

- 学习总入口：https://riddlego.github.io/leetcode/
- 面经导航：https://riddlego.github.io/interview-hub/index.html

## 4. 更新章节目录

新增或重命名文章后：

```powershell
python scripts/build_chapters_manifest.py
git add chapters.json index.html README.md
git commit -m "Update chapter manifest"
git push
```
