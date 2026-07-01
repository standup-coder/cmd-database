---
{
  "cmd_name": "yugabyted",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 YugabyteDB 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "ysqlsh",
    "ycqlsh"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# yugabyted

> YugabyteDB 集群生命周期管理命令

## 安装

```bash
随 YugabyteDB 安装
```

## 用法

```
yugabyted [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `start` | 启动 |
| `stop` | 停止 |
| `status` | 状态 |
| `destroy` | 销毁 |

## 示例

### 示例 1: 启动本地集群

```bash
yugabyted start
```

### 示例 2: 查看状态

```bash
yugabyted status
```

## 关联命令

- [[ysqlsh]]
- [[ycqlsh]]

## 风险提示

> ⚠️ **HIGH**: destroy 会删除所有本地数据，请谨慎

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
