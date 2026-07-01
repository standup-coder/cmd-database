---
{
  "cmd_name": "pytest",
  "cmd_category": "编程语言/Python工具链",
  "cmd_dimension": "Python工具链",
  "cmd_install": "pip install pytest",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "python",
    "pylint"
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

# pytest

> Python测试框架

## 安装

```bash
pip install pytest
```

## 用法

```
pytest [options] [files]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 显示详细输出 |
| `-k <pattern>` | 运行匹配的测试 |
| `--cov` | 显示覆盖率 |

## 示例

### 示例 1: 运行所有测试

```bash
pytest
```

### 示例 2: 运行指定文件的测试

```bash
pytest -v test_app.py
```

## 关联命令

- [[python]]
- [[pylint]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 所属维度

[[Python工具链-MOC|编程语言/Python工具链]]
