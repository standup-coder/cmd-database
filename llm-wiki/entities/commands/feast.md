---
cmd_name: feast
cmd_category: AI基础设施/数据与标注
cmd_dimension: 数据与标注
cmd_install: pip install feast
cmd_platforms:
- linux
- darwin
- windows
summary: "Feast开源特征存储平台，统一管理ML特征的定义、存储和服务"
cmd_level: intermediate
cmd_related:
- dvc
- mlflow
cmd_tags:
- data
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/data-labeling.yaml
---


# feast

> Feast开源特征存储平台，统一管理ML特征的定义、存储和服务

## 安装

```bash
pip install feast
```

## 用法

```
feast [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化特征仓库 |
| `apply` | 注册特征定义 |
| `materialize` | 物化特征到在线存储 |
| `serve` | 启动特征服务 |

## 示例

### 示例 1: 初始化特征仓库

```bash
feast init my_feature_repo
```

### 示例 2: 注册特征定义到元数据存储

```bash
feast apply
```

### 示例 3: 物化指定时间范围特征

```bash
feast materialize 2024-01-01 2024-06-01
```

## 关联命令

- [[dvc]]
- [[mlflow]]

## 风险提示

> ⚠️ **MEDIUM**: 特征定义变更影响线上推理

## 参考链接

- [https://feast.dev/](https://feast.dev/)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
