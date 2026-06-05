---
cmd_name: tkn pipeline start
cmd_category: "容器编排/K8s持续集成"
cmd_dimension: CD
cmd_install: Download from https://tekton.dev/docs/cli/
cmd_platforms:
- linux
- darwin
- windows
summary: "Start Tekton pipeline execution"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/container/k8s-cicd.yaml
---


# tkn pipeline start

> Start Tekton pipeline execution

## 安装

```bash
Download from https://tekton.dev/docs/cli/
```

## 用法

```
tkn pipeline start [pipeline-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Pipeline namespace |
| `-p` | Set pipeline parameter |
| `--showlog` | Show logs after starting |

## 示例

### 示例 1: Start pipeline execution

```bash
tkn pipeline start build-pipeline
```

### 示例 2: Start with parameter

```bash
tkn pipeline start build-pipeline -p repo-url=https://github.com/example/repo
```

### 示例 3: Start and follow logs

```bash
tkn pipeline start build-pipeline --showlog
```

## 风险提示

> ⚠️ **HIGH**: Executes pipeline which may build and deploy applications

## 所属维度

[[K8s持续集成-MOC|Kubernetes CI/CD]]
