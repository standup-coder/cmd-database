---
{
  "cmd_name": "grype",
  "cmd_category": "容器编排/K8s安全扩展",
  "cmd_dimension": "K8s安全扩展",
  "cmd_install": "参考 https://github.com/anchore/grype/releases",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "trivy",
    "syft"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-security-extra.yaml"
}
---

# grype

> 容器镜像与文件系统漏洞扫描器

## 安装

```bash
参考 https://github.com/anchore/grype/releases
```

## 用法

```
grype [OPTIONS] TARGET
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 显示详细输出 |
| `--only-fixed` | 只显示有补丁的漏洞 |

## 示例

### 示例 1: 扫描镜像漏洞

```bash
grype registry.example.com/myapp:latest
```

### 示例 2: 扫描当前目录文件系统

```bash
grype dir:.
```

## 风险提示

> ⚠️ **LOW**: 扫描镜像不会修改镜像，但会下载漏洞数据库，注意网络与安全策略

## 所属维度

[[K8s安全扩展-MOC|容器编排/K8s安全扩展]]
