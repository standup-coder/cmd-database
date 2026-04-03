# Changelog

All notable changes to cmd4coder project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.5.0] - 2026-04-03

### Added

- Fuzzy search with typo tolerance via sahilm/fuzzy
- Multi-word AND search logic
- TUI proportional layout (20/30/50), viewport scrolling, help overlay
- TUI risk-colored list items, favorite feedback, home screen with recent + favorites
- TUI vim navigation (g/G/Ctrl+u/Ctrl+d), related command navigation
- CLI color output (lipgloss), stdout/stderr separation, `--quiet`/`--no-color` flags
- CLI `--format`/`-f` for output formatting, `--limit`/`--risk`/`--platform` filters
- CLI dynamic shell completion (command names, categories, config keys)
- CLI command grouping (core/export/personal/system), `--version`/`-v` short flag
- "Did you mean?" command suggestion on not-found
- Lazy initialization (version/completion skip data loading)
- Search benchmarks (~37μs/op)
- 6 new data categories: Shell/Bash, CI-CD/GitHub Actions, Rust, AWS CLI, Build tools

### Changed

- Platform naming standardized (macos → darwin)

### Statistics

- 6 new data categories, expanded command coverage

## [1.4.0] - 2026-02-15

### Fixed

- Validator `dataDir` double-prefix bug
- `k8s-cluster.yaml` duplicate etcdctl commands merged
- `svn.yaml` install_subversion typo
- Sscanf silent failure in `configSetCmd`
- Deprecated PodSecurityPolicy replaced with PodSecurity admission labels

### Changed

- `GetConfig`/`GetFavorites` return value copies (prevent external mutation)
- Cache uses `sync.Mutex` (not `RWMutex`) since Get needs write lock
- `ErrDataLoadFailed` supports `Unwrap()` for `errors.Is` traversal
- Platform naming standardized: 84 occurrences macos → darwin across 15 files
- `config_test.go` rewritten to use `t.TempDir()` (NewConfigServiceWithDir)
- 5 new data categories with 19 new commands

### Statistics

- 5 new data categories, 19 new commands, 84 platform name fixes

## [1.3.0] - 2026-01-20

### Added

- `ExportToJSONCompact` CLI entry via `--compact` flag
- `Reload` CLI command for hot-reloading data
- TUI clipboard copy via atotto/clipboard (e key)
- Build tools data files: Maven, Gradle, Make/CMake
- `favoritesCmd` defaults to listing favorites when no subcommand
- `exportAllCmd` `--compact` flag support

### Changed

- Duplicate summary type extracted to package level
- `GetSortedCategories` bubble sort → `sort.Slice`
- Dead code removed (i18n.go, empty validator blocks, duplicate embed.go)

### Statistics

- 4 new build tool data files, algorithm optimization, dead code cleanup

## [1.2.0] - 2026-01-07

### Added

#### 监控工具完整命令集 (17个新增)
- **Prometheus生态** (10个命令):
  - `prometheus` - 启动Prometheus监控服务器
  - `promtool check config` - 验证Prometheus配置文件
  - `promtool query instant` - 执行即时PromQL查询
  - `promtool test rules` - 测试Prometheus告警规则
  - `promtool tsdb analyze` - 分析TSDB数据库
  - `alertmanager` - 启动Prometheus Alertmanager
  - `amtool check-config` - 验证Alertmanager配置
  - `amtool alert query` - 查询活动告警
  - `amtool silence add` - 添加告警静默
  - `node_exporter` - 启动节点指标导出器

- **Grafana** (5个命令):
  - `grafana-server` - 启动Grafana可视化服务器
  - `grafana-cli plugins install` - 安装Grafana插件
  - `grafana-cli plugins list-remote` - 列出可用插件
  - `grafana-cli plugins update` - 更新已安装插件
  - `grafana-cli admin reset-admin-password` - 重置管理员密码

- **OpenTelemetry** (5个新工具):
  - `otelcol` - 启动OpenTelemetry Collector
  - `otelcol validate` - 验证OTel配置文件
  - `otelcol-contrib` - 启动Contrib版Collector
  - `otel-cli span` - 发送Span追踪数据
  - `otel-cli status server` - 检查OTel服务器状态

#### 基础设施自动化完整命令集 (20个新增)

- **Terraform完整工具链** (12个新增):
  - `terraform validate` - 验证配置语法
  - `terraform fmt` - 格式化Terraform代码
  - `terraform state list` - 列出状态资源
  - `terraform state show` - 显示资源详细状态
  - `terraform state rm` - 从状态中移除资源
  - `terraform workspace list` - 列出所有工作区
  - `terraform workspace new` - 创建新工作区
  - `terraform workspace select` - 切换工作区
  - `terraform import` - 导入已有基础设施
  - `terraform taint` - 标记资源待重建
  - `terraform refresh` - 刷新状态与实际基础设施同步

- **Ansible完整工具链** (11个新增):
  - `ansible` - 执行临时命令
  - `ansible-galaxy install` - 安装Ansible角色
  - `ansible-vault encrypt` - 加密敏感文件
  - `ansible-vault decrypt` - 解密Vault文件
  - `ansible-inventory --list` - 显示清单信息
  - `ansible-config dump` - 显示Ansible配置
  - `ansible-doc` - 查看模块文档
  - `ansible-pull` - 从VCS拉取并执行配置
  - `ansible-console` - 交互式Ansible控制台

### Changed

- **数据文件优化**:
  - 清理 `k8s-monitor.yaml` 重复数据 (删除第253-505行重复内容)
  - 清理 `k8s-storage.yaml` 重复数据 (删除第231-461行重复内容)
  - 优化命令数据结构，提升数据质量

- **测试增强**:
  - 新增 `SearchMonitoringTools` 测试用例 - 验证监控工具命令搜索
  - 新增 `VerifyCriticalCommandRisks` 测试用例 - 验证Critical风险标注
  - 新增 `VerifyCommandExamples` 测试用例 - 验证命令示例完整性
  - 新增 `VerifyCategoryCommandCount` 测试用例 - 验证分类命令数量
  - 新增 `VerifyTotalCommandCount` 测试用例 - 验证总命令数量

- **文档更新**:
  - 更新 `README.md` - 命令数量统计 (350+ → 420+)
  - 更新 `TEST_REPORT.md` - 完整v1.2.0测试报告
  - 更新 `data/metadata.yaml` - 版本号和描述信息

### Fixed

- 修复 k8s-monitor.yaml 数据重复问题
- 修复 k8s-storage.yaml YAML格式问题

### Statistics

- **命令总数**: 350+ → 420+ (+37个, 增长10.6%)
- **K8s监控日志分类**: 11个 → 28个 (+154%增长)
- **K8s配置管理分类**: 7个 → 27个 (+286%增长)
- **Kubernetes生态命令**: 128条 → 165条 (+29%增长)
- **新增工具**: OpenTelemetry完整支持
- **命令质量**: 示例平均数 3.0 → 3.3, 风险标注覆盖率 90% → 100%

## [1.1.0] - 2026-01-06

### Added

- Kubernetes生态全栈工具命令集成
- 15个K8s子分类，128个专业命令
- 包含集群管理、运行时、监控、网络、存储等完整工具链
- 机器学习运维工具 (KServe, Kubeflow等)

### Changed

- 项目架构优化
- 测试覆盖率提升至75%

## [1.0.0] - 2025-12-14

### Added

- 初始版本发布
- 220个基础命令
- CLI和TUI双模式交互
- 命令搜索、分类浏览功能
- Markdown和JSON导出功能
- 17个基础分类支持

---

## Version Comparison

| 版本 | 发布日期 | 命令总数 | K8s命令 | 主要特性 |
|------|---------|---------|--------|---------|
| 1.5.0 | 2026-04-03 | — | — | UX Revolution: fuzzy search, TUI overhaul, CLI polish, 6 new categories |
| 1.4.0 | 2026-02-15 | — | — | Quality & Data Hardening: bug fixes, API safety, platform standardization |
| 1.3.0 | 2026-01-20 | — | — | Feature Expansion: compact export, hot-reload, clipboard, build tools |
| 1.2.0 | 2026-01-07 | 420+ | 165 | 监控与IaC工具完整覆盖 |
| 1.1.0 | 2026-01-06 | 350+ | 128 | Kubernetes生态全栈集成 |
| 1.0.0 | 2025-12-14 | 220 | 26 | 基础版本发布 |
