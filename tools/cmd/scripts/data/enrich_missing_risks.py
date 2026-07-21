#!/usr/bin/env python3
"""
为所有缺失 risks 的命令自动推断并补全风险评估。

推断规则（按优先级）：
1. 匹配 critical 关键词 → critical
2. 匹配 high 关键词 → high
3. 匹配 medium 关键词 → medium
4. 其余 → low

描述会结合命令自身功能简述，并对 high/critical 追加生产环境安全提示。
"""
import sys
import os
import re
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

RISK_LEVEL_VALUE = {"low": 1, "medium": 2, "high": 3, "critical": 4}

# 优先级从高到低匹配
CRITICAL_PATTERNS = [
    "rm -rf", "fdisk", "mkfs", "fsck", "dd", "wipe", "shred", "parted",
    "destroy", "format disk", "force push", "push --force", "reset --hard",
    "checkout -f", "rm -r", "rm -f",
]

HIGH_PATTERNS = [
    "delete", "drop", "prune", "purge", "kill", "uninstall", "remove",
    "clean", "write", "modify", "apply", "scale", "rollout", "patch",
    "exec", "reset", "revert", "checkout", "push", "shutdown", "reboot",
    "halt", "poweroff", "format",
]

MEDIUM_PATTERNS = [
    "install", "build", "run", "start", "config", "set", "enable", "disable",
    "restart", "create", "add", "update", "upgrade", "deploy", "init",
    "mount", "unmount", "register",
]

LOW_PATTERNS = [
    "show", "list", "get", "status", "log", "info", "describe", "explain",
    "version", "help", "check", "test", "validate", "search", "find",
    "ps", "top", "ping", "curl", "wget", "cat", "grep", "awk", "sed",
    "df", "du", "free", "uptime", "whoami", "env", "printenv", "clone",
    "pull", "fetch",
]


def match_any(text: str, patterns):
    """匹配关键词；短关键词（<=3 字符）要求前后为非字母字符，避免误命中子串。"""
    text_lower = text.lower()
    for p in patterns:
        p_lower = p.lower()
        if len(p_lower) <= 3:
            for m in re.finditer(r'\b' + re.escape(p_lower) + r'\b', text_lower):
                start, end = m.span()
                prev_ok = start == 0 or text_lower[start - 1] in ' \t\n/_-='
                next_ok = end == len(text_lower) or text_lower[end] in ' \t\n/_-=,.;:|'
                if prev_ok and next_ok:
                    return True
        elif p_lower in text_lower:
            return True
    return False


def infer_risk(name: str, description: str, category: str):
    text = f"{name} {description}"

    # 特殊规则：一些命令虽然含通用词，但实际风险更高/更低
    if name.startswith("git "):
        if match_any(text, ["reset", "checkout -f", "push --force", "force push", "clean -f"]):
            return "high", "Git 重写历史或强制推送会覆盖他人提交/丢失数据，生产分支请先备份并启用保护规则。"
        if match_any(text, ["push", "merge", "rebase", "cherry-pick"]):
            return "medium", "会改变仓库状态，请确认分支、提交范围及冲突处理后再执行。"
        return "low", "只读查询类 Git 操作，风险较低，但仍需确认仓库与分支。"

    if name.startswith("docker "):
        if match_any(text, ["rm", "rmi", "prune", "kill", "system prune", "volume rm", "network rm"]):
            return "high", "会删除容器、镜像或网络资源，生产环境请确认对象并评估依赖影响。"
        if match_any(text, ["run", "exec", "build", "create", "start", "stop", "restart"]):
            return "medium", "会改变容器生命周期或构建新镜像，请在测试环境验证参数后再用于生产。"
        return "low", "Docker 信息查询类操作，风险较低。"

    if name.startswith("kubectl "):
        if match_any(text, ["delete", "exec", "drain", "cordon", "taint", "scale", "rollout", "apply", "patch"]):
            return "high", "会直接影响集群运行态，生产环境请确认 namespace、label selector、级联影响及变更窗口。"
        if match_any(text, ["create", "run", "expose", "set", "edit", "label", "annotate"]):
            return "medium", "会创建或修改 Kubernetes 资源，请在非生产环境验证后再应用。"
        return "low", "Kubernetes 只读查询类操作，风险较低。"

    # 通用关键词匹配
    if match_any(text, CRITICAL_PATTERNS):
        return "critical", "可能导致数据永久丢失或系统不可用，生产环境执行前必须备份并仔细核对目标。"

    if match_any(text, HIGH_PATTERNS):
        return "high", "可能影响服务可用性或数据完整性，生产环境请先确认参数、通知相关方并在低峰期执行。"

    if match_any(text, MEDIUM_PATTERNS):
        return "medium", "会修改系统或应用状态，建议在测试环境验证后再应用于生产。"

    if match_any(text, LOW_PATTERNS):
        return "low", "只读/信息查询类命令，风险较低，但仍需确认目标对象。"

    # 默认按分类兜底
    cat_lower = category.lower()
    if any(x in cat_lower for x in ["诊断", "信息", "查询", "监控", "日志", "状态"]):
        return "low", "只读/信息查询类操作，风险较低，但仍需确认目标对象与权限。"
    if any(x in cat_lower for x in ["删除", "安全", "备份恢复", "故障排查"]):
        return "high", "可能影响服务或数据，生产环境请确认目标、备份数据并评估影响范围。"

    return "low", "命令风险较低，执行前请阅读文档并确认参数。"


def main(data_dir: str = "data") -> int:
    meta_path = os.path.join(data_dir, "metadata.yaml")
    meta = yaml.load(open(meta_path, "r", encoding="utf-8"))

    filled = 0
    for rel_file in meta.get("data_files", []):
        path = os.path.join(data_dir, rel_file)
        with open(path, "r", encoding="utf-8") as f:
            doc = yaml.load(f)

        changed = False
        for cmd in doc.get("commands", []):
            if cmd.get("risks"):
                continue
            level, desc = infer_risk(
                cmd.get("name", ""),
                cmd.get("description", ""),
                cmd.get("category", ""),
            )
            cmd["risks"] = [{"level": level, "description": desc}]
            changed = True
            filled += 1

        if changed:
            with open(path, "w", encoding="utf-8") as f:
                yaml.dump(doc, f)
            print(f"{rel_file}: filled {filled} commands")

    print(f"\nTotal commands filled with risk: {filled}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data"))
