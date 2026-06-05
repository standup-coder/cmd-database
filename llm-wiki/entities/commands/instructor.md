---
cmd_name: instructor
cmd_category: AI基础设施/大模型推理
cmd_dimension: 大模型推理
cmd_install: pip install instructor
cmd_platforms:
- linux
- darwin
- windows
summary: "Instructor结构化输出框架，基于Pydantic让LLM返回类型安全的结构化数据"
cmd_level: intermediate
cmd_related:
- openai-function-calling
- pydantic-ai
cmd_tags:
- inference
- safety
- data
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-inference.yaml
---


# instructor

> Instructor结构化输出框架，基于Pydantic让LLM返回类型安全的结构化数据

## 安装

```bash
pip install instructor
```

## 用法

```
python app.py (使用instructor库)
```

## 参数

| Flag | Description |
|------|-------------|
| `client.chat.completions.create_with_completion` | 创建结构化输出 |
| `response_model` | Pydantic响应模型 |

## 示例

### 示例 1: 提取结构化用户信息

```bash
python -c "import instructor, openai; client = instructor.from_openai(openai.OpenAI()); user = client.chat.completions.create(model='gpt-4', response_model=User, messages=[...])"
```

### 示例 2: 批量文档结构化提取

```bash
python extract.py --schema schema.json --input documents/
```

## 关联命令

- [[openai-function-calling]]
- [[pydantic-ai]]

## 风险提示

> ⚠️ **LOW**: 结构化提取安全

## 参考链接

- [https://github.com/jxnl/instructor](https://github.com/jxnl/instructor)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]
