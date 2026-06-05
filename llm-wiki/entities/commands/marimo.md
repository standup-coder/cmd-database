---
cmd_name: marimo
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: pip install marimo
cmd_platforms:
- linux
- darwin
- windows
summary: "Marimo响应式Python Notebook，支持交互式数据探索和模型实验"
cmd_level: intermediate
cmd_related:
- streamlit
- gradio
cmd_tags:
- inference
- data
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# marimo

> Marimo响应式Python Notebook，支持交互式数据探索和模型实验

## 安装

```bash
pip install marimo
```

## 用法

```
marimo [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `edit` | 编辑Notebook |
| `run` | 运行Notebook |
| `tutorial` | 启动交互式教程 |

## 示例

### 示例 1: 编辑Notebook文件

```bash
marimo edit notebook.py
```

### 示例 2: 以应用模式运行Notebook

```bash
marimo run notebook.py --port 8080
```

## 关联命令

- [[streamlit]]
- [[gradio]]

## 风险提示

> ⚠️ **LOW**: Notebook工具，风险较低

## 参考链接

- [https://marimo.io/](https://marimo.io/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
