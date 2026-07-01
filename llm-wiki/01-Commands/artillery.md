---
{
  "cmd_name": "artillery",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "npm install -g artillery",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "k6",
    "locust"
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

# artillery

> 现代 Node.js 负载测试与 SRE 工具

## 安装

```bash
npm install -g artillery
```

## 用法

```
artillery [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行测试 |
| `quick` | 快速压测 |
| `-o` | 输出报告 |

## 示例

### 示例 1: 快速压测

```bash
artillery quick --count 10 --num 50 https://example.com
```

### 示例 2: 运行 YAML 压测脚本

```bash
artillery run load-test.yml
```

## 关联命令

- [[k6]]
- [[locust]]

## 风险提示

> ⚠️ **HIGH**: 压测可能影响生产服务，请在授权沙箱或测试环境执行

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
