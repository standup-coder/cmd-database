package export

import (
	"fmt"
	"os"
	"strings"

	"github.com/cmd4coder/cmd4coder/internal/model"
)

// ExportToMarkdown 导出命令到Markdown格式
func ExportToMarkdown(commands []*model.Command, filename string) error {
	if err := ensureDir(filename); err != nil {
		return fmt.Errorf("failed to create directory: %w", err)
	}
	f, err := os.Create(filename)
	if err != nil {
		return fmt.Errorf("failed to create file: %w", err)
	}
	defer f.Close()

	// 写入标题
	fmt.Fprintf(f, "# 命令行工具大全\n\n")
	fmt.Fprintf(f, "总命令数: %d\n\n", len(commands))
	fmt.Fprintf(f, "---\n\n")

	// 按分类分组
	categoryMap := make(map[string][]*model.Command)
	for _, cmd := range commands {
		categoryMap[cmd.Category] = append(categoryMap[cmd.Category], cmd)
	}

	// 遍历分类
	for category, cmds := range categoryMap {
		fmt.Fprintf(f, "## %s\n\n", category)

		for _, cmd := range cmds {
			fmt.Fprintf(f, "### %s\n\n", cmd.Name)
			fmt.Fprintf(f, "**描述**: %s\n\n", cmd.Description)

			// 平台
			fmt.Fprintf(f, "**平台**: %s\n\n", strings.Join(cmd.Platforms, ", "))

			// 使用方式
			if len(cmd.Usage) > 0 {
				fmt.Fprintf(f, "**使用方式**:\n")
				for _, usage := range cmd.Usage {
					fmt.Fprintf(f, "```\n%s\n```\n", usage)
				}
				fmt.Fprintf(f, "\n")
			}

			// 选项
			if len(cmd.Options) > 0 {
				fmt.Fprintf(f, "**常用选项**:\n\n")
				for _, opt := range cmd.Options {
					fmt.Fprintf(f, "- `%s`: %s\n", opt.Flag, opt.Description)
				}
				fmt.Fprintf(f, "\n")
			}

			// 示例
			if len(cmd.Examples) > 0 {
				fmt.Fprintf(f, "**使用示例**:\n\n")
				for i, example := range cmd.Examples {
					fmt.Fprintf(f, "%d. %s\n", i+1, example.Description)
					fmt.Fprintf(f, "   ```bash\n   %s\n   ```\n", example.Command)
					if example.Output != "" {
						fmt.Fprintf(f, "   输出:\n   ```\n   %s\n   ```\n", example.Output)
					}
				}
				fmt.Fprintf(f, "\n")
			}

			// 风险说明
			if len(cmd.Risks) > 0 {
				fmt.Fprintf(f, "**风险说明**:\n\n")
				for _, risk := range cmd.Risks {
					emoji := getRiskEmoji(risk.Level)
					fmt.Fprintf(f, "- %s **[%s]** %s\n", emoji, risk.Level, risk.Description)
				}
				fmt.Fprintf(f, "\n")
			}

			// 安装方法
			if cmd.InstallMethod != "" {
				fmt.Fprintf(f, "**安装方法**: %s\n\n", cmd.InstallMethod)
			}

			fmt.Fprintf(f, "---\n\n")
		}
	}

	return nil
}

func getRiskEmoji(level model.RiskLevel) string {
	switch level {
	case model.RiskLevelLow:
		return "🟢"
	case model.RiskLevelMedium:
		return "🟡"
	case model.RiskLevelHigh:
		return "🟠"
	case model.RiskLevelCritical:
		return "🔴"
	default:
		return "⚪"
	}
}
