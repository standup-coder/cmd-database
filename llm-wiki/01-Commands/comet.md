---
{
  "cmd_name": "comet",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install comet-ml",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "wandb",
    "neptune"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/more.yaml"
}
---

# comet

> Comet.ml 实验跟踪平台

## 安装

```bash
pip install comet-ml
```

## 用法

```
comet [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` |  |
| `online` |  |
| `offline` |  |
| `upload` |  |

## 示例

### 示例 1: 初始化

```bash
comet init
```

### 示例 2: 上传离线实验

```bash
comet upload offline.zip
```

## 关联命令

- [[wandb]]
- [[neptune]]

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
