---
{
  "cmd_name": "tsar",
  "cmd_category": "System Diagnostic",
  "cmd_dimension": "System Diagnostic",
  "cmd_install": "Install from https://github.com/alibaba/tsar",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/diagnostic/tsar.yaml"
}
---

# tsar

> Display system performance statistics

## 安装

```bash
Install from https://github.com/alibaba/tsar
```

## 用法

```
tsar [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | Show live mode (default 2 seconds interval) |
| `-i` | Set display interval (seconds) |
| `-n` | Number of iterations |
| `-d` | Specify date to display (YYYYMMDD) |
| `--cpu` | Display CPU stats |
| `--mem` | Display memory stats |
| `--io` | Display I/O stats |
| `--traffic` | Display network traffic |

## 示例

### 示例 1: Display today's system statistics

```bash
tsar
```

### 示例 2: Display live statistics

```bash
tsar -l
```

### 示例 3: Display live stats every 5 seconds

```bash
tsar -l -i 5
```

### 示例 4: Display CPU and memory stats

```bash
tsar --cpu --mem
```

### 示例 5: Display stats for specific date

```bash
tsar -d 20241214
```

## 风险提示

> ⚠️ **LOW**: Read-only monitoring tool; no risks

## 所属维度

[[System Diagnostic-MOC|System Diagnostic]]
