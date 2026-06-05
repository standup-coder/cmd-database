---
cmd_name: wget
cmd_category: "网络工具/HTTP工具"
cmd_dimension: Network Tools
cmd_install: Pre-installed on most Linux; download for Windows
cmd_platforms:
- linux
- darwin
- windows
summary: "Download files from the web"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/network/http.yaml
---


# wget

> Download files from the web

## 安装

```bash
Pre-installed on most Linux; download for Windows
```

## 用法

```
wget [options] URL
```

## 参数

| Flag | Description |
|------|-------------|
| `-O` | Save to specific filename |
| `-c` | Continue interrupted download |
| `-r` | Recursive download |
| `-b` | Background download |
| `--limit-rate` | Limit download speed |

## 示例

### 示例 1: Download file

```bash
wget https://example.com/file.zip
```

### 示例 2: Download with custom filename

```bash
wget -O custom.zip https://example.com/file.zip
```

### 示例 3: Resume interrupted download

```bash
wget -c https://example.com/large-file.iso
```

### 示例 4: Limit download speed to 200KB/s

```bash
wget --limit-rate=200k https://example.com/file.zip
```

## 风险提示

> ⚠️ **MEDIUM**: Downloading from untrusted sources may introduce malware

## 所属维度

[[HTTP工具-MOC|Network Tools]]
