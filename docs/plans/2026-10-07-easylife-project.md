# EasyLife 项目文章发布

范围：将用户指定 Markdown 与四张配套截图发布到 /projects/easylife/，更新项目目录和首页代表项目；保留原文、阶段与证据边界。

文件：projects/easylife/source.md、render.py、index.html、assets/；项目模板支持可选平台说明；index.html、projects/index.html、styles.css 和 README.md。

任务：复制原文与引用截图；生成唯一 H1、章节目录和项目页；将 EasyLife 添加为第二个项目；约束手机截图阅读尺寸，支持窄屏表格滚动；记录重新生成命令。

验证：原文及图片字节一致；一个 H1、11 个编号章节及 Reflection；本地链接与资源、目录锚点正确；浏览器检查正文图片和表格、窄屏；git diff --check。提交合并并推送 main 后确认 Pages 与线上内容。

风险：作品处于可运行原型阶段，未进行目标老年用户验证；不扩写奖项或效果。原文中的“尚未发布”作为阶段记录保留。外部源文件不修改。

回滚：Git revert 回退内容接入提交。交付：线上地址、截图、提交和实际验证结果。
