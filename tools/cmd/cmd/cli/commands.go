package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"

	"github.com/charmbracelet/lipgloss"
	"github.com/cmd4coder/cmd4coder/internal/model"
	"github.com/cmd4coder/cmd4coder/pkg/export"
	"github.com/spf13/cobra"
	cobradoc "github.com/spf13/cobra/doc"
	"gopkg.in/yaml.v3"
)

func outputJSON(data interface{}) error {
	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")
	return enc.Encode(data)
}

func outputYAML(data interface{}) error {
	enc := yaml.NewEncoder(os.Stdout)
	defer enc.Close()
	return enc.Encode(data)
}

func emptyResultSlice() []struct{} {
	return []struct{}{}
}

func outputCommandsJSON(commands []*model.Command, includeInstall bool) error {
	if includeInstall {
		out := make([]commandSummaryWithInstall, len(commands))
		for i, c := range commands {
			out[i] = commandSummaryWithInstall{
				Name: c.Name, Risk: string(c.GetRiskLevel()),
				Install: c.InstallRequired, Description: c.Description,
			}
		}
		return outputJSON(out)
	}
	out := make([]commandSummary, len(commands))
	for i, c := range commands {
		out[i] = commandSummary{Name: c.Name, Risk: string(c.GetRiskLevel()), Description: c.Description}
	}
	return outputJSON(out)
}

func outputCommandsYAML(commands []*model.Command, includeInstall bool) error {
	if includeInstall {
		out := make([]commandSummaryWithInstall, len(commands))
		for i, c := range commands {
			out[i] = commandSummaryWithInstall{
				Name: c.Name, Risk: string(c.GetRiskLevel()),
				Install: c.InstallRequired, Description: c.Description,
			}
		}
		return outputYAML(out)
	}
	out := make([]commandSummary, len(commands))
	for i, c := range commands {
		out[i] = commandSummary{Name: c.Name, Risk: string(c.GetRiskLevel()), Description: c.Description}
	}
	return outputYAML(out)
}

var (
	outputFormat   string
	listLimit      int
	listRisk       string
	listPlatform   string
	searchLimit    int
	searchRisk     string
	searchPlatform string
)

type commandSummary struct {
	Name        string `json:"name"`
	Risk        string `json:"risk"`
	Description string `json:"description"`
}

type commandSummaryWithInstall struct {
	Name        string `json:"name"`
	Risk        string `json:"risk"`
	Install     bool   `json:"install_required"`
	Description string `json:"description"`
}

var (
	styleRiskLow      = lipgloss.NewStyle().Foreground(lipgloss.Color("2"))
	styleRiskMedium   = lipgloss.NewStyle().Foreground(lipgloss.Color("3"))
	styleRiskHigh     = lipgloss.NewStyle().Foreground(lipgloss.Color("208"))
	styleRiskCritical = lipgloss.NewStyle().Foreground(lipgloss.Color("1"))
	styleCategory     = lipgloss.NewStyle().Bold(true).Foreground(lipgloss.Color("4"))
	styleBold         = lipgloss.NewStyle().Bold(true)
)

func separator(width int) string {
	return strings.Repeat("─", width)
}

func getTerminalWidth() int {
	if cols := os.Getenv("COLUMNS"); cols != "" {
		var w int
		if _, err := fmt.Sscanf(cols, "%d", &w); err == nil && w > 0 {
			return w
		}
	}
	return 80
}

func getRiskStyle(risk model.RiskLevel) lipgloss.Style {
	switch risk {
	case model.RiskLevelLow:
		return styleRiskLow
	case model.RiskLevelMedium:
		return styleRiskMedium
	case model.RiskLevelHigh:
		return styleRiskHigh
	case model.RiskLevelCritical:
		return styleRiskCritical
	default:
		return lipgloss.NewStyle()
	}
}

func getRiskIndicator(risk model.RiskLevel) string {
	style := getRiskStyle(risk)
	return style.Render(string(risk))
}

func filterCommands(commands []*model.Command, risk, platform string) []*model.Command {
	result := commands
	if risk != "" {
		var filtered []*model.Command
		for _, c := range result {
			if string(c.GetRiskLevel()) == risk {
				filtered = append(filtered, c)
			}
		}
		result = filtered
	}
	if platform != "" {
		var filtered []*model.Command
		for _, c := range result {
			for _, p := range c.Platforms {
				if strings.EqualFold(p, platform) {
					filtered = append(filtered, c)
					break
				}
			}
		}
		result = filtered
	}
	return result
}

func printFooter(msg string) {
	if quiet {
		return
	}
	fmt.Fprintf(os.Stderr, "%s\n", msg)
}

func printMsg(msg string) {
	if quiet {
		return
	}
	fmt.Fprintf(os.Stderr, "%s\n", msg)
}

func completeCommandNames(cmd *cobra.Command, args []string, toComplete string) ([]string, cobra.ShellCompDirective) {
	if cmdService == nil {
		return nil, cobra.ShellCompDirectiveNoFileComp
	}
	names := cmdService.GetAllCommandNames()
	return names, cobra.ShellCompDirectiveNoFileComp
}

func completeCategoryNames(cmd *cobra.Command, args []string, toComplete string) ([]string, cobra.ShellCompDirective) {
	if cmdService == nil {
		return nil, cobra.ShellCompDirectiveNoFileComp
	}
	return cmdService.GetAllCategories(), cobra.ShellCompDirectiveNoFileComp
}

func completeConfigKeys(cmd *cobra.Command, args []string, toComplete string) ([]string, cobra.ShellCompDirective) {
	return []string{"language", "theme", "page_size", "format"}, cobra.ShellCompDirectiveNoFileComp
}

var listCmd = &cobra.Command{
	Use:     "list [category]",
	Short:   "列出命令",
	Long:    `列出指定分类下的所有命令，如果不指定分类则列出所有命令。支持按风险级别和平台过滤。`,
	GroupID: "core",
	Example: `  cmd4coder list
  cmd4coder list "操作系统/Ubuntu系统命令"
  cmd4coder list "编程语言/Java工具链"
  cmd4coder list --risk high
  cmd4coder list --platform linux -n 10`,
	ValidArgsFunction: completeCategoryNames,
	RunE: func(cmd *cobra.Command, args []string) error {
		if listRisk != "" {
			rl := model.RiskLevel(listRisk)
			if !rl.IsValid() {
				return fmt.Errorf("无效的风险级别: %s (有效值: low, medium, high, critical)", listRisk)
			}
		}

		if listPlatform != "" {
			validPlatforms := map[string]bool{"linux": true, "darwin": true, "windows": true, "unix": true}
			if !validPlatforms[listPlatform] {
				return fmt.Errorf("无效的平台: %s (有效值: linux, darwin, windows, unix)", listPlatform)
			}
		}

		var commands []*model.Command
		var title string

		if len(args) == 0 {
			commands = cmdService.GetAllCommands()
			title = "所有命令"
		} else {
			category := args[0]
			commands = cmdService.ListCommandsByCategory(category)
			title = fmt.Sprintf("分类: %s", category)
		}

		commands = filterCommands(commands, listRisk, listPlatform)
		total := len(commands)

		if listLimit > 0 && len(commands) > listLimit {
			commands = commands[:listLimit]
		}

		if len(commands) == 0 {
			if outputFormat == "json" || outputFormat == "yaml" {
				if outputFormat == "json" {
					if err := outputJSON(emptyResultSlice()); err != nil {
						return err
					}
				} else {
					if err := outputYAML(emptyResultSlice()); err != nil {
						return err
					}
				}
				return nil
			}
			fmt.Println("未找到命令")
			return nil
		}

		if outputFormat == "json" {
			return outputCommandsJSON(commands, true)
		}

		if outputFormat == "yaml" {
			return outputCommandsYAML(commands, true)
		}

		w := getTerminalWidth()
		fmt.Fprintf(os.Stderr, "\n%s (共 %d 个命令)\n", styleCategory.Render(title), total)
		fmt.Fprintf(os.Stderr, "%s\n", separator(w))

		for _, c := range commands {
			riskIndicator := getRiskIndicator(c.GetRiskLevel())
			installIndicator := ""
			if c.InstallRequired {
				installIndicator = "[需安装]"
			}

			fmt.Printf("%-20s %s %s %s\n",
				styleBold.Render(c.Name),
				riskIndicator,
				installIndicator,
				c.Description)
		}

		fmt.Fprintln(os.Stderr)
		if listLimit > 0 && total > listLimit {
			fmt.Fprintf(os.Stderr, "显示前 %d 条（共 %d 条），使用 --limit 0 显示全部\n", listLimit, total)
		}
		printFooter("使用 'cmd4coder show <命令名>' 查看详细信息")

		return nil
	},
}

var showCmd = &cobra.Command{
	Use:     "show <command>",
	Short:   "显示命令详细信息",
	Long:    `显示指定命令的完整信息，包括用法、选项、示例、注意事项和风险说明`,
	GroupID: "core",
	Example: `  cmd4coder show ls
  cmd4coder show docker --format json
  cmd4coder show git --format yaml`,
	Args:              cobra.ExactArgs(1),
	ValidArgsFunction: completeCommandNames,
	RunE: func(cmd *cobra.Command, args []string) error {
		cmdName := args[0]
		command, err := cmdService.GetCommand(cmdName)
		if err != nil {
			suggestion := cmdService.SuggestCommand(cmdName)
			if suggestion != "" {
				return fmt.Errorf("命令 '%s' 未找到: %w\n您是否想查找 '%s'？", cmdName, err, suggestion)
			}
			return fmt.Errorf("命令 '%s' 未找到: %w", cmdName, err)
		}

		if outputFormat == "json" {
			if err := outputJSON(command); err != nil {
				return err
			}
			return nil
		}

		if outputFormat == "yaml" {
			if err := outputYAML(command); err != nil {
				return err
			}
			return nil
		}

		printCommandDetail(command)
		return nil
	},
}

var searchCmd = &cobra.Command{
	Use:     "search <query>",
	Short:   "搜索命令",
	Long:    `根据关键词搜索命令，支持模糊匹配和多关键词。支持按风险级别和平台过滤。`,
	GroupID: "core",
	Example: `  cmd4coder search file
  cmd4coder search network
  cmd4coder search "java 诊断"
  cmd4coder search docker --risk critical
  cmd4coder search nginx --platform linux -n 5`,
	Args:              cobra.MinimumNArgs(1),
	ValidArgsFunction: completeCommandNames,
	RunE: func(cmd *cobra.Command, args []string) error {
		if searchRisk != "" {
			rl := model.RiskLevel(searchRisk)
			if !rl.IsValid() {
				return fmt.Errorf("无效的风险级别: %s (有效值: low, medium, high, critical)", searchRisk)
			}
		}

		if searchPlatform != "" {
			validPlatforms := map[string]bool{"linux": true, "darwin": true, "windows": true, "unix": true}
			if !validPlatforms[searchPlatform] {
				return fmt.Errorf("无效的平台: %s (有效值: linux, darwin, windows, unix)", searchPlatform)
			}
		}

		query := strings.Join(args, " ")
		commands := cmdService.SearchCommands(query)

		commands = filterCommands(commands, searchRisk, searchPlatform)
		total := len(commands)

		if searchLimit > 0 && len(commands) > searchLimit {
			commands = commands[:searchLimit]
		}

		if len(commands) == 0 {
			if outputFormat == "json" || outputFormat == "yaml" {
				if outputFormat == "json" {
					if err := outputJSON(emptyResultSlice()); err != nil {
						return err
					}
				} else {
					if err := outputYAML(emptyResultSlice()); err != nil {
						return err
					}
				}
				return nil
			}
			fmt.Printf("未找到与 '%s' 相关的命令\n", query)
			return nil
		}

		if outputFormat == "json" {
			return outputCommandsJSON(commands, false)
		}

		if outputFormat == "yaml" {
			return outputCommandsYAML(commands, false)
		}

		w := getTerminalWidth()
		fmt.Fprintf(os.Stderr, "\n搜索结果: '%s' (共 %d 个命令)\n", query, total)
		fmt.Fprintf(os.Stderr, "%s\n", separator(w))

		for _, command := range commands {
			riskIndicator := getRiskIndicator(command.GetRiskLevel())
			fmt.Printf("%-20s %s %s\n",
				styleBold.Render(command.Name),
				riskIndicator,
				command.Description)
		}

		fmt.Fprintln(os.Stderr)
		if searchLimit > 0 && total > searchLimit {
			fmt.Fprintf(os.Stderr, "显示前 %d 条（共 %d 条），使用 --limit 0 显示全部\n", searchLimit, total)
		}
		printFooter("使用 'cmd4coder show <命令名>' 查看详细信息")

		return nil
	},
}

var categoriesCmd = &cobra.Command{
	Use:     "categories",
	Short:   "列出所有分类",
	Long:    `显示所有可用的命令分类及其包含的命令数量。可以使用分类名作为 list 子命令的参数来查看该分类下的所有命令。`,
	GroupID: "core",
	Example: `  cmd4coder categories
  cmd4coder categories --format json
  cmd4coder list "操作系统/Ubuntu系统命令"`,
	RunE: func(cmd *cobra.Command, args []string) error {
		categories := cmdService.GetAllCategories()

		type categoryInfo struct {
			Name         string `json:"name" yaml:"name"`
			CommandCount int    `json:"command_count" yaml:"command_count"`
		}

		if outputFormat == "json" {
			out := make([]categoryInfo, len(categories))
			for i, cat := range categories {
				commands := cmdService.ListCommandsByCategory(cat)
				out[i] = categoryInfo{Name: cat, CommandCount: len(commands)}
			}
			return outputJSON(out)
		}

		if outputFormat == "yaml" {
			out := make([]categoryInfo, len(categories))
			for i, cat := range categories {
				commands := cmdService.ListCommandsByCategory(cat)
				out[i] = categoryInfo{Name: cat, CommandCount: len(commands)}
			}
			return outputYAML(out)
		}

		w := getTerminalWidth()
		fmt.Fprintf(os.Stderr, "\n所有分类 (共 %d 个)\n", len(categories))
		fmt.Fprintf(os.Stderr, "%s\n", separator(w))

		for _, category := range categories {
			commands := cmdService.ListCommandsByCategory(category)
			fmt.Printf("%-40s (%d 个命令)\n", styleCategory.Render(category), len(commands))
		}

		fmt.Fprintln(os.Stderr)
		printFooter("使用 'cmd4coder list <分类名>' 查看分类下的命令")

		return nil
	},
}

var versionCmd = &cobra.Command{
	Use:     "version",
	Short:   "显示版本信息",
	GroupID: "system",
	Example: `  cmd4coder version
  cmd4coder -v`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Printf("cmd4coder version %s\n", Version)
		fmt.Printf("Build time: %s\n", BuildTime)
		fmt.Printf("Commit: %s\n", CommitHash)

		if cmdService != nil {
			metadata := cmdService.GetMetadata()
			if metadata != nil {
				fmt.Printf("Data version: %s\n", metadata.Version)
				fmt.Printf("Data updated: %s\n", metadata.UpdatedAt)
			}
			fmt.Printf("Total commands: %d\n", cmdService.GetCommandCount())
			fmt.Printf("Total categories: %d\n", cmdService.GetCategoryCount())
		}
	},
}

var (
	exportFormat      string
	exportOutput      string
	exportCompact     bool
	exportStdout      bool
	exportAllRisk     string
	exportAllPlatform string
)

var exportCmd = &cobra.Command{
	Use:     "export <command>",
	Short:   "导出单个命令到文件",
	Long:    `将指定命令导出为 Markdown、JSON 或 YAML 格式文件`,
	GroupID: "export",
	Example: `  cmd4coder export ls -f markdown -o ls.md
  cmd4coder export docker -f json -o docker.json
  cmd4coder export docker -f yaml -o docker.yaml`,
	Args:              cobra.ExactArgs(1),
	ValidArgsFunction: completeCommandNames,
	RunE: func(cmd *cobra.Command, args []string) error {
		cmdName := args[0]
		command, err := cmdService.GetCommand(cmdName)
		if err != nil {
			return fmt.Errorf("命令 '%s' 未找到: %w", cmdName, err)
		}

		if exportStdout {
			switch exportFormat {
			case "yaml":
				if err := outputYAML(command); err != nil {
					return err
				}
			case "markdown":
				printCommandDetail(command)
			default:
				if err := outputJSON(command); err != nil {
					return err
				}
			}
			printMsg(fmt.Sprintf("已导出命令 '%s' 到 stdout", cmdName))
			return nil
		}

		if exportOutput == "" {
			exportOutput = cmdName + "." + exportFormat
		}

		commands := []*model.Command{command}
		if exportCompact {
			err = export.ExportToJSONCompact(commands, exportOutput)
		} else {
			switch exportFormat {
			case "markdown":
				err = export.ExportToMarkdown(commands, exportOutput)
			case "json":
				err = export.ExportToJSON(commands, exportOutput)
			case "yaml":
				err = export.ExportToYAML(commands, exportOutput)
			default:
				return fmt.Errorf("不支持的格式: %s（支持 markdown/json/yaml）", exportFormat)
			}
		}

		if err != nil {
			return fmt.Errorf("导出失败: %w", err)
		}

		printMsg(fmt.Sprintf("已导出命令 '%s' 到 %s", cmdName, exportOutput))
		return nil
	},
}

var exportAllCmd = &cobra.Command{
	Use:     "export-all",
	Short:   "导出所有命令到文件",
	Long:    `将所有命令导出为 Markdown、JSON 或 YAML 格式文件`,
	GroupID: "export",
	Example: `  cmd4coder export-all -f markdown -o commands.md
  cmd4coder export-all -f json -o commands.json
  cmd4coder export-all -f yaml -o commands.yaml`,
	RunE: func(cmd *cobra.Command, args []string) error {
		commands := cmdService.GetAllCommands()
		commands = filterCommands(commands, exportAllRisk, exportAllPlatform)

		if exportStdout {
			switch exportFormat {
			case "yaml":
				if err := outputYAML(commands); err != nil {
					return err
				}
			case "markdown":
				for _, c := range commands {
					printCommandDetail(c)
				}
			default:
				if err := outputJSON(commands); err != nil {
					return err
				}
			}
			printMsg(fmt.Sprintf("已导出 %d 个命令到 stdout", len(commands)))
			return nil
		}

		if exportOutput == "" {
			exportOutput = "commands." + exportFormat
		}

		if exportCompact {
			err := export.ExportToJSONCompact(commands, exportOutput)
			if err != nil {
				return fmt.Errorf("导出失败: %w", err)
			}
		} else {
			switch exportFormat {
			case "markdown":
				err := export.ExportToMarkdown(commands, exportOutput)
				if err != nil {
					return fmt.Errorf("导出失败: %w", err)
				}
			case "json":
				err := export.ExportToJSON(commands, exportOutput)
				if err != nil {
					return fmt.Errorf("导出失败: %w", err)
				}
			case "yaml":
				err := export.ExportToYAML(commands, exportOutput)
				if err != nil {
					return fmt.Errorf("导出失败: %w", err)
				}
			default:
				return fmt.Errorf("不支持的格式: %s（支持 markdown/json/yaml）", exportFormat)
			}
		}

		printMsg(fmt.Sprintf("已导出 %d 个命令到 %s", len(commands), exportOutput))
		return nil
	},
}

var manCmd = &cobra.Command{
	Use:     "man",
	Short:   "生成 man page",
	Long:    `生成 cmd4coder 的 man page 到指定目录`,
	GroupID: "system",
	Example: `  cmd4coder man
  cmd4coder man -o /usr/local/share/man/man1`,
	Args: cobra.NoArgs,
	RunE: func(cmd *cobra.Command, args []string) error {
		manDir := "man"
		if o, err := cmd.Flags().GetString("output"); err == nil && o != "" {
			manDir = o
		}
		if err := os.MkdirAll(manDir, 0755); err != nil {
			return err
		}
		return cobradoc.GenManTree(rootCmd, &cobradoc.GenManHeader{
			Title:   "CMD4CODER",
			Section: "1",
		}, manDir)
	},
}

var completionCmd = &cobra.Command{
	Use:     "completion [bash|zsh|fish|powershell]",
	Short:   "生成 shell 自动补全脚本",
	Long:    `生成指定 shell 的自动补全脚本，支持 bash、zsh、fish 和 powershell`,
	GroupID: "system",
	Example: `  cmd4coder completion bash > /etc/bash_completion.d/cmd4coder
  cmd4coder completion zsh > "${fpath[1]}/_cmd4coder"
  cmd4coder completion fish > ~/.config/fish/completions/cmd4coder.fish`,
	Args:      cobra.ExactArgs(1),
	ValidArgs: []string{"bash", "zsh", "fish", "powershell"},
	RunE: func(cmd *cobra.Command, args []string) error {
		switch args[0] {
		case "bash":
			return rootCmd.GenBashCompletion(os.Stdout)
		case "zsh":
			return rootCmd.GenZshCompletion(os.Stdout)
		case "fish":
			return rootCmd.GenFishCompletion(os.Stdout, true)
		case "powershell":
			return rootCmd.GenPowerShellCompletionWithDesc(os.Stdout)
		}
		return nil
	},
}

var favoritesCmd = &cobra.Command{
	Use:     "favorites",
	Short:   "管理收藏的命令",
	Long:    `管理个人收藏的命令。可以将常用命令添加到收藏夹以便快速访问，支持为每个收藏添加备注。`,
	GroupID: "personal",
	Example: `  cmd4coder favorites
  cmd4coder favorites add docker "容器管理工具"
  cmd4coder favorites list
  cmd4coder favorites remove docker`,
	RunE: func(cmd *cobra.Command, args []string) error {
		if cfgService == nil {
			return fmt.Errorf("配置服务未初始化")
		}
		favorites := cfgService.GetFavorites()
		if len(favorites) == 0 {
			fmt.Println("暂无收藏命令")
			return nil
		}
		fmt.Fprintf(os.Stderr, "收藏命令 (共 %d 个):\n", len(favorites))
		fmt.Fprintf(os.Stderr, "%s\n", separator(60))
		for _, fav := range favorites {
			fmt.Printf("  %-25s %s\n", styleBold.Render(fav.CommandName), fav.Category)
		}
		return nil
	},
}

var favListCmd = &cobra.Command{
	Use:     "list",
	Short:   "列出所有收藏",
	Example: `  cmd4coder favorites list`,
	RunE: func(cmd *cobra.Command, args []string) error {
		if cfgService == nil {
			return fmt.Errorf("配置服务未初始化")
		}
		favorites := cfgService.GetFavorites()
		if len(favorites) == 0 {
			fmt.Println("暂无收藏")
			return nil
		}

		w := getTerminalWidth()
		fmt.Fprintf(os.Stderr, "\n收藏列表 (共 %d 个)\n", len(favorites))
		fmt.Fprintf(os.Stderr, "%s\n", separator(w))
		for _, fav := range favorites {
			note := ""
			if fav.Note != "" {
				note = fmt.Sprintf(" - %s", fav.Note)
			}
			fmt.Printf("  %-20s [%s]%s\n", styleBold.Render(fav.CommandName), fav.Category, note)
		}
		return nil
	},
}

var favAddCmd = &cobra.Command{
	Use:   "add <command> [note]",
	Short: "添加收藏",
	Example: `  cmd4coder favorites add docker
  cmd4coder favorites add git "版本控制"`,
	Args: cobra.MinimumNArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		if cfgService == nil {
			return fmt.Errorf("配置服务未初始化")
		}
		cmdName := args[0]
		note := ""
		if len(args) > 1 {
			note = strings.Join(args[1:], " ")
		}

		command, err := cmdService.GetCommand(cmdName)
		if err != nil {
			return fmt.Errorf("命令 '%s' 未找到: %w", cmdName, err)
		}

		if err := cfgService.AddFavorite(command.Name, command.Category, note); err != nil {
			return fmt.Errorf("添加收藏失败: %w", err)
		}
		printMsg(fmt.Sprintf("已收藏: %s", command.Name))
		return nil
	},
}

var favRemoveCmd = &cobra.Command{
	Use:     "remove <command>",
	Short:   "删除收藏",
	Example: `  cmd4coder favorites remove docker`,
	Args:    cobra.ExactArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		if cfgService == nil {
			return fmt.Errorf("配置服务未初始化")
		}
		cmdName := args[0]
		if err := cfgService.RemoveFavorite(cmdName); err != nil {
			return fmt.Errorf("删除收藏失败: %w", err)
		}
		printMsg(fmt.Sprintf("已取消收藏: %s", cmdName))
		return nil
	},
}

var historyCmd = &cobra.Command{
	Use:     "history",
	Short:   "查看命令访问历史",
	Long:    `查看最近访问的命令历史记录，按时间倒序排列`,
	GroupID: "personal",
	Example: `  cmd4coder history
  cmd4coder history clear`,
	RunE: func(cmd *cobra.Command, args []string) error {
		if cfgService == nil {
			return fmt.Errorf("配置服务未初始化")
		}
		entries := cfgService.GetRecentHistory(20)
		if len(entries) == 0 {
			fmt.Println("暂无历史记录")
			return nil
		}

		w := getTerminalWidth()
		fmt.Fprintf(os.Stderr, "\n最近访问 (共 %d 条)\n", len(entries))
		fmt.Fprintf(os.Stderr, "%s\n", separator(w))
		for i, entry := range entries {
			fmt.Printf("  %2d. %-20s [%s] %s\n",
				i+1,
				styleBold.Render(entry.CommandName),
				entry.Category,
				entry.AccessedAt.Format("01-02 15:04"))
		}
		return nil
	},
}

var historyClearCmd = &cobra.Command{
	Use:     "clear",
	Short:   "清空历史记录",
	Example: `  cmd4coder history clear`,
	RunE: func(cmd *cobra.Command, args []string) error {
		if cfgService == nil {
			return fmt.Errorf("配置服务未初始化")
		}
		if err := cfgService.ClearHistory(); err != nil {
			return fmt.Errorf("清空历史失败: %w", err)
		}
		printMsg("历史记录已清空")
		return nil
	},
}

var configCmd = &cobra.Command{
	Use:     "config",
	Short:   "查看和管理配置",
	Long:    `查看和修改应用程序配置，包括语言、主题、每页数量和默认导出格式。配置变更会持久化到本地配置文件。`,
	GroupID: "personal",
	Example: `  cmd4coder config show
  cmd4coder config set theme dark
  cmd4coder config set page_size 50`,
}

var configShowCmd = &cobra.Command{
	Use:     "show",
	Short:   "显示当前配置",
	Example: `  cmd4coder config show`,
	RunE: func(cmd *cobra.Command, args []string) error {
		if cfgService == nil {
			return fmt.Errorf("配置服务未初始化")
		}
		config := cfgService.GetConfig()
		fmt.Printf("语言: %s\n", config.Language)
		fmt.Printf("主题: %s\n", config.Theme)
		fmt.Printf("每页数量: %d\n", config.PageSize)
		fmt.Printf("默认导出格式: %s\n", config.Export.DefaultFormat)
		fmt.Printf("搜索最大结果: %d\n", config.Search.MaxResults)
		fmt.Printf("TUI: %v\n", config.TUI.Enabled)
		return nil
	},
}

var reloadCmd = &cobra.Command{
	Use:     "reload",
	Short:   "重新加载数据",
	Long:    `从数据目录重新加载所有命令数据，刷新缓存`,
	GroupID: "system",
	Example: `  cmd4coder reload`,
	RunE: func(cmd *cobra.Command, args []string) error {
		if err := cmdService.Reload(); err != nil {
			return fmt.Errorf("重新加载失败: %w", err)
		}
		printMsg("数据已重新加载")
		printMsg(fmt.Sprintf("命令数: %d", cmdService.GetCommandCount()))
		printMsg(fmt.Sprintf("分类数: %d", cmdService.GetCategoryCount()))
		return nil
	},
}

var configSetCmd = &cobra.Command{
	Use:               "set <key> <value>",
	Short:             "设置配置项",
	Example:           `  cmd4coder config set language zh\n  cmd4coder config set theme dark\n  cmd4coder config set page_size 50\n  cmd4coder config set format json`,
	Args:              cobra.ExactArgs(2),
	ValidArgsFunction: completeConfigKeys,
	RunE: func(cmd *cobra.Command, args []string) error {
		if cfgService == nil {
			return fmt.Errorf("配置服务未初始化")
		}
		key := args[0]
		value := args[1]

		switch key {
		case "language":
			return cfgService.SetLanguage(value)
		case "theme":
			return cfgService.SetTheme(value)
		case "page_size":
			size := 20
			if n, _ := fmt.Sscanf(value, "%d", &size); n != 1 {
				return fmt.Errorf("无效的 page_size 值: %s（必须是正整数）", value)
			}
			return cfgService.SetPageSize(size)
		case "format":
			return cfgService.SetDefaultExportFormat(value)
		default:
			return fmt.Errorf("未知配置项: %s（支持 language/theme/page_size/format）", key)
		}
	},
}

func init() {
	listCmd.Flags().StringVarP(&outputFormat, "format", "f", "", "输出格式 (json/yaml)")
	listCmd.Flags().IntVarP(&listLimit, "limit", "n", 0, "显示数量限制 (0 显示全部)")
	listCmd.Flags().StringVar(&listRisk, "risk", "", "按风险级别过滤 (low/medium/high/critical)")
	listCmd.Flags().StringVar(&listPlatform, "platform", "", "按平台过滤 (linux/darwin/windows)")

	showCmd.Flags().StringVarP(&outputFormat, "format", "f", "", "输出格式 (json/yaml)")

	categoriesCmd.Flags().StringVarP(&outputFormat, "format", "f", "", "输出格式 (json/yaml)")

	searchCmd.Flags().StringVarP(&outputFormat, "format", "f", "", "输出格式 (json/yaml)")
	searchCmd.Flags().IntVarP(&searchLimit, "limit", "n", 0, "显示数量限制 (0 显示全部)")
	searchCmd.Flags().StringVar(&searchRisk, "risk", "", "按风险级别过滤 (low/medium/high/critical)")
	searchCmd.Flags().StringVar(&searchPlatform, "platform", "", "按平台过滤 (linux/darwin/windows)")

	exportCmd.Flags().StringVarP(&exportFormat, "format", "f", "markdown", "导出格式 (markdown/json/yaml)")
	exportCmd.Flags().StringVarP(&exportOutput, "output", "o", "", "输出文件路径")
	exportCmd.Flags().BoolVar(&exportCompact, "compact", false, "JSON 紧凑输出")
	exportCmd.Flags().BoolVar(&exportStdout, "stdout", false, "输出到 stdout 而非文件（用于管道）")
	exportAllCmd.Flags().StringVarP(&exportFormat, "format", "f", "markdown", "导出格式 (markdown/json/yaml)")
	exportAllCmd.Flags().StringVarP(&exportOutput, "output", "o", "", "输出文件路径")
	exportAllCmd.Flags().BoolVar(&exportCompact, "compact", false, "JSON 紧凑输出")
	exportAllCmd.Flags().BoolVar(&exportStdout, "stdout", false, "输出到 stdout 而非文件（用于管道）")
	exportAllCmd.Flags().StringVar(&exportAllRisk, "risk", "", "按风险级别过滤 (low/medium/high/critical)")
	exportAllCmd.Flags().StringVar(&exportAllPlatform, "platform", "", "按平台过滤 (linux/darwin/windows)")

	manCmd.Flags().StringP("output", "o", "man", "man page 输出目录")

	favoritesCmd.AddCommand(favListCmd)
	favoritesCmd.AddCommand(favAddCmd)
	favoritesCmd.AddCommand(favRemoveCmd)

	historyCmd.AddCommand(historyClearCmd)

	configCmd.AddCommand(configShowCmd)
	configCmd.AddCommand(configSetCmd)
}

func printCommandDetail(cmd *model.Command) {
	w := getTerminalWidth()

	fmt.Fprintf(os.Stderr, "\n命令: %s\n", styleBold.Render(cmd.Name))
	fmt.Fprintf(os.Stderr, "%s\n", separator(w))

	fmt.Fprintf(os.Stderr, "\n描述:\n  %s\n", cmd.Description)
	fmt.Fprintf(os.Stderr, "\n分类: %s\n", styleCategory.Render(cmd.Category))
	fmt.Fprintf(os.Stderr, "平台: %s\n", strings.Join(cmd.Platforms, ", "))

	if cmd.InstallRequired {
		fmt.Fprintf(os.Stderr, "\n安装方式:\n  %s\n", cmd.InstallMethod)
	}

	fmt.Fprintf(os.Stderr, "\n使用方式:\n")
	for _, usage := range cmd.Usage {
		fmt.Fprintf(os.Stderr, "  %s\n", usage)
	}

	if len(cmd.Options) > 0 {
		fmt.Fprintf(os.Stderr, "\n常用选项:\n")
		for _, opt := range cmd.Options {
			fmt.Fprintf(os.Stderr, "  %-20s %s\n", opt.Flag, opt.Description)
		}
	}

	if len(cmd.Examples) > 0 {
		fmt.Fprintf(os.Stderr, "\n使用示例:\n")
		for i, example := range cmd.Examples {
			fmt.Fprintf(os.Stderr, "\n  示例 %d: %s\n", i+1, example.Description)
			fmt.Fprintf(os.Stderr, "  $ %s\n", example.Command)
			if example.Output != "" {
				fmt.Fprintf(os.Stderr, "  输出: %s\n", example.Output)
			}
		}
	}

	if len(cmd.Notes) > 0 {
		fmt.Fprintf(os.Stderr, "\n注意事项:\n")
		for _, note := range cmd.Notes {
			fmt.Fprintf(os.Stderr, "  • %s\n", note)
		}
	}

	if len(cmd.Risks) > 0 {
		fmt.Fprintf(os.Stderr, "\n风险说明:\n")
		for _, risk := range cmd.Risks {
			indicator := getRiskIndicator(risk.Level)
			fmt.Fprintf(os.Stderr, "  %s [%s] %s\n", indicator, risk.Level, risk.Description)
		}
	}

	if len(cmd.RelatedCommands) > 0 {
		fmt.Fprintf(os.Stderr, "\n相关命令: %s\n", strings.Join(cmd.RelatedCommands, ", "))
	}

	if len(cmd.References) > 0 {
		fmt.Fprintf(os.Stderr, "\n参考链接:\n")
		for _, ref := range cmd.References {
			fmt.Fprintf(os.Stderr, "  %s\n", ref)
		}
	}

	fmt.Fprintln(os.Stderr)
}
