---
cmd_name: great-expectations
cmd_category: AI基础设施/数据与标注
cmd_dimension: 数据与标注
cmd_install: pip install great_expectations
cmd_platforms:
- linux
- darwin
- windows
summary: "Great Expectations数据质量验证框架，定义和监控数据期望"
cmd_level: intermediate
cmd_related:
- dvc
- cleanlab
cmd_tags:
- monitoring
- data
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/data-labeling.yaml
---


# great-expectations

> Great Expectations数据质量验证框架，定义和监控数据期望

## 安装

```bash
pip install great_expectations
```

## 用法

```
great_expectations [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化项目 |
| `checkpoint run` | 运行检查点 |
| `suite new` | 创建期望套件 |

## 示例

### 示例 1: 初始化GX项目

```bash
great_expectations init
```

### 示例 2: 运行数据质量检查

```bash
great_expectations checkpoint run my_checkpoint
```

## 关联命令

- [[dvc]]
- [[cleanlab]]

## 风险提示

> ⚠️ **LOW**: 验证操作不改数据

## 参考链接

- [https://greatexpectations.io/](https://greatexpectations.io/)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
