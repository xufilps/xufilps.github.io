"""Render EasyLife from the unchanged user-provided Markdown."""
from pathlib import Path
import subprocess

project = Path(__file__).resolve().parent
root = project.parents[1]
lines = (project / "source.md").read_text().splitlines()
title = "EasyLife — 从日常小事开始的老年人陪伴设计"
assert lines[0] == "# " + title
subprocess.run([
    "pandoc", "--from=gfm", "--standalone", "--toc", "--toc-depth=2",
    "--metadata", "title=" + title,
    "--metadata", "description=以小安的角色互动、日常记录与家友联系，探索老年人的数字陪伴体验。当前为可运行 iOS 原型，尚未开展目标老年用户验证。",
    "--metadata", "project_meta=iPhone / SwiftUI + SpriteKit · 可运行原型 · 记录于 2026-10-07",
    f"--template={root / 'projects/_templates/project.html'}",
    "-o", str(project / "index.html"),
], input="\n".join(lines[1:]), text=True, check=True)
