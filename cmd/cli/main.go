package main

import (
	"fmt"
	"os"

	"github.com/charmbracelet/lipgloss"
	"github.com/cmd4coder/cmd4coder/internal/service"
	"github.com/cmd4coder/cmd4coder/internal/ui/tui"
	"github.com/cmd4coder/cmd4coder/internal/version"
	"github.com/muesli/termenv"
	"github.com/spf13/cobra"
)

var (
	Version    = version.Version
	BuildTime  = "unknown"
	CommitHash = "unknown"

	cmdService *service.CommandService
	cfgService *service.ConfigService
	dataDir    string

	quiet         bool
	noColor       bool
	showedVersion bool
)

func main() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}
}

func needsData(cmd *cobra.Command) bool {
	for ; cmd != nil; cmd = cmd.Parent() {
		switch cmd.Use {
		case "version", "completion", "man":
			return false
		}
	}
	return true
}

var rootCmd = &cobra.Command{
	Use:   "cmd4coder",
	Short: "命令行工具大全 - 面向运维和开发者的命令行参考工具",
	Long: `cmd4coder 是一个简单优雅的命令行工具大全。

它提供了完整的命令清单，包括：
  - Linux 命令（Ubuntu/CentOS/通用）
  - 编程语言工具链（Java/Go/Python/Node.js等）
  - 诊断工具（Arthas/tsar等）
  - 网络工具（dig/curl/tcpdump等）
  - 容器编排（Docker/Kubernetes）
  - 数据库工具（MySQL/Redis/PostgreSQL）
  - 版本控制（Git/SVN）
  - 构建工具（Maven/Gradle/Make）

支持两种使用模式：
  1. CLI模式：通过命令行参数快速查询
  2. TUI模式：交互式文本界面浏览

更多信息请访问: https://github.com/cmd4coder/cmd4coder`,
	PersistentPreRunE: func(cmd *cobra.Command, args []string) error {
		showVersion, _ := cmd.Flags().GetBool("version")
		if showVersion {
			fmt.Printf("cmd4coder version %s\n", Version)
			fmt.Printf("Build time: %s\n", BuildTime)
			fmt.Printf("Commit: %s\n", CommitHash)
			cmd.SilenceUsage = true
			cmd.SilenceErrors = true
			showedVersion = true
			return nil
		}

		if noColor {
			lipgloss.SetColorProfile(termenv.Ascii)
		}

		if !needsData(cmd) {
			return nil
		}

		var err error
		cmdService, err = service.NewCommandService(dataDir)
		if err != nil {
			return fmt.Errorf("failed to initialize command service: %w", err)
		}

		var cfgErr error
		cfgService, cfgErr = service.NewConfigService()
		if cfgErr != nil {
			fmt.Fprintf(os.Stderr, "Warning: config init failed: %v\n", cfgErr)
		}

		return nil
	},
	Run: func(cmd *cobra.Command, args []string) {
		if showedVersion {
			return
		}
		if err := tui.Run(cmdService, cfgService); err != nil {
			fmt.Fprintf(os.Stderr, "TUI错误: %v\n", err)
			os.Exit(1)
		}
	},
}

func init() {
	rootCmd.PersistentFlags().StringVarP(&dataDir, "data-dir", "d", "", "数据目录路径（默认使用嵌入数据）")
	rootCmd.Flags().BoolP("version", "v", false, "显示版本信息")
	rootCmd.PersistentFlags().BoolVarP(&quiet, "quiet", "q", false, "静默模式，仅输出错误信息")
	rootCmd.PersistentFlags().BoolVar(&noColor, "no-color", false, "禁用颜色输出")

	rootCmd.AddGroup(&cobra.Group{ID: "core", Title: "Core Commands:"})
	rootCmd.AddGroup(&cobra.Group{ID: "export", Title: "Export Commands:"})
	rootCmd.AddGroup(&cobra.Group{ID: "personal", Title: "Personal Commands:"})
	rootCmd.AddGroup(&cobra.Group{ID: "system", Title: "System Commands:"})

	rootCmd.AddCommand(listCmd)
	rootCmd.AddCommand(showCmd)
	rootCmd.AddCommand(searchCmd)
	rootCmd.AddCommand(categoriesCmd)
	rootCmd.AddCommand(versionCmd)
	rootCmd.AddCommand(exportCmd)
	rootCmd.AddCommand(exportAllCmd)
	rootCmd.AddCommand(completionCmd)
	rootCmd.AddCommand(favoritesCmd)
	rootCmd.AddCommand(historyCmd)
	rootCmd.AddCommand(configCmd)
	rootCmd.AddCommand(reloadCmd)
	rootCmd.AddCommand(manCmd)
}
