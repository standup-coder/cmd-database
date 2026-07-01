---
{
  "cmd_name": "llm-guard",
  "cmd_category": "AI基础设施/AI安全",
  "cmd_dimension": "AI安全",
  "cmd_install": "pip install llm-guard",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "garak",
    "safety-eval"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-safety.yaml"
}
---

# llm-guard

> LLM Guard输入输出安全过滤器，检测PII泄露、毒性、越狱、提示注入

## 安装

```bash
pip install llm-guard
```

## 用法

```
python app.py (使用llm_guard库)
```

```
docker run [OPTIONS] laiyio/llm-guard-api
```

## 参数

| Flag | Description |
|------|-------------|
| `input_scanners` | 输入扫描器列表 |
| `output_scanners` | 输出扫描器列表 |

## 示例

### 示例 1: 启动LLM Guard API服务

```bash
docker run -p 8000:8000 laiyio/llm-guard-api:latest
```

### 示例 2: Python调用输入过滤

```bash
python -c "from llm_guard import scan_prompt; result = scan_prompt('prompt', scanners=['Anonymize', 'PromptInjection'])"
```

## 关联命令

- [[garak]]
- [[safety-eval]]

## 风险提示

> ⚠️ **LOW**: 过滤器可能误判合法输入，需调优阈值

## 参考链接

- [https://github.com/laiyer-ai/llm-guard](https://github.com/laiyer-ai/llm-guard)

## 所属维度

[[AI安全-MOC|AI基础设施/AI安全]]
