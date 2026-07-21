---
{
  "cmd_name": "subfinder",
  "cmd_category": "网络工具/网络安全",
  "cmd_dimension": "网络安全",
  "cmd_install": "参考 https://github.com/projectdiscovery/subfinder/releases",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "httpx",
    "nuclei"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/security.yaml"
}
---

# subfinder

> 子域名发现工具

## 安装

```bash
参考 https://github.com/projectdiscovery/subfinder/releases
```

## 用法

```
subfinder [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 指定目标域名 |
| `-o` | 输出结果文件 |

## 示例

### 示例 1: 发现 example.com 的子域名

```bash
subfinder -d example.com
```

### 示例 2: 将子域名结果保存到文件

```bash
subfinder -d example.com -o subs.txt
```

## 关联命令

- [[httpx]]
- [[nuclei]]

## 风险提示

> ⚠️ **MEDIUM**: 子域名枚举应仅针对自己拥有或授权评估的域名

## 所属维度

[[网络安全-MOC|网络工具/网络安全]]
