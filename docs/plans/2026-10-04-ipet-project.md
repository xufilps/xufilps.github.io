# iPet 项目文章接入计划

范围：将用户指定的 iPet Markdown 原文接入个人网站项目栏目，生成 /projects/ipet/，更新项目目录和首页代表项目。保留原文及其开发状态、AI 协作和未完成事项，不增加未提供的图片或成果。

文件：projects/ipet/source.md（原文副本）、projects/ipet/index.html（生成页）、projects/_templates/project.html（项目模板）、index.html、projects/index.html、README.md；必要时为长文补充少量 CSS。

任务：保存原文，使用现有 Pandoc 流程生成页面；替换项目占位条目；检查导航与本地路径；预览桌面及手机页面；提交并合并到 main，推送现有 origin。

验证：原文副本字节一致；页面只有一个 H1 且完整包含 14 个章节；本地链接和资源存在；git diff --check；浏览器检查标题、项目入口和窄屏代码块。发布后核对远端提交及线上页面。

风险：文章中的版本与状态是作者提供的项目快照，不独立扩写；Markdown 中大量代码块需横向滚动避免撑开手机页面。

回滚：通过 Git revert 回退接入提交；外部原始 Markdown 不修改。

交付：项目 URL、Git 提交及实际发布状态。
