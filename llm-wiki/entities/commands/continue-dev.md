---
cmd_name: continue-dev
cmd_category: AI基础设施/AI编程
cmd_dimension: AI编程
cmd_install: VS Code/Cursor 插件市场安装 Continue
cmd_platforms:
- linux
- darwin
- windows
summary: "Continue.dev开源IDE AI编程助手，支持VS Code/JetBrains，本地/云端模型自由切换"
cmd_level: intermediate
cmd_related:
- aider
- codeium
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/ai-coding.yaml
---


# continue-dev

> Continue.dev开源IDE AI编程助手，支持VS Code/JetBrains，本地/云端模型自由切换

## 安装

```bash
VS Code/Cursor 插件市场安装 Continue
```

## 用法

```
VS Code命令面板 > Continue
```

## 参数

| Flag | Description |
|------|-------------|
| `config.json` | 模型配置 |
| `cmd+L` | 打开侧边栏 |
| `cmd+K` | 内联编辑 |

## 示例

### 示例 1: 配置本地Ollama模型

```bash
echo '{"models": [{"title": "Ollama", "provider": "ollama", "model": "llama3.1"}]}' > ~/.continue/config.json
```

## 关联命令

- [[aider]]
- [[codeium]]

## 风险提示

> ⚠️ **LOW**: IDE插件风险较低

## 参考链接

- [https://www.continue.dev/](https://www.continue.dev/)

## 所属维度

[[AI编程-MOC|AI基础设施/AI编程]]
