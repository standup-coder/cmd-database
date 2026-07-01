---
{
  "cmd_name": "oha",
  "cmd_category": "网络工具/性能压测",
  "cmd_dimension": "性能压测",
  "cmd_install": "参考 https://github.com/hatoo/oha",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "wrk",
    "k6"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/performance.yaml"
}
---

# oha

> Rust 编写的实时 HTTP 负载生成器

## 安装

```bash
参考 https://github.com/hatoo/oha
```

## 用法

```
oha [OPTIONS] URL
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 总请求数 |
| `-c` | 并发连接数 |
| `-z` | 测试持续时间 |

## 示例

### 示例 1: 100 并发共发送 10000 个请求

```bash
oha -n 10000 -c 100 https://example.com
```

### 示例 2: 10 并发持续 30 秒压测

```bash
oha -c 10 -z 30s https://example.com
```

## 关联命令

- [[wrk]]
- [[k6]]

## 风险提示

> ⚠️ **HIGH**: 高并发请求会占用目标资源，请确保目标可承受并获授权

## 所属维度

[[性能压测-MOC|网络工具/性能压测]]
