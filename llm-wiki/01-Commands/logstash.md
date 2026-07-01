---
{
  "cmd_name": "logstash",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://www.elastic.co/guide/en/logstash/current/installing-logstash.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "filebeat",
    "elasticsearch"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/extra.yaml"
}
---

# logstash

> 日志收集与转换管道

## 安装

```bash
参考 https://www.elastic.co/guide/en/logstash/current/installing-logstash.html
```

## 用法

```
logstash [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 指定配置文件 |
| `-e` | 直接指定管道 |
| `-t` | 测试配置 |
| `--config.reload.automatic` |  |

## 示例

### 示例 1: 启动 Logstash

```bash
logstash -f logstash.conf
```

### 示例 2: 从 stdin 读取并输出

```bash
logstash -e 'input { stdin {} } output { stdout {} }'
```

## 关联命令

- [[elasticsearch]]

## 风险提示

> ⚠️ **MEDIUM**: 错误的 grok/filter 会导致日志解析失败或数据丢失，请先用 -t 测试

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
