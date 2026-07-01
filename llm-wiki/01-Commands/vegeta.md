---
{
  "cmd_name": "vegeta",
  "cmd_category": "网络工具/性能压测",
  "cmd_dimension": "性能压测",
  "cmd_install": "参考 https://github.com/tsenart/vegeta/releases",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
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
  "source_file": "data/network/performance.yaml"
}
---

# vegeta

> 多功能的 HTTP 负载测试 CLI 和库

## 安装

```bash
参考 https://github.com/tsenart/vegeta/releases
```

## 用法

```
vegeta [GLOBAL OPTIONS] COMMAND [COMMAND OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `attack` | 发起压测攻击 |
| `report` | 生成测试报告 |
| `-rate` | 每秒请求速率 |

## 示例

### 示例 1: 以 100 RPS 压测 30 秒并生成报告

```bash
echo "GET https://example.com" | vegeta attack -rate=100 -duration=30s | vegeta report
```

### 示例 2: 从文件读取目标列表并压测 1 分钟

```bash
vegeta attack -targets=targets.txt -rate=500 -duration=1m | tee results.bin | vegeta report
```

## 关联命令

- [[k6]]
- [[wrk]]

## 风险提示

> ⚠️ **HIGH**: 定向压测可能导致目标服务不可用，请仅在授权范围内使用

## 所属维度

[[性能压测-MOC|网络工具/性能压测]]
