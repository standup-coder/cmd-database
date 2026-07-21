---
{
  "cmd_name": "mitmproxy",
  "cmd_category": "网络工具/网络安全",
  "cmd_dimension": "网络安全",
  "cmd_install": "pip install mitmproxy 或参考官网 https://mitmproxy.org/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "curl",
    "wireshark"
  ],
  "cmd_tags": [
    "safety",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/security.yaml"
}
---

# mitmproxy

> 交互式 HTTPS 代理与流量分析工具

## 安装

```bash
pip install mitmproxy 或参考官网 https://mitmproxy.org/
```

## 用法

```
mitmproxy [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--mode` | 运行模式（regular、transparent、reverse 等） |
| `--listen-port` | 监听端口 |

## 示例

### 示例 1: 启动交互式代理界面

```bash
mitmproxy
```

### 示例 2: 启动 Web 界面代理

```bash
mitmweb --listen-port 8080
```

## 关联命令

- [[curl]]

## 风险提示

> ⚠️ **HIGH**: 拦截 HTTPS 需要安装自定义证书，可能违反合规政策并泄露敏感流量，请获得授权

## 所属维度

[[网络安全-MOC|网络工具/网络安全]]
