---
{
  "cmd_name": "together",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install together",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "groq",
    "fireworks"
  ],
  "cmd_tags": [
    "inference",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# together

> Together AI API客户端，访问高性能开源模型推理API

## 安装

```bash
pip install together
```

## 用法

```
python app.py (使用together库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Together(api_key=...)` | 初始化客户端 |
| `chat.completions.create` | 创建聊天补全 |

## 示例

### 示例 1: 调用Together AI API推理

```bash
python -c "from together import Together; c = Together(); r = c.chat.completions.create(model='meta-llama/Llama-3-70b', messages=[{'role':'user','content':'Hello'}])"
```

### 示例 2: 控制生成长度和随机性

```bash
python -c "from together import Together; c=Together(); r=c.chat.completions.create(model='meta-llama/Llama-3-8b', messages=[{'role':'user','content':'Hi'}], max_tokens=128, temperature=0.7)"
```

## 关联命令

- [[groq]]
- [[fireworks]]

## 风险提示

> ⚠️ **LOW**: API调用计费，注意token消耗

## 参考链接

- [https://www.together.ai/](https://www.together.ai/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
