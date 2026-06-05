---
cmd_name: garak
cmd_category: AI基础设施/AI安全
cmd_dimension: AI安全
cmd_install: pip install garak
cmd_platforms:
- linux
- darwin
- windows
summary: "Garak LLM漏洞扫描框架，探测越狱、提示注入、数据泄露、幻觉等安全风险"
cmd_level: advanced
cmd_related:
- red-teaming
- llm-guard
cmd_tags:
- safety
- data
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/ai/ai-safety.yaml
---


# garak

> Garak LLM漏洞扫描框架，探测越狱、提示注入、数据泄露、幻觉等安全风险

## 安装

```bash
pip install garak
```

## 用法

```
garak [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model_type` | 模型类型 (openai, huggingface, replicate) |
| `--model_name` | 模型名称 |
| `--probes` | 探测插件列表 |
| `--generations` | 每探测生成次数 |

## 示例

### 示例 1: 全面扫描GPT-4安全风险

```bash
garak --model_type openai --model_name gpt-4 --probes all
```

### 示例 2: 针对性检测已知攻击向量

```bash
garak --model_type huggingface --model_name meta-llama/Llama-2-7b-chat-hf --probes encoding,dan,knownbadsignatures
```

## 关联命令

- [[red-teaming]]
- [[llm-guard]]

## 风险提示

> ⚠️ **HIGH**: 安全测试可能触发内容过滤器，需在隔离环境执行

## 参考链接

- [https://github.com/leondz/garak](https://github.com/leondz/garak)

## 所属维度

[[AI安全-MOC|AI基础设施/AI安全]]
