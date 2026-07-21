---
{
  "cmd_name": "envoy",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://www.envoyproxy.io/docs/envoy/latest/start/install",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "istioctl",
    "consul"
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

# envoy

> 云原生高性能代理

## 安装

```bash
参考 https://www.envoyproxy.io/docs/envoy/latest/start/install
```

## 用法

```
envoy [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 指定配置文件 |
| `--mode` |  |
| `--admin-address-path` |  |

## 示例

### 示例 1: 启动 Envoy

```bash
envoy -c envoy.yaml
```

### 示例 2: 验证配置

```bash
envoy --mode validate -c envoy.yaml
```

## 关联命令

- [[consul]]

## 风险提示

> ⚠️ **MEDIUM**: Envoy 作为数据平面，配置错误会中断流量

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
