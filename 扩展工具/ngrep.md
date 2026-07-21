---
{
  "cmd_name": "ngrep",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "包管理器安装，如 sudo apt install ngrep",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "tcpdump",
    "grep"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# ngrep

> 网络数据包内容过滤工具

## 安装

```bash
包管理器安装，如 sudo apt install ngrep
```

## 用法

```
ngrep [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 忽略大小写 |
| `-W` | byline |
| `-q` | 静默 |
| `-d` | 指定网卡 |

## 示例

### 示例 1: 过滤 80 端口的 GET 请求

```bash
sudo ngrep -d eth0 'GET' 'tcp port 80'
```

### 示例 2: 查找含 password 的流量

```bash
sudo ngrep -q 'password' 'port 3306'
```

## 关联命令

- [[tcpdump]]
- [[grep]]

## 风险提示

> ⚠️ **HIGH**: 匹配敏感关键词会泄露数据，请仅在授权环境使用

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
