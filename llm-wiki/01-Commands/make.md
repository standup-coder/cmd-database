---
{
  "cmd_name": "make",
  "cmd_category": "构建工具/Make",
  "cmd_dimension": "Make",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mvn",
    "gradle"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/build-tools/make.yaml"
}
---

# make

> GNU Make 构建自动化工具，通过 Makefile 定义构建规则

## 用法

```
make [目标]
```

```
make -f Makefile [目标]
```

```
make -j[N] [目标]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 指定 Makefile 文件 |
| `-j` | 并行构建（指定任务数） |
| `-C` | 切换到指定目录 |
| `-n` | 仅显示命令不执行（dry run） |
| `-B` | 强制重新构建 |

## 示例

### 示例 1: 构建默认目标

```bash
make
```

### 示例 2: 构建所有目标

```bash
make all
```

### 示例 3: 清理后重新构建

```bash
make clean && make
```

### 示例 4: 4 线程并行构建

```bash
make -j4
```

### 示例 5: 预览构建命令

```bash
make -n build
```

## 关联命令

- [[mvn]]
- [[gradle]]

## 风险提示

> ⚠️ **MEDIUM**: make -j 可能导致构建输出交错

## 所属维度

[[Make-MOC|构建工具/Make]]
