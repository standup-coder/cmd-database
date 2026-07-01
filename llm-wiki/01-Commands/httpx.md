---
{
  "cmd_name": "httpx",
  "cmd_category": "网络工具/网络安全",
  "cmd_dimension": "网络安全",
  "cmd_install": "参考 https://github.com/projectdiscovery/httpx/releases",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nuclei",
    "subfinder"
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

# httpx

> 快速多线程 HTTP 探活与信息收集工具

## 安装

```bash
参考 https://github.com/projectdiscovery/httpx/releases
```

## 用法

```
httpx [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 指定包含 URL 列表的文件 |
| `-status-code` | 显示响应状态码 |
| `-title` | 显示页面标题 |

## 示例

### 示例 1: 探测单个域名并显示状态码和标题

```bash
echo "example.com" | httpx -status-code -title
```

### 示例 2: 批量探测存活 URL 并输出到文件

```bash
httpx -l urls.txt -o live.txt
```

## 关联命令

- [[nuclei]]
- [[subfinder]]

## 风险提示

> ⚠️ **MEDIUM**: 批量探测应限制速率，避免对目标造成拒绝服务或被封禁

## 所属维度

[[网络安全-MOC|网络工具/网络安全]]
