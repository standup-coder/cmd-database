---
{
  "cmd_name": "gradio",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install gradio",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "streamlit",
    "chainlit"
  ],
  "cmd_tags": [
    "inference",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# gradio

> Gradio快速构建ML模型交互式Demo，自动生成可分享的Web界面

## 安装

```bash
pip install gradio
```

## 用法

```
python app.py (使用gradio库)
```

## 参数

| Flag | Description |
|------|-------------|
| `gr.Interface` | 创建交互界面 |
| `gr.ChatInterface` | 创建聊天界面 |
| `gr.Blocks` | 构建复杂多页面应用 |

## 示例

### 示例 1: 启动Gradio应用并生成公网链接

```bash
python app.py --share
```

### 示例 2: 单行代码创建文本生成Demo

```bash
python -c "import gradio as gr; gr.Interface(fn=predict, inputs='text', outputs='text').launch()"
```

## 关联命令

- [[streamlit]]
- [[chainlit]]

## 风险提示

> ⚠️ **MEDIUM**: --share生成公网链接，注意数据安全

## 参考链接

- [https://www.gradio.app/](https://www.gradio.app/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
