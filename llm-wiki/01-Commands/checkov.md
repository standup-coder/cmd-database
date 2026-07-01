---
{
  "cmd_name": "checkov",
  "cmd_category": "容器编排/K8s安全扩展",
  "cmd_dimension": "K8s安全扩展",
  "cmd_install": "pip install checkov",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "trivy",
    "terraform"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-security-extra.yaml"
}
---

# checkov

> 基础设施即代码静态安全分析工具

## 安装

```bash
pip install checkov
```

## 用法

```
checkov [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 扫描目录 |
| `-f` | 扫描文件 |
| `--framework` | 指定框架（terraform、kubernetes、dockerfile 等） |

## 示例

### 示例 1: 扫描 K8s YAML 清单

```bash
checkov -d ./k8s-manifests
```

### 示例 2: 扫描 Terraform 文件

```bash
checkov -f main.tf --framework terraform
```

## 关联命令

- [[terraform]]

## 风险提示

> ⚠️ **LOW**: 静态扫描不会修改基础设施，但可能产生大量告警，请结合优先级处理

## 所属维度

[[K8s安全扩展-MOC|容器编排/K8s安全扩展]]
