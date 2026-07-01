---
{
  "cmd_name": "wrk2",
  "cmd_category": "网络工具/性能压测",
  "cmd_dimension": "性能压测",
  "cmd_install": "参考 https://github.com/giltene/wrk2",
  "cmd_platforms": [
    "linux",
    "darwin"
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

# wrk2

> 支持恒定吞吐量请求与精确延迟测量的 HTTP 压测工具

## 安装

```bash
参考 https://github.com/giltene/wrk2
```

## 用法

```
wrk2 [OPTIONS] URL
```

## 参数

| Flag | Description |
|------|-------------|
| `-R` | 目标每秒请求数（RPS） |
| `-t` | 线程数 |
| `-c` | 并发连接数 |
| `-d` | 测试持续时间 |

## 示例

### 示例 1: 以 2000 RPS 的恒定速率压测 60 秒

```bash
wrk2 -t4 -c100 -d60s -R2000 https://example.com
```

### 示例 2: 低恒定速率测试 API 延迟

```bash
wrk2 -t2 -c50 -d30s -R500 --latency https://example.com/api
```

## 关联命令

- [[wrk]]
- [[k6]]

## 风险提示

> ⚠️ **HIGH**: 恒定高压测试更容易压垮后端，请在隔离环境或授权沙箱中执行

## 所属维度

[[性能压测-MOC|网络工具/性能压测]]
