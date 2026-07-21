---
{
  "cmd_name": "npm update",
  "cmd_category": "Programming Language",
  "cmd_dimension": "Programming Language",
  "cmd_install": "Included with Node.js",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/lang/nodejs.yaml"
}
---

# npm update

> Update packages to their latest versions

## 安装

```bash
Included with Node.js
```

## 用法

```
npm update [package]
```

## 参数

| Flag | Description |
|------|-------------|
| `-g` | Update global packages |

## 示例

### 示例 1: Update all packages

```bash
npm update
```

### 示例 2: Update specific package

```bash
npm update express
```

### 示例 3: Update all global packages

```bash
npm update -g
```

## 风险提示

> ⚠️ **MEDIUM**: Updates may introduce breaking changes

## 所属维度

[[Node.js工具链-MOC|Programming Language]]
