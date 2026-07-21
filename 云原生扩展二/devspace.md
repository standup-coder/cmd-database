---
{
  "cmd_name": "devspace",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://www.devspace.sh/docs/getting-started/install",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "telepresence",
    "okteto"
  ],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# devspace

> Kubernetes 本地开发工作流

## 安装

```bash
参考 https://www.devspace.sh/docs/getting-started/install
```

## 用法

```
devspace [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `dev` | 启动开发模式 |
| `deploy` | 部署 |
| `purge` | 清理 |
| `logs` |  |

## 示例

### 示例 1: 进入开发模式

```bash
devspace dev
```

### 示例 2: 部署到集群

```bash
devspace deploy
```

## 关联命令

- [[telepresence]]
- [[okteto]]

## 风险提示

> ⚠️ **MEDIUM**: devspace deploy 会修改集群，请确认 namespace 和 values

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
