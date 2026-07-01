---
{
  "cmd_name": "atlantis",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://www.runatlantis.io/docs/installation-guide.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "terraform",
    "github-actions"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# atlantis

> Terraform 自动化 PR 工作流工具

## 安装

```bash
参考 https://www.runatlantis.io/docs/installation-guide.html
```

## 用法

```
atlantis [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `plan` | 触发计划 |
| `apply` | 触发应用 |
| `version` |  |

## 示例

### 示例 1: 对当前 PR 执行 plan

```bash
atlantis plan
```

### 示例 2: 应用已批准的 plan

```bash
atlantis apply
```

## 关联命令

- [[terraform]]

## 风险提示

> ⚠️ **HIGH**: atlantis apply 会修改真实基础设施，请确保 PR 已审查

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
