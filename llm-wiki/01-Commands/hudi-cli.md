---
{
  "cmd_name": "hudi-cli",
  "cmd_category": "大数据/数据湖",
  "cmd_dimension": "数据湖",
  "cmd_install": "随 Apache Hudi 安装",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "spark-submit",
    "hadoop"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/data-lake.yaml"
}
---

# hudi-cli

> Apache Hudi 表管理命令行工具

## 安装

```bash
随 Apache Hudi 安装
```

## 用法

```
hudi-cli [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `connect` | 连接到 Hudi 表路径 |
| `commits show` | 查看提交历史 |

## 示例

### 示例 1: 启动 Hudi CLI

```bash
hudi-cli --hudi-conf-dir /etc/hudi
```

### 示例 2: 连接表并查看提交历史

```bash
connect --path /path/to/hudi_table
commits show

```

## 关联命令

- [[spark-submit]]
- [[hadoop]]

## 风险提示

> ⚠️ **HIGH**: rollback、clean 等操作会直接修改表状态，生产环境需谨慎

## 所属维度

[[数据湖-MOC|大数据/数据湖]]
