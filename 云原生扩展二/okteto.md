---
{
  "cmd_name": "okteto",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://www.okteto.com/docs/getting-started/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "devspace",
    "telepresence"
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

# okteto

> 云端到本地的 Kubernetes 开发环境

## 安装

```bash
参考 https://www.okteto.com/docs/getting-started/
```

## 用法

```
okteto [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `up` | 启动开发环境 |
| `down` | 停止 |
| `context` |  |
| `deploy` |  |

## 示例

### 示例 1: 启动 Okteto 开发环境

```bash
okteto up
```

### 示例 2: 切换上下文

```bash
okteto context use https://okteto.example.com
```

## 关联命令

- [[devspace]]
- [[telepresence]]

## 风险提示

> ⚠️ **MEDIUM**: okteto up 会同步本地代码到集群，请确认忽略文件

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
