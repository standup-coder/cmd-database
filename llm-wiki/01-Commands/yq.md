---
{
  "cmd_name": "yq",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "参考 https://github.com/mikefarah/yq/releases",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "jq",
    "sed"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# yq

> 命令行 YAML/JSON/TOML 处理器

## 安装

```bash
参考 https://github.com/mikefarah/yq/releases
```

## 用法

```
yq [OPTIONS] [COMMAND] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 将输出编码为 JSON |
| `-i` | 原地编辑文件 |
| `-P` | 输出为 pretty YAML |

## 示例

### 示例 1: 读取 YAML 中 metadata.name

```bash
yq '.metadata.name' deploy.yaml
```

### 示例 2: 原地修改 replicas 为 3

```bash
yq -i '.spec.replicas = 3' deploy.yaml
```

## 关联命令

- [[jq]]
- [[sed]]

## 风险提示

> ⚠️ **HIGH**: -i 原地编辑会直接修改文件，建议先备份

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
