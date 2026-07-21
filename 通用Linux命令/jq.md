---
{
  "cmd_name": "jq",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "包管理器安装，如 sudo apt install jq / sudo yum install jq",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "yq",
    "sed"
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

# jq

> 命令行 JSON 处理器

## 安装

```bash
包管理器安装，如 sudo apt install jq / sudo yum install jq
```

## 用法

```
jq [OPTIONS] FILTER [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 输出原始字符串（不带引号） |
| `-c` | 紧凑输出 |
| `-s` | 将所有输入读取为数组 |

## 示例

### 示例 1: 提取 name 字段

```bash
jq '.name' data.json
```

### 示例 2: 提取数组中每个对象的 id

```bash
jq -r '.items[] | .id' data.json
```

## 关联命令

- [[yq]]
- [[sed]]

## 风险提示

> ⚠️ **LOW**: 只读处理，注意输出重定向会覆盖目标文件

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
