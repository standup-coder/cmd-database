---
{
  "cmd_name": "locust",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "pip install locust",
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
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# locust

> Python 编写的可编程负载测试工具

## 安装

```bash
pip install locust
```

## 用法

```
locust [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 指定 locustfile |
| `--host` | 目标主机 |
| `-u` | 用户数 |
| `-r` | 每秒启动数 |

## 示例

### 示例 1: 启动 Locust Web 界面

```bash
locust -f locustfile.py --host https://example.com
```

### 示例 2: 无头模式运行 60 秒

```bash
locust -f locustfile.py -u 100 -r 10 --run-time 60s --headless
```

## 关联命令

- [[k6]]
- [[wrk]]

## 风险提示

> ⚠️ **HIGH**: Locust 压测会消耗目标资源，请获得授权并配置限流

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
