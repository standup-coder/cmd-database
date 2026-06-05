---
cmd_name: fireworks
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: pip install fireworks-ai
cmd_platforms:
- linux
- darwin
- windows
summary: "Fireworks AI快速推理API，针对开源模型优化的高性能端点"
cmd_level: intermediate
cmd_related:
- together
- groq
cmd_tags:
- inference
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# fireworks

> Fireworks AI快速推理API，针对开源模型优化的高性能端点

## 安装

```bash
pip install fireworks-ai
```

## 用法

```
python app.py (使用fireworks库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Fireworks(api_key=...)` | 初始化客户端 |
| `completion.create` | 创建补全 |

## 示例

### 示例 1: 调用Fireworks API推理

```bash
python -c "from fireworks.client import Fireworks; fw = Fireworks(); r = fw.completion.create(model='accounts/fireworks/models/llama-v3-70b', prompt='Hello')"
```

## 关联命令

- [[together]]
- [[groq]]

## 风险提示

> ⚠️ **LOW**: API调用计费

## 参考链接

- [https://fireworks.ai/](https://fireworks.ai/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
