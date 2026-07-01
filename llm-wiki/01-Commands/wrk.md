---
{
  "cmd_name": "wrk",
  "cmd_category": "网络工具/性能压测",
  "cmd_dimension": "性能压测",
  "cmd_install": "参考 https://github.com/wg/wrk",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "wrk2",
    "ab"
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

# wrk

> 高性能 HTTP 基准测试工具

## 安装

```bash
参考 https://github.com/wg/wrk
```

## 用法

```
wrk [OPTIONS] URL
```

## 参数

| Flag | Description |
|------|-------------|
| `-t` | 线程数 |
| `-c` | 并发连接数 |
| `-d` | 测试持续时间 |
| `-s` | 加载 Lua 脚本 |

## 示例

### 示例 1: 12 线程 400 并发压测 30 秒

```bash
wrk -t12 -c400 -d30s https://example.com
```

### 示例 2: 小并发短时长测试并显示延迟分布

```bash
wrk -t2 -c10 -d10s --latency https://example.com/api
```

## 关联命令

- [[wrk2]]
- [[ab]]

## 风险提示

> ⚠️ **HIGH**: 对生产环境或无授权目标压测可能造成拒绝服务，请获得许可并控制速率

## 所属维度

[[性能压测-MOC|网络工具/性能压测]]
