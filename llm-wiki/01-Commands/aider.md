---
{
  "cmd_name": "aider",
  "cmd_category": "AI基础设施/AI编程",
  "cmd_dimension": "AI编程",
  "cmd_install": "pip install aider-chat",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "openhands",
    "swe-agent"
  ],
  "cmd_tags": [
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-coding.yaml"
}
---

# aider

> Aider终端AI编程助手，多文件编辑、Git集成、支持GPT-4/Claude，自动提交更改

## 安装

```bash
pip install aider-chat
```

## 用法

```
aider [OPTIONS] [FILES]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` | 模型名称 |
| `--edit-format` | 编辑格式 (diff, whole, udiff) |
| `--commit` | 自动提交更改 |
| `--test-cmd` | 测试命令 |

## 示例

### 示例 1: GPT-4模式，自动Git提交

```bash
aider --model gpt-4 --commit
```

### 示例 2: 指定文件进行AI编辑

```bash
aider src/main.py src/utils.py
```

### 示例 3: 带测试反馈的Sonnet编程

```bash
aider --test-cmd 'pytest' --model claude-3-5-sonnet
```

## 关联命令

- [[openhands]]
- [[swe-agent]]

## 风险提示

> ⚠️ **HIGH**: 自动修改代码需审查，防止破坏代码库

## 参考链接

- [https://github.com/paul-gauthier/aider](https://github.com/paul-gauthier/aider)

## 所属维度

[[AI编程-MOC|AI基础设施/AI编程]]
