---
{
  "cmd_name": "nginx",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "haproxy",
    "traefik",
    "caddy"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/infra.yaml"
}
---

# nginx

> 高性能 Web 服务器与反向代理

## 用法

```
nginx [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-t` | 测试配置 |
| `-s` | signal 发送信号 |
| `-c` | 指定配置文件 |
| `-g` | 全局指令 |

## 示例

### 示例 1: 测试配置文件

```bash
sudo nginx -t
```

### 示例 2: 平滑重载配置

```bash
sudo nginx -s reload
```

## 关联命令

- [[haproxy]]
- [[traefik]]
- [[caddy]]

## 风险提示

> ⚠️ **MEDIUM**: reload 失败或配置错误会中断服务，请先在测试环境验证

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
