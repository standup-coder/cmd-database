---
{
  "cmd_name": "postman",
  "cmd_category": "Network Tools",
  "cmd_dimension": "Network Tools",
  "cmd_install": "npm install -g newman",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/network/http.yaml"
}
---

# postman

> API development and testing platform (CLI)

## 安装

```bash
npm install -g newman
```

## 用法

```
newman run <collection>
```

## 示例

### 示例 1: Run Postman collection

```bash
newman run api-collection.json
```

### 示例 2: Run with environment variables

```bash
newman run collection.json -e environment.json
```

## 风险提示

> ⚠️ **LOW**: API calls may modify data on target system

## 所属维度

[[Network Tools-MOC|Network Tools]]
