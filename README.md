# cmd4coder - 命令行工具大全

![Version](https://img.shields.io/badge/version-1.5.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Go Version](https://img.shields.io/badge/go-%3E%3D1.21-blue)
![Test Coverage](https://img.shields.io/badge/coverage-75%25-green)
![Build Status](https://img.shields.io/badge/build-passing-success)

## 📖 简介

cmd4coder 是一个面向运维工程师和开发者的命令行工具大全，通过 Go 语言实现，提供简单优雅的用户体验。

### ✨ 核心特性

- 📚 **全面的命令清单**: 涵盖 Linux、编程语言工具链、诊断工具、网络工具、Kubernetes生态系统等38+分类，500+精选命令
- 🔍 **强大的搜索功能**: 支持模糊搜索、关键词匹配和智能排序，4级优先级匹配算法
- ⚡ **快速查询**: 本地化存储，无需网络，毫秒级响应，LRU缓存优化
- 📝 **详细的命令说明**: 包含用法、选项、示例、注意事项和风险提示
- 🎨 **双模式交互**: 支持传统CLI和交互式TUI两种使用方式
- 💾 **配置管理**: 支持收藏、历史记录、自定义配置
- 📤 **导出功能**: 支持Markdown和JSON格式导出
- 🌐 **跨平台支持**: 支持 Linux、macOS 和 Windows

## 🚀 快速开始

### 安装

#### 下载预编译版本（推荐）

从 [Releases](https://github.com/cmd4coder/cmd4coder/releases) 页面下载对应平台的可执行文件：

- **Linux (amd64)**: `cmd4coder-v1.5.0-linux-amd64.tar.gz`
- **macOS (amd64)**: `cmd4coder-v1.5.0-darwin-amd64.tar.gz`
- **macOS (arm64)**: `cmd4coder-v1.5.0-darwin-arm64.tar.gz`
- **Windows (amd64)**: `cmd4coder-v1.5.0-windows-amd64.zip`

解压后将可执行文件放到PATH路径下即可使用。

#### 从源码构建

```bash
git clone https://github.com/cmd4coder/cmd4coder.git
cd cmd4coder
go build -o bin/cmd4coder ./cmd/cli
# Windows
.\build.ps1
# Linux/macOS
./build.sh
```

### 基本使用

> **注意**: 以下示例中的 `cmd4coder` 可替换为以下任一方式执行：
> - **开发模式**: `go run ./cmd/cli`
> - **构建后**: `./build/cmd4coder-v1.0.0-windows-amd64.exe` (Windows) 或对应平台的可执行文件
> - **安装后**: 如果已通过 `go install ./cmd/cli` 安装，可直接使用 `cli`

#### CLI 模式

```bash
# 查看帮助
go run ./cmd/cli --help

# 列出所有分类
go run ./cmd/cli categories -d ./data

# 列出所有命令
go run ./cmd/cli list -d ./data

# 列出指定分类的命令
go run ./cmd/cli list "操作系统/通用Linux命令" -d ./data

# 查看命令详情
go run ./cmd/cli show ls -d ./data

# 搜索命令
go run ./cmd/cli search file -d ./data
go run ./cmd/cli search "网络诊断" -d ./data

# 导出命令到Markdown
go run ./cmd/cli export ls -f markdown -o ls.md -d ./data

# 导出所有命令到JSON
go run ./cmd/cli export-all -f json -o commands.json -d ./data

# 查看版本信息
go run ./cmd/cli version
```

### 管道集成

cmd4coder 的 JSON 输出可以与 fzf 组合实现交互式模糊搜索：

```bash
# 交互式选择命令
cmd4coder list -f json | jq -r '.[].name' | fzf --preview 'cmd4coder show {1}' | xargs -I{} cmd4coder show {}

# 按分类搜索
cmd4coder list -f json | jq -r '.[] | fzf --filter 'jq -r .category' | head -1 | xargs cmd4coder list

# 搜索结果管道
cmd4coder search docker -f json | jq -r '.[].name' | fzf --multi --preview 'cmd4coder show {}'
```

#### TUI 交互模式

无参数启动进入交互式界面：

```bash
go run ./cmd/cli -d ./data
```

**快捷键**:
- `↑/↓`: 上下移动
- `Tab`: 切换面板
- `/`: 搜索
- `f`: 收藏命令
- `h`: 向左切换面板
- `e`: 导出当前命令
- `?`: 显示帮助
- `q`: 退出

## 📚 文档组织

项目文档按照用途进行了分类整理：

### 📖 使用指南 (docs/guides/)
- **DEPLOYMENT.md**: 部署指南和最佳实践

### 📊 技术参考 (docs/reference/)
- **IMPLEMENTATION_SUMMARY.md**: 实现摘要和技术细节
- **K8S_INTEGRATION_REPORT.md**: Kubernetes集成报告
- **KUBERNETES_COMMANDS.md**: Kubernetes命令清单

### 🏗️ 架构文档 (docs/architecture/)
- **ARCHITECTURE.md**: 系统架构设计文档

### 📈 项目报告 (docs/reports/)
包含项目开发过程中的各类报告文档。

### 🎨 网站资源 (docs/css/, docs/js/, docs/assets/)
项目官网的前端资源文件。

### 操作系统 (45个命令)
- ✅ Ubuntu 系统命令 (20个)
- ✅ CentOS 系统命令 (16个)
- ✅ 通用 Linux 命令 (9个)

### 编程语言工具链 (31个命令)
- ✅ Java 工具链 (javac, java, jps, jstat, jmap, jstack等) (9个)
- ✅ Go 工具链 (go build, go test, go mod等) (7个)
- ✅ Python 工具链 (pip, virtualenv等) (5个)
- ✅ Node.js 工具链 (npm, node等) (10个)

### 诊断工具 (22个命令)
- ✅ Arthas - Java 应用诊断工具 (12个)
- ✅ tsar - 系统性能诊断工具 (10个)

### 网络工具 (14个命令)
- ✅ DNS 工具 (dig, nslookup等) (3个)
- ✅ 网络诊断 (tcpdump, netstat, ss等) (6个)
- ✅ HTTP 工具 (curl, wget等) (5个)

### 容器编排 (200+个命令)
- ✅ Docker 命令 (10个)
- ✅ Kubernetes 命令 (kubectl) (25个)
- ✅ K8s 集群管理 (kubeadm, kubelet, etcdctl) (20个)
- ✅ K8s 容器运行时 (crictl, ctr, containerd) (9个)
- ✅ K8s 监控日志 (prometheus, grafana, opentelemetry, loki, fluentd) (45个)
- ✅ K8s 网络插件 (calicoctl, cilium) (15个)
- ✅ K8s 存储管理 (PV/PVC, StorageClass) (25个)
- ✅ K8s Helm包管理 (35个)
- ✅ K8s CI/CD (argocd, flux, tekton) (11个)
- ✅ K8s 配置管理 (ansible, terraform) (27个)
- ✅ K8s 备份恢复 (velero, restic) (8个)
- ✅ K8s 安全工具 (trivy, kube-bench, falco, RBAC) (25个)
- ✅ K8s 故障排查 (30个)
- ✅ K8s 辅助工具 (k9s, kubectx, kubens, stern, popeye) (5个)
- ✅ K8s 云平台工具 (eksctl, az aks, gcloud) (9个)
- ✅ K8s 开发调试 (skaffold, tilt, telepresence) (8个)

### 数据库工具 (28个命令)
- ✅ MySQL 工具 (mysql, mysqldump等) (8个)
- ✅ Redis 工具 (redis-cli) (10个)
- ✅ PostgreSQL 工具 (psql) (10个)

### 版本控制 (25个命令)
- ✅ Git 命令 (11个)
- ✅ SVN 命令 (14个)

### 构建工具 (29个命令)
- ✅ Maven (12个)
- ✅ Gradle (10个)
- ✅ Make (7个)

### Shell/Bash 工具
- ✅ Bash 脚本编写和调试工具

### CI-CD/GitHub Actions
- ✅ GitHub Actions 持续集成和持续部署工具

### Rust 工具链
- ✅ Rust 编程语言工具链命令 (rustc, cargo等)

### AWS CLI
- ✅ Amazon Web Services 命令行工具

### 构建工具 (Maven/Gradle/Make)
- ✅ Maven 项目管理和构建工具
- ✅ Gradle 项目自动化构建工具
- ✅ GNU Make 和 CMake 构建工具

### AI基础设施 (4个命令)
- ✅ ML框架 (torchrun, tensorboard) (2个)
- ✅ MLOps平台 (kfp, mlflow) (2个)
- ✅ 模型服务 (bentoml) (1个)

**总计**: 500+个精选命令

## 📁 目录结构

```
cmd4coder/
├── cmd/                # 命令行程序入口
│   ├── cli/            # 主CLI程序
│   └── validator/      # 数据验证工具
├── internal/           # 内部包
│   ├── model/          # 数据模型
│   ├── data/           # 数据加载和索引
│   ├── service/        # 业务逻辑层
│   └── ui/tui/         # TUI用户界面
├── pkg/                # 公共包
│   └── export/         # 导出功能
├── data/               # YAML命令清单数据
│   ├── metadata.yaml   # 元数据
│   ├── os/             # 操作系统命令
│   ├── lang/           # 编程语言工具
│   ├── diagnostic/     # 诊断工具
│   ├── network/        # 网络工具
│   ├── container/      # 容器编排
│   ├── database/       # 数据库工具
│   ├── vcs/            # 版本控制
│   └── build/          # 构建工具
├── docs/               # 文档目录
│   ├── guides/         # 使用指南
│   ├── reference/      # 技术参考
│   ├── architecture/   # 架构文档
│   ├── reports/        # 项目报告
│   ├── css/            # 样式文件
│   ├── js/             # JavaScript文件
│   ├── assets/         # 静态资源
│   └── index.html      # 主页
├── scripts/            # 构建脚本
│   ├── build.sh        # Linux/macOS构建脚本
│   └── build.ps1       # Windows构建脚本
├── coverage_reports/   # 测试覆盖率报告
├── test/               # 集成测试
├── .github/            # GitHub配置
└── .git/               # Git版本控制
```

## 🔧 开发

### 环境要求

- Go 1.24 或更高版本
- Git

### 运行测试

```bash
# 运行所有测试
go test ./...

# 运行测试并查看覆盖率
go test -cover ./...

# 生成覆盖率报告
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out

# 运行竞态检测
go test -race ./...

# 运行性能基准测试
go test -bench=. ./...
```

### 代码质量检查

```bash
# 代码格式化
go fmt ./...

# 代码静态检查
go vet ./...

# 使用golangci-lint（如果已安装）
golangci-lint run
```

### 构建项目

```bash
# 使用构建脚本
./scripts/build.sh     # Linux/macOS
cd scripts && ./build.ps1  # Windows (PowerShell)

# 或者手动构建
go build -o bin/cmd4coder ./cmd/cli

# 如果需要指定模块目录
cd build/config && go build -o ../../bin/cmd4coder ../../cmd/cli
```

### 查看测试覆盖率

```bash
# 生成覆盖率报告
go test -coverprofile=coverage_reports/coverage.out ./...
go tool cover -html=coverage_reports/coverage.out -o coverage_reports/coverage.html

# 查看覆盖率统计
go tool cover -func=coverage_reports/coverage.out
```

### 添加新命令

1. 在对应的 YAML 文件中添加命令定义
2. 确保包含所有必填字段
3. 运行数据验证工具
4. 提交 Pull Request

## 📄 数据格式

命令定义采用 YAML 格式，示例：

```yaml
- name: ls
  category: "操作系统/通用Linux命令"
  install_required: false
  description: "列出目录内容"
  usage:
    - "ls [选项] [文件或目录]"
  options:
    - flag: "-l"
      description: "使用长格式列表"
  examples:
    - command: "ls -la"
      description: "列出所有文件包括隐藏文件"
  platforms:
    - "linux"
    - "darwin"
```

## 🤝 贡献

欢迎贡献！请查看 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) 了解详情。

### 贡献方式

- 🐛 报告 Bug
- 💡 提出新功能建议
- 📝 改进文档
- ➕ 添加新命令
- 🔧 修复问题

### 行为准则

请阅读并遵守 [docs/legal/CODE_OF_CONDUCT.md](docs/legal/CODE_OF_CONDUCT.md) 中的社区准则。

## ❓ 常见问题 (FAQ)

### Q: 如何指定自定义数据目录？

A: 使用 `-d` 或 `--data-dir` 参数：
```bash
go run ./cmd/cli list -d /path/to/data
```

### Q: 如何导出所有命令？

A: 使用 `export-all` 命令：
```bash
# 导出为Markdown
go run ./cmd/cli export-all -f markdown -o commands.md -d ./data

# 导出为JSON
go run ./cmd/cli export-all -f json -o commands.json -d ./data
```

### Q: TUI模式如何关闭？

A: 按 `q` 键退出。

### Q: 如何添加自定义命令？

A: 在 `data/` 目录下创建或编辑YAML文件，遵循现有格式。请参考 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细格式。

### Q: 支持哪些平台？

A: 支持 Linux (amd64/arm64)、macOS (amd64/arm64) 和 Windows (amd64)。

### Q: 命令数据从哪里来？

A: 所有命令数据都经过人工筛选和验证，基于官方文档和最佳实践编写。

### Q: 性能如何？

A: 
- 启动时间: <500ms
- 搜索响应: <100ms
- 内存占用: <50MB
- 使用LRU缓存优化查询性能

## 📝 许可证

本项目采用 MIT 许可证。详见 [docs/legal/LICENSE](docs/legal/LICENSE) 文件。

## 🙏 致谢

感谢所有贡献者和开源社区的支持。

## 📧 联系方式

- 项目主页: https://github.com/cmd4coder/cmd4coder
- 问题反馈: https://github.com/cmd4coder/cmd4coder/issues

---

⭐ 如果这个项目对你有帮助，请给一个 Star！
