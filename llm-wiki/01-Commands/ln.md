---
{
  "cmd_name": "ln",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cp",
    "mv"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# ln

> 创建文件链接

## 用法

```
ln [OPTIONS] TARGET [LINK_NAME]
```

## 参数

| Flag | Description |
|------|-------------|
| `-s` | 创建符号链接 |
| `-f` | 强制覆盖 |
| `-v` | 显示过程 |

## 示例

### 示例 1: 创建符号链接

```bash
ln -s /path/to/file link
```

### 示例 2: 创建硬链接

```bash
ln file hardlink
```

## 关联命令

- [[cp]]
- [[mv]]

## 风险提示

> ⚠️ **MEDIUM**: 覆盖或错误的符号链接可能影响依赖路径，请确认目标

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
