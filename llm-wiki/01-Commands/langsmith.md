---
{
  "cmd_name": "langsmith",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "pip install langsmith",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langfuse",
    "promptlayer"
  ],
  "cmd_tags": [
    "monitoring",
    "application",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/monitoring.yaml"
}
---

# langsmith

> LangSmith LLM应用全链路追踪与评估平台，记录输入输出、token消耗、延迟

## 安装

```bash
pip install langsmith
```

## 用法

```
python app.py (使用langsmith库)
```

## 参数

| Flag | Description |
|------|-------------|
| `@traceable` | 装饰器自动追踪函数调用 |
| `Client` | 创建LangSmith客户端 |
| `evaluate` | 运行评估数据集 |

## 示例

### 示例 1: 配置API Key并运行追踪

```bash
export LANGCHAIN_API_KEY=ls-xxx && python app.py
```

### 示例 2: 在数据集上运行QA评估

```bash
python evaluate.py --dataset my-dataset --evaluator qa
```

## 关联命令

- [[langfuse]]
- [[promptlayer]]

## 风险提示

> ⚠️ **LOW**: 追踪数据上传云端，注意隐私

## 参考链接

- [https://smith.langchain.com/](https://smith.langchain.com/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
