---
{
  "cmd_name": "chmod",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "chown",
    "umask"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# chmod

> 修改文件或目录权限

## 用法

```
chmod [OPTIONS] MODE FILE...
```

## 参数

| Flag | Description |
|------|-------------|
| `-R` | 递归修改 |
| `-v` | 显示修改过程 |
| `--reference` | 参考其他文件权限 |

## 示例

### 示例 1: 设置文件权限为 rwxr-xr-x

```bash
chmod 755 script.sh
```

### 示例 2: 递归添加用户写权限

```bash
chmod -R u+w dir
```

## 关联命令

- [[chown]]
- [[umask]]

## 风险提示

> ⚠️ **HIGH**: 错误的权限设置可能导致服务无法访问或安全暴露

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
