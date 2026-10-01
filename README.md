# xufilps.github.io

个人作品集的静态站点。首页、项目、文章和关于页面由 HTML 与 CSS 组成，主题切换使用一小段原生 JavaScript；无构建步骤或远程依赖。

## 本地预览

在仓库根目录运行 `python3 -m http.server 8000`，然后打开 `http://localhost:8000/`。四个页面都可以在关闭 JavaScript 后阅读和导航。

## 用 Markdown 写文章

仓库提供 [Markdown 正文模板](writing/_templates/post.md) 和 [HTML 页面模板](writing/_templates/post.html)。Markdown 文件开头的 `---` 区域填写标题、摘要、日期和分类；正文从引言开始，页面模板会生成唯一的主标题。发布前把模板中的提示文字替换成自己的内容，不确定的事实和结果应如实标明。

在仓库根目录执行以下命令，先把 `my-first-post` 换成文章的英文短名，再编辑新建的 Markdown 文件：

```sh
mkdir -p writing/_drafts writing/my-first-post
cp writing/_templates/post.md writing/_drafts/my-first-post.md
pandoc writing/_drafts/my-first-post.md --standalone --template=writing/_templates/post.html -o writing/my-first-post/index.html
```

每次修改草稿后重新运行最后一行。生成的页面地址是 `/writing/my-first-post/`；图片可以放在该文章目录下，在 Markdown 中使用相对路径。发布时还需手动更新 `writing/index.html` 的文章卡片和篇数，并按需更新首页的文章入口。Pandoc 只负责转换和套用页面模板，不会自动维护文章列表。若本机没有 Pandoc，需先安装它才能运行转换命令。

## 网站图标

浏览器标签页使用 `assets/site-icon.svg`，iPhone 或 iPad“添加到主屏幕”使用仓库根目录的 `apple-touch-icon.png`（180 × 180 像素）。当前图标是使用本站配色制作的 `x` 标识，四个页面和今后生成的文章页都已引用它。以后更换设计时，同时更新 SVG 与 PNG，保持两处图案一致；发布后若主屏幕仍显示旧图标，可移除旧快捷方式再重新添加。

## 页面中的个人照片

目前首页和关于页都使用纯白的 `assets/avatar-placeholder.svg`。准备一张自己有权使用的正方形照片或插画，裁切时让主体居中，导出为适合网页使用的 `assets/avatar.webp`（或 PNG/JPEG），然后把 `index.html` 与 `about/index.html` 中的头像 `src` 都改为新文件路径，并将 `alt` 改为准确描述。现有样式会分别以 88 × 88 和 112 × 112 像素展示；替换后要在手机宽度和明暗主题下检查裁切效果。


## 发布

GitHub Pages 从 `main` 分支的仓库根目录发布。改动先在功能分支预览和检查，再合并到 `main`；增加个人项目、文章、图片或联系信息时，发布前核对内容与公开权限。
