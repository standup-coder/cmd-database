---
{
  "cmd_name": "zeppelin",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://zeppelin.apache.org/docs/latest/quickstart/install.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "jupyter",
    "spark-submit"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# zeppelin

> Apache Zeppelin 交互式数据分析笔记本

## 安装

```bash
参考 https://zeppelin.apache.org/docs/latest/quickstart/install.html
```

## 用法

```
zeppelin [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `daemon.sh` | 启动/停止 |
| `--config` |  |

## 示例

### 示例 1: 启动 Zeppelin

```bash
bin/zeppelin-daemon.sh start
```

### 示例 2: 停止 Zeppelin

```bash
bin/zeppelin-daemon.sh stop
```

## 关联命令

- [[spark-submit]]

## 风险提示

> ⚠️ **MEDIUM**: Zeppelin 解释器可执行任意代码，请配置认证和权限

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
