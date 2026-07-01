---
{
  "cmd_name": "streamlit",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install streamlit",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gradio",
    "chainlit"
  ],
  "cmd_tags": [
    "inference",
    "application",
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# streamlit

> Streamlit数据应用与模型展示框架，纯Python构建数据科学应用

## 安装

```bash
pip install streamlit
```

## 用法

```
streamlit [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行Streamlit应用 |
| `--server.port` | 服务端口号 |
| `--server.address` | 绑定地址 |

## 示例

### 示例 1: 启动Streamlit应用

```bash
streamlit run app.py
```

### 示例 2: 指定端口启动

```bash
streamlit run app.py --server.port 8501
```

### 示例 3: 使用深色主题启动

```bash
streamlit run app.py --theme.base dark
```

## 关联命令

- [[gradio]]
- [[chainlit]]

## 风险提示

> ⚠️ **LOW**: 本地开发工具，风险较低

## 参考链接

- [https://streamlit.io/](https://streamlit.io/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
