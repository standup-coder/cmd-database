---
cmd_name: sky-pilot
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: pip install skypilot
cmd_platforms:
- linux
- darwin
- windows
summary: "SkyPilot云端ML任务调度器，一键在AWS/GCP/Azure/Lambda运行训练/推理"
cmd_level: intermediate
cmd_related:
- modal
- vllm
cmd_tags:
- training
- inference
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# sky-pilot

> SkyPilot云端ML任务调度器，一键在AWS/GCP/Azure/Lambda运行训练/推理

## 安装

```bash
pip install skypilot
```

## 用法

```
sky [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `launch` | 启动任务 |
| `serve up` | 部署服务 |
| `show-gpus` | 查看可用GPU |
| `spot` | 使用Spot实例降低成本 |

## 示例

### 示例 1: 在云端启动训练集群

```bash
sky launch -c mycluster task.yaml
```

### 示例 2: 部署推理服务

```bash
sky serve up service.yaml
```

### 示例 3: 查看AWS可用GPU类型和价格

```bash
sky show-gpus --cloud aws
```

## 关联命令

- [[modal]]
- [[vllm]]

## 风险提示

> ⚠️ **MEDIUM**: 云端计费，注意成本控制

## 参考链接

- [https://skypilot.readthedocs.io/](https://skypilot.readthedocs.io/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
