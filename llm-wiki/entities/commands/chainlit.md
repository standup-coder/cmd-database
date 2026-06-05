---
cmd_name: chainlit
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: pip install chainlit
cmd_platforms:
- linux
- darwin
- windows
summary: "Chainlit对话式AI应用框架，专为LLM应用设计的Python框架"
cmd_level: intermediate
cmd_related:
- gradio
- streamlit
cmd_tags:
- inference
- application
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# chainlit

> Chainlit对话式AI应用框架，专为LLM应用设计的Python框架

## 安装

```bash
pip install chainlit
```

## 用法

```
chainlit [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行Chainlit应用 |
| `init` | 初始化新项目 |
| `--host` | 绑定主机 |
| `--port` | 绑定端口 |

## 示例

### 示例 1: 初始化Chainlit项目

```bash
chainlit init
```

### 示例 2: 热重载模式运行

```bash
chainlit run app.py -w
```

### 示例 3: 绑定所有网卡，端口8000

```bash
chainlit run app.py --host 0.0.0.0 --port 8000
```

## 关联命令

- [[gradio]]
- [[streamlit]]

## 风险提示

> ⚠️ **LOW**: 开发框架，风险较低

## 参考链接

- [https://github.com/Chainlit/chainlit](https://github.com/Chainlit/chainlit)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
