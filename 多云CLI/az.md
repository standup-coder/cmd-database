---
{
  "cmd_name": "az",
  "cmd_category": "云平台/多云CLI",
  "cmd_dimension": "多云CLI",
  "cmd_install": "参考 https://learn.microsoft.com/cli/azure/install-azure-cli",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "aws",
    "terraform"
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

# az

> Azure 官方 CLI

## 安装

```bash
参考 https://learn.microsoft.com/cli/azure/install-azure-cli
```

## 用法

```
az [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `login` |  |
| `group` |  |
| `vm` |  |
| `aks` |  |
| `account` |  |

## 示例

### 示例 1: 登录 Azure

```bash
az login
```

### 示例 2: 列出虚拟机

```bash
az vm list
```

## 关联命令

- [[aws]]
- [[terraform]]

## 风险提示

> ⚠️ **MEDIUM**: az 操作会产生费用，请确认订阅和资源组

## 所属维度

[[多云CLI-MOC|云平台/多云CLI]]
