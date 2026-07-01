---
{
  "cmd_name": "yarn",
  "cmd_category": "大数据/Hadoop生态",
  "cmd_dimension": "Hadoop生态",
  "cmd_install": "随 Hadoop 发行版安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "hadoop",
    "hdfs"
  ],
  "cmd_tags": [
    "monitoring",
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/hadoop.yaml"
}
---

# yarn

> Hadoop 资源调度与作业监控命令

## 安装

```bash
随 Hadoop 发行版安装
```

## 用法

```
yarn [OPTIONS] SUBCOMMAND [SUBCOMMAND OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `application -list` | 列出运行中的应用 |
| `application -kill` | 终止指定应用 |

## 示例

### 示例 1: 查看 YARN 上运行的应用

```bash
yarn application -list
```

### 示例 2: 终止指定的 YARN 应用

```bash
yarn application -kill application_12345_0001
```

## 关联命令

- [[hadoop]]
- [[hdfs]]

## 风险提示

> ⚠️ **MEDIUM**: 终止生产环境应用可能影响业务，请先确认应用状态

## 所属维度

[[Hadoop生态-MOC|大数据/Hadoop生态]]
