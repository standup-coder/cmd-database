---
cmd_name: aim
cmd_category: AI基础设施/监控与评估
cmd_dimension: 监控与评估
cmd_install: pip install aim
cmd_platforms:
- linux
- darwin
- windows
summary: "Aim开源超大规模实验跟踪工具，支持百万级实验，高性能查询"
cmd_level: advanced
cmd_related:
- wandb
- tensorboard
cmd_tags:
- monitoring
- advanced
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/monitoring.yaml
---


# aim

> Aim开源超大规模实验跟踪工具，支持百万级实验，高性能查询

## 安装

```bash
pip install aim
```

## 用法

```
aim [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `up` | 启动Aim UI |
| `init` | 初始化仓库 |
| `reindex` | 重新索引数据 |

## 示例

### 示例 1: 初始化Aim仓库

```bash
aim init
```

### 示例 2: 启动Aim UI服务

```bash
aim up --host 0.0.0.0 --port 43800
```

### 示例 3: 训练并记录到Aim

```bash
python train.py --use_aim --experiment bert-finetune
```

## 关联命令

- [[wandb]]
- [[tensorboard]]

## 风险提示

> ⚠️ **LOW**: 本地部署，数据安全

## 参考链接

- [https://aimstack.io/](https://aimstack.io/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
