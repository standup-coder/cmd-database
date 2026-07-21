---
{
  "cmd_name": "snyk",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://docs.snyk.io/snyk-cli/install-the-snyk-cli",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "trivy",
    "grype"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# snyk

> 开发者安全扫描平台 CLI

## 安装

```bash
参考 https://docs.snyk.io/snyk-cli/install-the-snyk-cli
```

## 用法

```
snyk [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `test` | 扫描 |
| `container` | test 扫描镜像 |
| `code` | test 扫描代码 |
| `monitor` | 监控 |

## 示例

### 示例 1: 扫描项目依赖漏洞

```bash
snyk test
```

### 示例 2: 扫描容器镜像

```bash
snyk container test myapp:latest
```

## 关联命令

- [[grype]]

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
