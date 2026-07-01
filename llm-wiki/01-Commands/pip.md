---
{
  "cmd_name": "pip",
  "cmd_category": "编程语言/Python工具链",
  "cmd_dimension": "Python工具链",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "virtualenv",
    "python"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/lang/python.yaml"
}
---

# pip

> Python包管理器

## 用法

```
pip <command> [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `install` | 安装包 |
| `uninstall` | 卸载包 |
| `list` | 列出已安装的包 |
| `freeze` | 输出已安装包列表 |

## 示例

### 示例 1: 安装requests库

```bash
pip install requests
```

### 示例 2: 从文件安装依赖

```bash
pip install -r requirements.txt
```

### 示例 3: 导出依赖列表

```bash
pip freeze > requirements.txt
```

## 关联命令

- [[virtualenv]]
- [[python]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 所属维度

[[Python工具链-MOC|编程语言/Python工具链]]
