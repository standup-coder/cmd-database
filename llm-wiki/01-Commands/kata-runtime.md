---
{
  "cmd_name": "kata-runtime",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://github.com/kata-containers/kata-containers/blob/main/docs/install/README.md",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "containerd",
    "firecracker"
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

# kata-runtime

> Kata Containers 运行时

## 安装

```bash
参考 https://github.com/kata-containers/kata-containers/blob/main/docs/install/README.md
```

## 用法

```
kata-runtime [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `version` |  |
| `check` |  |
| `factory` |  |

## 示例

### 示例 1: 查看版本

```bash
kata-runtime version
```

### 示例 2: 检查系统兼容性

```bash
kata-runtime check
```

## 关联命令

- [[containerd]]
- [[firecracker]]

## 风险提示

> ⚠️ **MEDIUM**: Kata 使用 VM，需确认内核和虚拟化支持

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
