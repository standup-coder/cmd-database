---
{
  "cmd_name": "hbase hbck",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 Apache HBase 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "hbase shell",
    "hdfs"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# hbase hbck

> HBase 一致性检查与修复

## 安装

```bash
随 Apache HBase 安装
```

## 用法

```
hbase hbck [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-details` | 详细信息 |
| `-fix` | 修复 |
| `-repair` | 修复所有 |

## 示例

### 示例 1: 检查 HBase 一致性

```bash
hbase hbck
```

### 示例 2: 修复不一致

```bash
hbase hbck -fix
```

## 关联命令

- [[hbase-shell]]
- [[hdfs]]

## 风险提示

> ⚠️ **HIGH**: -fix/-repair 会修改 HBase 元数据，请在备份后执行

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
