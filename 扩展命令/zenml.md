---
{
  "cmd_name": "zenml",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install zenml",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mlflow",
    "metaflow"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/more.yaml"
}
---

# zenml

> MLOps 管道编排工具

## 安装

```bash
pip install zenml
```

## 用法

```
zenml [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化 |
| `stack` | register |
| `pipeline` | run |
| `server` |  |

## 示例

### 示例 1: 初始化项目

```bash
zenml init
```

### 示例 2: 设置默认 stack

```bash
zenml stack set default
```

## 关联命令

- [[mlflow]]
- [[metaflow]]

## 风险提示

> ⚠️ **MEDIUM**: zenml stack 涉及云凭据，请安全存储

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
