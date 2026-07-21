---
{
  "cmd_name": "keptn",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://keptn.sh/docs/install/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "argocd",
    "flagger"
  ],
  "cmd_tags": [
    "application",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# keptn

> Keptn 云原生应用生命周期编排

## 安装

```bash
参考 https://keptn.sh/docs/install/
```

## 用法

```
keptn [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `install` |  |
| `create` | project |
| `trigger` | delivery |
| `get` | event |

## 示例

### 示例 1: 安装 Keptn

```bash
keptn install
```

### 示例 2: 触发交付

```bash
keptn trigger delivery --project=myproj --service=mysvc --image=myimage:v2
```

## 关联命令

- [[flagger]]

## 风险提示

> ⚠️ **MEDIUM**: Keptn 编排会影响部署和 SLO 评估，请确认配置

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
