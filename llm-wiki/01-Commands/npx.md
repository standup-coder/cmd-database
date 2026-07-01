---
{
  "cmd_name": "npx",
  "cmd_category": "Programming Language",
  "cmd_dimension": "Programming Language",
  "cmd_install": "Included with npm 5.2+",
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

# npx

> Execute npm package binaries

## 安装

```bash
Included with npm 5.2+
```

## 用法

```
npx <command>
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | Install package if not found |
| `--no-install` | Skip auto-installation |

## 示例

### 示例 1: Create React app without global install

```bash
npx create-react-app myapp
```

### 示例 2: Run ESLint from local or remote package

```bash
npx eslint .
```

### 示例 3: Use specific package version

```bash
npx -p @angular/cli ng new myapp
```

## 风险提示

> ⚠️ **MEDIUM**: Downloads and executes code from npm registry

## 所属维度

[[Programming Language-MOC|Programming Language]]
