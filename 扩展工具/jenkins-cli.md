---
{
  "cmd_name": "jenkins-cli",
  "cmd_category": "CI/CD/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "从 Jenkins 管理页下载 jenkins-cli.jar",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gitlab-runner",
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

# jenkins-cli

> Jenkins 命令行管理工具

## 安装

```bash
从 Jenkins 管理页下载 jenkins-cli.jar
```

## 用法

```
java -jar jenkins-cli.jar [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `-s` | Jenkins URL |
| `-auth` | 认证 |
| `who-am-i` |  |
| `build` | 触发构建 |
| `install-plugin` |  |

## 示例

### 示例 1: 查看当前用户

```bash
java -jar jenkins-cli.jar -s http://jenkins:8080 who-am-i
```

### 示例 2: 触发构建

```bash
java -jar jenkins-cli.jar -s http://jenkins:8080 build myjob
```

## 关联命令

- [[gitlab-runner]]

## 风险提示

> ⚠️ **MEDIUM**: jenkins-cli 可安装插件和重启 Jenkins，请保护好凭据

## 所属维度

[[扩展工具-MOC|CI/CD/扩展工具]]
