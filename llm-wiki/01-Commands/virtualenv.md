---
{
  "cmd_name": "virtualenv",
  "cmd_category": "编程语言/Python工具链",
  "cmd_dimension": "Python工具链",
  "cmd_install": "pip install virtualenv",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "pip",
    "python"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/lang/python.yaml"
}
---

# virtualenv

> 创建Python虚拟环境

## 安装

```bash
pip install virtualenv
```

## 用法

```
virtualenv [options] <env_name>
```

## 示例

### 示例 1: 创建虚拟环境

```bash
virtualenv venv
```

### 示例 2: 激活虚拟环境(Linux/Mac)

```bash
source venv/bin/activate
```

### 示例 3: 激活虚拟环境(Windows)

```bash
venv\Scripts\activate
```

## 关联命令

- [[pip]]
- [[python]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 所属维度

[[Python工具链-MOC|编程语言/Python工具链]]
