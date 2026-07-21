---
{
  "cmd_name": "chown",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "chmod",
    "useradd"
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

# chown

> 修改文件或目录所有者

## 用法

```
chown [OPTIONS] [OWNER][:[GROUP]] FILE...
```

## 参数

| Flag | Description |
|------|-------------|
| `-R` | 递归修改 |
| `--reference` | 参考其他文件所有者 |

## 示例

### 示例 1: 修改所有者和组

```bash
sudo chown user:group file.txt
```

### 示例 2: 递归修改目录所有者

```bash
sudo chown -R www-data: /var/www
```

## 关联命令

- [[chmod]]
- [[useradd]]

## 风险提示

> ⚠️ **HIGH**: 更改系统目录所有者可能影响服务运行，请谨慎使用 -R

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
