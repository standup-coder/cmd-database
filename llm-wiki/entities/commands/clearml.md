---
cmd_name: clearml
cmd_category: AI基础设施/监控与评估
cmd_dimension: 监控与评估
cmd_install: pip install clearml
cmd_platforms:
- linux
- darwin
- windows
summary: "ClearML端到端MLOps平台，涵盖实验跟踪、数据管理、Pipeline编排、模型服务"
cmd_level: intermediate
cmd_related:
- wandb
- neptune
cmd_tags:
- monitoring
- data
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/monitoring.yaml
---


# clearml

> ClearML端到端MLOps平台，涵盖实验跟踪、数据管理、Pipeline编排、模型服务

## 安装

```bash
pip install clearml
```

## 用法

```
clearml-init
```

```
clearml-agent [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `clearml-init` | 配置服务器连接 |
| `clearml-agent daemon` | 启动代理守护进程 |
| `clearml-agent execute` | 执行实验任务 |

## 示例

### 示例 1: 初始化ClearML配置

```bash
clearml-init
```

### 示例 2: 在GPU0上启动代理监听默认队列

```bash
clearml-agent daemon --gpus 0 --queue default
```

### 示例 3: 执行指定实验任务

```bash
clearml-agent execute --id <task_id>
```

## 关联命令

- [[wandb]]
- [[neptune]]

## 风险提示

> ⚠️ **MEDIUM**: 代理执行远程代码，需信任任务来源

## 参考链接

- [https://clear.ml/](https://clear.ml/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
