---
{
  "cmd_name": "arena",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mt-bench",
    "alpaca-eval"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# arena

> LMSYS Chatbot Arena众测平台，人类盲测对比不同LLM的对话质量

## 用法

```
访问 chat.lmsys.org 参与评测
```

## 参数

| Flag | Description |
|------|-------------|
| `battle` | 匿名对战模式 |
| `ranking` | 查看ELO排名 |

## 示例

### 示例 1: 获取Arena排行榜数据

```bash
curl https://chat.lmsys.org/api/leaderboard
```

### 示例 2: 以 JSON 格式查看排行榜

```bash
curl https://chat.lmsys.org/api/leaderboard | jq .
```

## 关联命令

- [[mt-bench]]
- [[alpaca-eval]]

## 风险提示

> ⚠️ **LOW**: 众测平台，客观评测

## 参考链接

- [https://chat.lmsys.org/](https://chat.lmsys.org/)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
