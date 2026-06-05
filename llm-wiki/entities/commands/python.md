---
cmd_name: python
cmd_category: 编程语言/Python工具链
cmd_dimension: Python工具链
cmd_install: ''
cmd_platforms:
- linux
- darwin
- windows
summary: "运行Python解释器"
cmd_level: intermediate
cmd_related:
- pip
- pytest
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/lang/python.yaml
---


# python

> 运行Python解释器

## 用法

```
python [options] [script]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c <command>` | 执行Python命令 |
| `-m <module>` | 运行模块 |
| `-V, --version` | 显示版本信息 |

## 示例

### 示例 1: 运行Python脚本

```bash
python script.py
```

### 示例 2: 启动简单HTTP服务器

```bash
python -m http.server 8000
```

### 示例 3: 执行单行命令

```bash
python -c 'print("Hello")'
```

## 关联命令

- [[pip]]
- [[pytest]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 所属维度

[[Python工具链-MOC|编程语言/Python工具链]]
