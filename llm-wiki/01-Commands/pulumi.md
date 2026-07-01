---
{
  "cmd_name": "pulumi",
  "cmd_category": "云平台/Pulumi",
  "cmd_dimension": "Pulumi",
  "cmd_install": "参考 https://www.pulumi.com/docs/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "terraform",
    "aws"
  ],
  "cmd_tags": [
    "deployment",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/cloud/pulumi.yaml"
}
---

# pulumi

> 使用通用编程语言（TypeScript/Python/Go 等）定义和部署云资源

## 安装

```bash
参考 https://www.pulumi.com/docs/install/
```

## 用法

```
pulumi [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `up` | 预览并部署资源变更 |
| `preview` | 预览变更但不部署 |
| `destroy` | 销毁所有管理的资源 |
| `stack` | 管理堆栈 |

## 示例

### 示例 1: 预览并部署当前项目

```bash
pulumi up
```

### 示例 2: 显示详细的资源差异

```bash
pulumi preview --diff
```

## 关联命令

- [[terraform]]
- [[aws]]

## 风险提示

> ⚠️ **HIGH**: pulumi up/destroy 会创建或删除真实云资源，请在确认变更范围后执行

## 所属维度

[[Pulumi-MOC|云平台/Pulumi]]
