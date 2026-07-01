---
{
  "cmd_name": "consul",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://developer.hashicorp.com/consul/downloads",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "vault",
    "envoy"
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

# consul

> HashiCorp Consul 服务网格与发现

## 安装

```bash
参考 https://developer.hashicorp.com/consul/downloads
```

## 用法

```
consul [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `agent` | 启动代理 |
| `kv` | 管理键值 |
| `catalog` | 查看服务 |
| `connect` |  |

## 示例

### 示例 1: 开发模式启动 Consul

```bash
consul agent -dev
```

### 示例 2: 递归读取配置

```bash
consul kv get -recurse config/
```

## 关联命令

- [[vault]]
- [[envoy]]

## 风险提示

> ⚠️ **MEDIUM**: Consul 为控制平面，配置错误会影响服务发现

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
