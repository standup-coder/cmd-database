---
cmd_name: modal
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install modal
cmd_platforms:
- linux
- darwin
- windows
summary: "Modal Serverless云平台，按需弹性运行AI训练与推理任务"
cmd_level: intermediate
cmd_related:
- sky-pilot
cmd_tags:
- training
- inference
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# modal

> Modal Serverless云平台，按需弹性运行AI训练与推理任务

## 安装

```bash
pip install modal
```

## 用法

```
modal [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行Modal应用 |
| `serve` | 部署为服务 |
| `deploy` | 部署应用 |

## 示例

### 示例 1: 在Modal云端运行训练任务

```bash
modal run train.py
```

### 示例 2: 部署推理服务

```bash
modal serve inference.py
```

## 关联命令

- [[sky-pilot]]

## 风险提示

> ⚠️ **MEDIUM**: 云端计费，注意成本控制

## 参考链接

- [https://modal.com/](https://modal.com/)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
