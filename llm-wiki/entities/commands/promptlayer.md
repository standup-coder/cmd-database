---
cmd_name: promptlayer
cmd_category: AI基础设施/监控与评估
cmd_dimension: 监控与评估
cmd_install: pip install promptlayer
cmd_platforms:
- linux
- darwin
- windows
summary: "PromptLayer提示词版本管理与追踪，记录提示词迭代历史和效果对比"
cmd_level: intermediate
cmd_related:
- langsmith
- langfuse
cmd_tags:
- monitoring
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/monitoring.yaml
---


# promptlayer

> PromptLayer提示词版本管理与追踪，记录提示词迭代历史和效果对比

## 安装

```bash
pip install promptlayer
```

## 用法

```
python app.py (使用promptlayer库)
```

## 参数

| Flag | Description |
|------|-------------|
| `promptlayer.track.prompt` | 追踪提示词模板 |
| `promptlayer.track.score` | 记录输出质量评分 |
| `promptlayer.templates.get` | 获取已发布的提示词模板 |

## 示例

### 示例 1: 发布提示词模板

```bash
python -c "import promptlayer; promptlayer.api_key = 'pl-xxx'; promptlayer.templates.publish('greeting', template)"
```

### 示例 2: 追踪所有提示词并收集人工评分

```bash
python track_prompts.py --track_all --score_function human_eval
```

## 关联命令

- [[langsmith]]
- [[langfuse]]

## 风险提示

> ⚠️ **LOW**: 提示词追踪无技术风险

## 参考链接

- [https://www.promptlayer.com/](https://www.promptlayer.com/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
