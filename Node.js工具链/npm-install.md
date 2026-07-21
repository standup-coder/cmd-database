---
{
  "cmd_name": "npm install",
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

# npm install

> Install package dependencies

## 安装

```bash
Included with Node.js
```

## 用法

```
npm install [package]
```

## 参数

| Flag | Description |
|------|-------------|
| `-g` | Install globally |
| `--save` | Save to dependencies |
| `--save-dev` | Save to devDependencies |
| `--production` | Skip devDependencies |

## 示例

### 示例 1: Install all dependencies from package.json

```bash
npm install
```

### 示例 2: Install express package

```bash
npm install express
```

### 示例 3: Install TypeScript globally

```bash
npm install -g typescript
```

### 示例 4: Install only production dependencies

```bash
npm install --production
```

## 风险提示

> ⚠️ **MEDIUM**: Installing packages from untrusted sources may introduce vulnerabilities

## 所属维度

[[Node.js工具链-MOC|Programming Language]]
