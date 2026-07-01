---
{
  "cmd_name": "infracost",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://www.infracost.io/docs/#quick-start",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "terraform",
    "pulumi"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# infracost

> 云基础设施成本估算工具

## 安装

```bash
参考 https://www.infracost.io/docs/#quick-start
```

## 用法

```
infracost [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `breakdown` | 生成成本明细 |
| `diff` | 比较成本差异 |
| `--path` | 指定 IaC 目录 |

## 示例

### 示例 1: 估算当前目录 IaC 成本

```bash
infracost breakdown --path .
```

### 示例 2: 比较成本差异

```bash
infracost diff --path . --compare-to infracost-base.json
```

## 关联命令

- [[terraform]]
- [[pulumi]]

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
