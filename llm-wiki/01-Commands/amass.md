---
{
  "cmd_name": "amass",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://github.com/owasp-amass/amass/releases",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "subfinder",
    "httpx"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# amass

> 深度子域名枚举与资产发现

## 安装

```bash
参考 https://github.com/owasp-amass/amass/releases
```

## 用法

```
amass [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `enum` | 枚举 |
| `-d` | 目标域名 |
| `-o` | 输出文件 |
| `-active` | 主动模式 |

## 示例

### 示例 1: 枚举 example.com 子域名

```bash
amass enum -d example.com
```

### 示例 2: 保存结果

```bash
amass enum -d example.com -o subs.txt
```

## 关联命令

- [[subfinder]]
- [[httpx]]

## 风险提示

> ⚠️ **MEDIUM**: 主动枚举可能触发目标告警，请仅对授权域名执行

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
