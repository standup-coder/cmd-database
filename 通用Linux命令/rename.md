---
{
  "cmd_name": "rename",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mv",
    "cp",
    "find"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# rename

> 批量重命名文件（Perl正则表达式版或util-linux版）

## 用法

```
rename [选项] 表达式 替换 文件...
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 模拟运行，不实际修改 |
| `-v` | 显示详细操作 |

## 示例

### 示例 1: 将所有txt改为bak

```bash
rename 's/\.txt$/.bak/' *.txt
```

### 示例 2: 模拟替换文件名中的foo为bar

```bash
rename -n 's/foo/bar/' *
```

## 关联命令

- [[mv]]
- [[cp]]
- [[find]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
