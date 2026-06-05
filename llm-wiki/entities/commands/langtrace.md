---
cmd_name: langtrace
cmd_category: AI基础设施/监控与评估
cmd_dimension: 监控与评估
cmd_install: pip install langtrace-python-sdk
cmd_platforms:
- linux
- darwin
- windows
summary: "Langtrace开源LLM应用追踪，兼容OpenTelemetry，支持多框架"
cmd_level: intermediate
cmd_related:
- langsmith
- phoenix
cmd_tags:
- monitoring
- application
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/monitoring.yaml
---


# langtrace

> Langtrace开源LLM应用追踪，兼容OpenTelemetry，支持多框架

## 安装

```bash
pip install langtrace-python-sdk
```

## 用法

```
python app.py (使用langtrace库)
```

## 参数

| Flag | Description |
|------|-------------|
| `langtrace.init` | 初始化追踪 |
| `with_langtrace_root_span` | 装饰器追踪根跨度 |

## 示例

### 示例 1: 初始化Langtrace追踪

```bash
python -c "import langtrace; langtrace.init(api_key='xxx')"
```

### 示例 2: 追踪LLM、向量库和框架调用

```bash
python app.py --trace_llm --trace_vectorstore --trace_framework
```

## 关联命令

- [[langsmith]]
- [[phoenix]]

## 风险提示

> ⚠️ **LOW**: 追踪数据上传注意隐私

## 参考链接

- [https://langtrace.ai/](https://langtrace.ai/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
