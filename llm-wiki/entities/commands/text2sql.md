---
cmd_name: text2sql
cmd_category: AI基础设施/AI应用
cmd_dimension: AI应用
cmd_install: pip install text2sql
cmd_platforms:
- linux
- darwin
- windows
summary: "Text2SQL自然语言转SQL工具，基于LLM将业务问题转换为可执行的数据库查询"
cmd_level: advanced
cmd_related:
- langchain
- dify
cmd_tags:
- application
- data
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/ai/ai-applications.yaml
---


# text2sql

> Text2SQL自然语言转SQL工具，基于LLM将业务问题转换为可执行的数据库查询

## 安装

```bash
pip install text2sql
```

## 用法

```
python app.py (使用text2sql库)
```

## 参数

| Flag | Description |
|------|-------------|
| `--schema` | 数据库Schema文件 |
| `--model` | LLM模型 |
| `--dialect` | SQL方言 (mysql, postgresql, sqlite) |

## 示例

### 示例 1: 自然语言生成SQL

```bash
python -c "from text2sql import Text2SQL; t = Text2SQL(schema='schema.json', model='gpt-4'); sql = t.convert('Show me top 10 customers by revenue')"
```

### 示例 2: 命令行生成MySQL查询

```bash
python text2sql.py --schema schema.sql --dialect mysql --question 'What is the average order value?'
```

## 关联命令

- [[langchain]]
- [[dify]]

## 风险提示

> ⚠️ **HIGH**: 生成的SQL可能包含DELETE/DROP，需审查和沙箱执行

## 参考链接

- [https://github.com/eosphoros-ai/DB-GPT](https://github.com/eosphoros-ai/DB-GPT)

## 所属维度

[[AI应用-MOC|AI基础设施/AI应用]]
