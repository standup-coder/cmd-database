---
{
  "cmd_name": "firecracker",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://github.com/firecracker-microvm/firecracker",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kata-runtime",
    "containerd"
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

# firecracker

> AWS 开源微虚拟机（microVM）

## 安装

```bash
参考 https://github.com/firecracker-microvm/firecracker
```

## 用法

```
firecracker [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--api-sock` |  |
| `--config-file` |  |
| `--id` |  |

## 示例

### 示例 1: 启动 API 服务

```bash
firecracker --api-sock /tmp/firecracker.sock
```

### 示例 2: 配置 MMDS

```bash
curl --unix-socket /tmp/firecracker.sock -X PUT http://localhost/mmds -d '{"latest":{}}'
```

## 关联命令

- [[kata-runtime]]
- [[containerd]]

## 风险提示

> ⚠️ **MEDIUM**: Firecracker 直接运行微虚拟机，需配置安全组和资源限制

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
