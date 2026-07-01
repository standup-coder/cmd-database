---
{
  "cmd_name": "pylint",
  "cmd_category": "编程语言/Python工具链",
  "cmd_dimension": "Python工具链",
  "cmd_install": "pip install pylint",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "pytest",
    "python"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/python.yaml"
}
---

# pylint

> Python代码检查工具

## 安装

```bash
pip install pylint
```

## 用法

```
pylint [options] <modules>
```

## 示例

### 示例 1: 检查代码质量

```bash
pylint mymodule.py
```

### 示例 2: 禁用指定警告后检查

```bash
pylint --disable=C0103 mymodule.py
```

## 关联命令

- [[pytest]]
- [[python]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 所属维度

[[Python工具链-MOC|编程语言/Python工具链]]
