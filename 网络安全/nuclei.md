---
{
  "cmd_name": "nuclei",
  "cmd_category": "网络工具/网络安全",
  "cmd_dimension": "网络安全",
  "cmd_install": "参考 https://github.com/projectdiscovery/nuclei/releases",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "httpx",
    "subfinder"
  ],
  "cmd_tags": [
    "safety",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/security.yaml"
}
---

# nuclei

> 基于模板的快速漏洞扫描器

## 安装

```bash
参考 https://github.com/projectdiscovery/nuclei/releases
```

## 用法

```
nuclei [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 指定目标 URL |
| `-t` | 指定模板或模板目录 |
| `-severity` | 按严重程度过滤（info/low/medium/high/critical） |

## 示例

### 示例 1: 对目标网站进行默认模板扫描

```bash
nuclei -u https://example.com
```

### 示例 2: 只扫描高危和严重漏洞

```bash
nuclei -u https://example.com -severity high,critical
```

## 关联命令

- [[httpx]]
- [[subfinder]]

## 风险提示

> ⚠️ **HIGH**: 漏洞扫描可能对目标服务造成压力，请仅对授权资产执行

## 所属维度

[[网络安全-MOC|网络工具/网络安全]]
