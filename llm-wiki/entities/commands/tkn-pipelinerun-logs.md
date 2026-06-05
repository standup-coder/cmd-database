---
cmd_name: tkn pipelinerun logs
cmd_category: "容器编排/K8s持续集成"
cmd_dimension: CD
cmd_install: Download from https://tekton.dev/docs/cli/
cmd_platforms:
- linux
- darwin
- windows
summary: "View Tekton pipeline run logs"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-cicd.yaml
---


# tkn pipelinerun logs

> View Tekton pipeline run logs

## 安装

```bash
Download from https://tekton.dev/docs/cli/
```

## 用法

```
tkn pipelinerun logs [pipelinerun-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Follow logs in real-time |
| `-n` | Namespace |

## 示例

### 示例 1: View pipeline run logs

```bash
tkn pipelinerun logs build-run-123
```

### 示例 2: Follow pipeline run logs

```bash
tkn pipelinerun logs build-run-123 -f
```

### 示例 3: Follow latest pipeline run in cicd namespace

```bash
tkn pipelinerun logs -n cicd -f
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; views logs only

## 所属维度

[[K8s持续集成-MOC|Kubernetes CI/CD]]
