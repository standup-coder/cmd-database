---
cmd_name: bertviz
cmd_category: AI基础设施/模型架构
cmd_dimension: 模型架构
cmd_install: pip install bertviz
cmd_platforms:
- linux
- darwin
- windows
summary: "BertViz Transformer注意力可视化工具，交互式查看各层各头的注意力权重分布"
cmd_level: intermediate
cmd_related:
- transformers-cli
- calflops
cmd_tags:
- architecture
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/model-architecture.yaml
---


# bertviz

> BertViz Transformer注意力可视化工具，交互式查看各层各头的注意力权重分布

## 安装

```bash
pip install bertviz
```

## 用法

```
python visualize.py (使用bertviz库)
```

## 参数

| Flag | Description |
|------|-------------|
| `model_view` | 模型层级注意力视图 |
| `head_view` | 单头注意力动态视图 |
| `neuron_view` | 神经元级别视图 |

## 示例

### 示例 1: 生成注意力头可视化

```bash
python -c "from bertviz import head_view; head_view(attention, tokens)"
```

### 示例 2: 生成模型层级视图

```bash
python -c "from bertviz import model_view; model_view(attention, tokens)"
```

## 关联命令

- [[transformers-cli]]
- [[calflops]]

## 风险提示

> ⚠️ **LOW**: 可视化工具安全

## 参考链接

- [https://github.com/jessevig/bertviz](https://github.com/jessevig/bertviz)

## 所属维度

[[模型架构-MOC|AI基础设施/模型架构]]
