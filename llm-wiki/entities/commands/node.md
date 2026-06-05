---
cmd_name: node
cmd_category: "编程语言/Node.js工具链"
cmd_dimension: Programming Language
cmd_install: Download from https://nodejs.org/
cmd_platforms:
- linux
- darwin
- windows
summary: "Execute JavaScript code using Node.js runtime"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/lang/nodejs.yaml
---


# node

> Execute JavaScript code using Node.js runtime

## 安装

```bash
Download from https://nodejs.org/
```

## 用法

```
node [options] [script.js] [arguments]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | Print Node.js version |
| `-e` | Evaluate script from command line |
| `--inspect` | Enable inspector for debugging |
| `--max-old-space-size` | Set maximum old space size (MB) |

## 示例

### 示例 1: Run JavaScript file

```bash
node app.js
```

### 示例 2: Check Node.js version

```bash
node -v
```

### 示例 3: Execute inline JavaScript

```bash
node -e 'console.log("Hello")'
```

### 示例 4: Run with debugger enabled

```bash
node --inspect app.js
```

## 风险提示

> ⚠️ **MEDIUM**: Running untrusted scripts can execute malicious code

## 所属维度

[[Nodejs工具链-MOC|Programming Language]]
