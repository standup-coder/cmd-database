---
{
  "cmd_name": "gcloud",
  "cmd_category": "云平台/多云CLI",
  "cmd_dimension": "多云CLI",
  "cmd_install": "参考 https://cloud.google.com/sdk/docs/install",
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

# gcloud

> Google Cloud 官方 CLI

## 安装

```bash
参考 https://cloud.google.com/sdk/docs/install
```

## 用法

```
gcloud [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `config` | 配置 |
| `compute` | 计算 |
| `container` | 容器 |
| `run` | 部署 |
| `auth` |  |

## 示例

### 示例 1: 登录

```bash
gcloud auth login
```

### 示例 2: 列出 VM

```bash
gcloud compute instances list
```

## 关联命令

- [[aws]]
- [[terraform]]

## 风险提示

> ⚠️ **MEDIUM**: gcloud 会创建/删除云资源并计费，请确认项目和区域

## 所属维度

[[多云CLI-MOC|云平台/多云CLI]]
