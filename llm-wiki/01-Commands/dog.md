---
{
  "cmd_name": "dog",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://github.com/ogham/dog/releases",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dig",
    "host"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# dog

> 友好的命令行 DNS 客户端

## 安装

```bash
参考 https://github.com/ogham/dog/releases
```

## 用法

```
dog [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-t` | 指定记录类型 |
| `-n` | 指定名称服务器 |
| `--json` | JSON 输出 |

## 示例

### 示例 1: 查询 A 记录

```bash
dog example.com
```

### 示例 2: 使用指定 DNS 查询 MX

```bash
dog example.com MX -n 8.8.8.8
```

## 关联命令

- [[dig]]
- [[host]]

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
