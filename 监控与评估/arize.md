---
{
  "cmd_name": "arize",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "pip install arize",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "phoenix",
    "langfuse"
  ],
  "cmd_tags": [
    "monitoring",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/monitoring.yaml"
}
---

# arize

> Arize AI ML可观测性平台，支持漂移检测、性能监控、根因分析

## 安装

```bash
pip install arize
```

## 用法

```
python monitor.py (使用arize库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Client` | Arize客户端 |
| `log` | 记录预测日志 |

## 示例

### 示例 1: 记录模型预测到Arize

```bash
python -c "from arize.api import Client; c = Client(space_key='xxx', api_key='xxx'); c.log(prediction_id='1', model_id='m', prediction_label='cat')"
```

### 示例 2: 查看日志 API 帮助

```bash
python -c "from arize.api import Client; help(Client.log)"
```

## 关联命令

- [[phoenix]]
- [[langfuse]]

## 风险提示

> ⚠️ **LOW**: 云端上传注意隐私

## 参考链接

- [https://arize.com/](https://arize.com/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
