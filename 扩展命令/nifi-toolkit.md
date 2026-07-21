---
{
  "cmd_name": "nifi-toolkit",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 Apache NiFi 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "nifi",
    "openssl"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# nifi-toolkit

> Apache NiFi 命令行工具包

## 安装

```bash
随 Apache NiFi 安装
```

## 用法

```
nifi-toolkit [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `tls` | 证书生成 |
| `encrypt-config` |  |
| `file-manager` |  |

## 示例

### 示例 1: 生成 TLS 证书

```bash
bin/tls-toolkit.sh standalone -n 'nifi[1-3].example.com' -C 'CN=admin'
```

### 示例 2: 加密配置

```bash
bin/encrypt-config.sh
```

## 关联命令

- [[nifi]]

## 风险提示

> ⚠️ **HIGH**: 加密配置前请备份，丢失密钥将无法解密

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
