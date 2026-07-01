---
{
  "cmd_name": "external-dns",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://kubernetes-sigs.github.io/external-dns/latest/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubectl",
    "aws"
  ],
  "cmd_tags": [
    "kubernetes",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# external-dns

> Kubernetes DNS 记录自动同步

## 安装

```bash
参考 https://kubernetes-sigs.github.io/external-dns/latest/
```

## 用法

```
external-dns [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--provider` | 指定 DNS 服务商 |
| `--source` | 指定来源 |
| `--dry-run` |  |

## 示例

### 示例 1: dry-run 查看待同步记录

```bash
external-dns --provider aws --source ingress --dry-run
```

### 示例 2: 同步 Service 到 DNS

```bash
external-dns --provider aws --source service
```

## 关联命令

- [[kubectl]]
- [[aws]]

## 风险提示

> ⚠️ **HIGH**: external-dns 会修改公共 DNS 记录，dry-run 验证后再执行

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
