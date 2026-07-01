---
{
  "cmd_name": "gitlab-runner",
  "cmd_category": "CI/CD/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://docs.gitlab.com/runner/install/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "jenkins-cli",
    "github-actions"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/cicd/more.yaml"
}
---

# gitlab-runner

> GitLab CI 运行器

## 安装

```bash
参考 https://docs.gitlab.com/runner/install/
```

## 用法

```
gitlab-runner [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `register` | 注册 |
| `list` |  |
| `run` | 单 runner |
| `unregister` |  |

## 示例

### 示例 1: 注册 runner

```bash
gitlab-runner register
```

### 示例 2: 列出 runner

```bash
gitlab-runner list
```

## 关联命令

- [[jenkins-cli]]

## 风险提示

> ⚠️ **MEDIUM**: register 需要 GitLab token，请勿泄露

## 所属维度

[[扩展工具-MOC|CI/CD/扩展工具]]
