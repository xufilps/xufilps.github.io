"""Render the supplied iPet article without editing its Markdown source."""
from pathlib import Path
import re
import subprocess

project = Path(__file__).resolve().parent
root = project.parents[1]
source = (project / "source.md").read_text()
lines = source.splitlines()
assert lines[0].strip() == "# iPet"
assert lines[1] == "## 一次关于桌面陪伴体验的跨平台再设计"
# The template owns the title; numbered sections belong below that H1.
body = "\n".join(lines[2:])
body = re.sub(r"^# (\d{2} / .+)$", r"## \1", body, flags=re.MULTILINE)
subprocess.run([
    "pandoc", "--from=gfm", "--standalone", "--toc", "--toc-depth=2",
    "--metadata", "title=iPet — 一次关于桌面陪伴体验的跨平台再设计",
    "--metadata", "description=从桌面空间、角色互动到移动端养成，探索数字陪伴体验如何融入 Apple 设备。",
    f"--template={root / 'projects/_templates/project.html'}",
    "-o", str(project / "index.html"),
], input=body, text=True, check=True)
