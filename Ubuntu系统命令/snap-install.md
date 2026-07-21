---
{
  "cmd_name": "snap install",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on Ubuntu 16.04+",
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
  "source_file": "data/os/ubuntu.yaml"
}
---

# snap install

> Install snap package

## 安装

```bash
Pre-installed on Ubuntu 16.04+
```

## 用法

```
sudo snap install <package>
```

## 参数

| Flag | Description |
|------|-------------|
| `--classic` | Install with classic confinement |

## 示例

### 示例 1: Install VS Code

```bash
sudo snap install code --classic
```

### 示例 2: Install VLC media player

```bash
sudo snap install vlc
```

## 风险提示

> ⚠️ **LOW**: Snaps are sandboxed; generally safe

## 所属维度

[[通用Linux命令-MOC|Operating System]]
