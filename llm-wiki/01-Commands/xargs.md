---
{
  "cmd_name": "xargs",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "find",
    "parallel"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# xargs

> 从标准输入构建并执行命令

## 用法

```
xargs [OPTIONS] [COMMAND [INITIAL-ARGS]]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 每次传递的参数个数 |
| `-P` | 并行进程数 |
| `-I` | 替换字符串占位符 |

## 示例

### 示例 1: 删除所有找到的 log 文件

```bash
find . -name "*.log" | xargs rm
```

### 示例 2: 并行下载 4 个 URL

```bash
cat urls.txt | xargs -n 1 -P 4 curl -O
```

## 关联命令

- [[find]]

## 风险提示

> ⚠️ **HIGH**: xargs 执行 rm 等命令是批量操作，建议先用 xargs echo 预览

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
