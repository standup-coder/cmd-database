---
{
  "cmd_name": "nomad",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://developer.hashicorp.com/nomad/downloads",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "consul",
    "vault"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# nomad

> HashiCorp Nomad 工作负载调度器

## 安装

```bash
参考 https://developer.hashicorp.com/nomad/downloads
```

## 用法

```
nomad [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `job` | run 运行作业 |
| `status` | 查看状态 |
| `alloc` | 管理分配 |

## 示例

### 示例 1: 提交 Nomad 作业

```bash
nomad job run example.nomad
```

### 示例 2: 查看所有作业状态

```bash
nomad status
```

## 关联命令

- [[consul]]
- [[vault]]

## 风险提示

> ⚠️ **MEDIUM**: job stop 会停止工作负载，请确认影响范围

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
