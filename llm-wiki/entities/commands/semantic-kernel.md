---
cmd_name: semantic-kernel
cmd_category: AI基础设施/Agent工程
cmd_dimension: Agent工程
cmd_install: pip install semantic-kernel
cmd_platforms:
- linux
- darwin
- windows
summary: "Microsoft Semantic Kernel SDK，连接LLM、记忆、规划器和插件"
cmd_level: intermediate
cmd_related:
- langchain
- autogen
cmd_tags:
- agent
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/agent-engineering.yaml
---


# semantic-kernel

> Microsoft Semantic Kernel SDK，连接LLM、记忆、规划器和插件

## 安装

```bash
pip install semantic-kernel
```

## 用法

```
python app.py (使用semantic_kernel库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Kernel` | 核心编排器 |
| `plugins` | 注册插件 |
| `planners` | 任务规划器 |

## 示例

### 示例 1: 初始化Semantic Kernel

```bash
python -c "import semantic_kernel as sk; kernel = sk.Kernel(); kernel.add_service(sk.OpenAIChatCompletion())"
```

### 示例 2: Handlebars规划器多插件协作

```bash
python planner.py --planner HandlebarsPlanner --plugins search,math
```

## 关联命令

- [[langchain]]
- [[autogen]]

## 风险提示

> ⚠️ **MEDIUM**: 插件调用需注意权限

## 参考链接

- [https://github.com/microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
