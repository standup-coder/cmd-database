---
{
  "cmd_name": "longhornctl",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://longhorn.io/docs/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubectl",
    "rookctl"
  ],
  "cmd_tags": [
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# longhornctl

> Longhorn 分布式存储管理

## 安装

```bash
参考 https://longhorn.io/docs/
```

## 用法

```
longhornctl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `install` |  |
| `uninstall` |  |
| `check` |  |

## 示例

### 示例 1: 安装 Longhorn

```bash
longhornctl install
```

### 示例 2: 检查环境

```bash
longhornctl check
```

## 关联命令

- [[kubectl]]
- [[rookctl]]

## 风险提示

> ⚠️ **HIGH**: 卸载 Longhorn 会丢失卷数据，请先备份

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
