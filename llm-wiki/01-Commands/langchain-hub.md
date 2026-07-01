---
{
  "cmd_name": "langchain-hub",
  "cmd_category": "AI基础设施/AI应用",
  "cmd_dimension": "AI应用",
  "cmd_install": "pip install langchainhub",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "langchain",
    "promptflow"
  ],
  "cmd_tags": [
    "application",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-applications.yaml"
}
---

# langchain-hub

> LangChain Hub Prompt模板共享平台，复用社区验证的Prompt模板和链式组件

## 安装

```bash
pip install langchainhub
```

## 用法

```
python app.py (使用langchainhub库)
```

## 参数

| Flag | Description |
|------|-------------|
| `hub.pull()` | 拉取模板 |
| `hub.push()` | 推送模板 |

## 示例

### 示例 1: 拉取OpenAI Functions Agent模板

```bash
python -c "from langchain import hub; prompt = hub.pull('hwchase17/openai-functions-agent')"
```

### 示例 2: 推送自定义Prompt

```bash
python -c "from langchain import hub; hub.push('my-repo/my-prompt', prompt)"
```

## 关联命令

- [[langchain]]
- [[promptflow]]

## 风险提示

> ⚠️ **LOW**: 模板共享安全

## 参考链接

- [https://github.com/hwchase17/langchain-hub](https://github.com/hwchase17/langchain-hub)

## 所属维度

[[AI应用-MOC|AI基础设施/AI应用]]
