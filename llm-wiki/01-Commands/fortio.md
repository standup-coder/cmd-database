---
{
  "cmd_name": "fortio",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://github.com/fortio/fortio/releases",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "k6",
    "wrk"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# fortio

> Istio 配套的负载测试与 echo 服务器

## 安装

```bash
参考 https://github.com/fortio/fortio/releases
```

## 用法

```
fortio [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `load` | 压测 |
| `server` | 启动 echo 服务器 |
| `-qps` | 每秒查询数 |
| `-t` | 持续时间 |

## 示例

### 示例 1: 以 100 QPS 压测 30 秒

```bash
fortio load -qps 100 -t 30s https://example.com
```

### 示例 2: 启动 echo 服务器

```bash
fortio server
```

## 关联命令

- [[k6]]
- [[wrk]]

## 风险提示

> ⚠️ **HIGH**: 高 QPS 压测会消耗目标资源，请获得授权

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
