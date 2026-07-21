---
{
  "cmd_name": "vanna",
  "cmd_category": "AI基础设施/AI应用",
  "cmd_dimension": "AI应用",
  "cmd_install": "pip install vanna",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "text2sql",
    "langchain"
  ],
  "cmd_tags": [
    "training",
    "application",
    "rag",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-applications.yaml"
}
---

# vanna

> Vanna AI SQL生成框架，RAG增强的Text2SQL，支持训练领域Schema并持续优化

## 安装

```bash
pip install vanna
```

## 用法

```
python app.py (使用vanna库)
```

## 参数

| Flag | Description |
|------|-------------|
| `VN.train` | 训练Schema和查询样例 |
| `VN.ask` | 自然语言提问 |
| `VN.generate_sql` | 生成SQL |

## 示例

### 示例 1: 训练Schema并提问

```bash
python -c "import vanna; vn = vanna.DefaultVanna(config={'api_key': '...'}); vn.train(ddl='CREATE TABLE ...'); print(vn.ask('How many users?'))"
```

### 示例 2: 批量训练领域知识

```bash
python train_vanna.py --ddl schema.sql --questions questions.csv
```

## 关联命令

- [[text2sql]]
- [[langchain]]

## 风险提示

> ⚠️ **HIGH**: SQL生成需审查，防止数据泄露和误操作

## 参考链接

- [https://github.com/vanna-ai/vanna](https://github.com/vanna-ai/vanna)

## 所属维度

[[AI应用-MOC|AI基础设施/AI应用]]
