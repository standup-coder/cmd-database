---
{
  "cmd_name": "curl",
  "cmd_category": "网络工具/网络诊断",
  "cmd_dimension": "网络诊断",
  "cmd_install": "apt install curl (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "wget"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/network/diagnostic.yaml"
}
---

# curl

> 命令行HTTP客户端

## 安装

```bash
apt install curl (Ubuntu)
```

## 用法

```
curl [options] <URL>
```

## 参数

| Flag | Description |
|------|-------------|
| `-X <method>` | 指定HTTP方法 |
| `-H <header>` | 添加请求头 |
| `-d <data>` | 发送POST数据 |
| `-o <file>` | 保存到文件 |
| `-v` | 详细输出 |

## 示例

### 示例 1: 发送GET请求

```bash
curl https://api.github.com
```

### 示例 2: 发送POST请求

```bash
curl -X POST -d 'key=value' https://example.com
```

### 示例 3: 下载文件

```bash
curl -o file.zip https://example.com/file.zip
```

## 关联命令

- [[wget]]

## 所属维度

[[网络诊断-MOC|网络工具/网络诊断]]
