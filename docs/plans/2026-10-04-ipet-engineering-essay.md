# 发布 iPet 工程实践文章

范围：用户指定的原始工程文章放入 /writing/ipet-native-apple/，更新文章目录和首页思考记录；项目中的设计案例保持原状。

文件：writing/ipet-native-apple/source.md 与 index.html、writing/_templates/post.html、writing/index.html、index.html、README.md。

任务：保留原文副本，使用 Pandoc 生成唯一主标题和可展开目录；标注工程实践分类与网站发布日期；替换空目录和首页占位条目，记录重新生成命令。

验证：原文一致、一个 H1 与 14 个章节、资源及目录锚点可用、手机不溢出、浏览器检查；git diff --check，提交合并并推送 main，确认 Pages 和线上文章。

风险与回滚：文章版本信息沿用作者原文，不另作扩写；Git revert 回退本次功能提交，外部原文件不修改。

交付：文章地址、发布状态、截图及 Git 提交。
