---
{
  "cmd_name": "resolvectl",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dig",
    "systemd-resolve"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# resolvectl

> systemd-resolved DNS 解析控制

## 用法

```
resolvectl [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `query` | 解析域名 |
| `status` | 查看状态 |
| `flush-caches` | 清空缓存 |

## 示例

### 示例 1: 查询域名

```bash
resolvectl query example.com
```

### 示例 2: 清空 DNS 缓存

```bash
resolvectl flush-caches
```

## 关联命令

- [[dig]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
