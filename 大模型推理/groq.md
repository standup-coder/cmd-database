---
{
  "cmd_name": "groq",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install groq",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "together",
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

# groq

> Groq极速推理API，基于LPU芯片实现业界最快token生成速度

## 安装

```bash
pip install groq
```

## 用法

```
python app.py (使用groq库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Groq(api_key=...)` | 初始化客户端 |
| `chat.completions.create` | 创建聊天补全 |

## 示例

### 示例 1: 使用Groq极速推理

```bash
python -c "from groq import Groq; g = Groq(); r = g.chat.completions.create(model='llama-3.1-70b', messages=[{'role':'user','content':'Explain quantum computing'}])"
```

### 示例 2: 限制最大输出 token 数

```bash
python -c "from groq import Groq; g=Groq(); r=g.chat.completions.create(model='llama-3.1-8b', messages=[{'role':'user','content':'Hi'}], max_tokens=1024)"
```

## 关联命令

- [[together]]
- [[fireworks]]

## 风险提示

> ⚠️ **LOW**: API调用计费

## 参考链接

- [https://groq.com/](https://groq.com/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
