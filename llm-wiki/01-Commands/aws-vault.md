---
{
  "cmd_name": "aws-vault",
  "cmd_category": "云平台/多云CLI",
  "cmd_dimension": "多云CLI",
  "cmd_install": "参考 https://github.com/99designs/aws-vault",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "aws",
    "aws-vault"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/cloud/more.yaml"
}
---

# aws-vault

> AWS 凭据安全存储与切换工具

## 安装

```bash
参考 https://github.com/99designs/aws-vault
```

## 用法

```
aws-vault [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `add` | 添加 profile |
| `exec` | 执行命令 |
| `list` |  |
| `rotate` |  |

## 示例

### 示例 1: 添加凭据

```bash
aws-vault add myprofile
```

### 示例 2: 以指定 profile 执行 AWS 命令

```bash
aws-vault exec myprofile -- aws s3 ls
```

## 关联命令

- [[aws]]
- [[aws-vault]]

## 所属维度

[[多云CLI-MOC|云平台/多云CLI]]
