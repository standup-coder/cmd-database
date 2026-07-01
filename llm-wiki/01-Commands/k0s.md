---
{
  "cmd_name": "k0s",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://docs.k0sproject.io/stable/install/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "k3s",
    "kubectl"
  ],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# k0s

> 零依赖单二进制 Kubernetes 发行版

## 安装

```bash
参考 https://docs.k0sproject.io/stable/install/
```

## 用法

```
k0s [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `controller` | 启动控制节点 |
| `worker` | 启动工作节点 |
| `status` |  |

## 示例

### 示例 1: 单节点安装

```bash
k0s install controller --single
```

### 示例 2: 查看集群状态

```bash
k0s status
```

## 关联命令

- [[k3s]]
- [[kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: k0s 需要 root 权限并配置系统服务，请在测试环境验证

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
