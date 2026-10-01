# xufilps.github.io

个人作品集的静态站点。首页、项目、文章和关于页面由 HTML 与 CSS 组成，主题切换使用一小段原生 JavaScript；无构建步骤或远程依赖。

## 本地预览

在仓库根目录运行 `python3 -m http.server 8000`，然后打开 `http://localhost:8000/`。四个页面都可以在关闭 JavaScript 后阅读和导航。

## 更新内容

- `index.html`：紧凑身份区，以及关于我、代表项目、思考记录和联系侧栏。新内容应替换对应的空状态。
- `projects/index.html`：双栏项目目录。先补充有证据的项目背景、职责、过程、结果与链接。
- `writing/index.html`：文章分类、数量和卡片目录。发布前建立独立文章页面，再添加目录和首页链接。
- `about/index.html`：正文介绍与资料侧栏，只填写本人确认并愿意公开的内容。
- `styles.css`：全站视觉与响应式样式；`theme.js`：深浅主题切换；`assets/github-mark.svg`：导航中的 GitHub 图标。

首页和关于页的头像使用 `assets/avatar-placeholder.svg` 纯白占位图。添加真实头像时，把图片放入 `assets/`，再更新两个页面中头像的 `src` 和 `alt`；现有样式会保持尺寸并居中裁切。

现有 `notes/notes-20260930.md` 保留在仓库，未接入公开文章目录。旧版页面可从 Git 历史恢复。

## 发布

GitHub Pages 从 `main` 分支的仓库根目录发布。改动先在功能分支预览和检查，再合并到 `main`；增加个人项目、文章、图片或联系信息时，发布前核对内容与公开权限。
