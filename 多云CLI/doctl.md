---
{
  "cmd_name": "doctl",
  "cmd_category": "云平台/多云CLI",
  "cmd_dimension": "多云CLI",
  "cmd_install": "参考 https://docs.digitalocean.com/reference/doctl/how-to/install/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "linode-cli",
    "aws"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/cloud/more.yaml"
}
---

# doctl

> DigitalOcean 官方 CLI

## 安装

```bash
参考 https://docs.digitalocean.com/reference/doctl/how-to/install/
```

## 用法

```
doctl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `auth` | init |
| `compute` | droplet |
| `kubernetes` | cluster |
| `apps` |  |

## 示例

### 示例 1: 初始化认证

```bash
doctl auth init
```

### 示例 2: 列出 droplet

```bash
doctl compute droplet list
```

## 关联命令

- [[linode-cli]]
- [[aws]]

## 风险提示

> ⚠️ **MEDIUM**: droplet 操作会计费，请确认

## 所属维度

[[多云CLI-MOC|云平台/多云CLI]]
