# xufilps.github.io

个人作品集的静态站点。首页、项目、文章和关于页面由 HTML 与 CSS 组成，主题切换使用一小段原生 JavaScript；无构建步骤或远程依赖。

## 本地预览

在仓库根目录运行 `python3 -m http.server 8000`，然后打开 `http://localhost:8000/`。四个页面都可以在关闭 JavaScript 后阅读和导航。

## 更新内容

- `index.html`：首页介绍、代表项目和文章入口。新内容应替换对应的空状态。
- `projects/index.html`：公开项目目录。先补充有证据的项目背景、职责、过程、结果与链接。
- `writing/index.html`：已发布文章目录。发布前建立独立文章页面，再添加目录和首页链接。
- `about/index.html`：个人简介、关注方向和本人愿意公开的联系方式。
- `styles.css`：全站视觉与响应式样式；`theme.js`：深浅主题切换。

现有 `notes/notes-20260930.md` 保留在仓库，未接入公开文章目录。旧版页面可从 Git 历史恢复。

## 发布

GitHub Pages 使用仓库根目录的静态文件。这个改版目前位于 `feat/portfolio-redesign-20261001` 分支；合并或推送到实际发布分支前，请先补入并核对准备公开的个人内容。
