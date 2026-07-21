---
{
  "cmd_name": "telepresence",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://www.telepresence.io/docs/latest/install/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubectl",
    "devspace"
  ],
  "cmd_tags": [
    "kubernetes",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# telepresence

> 本地开发连接远程 Kubernetes 服务

## 安装

```bash
参考 https://www.telepresence.io/docs/latest/install/
```

## 用法

```
telepresence [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `connect` | 连接 |
| `intercept` | 拦截 |
| `list` | 列出 |
| `quit` | 退出 |

## 示例

### 示例 1: 连接集群

```bash
telepresence connect
```

### 示例 2: 拦截服务到本地

```bash
telepresence intercept myservice --port 8080:http
```

## 关联命令

- [[kubectl]]
- [[devspace]]

## 风险提示

> ⚠️ **HIGH**: intercept 会将生产流量引到本地，请确认目标环境和回滚策略

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
