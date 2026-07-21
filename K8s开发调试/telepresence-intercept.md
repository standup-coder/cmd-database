---
{
  "cmd_name": "telepresence intercept",
  "cmd_category": "Kubernetes Development",
  "cmd_dimension": "Kubernetes Development",
  "cmd_install": "Download from https://www.telepresence.io/docs/latest/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-dev.yaml"
}
---

# telepresence intercept

> Intercept traffic to service and redirect to local process

## 安装

```bash
Download from https://www.telepresence.io/docs/latest/install/
```

## 用法

```
telepresence intercept [deployment-name] --port [local-port]:[remote-port] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--port` | Port mapping local:remote |
| `--namespace` | Service namespace |

## 示例

### 示例 1: Intercept service traffic to local port 8080

```bash
telepresence intercept myservice --port 8080:80
```

### 示例 2: Intercept production service to local dev

```bash
telepresence intercept api --port 3000:8080 --namespace production
```

### 示例 3: Stop intercepting service

```bash
telepresence leave api
```

## 风险提示

> ⚠️ **CRITICAL**: Redirects production traffic to local machine

## 所属维度

[[K8s开发调试-MOC|Kubernetes Development]]
