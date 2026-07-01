---
{
  "cmd_name": "npm publish",
  "cmd_category": "Programming Language",
  "cmd_dimension": "Programming Language",
  "cmd_install": "Included with Node.js",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/lang/nodejs.yaml"
}
---

# npm publish

> Publish package to npm registry

## 安装

```bash
Included with Node.js
```

## 用法

```
npm publish [tarball|folder]
```

## 参数

| Flag | Description |
|------|-------------|
| `--access` | Set package access (public\|restricted) |
| `--tag` | Register with given tag |

## 示例

### 示例 1: Publish current package

```bash
npm publish
```

### 示例 2: Publish as public package

```bash
npm publish --access public
```

### 示例 3: Publish with beta tag

```bash
npm publish --tag beta
```

## 风险提示

> ⚠️ **HIGH**: Publishes package publicly; cannot be easily undone

## 所属维度

[[Programming Language-MOC|Programming Language]]
