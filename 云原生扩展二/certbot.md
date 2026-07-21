---
{
  "cmd_name": "certbot",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://certbot.eff.org/instructions",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cert-manager",
    "openssl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# certbot

> Let's Encrypt 证书自动申请工具

## 安装

```bash
参考 https://certbot.eff.org/instructions
```

## 用法

```
certbot [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `certonly` |  |
| `--standalone` |  |
| `--nginx` |  |
| `--dns-cloudflare` |  |
| `--renew` |  |

## 示例

### 示例 1: 申请证书

```bash
sudo certbot certonly --standalone -d example.com
```

### 示例 2: 测试续期

```bash
sudo certbot renew --dry-run
```

## 关联命令

- [[cert-manager]]

## 风险提示

> ⚠️ **MEDIUM**: 生产环境 renew 前请先用 dry-run 验证

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
