---
{
  "cmd_name": "linode-cli",
  "cmd_category": "云平台/多云CLI",
  "cmd_dimension": "多云CLI",
  "cmd_install": "pip install linode-cli",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "doctl",
    "aws"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/cloud/more.yaml"
}
---

# linode-cli

> Linode 官方 CLI

## 安装

```bash
pip install linode-cli
```

## 用法

```
linode-cli [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `linodes` | list |
| `volumes` |  |
| `domains` |  |
| `account` |  |

## 示例

### 示例 1: 列出 Linode

```bash
linode-cli linodes list
```

### 示例 2: 创建实例

```bash
linode-cli linodes create --region us-east --type g6-standard-2
```

## 关联命令

- [[doctl]]
- [[aws]]

## 风险提示

> ⚠️ **MEDIUM**: 创建实例会计费

## 所属维度

[[多云CLI-MOC|云平台/多云CLI]]
