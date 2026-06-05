---
cmd_name: npm audit
cmd_category: "编程语言/Node.js工具链"
cmd_dimension: Programming Language
cmd_install: Included with Node.js
cmd_platforms:
- linux
- darwin
- windows
summary: "Check for security vulnerabilities"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/lang/nodejs.yaml
---


# npm audit

> Check for security vulnerabilities

## 安装

```bash
Included with Node.js
```

## 用法

```
npm audit [fix]
```

## 参数

| Flag | Description |
|------|-------------|
| `fix` | Automatically fix vulnerabilities |
| `--force` | Apply fixes even with breaking changes |

## 示例

### 示例 1: Scan for vulnerabilities

```bash
npm audit
```

### 示例 2: Fix vulnerabilities automatically

```bash
npm audit fix
```

### 示例 3: Force fix all vulnerabilities

```bash
npm audit fix --force
```

## 风险提示

> ⚠️ **MEDIUM**: Auto-fix may introduce breaking changes

## 所属维度

[[Nodejs工具链-MOC|Programming Language]]
