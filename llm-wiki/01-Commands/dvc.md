---
{
  "cmd_name": "dvc",
  "cmd_category": "AI基础设施/数据与标注",
  "cmd_dimension": "数据与标注",
  "cmd_install": "pip install dvc",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "git-lfs",
    "cleanlab"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/data-labeling.yaml"
}
---

# dvc

> DVC数据版本控制，Git-like管理数据集和模型，支持S3/GS/Azure存储

## 安装

```bash
pip install dvc
```

## 用法

```
dvc [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化DVC仓库 |
| `add` | 追踪数据文件 |
| `push` | 推送到远程存储 |
| `pull` | 从远程拉取数据 |
| `remote add` | 添加远程存储 |

## 示例

### 示例 1: 初始化DVC

```bash
dvc init
```

### 示例 2: 追踪训练数据

```bash
dvc add data/train.csv
```

### 示例 3: 上传数据到远程存储

```bash
dvc push
```

### 示例 4: 配置S3远程存储

```bash
dvc remote add -d myremote s3://mybucket/dvcstore
```

## 关联命令

- [[git-lfs]]
- [[cleanlab]]

## 风险提示

> ⚠️ **MEDIUM**: 误操作可能导致数据版本混乱

## 参考链接

- [https://dvc.org/](https://dvc.org/)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
