package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/cmd4coder/cmd4coder/internal/data"
	"github.com/cmd4coder/cmd4coder/internal/model"
)

// ValidationReport 验证报告
type ValidationReport struct {
	TotalFiles         int
	TotalCommands      int
	SuccessFiles       int
	FailedFiles        int
	Errors             []ValidationError
	Warnings           []ValidationWarning
	CommandsByCategory map[string]int
}

// ValidationError 验证错误
type ValidationError struct {
	File    string
	Command string
	Field   string
	Message string
}

// ValidationWarning 验证警告
type ValidationWarning struct {
	File    string
	Command string
	Message string
}

// validateDataDir 验证指定数据目录，返回验证报告
func validateDataDir(dataDir string) (*ValidationReport, error) {
	loader := data.NewLoader(dataDir)

	metadata, err := loader.LoadMetadata()
	if err != nil {
		return nil, fmt.Errorf("无法加载元数据: %w", err)
	}

	report := &ValidationReport{
		TotalFiles:         len(metadata.DataFiles),
		CommandsByCategory: make(map[string]int),
	}

	commandLocations := make(map[string][]string)

	for _, dataFile := range metadata.DataFiles {
		cmdList, err := loader.LoadCommandList(dataFile)
		if err != nil {
			report.FailedFiles++
			report.Errors = append(report.Errors, ValidationError{
				File:    dataFile,
				Message: err.Error(),
			})
			continue
		}

		if err := cmdList.Validate(); err != nil {
			report.FailedFiles++
			report.Errors = append(report.Errors, ValidationError{
				File:    dataFile,
				Message: err.Error(),
			})
			continue
		}

		report.SuccessFiles++
		report.TotalCommands += len(cmdList.Commands)
		report.CommandsByCategory[cmdList.Category] += len(cmdList.Commands)

		for _, cmd := range cmdList.Commands {
			commandLocations[cmd.Name] = append(commandLocations[cmd.Name], dataFile)
			// install_method 仅在需要单独安装时才强制要求
			if cmd.InstallRequired && cmd.InstallMethod == "" {
				report.Warnings = append(report.Warnings, ValidationWarning{
					File:    dataFile,
					Command: cmd.Name,
					Message: "install_required=true 但缺少 install_method 字段",
				})
			}

			if len(cmd.Examples) < 2 {
				report.Warnings = append(report.Warnings, ValidationWarning{
					File:    dataFile,
					Command: cmd.Name,
					Message: fmt.Sprintf("示例数量较少 (%d)，建议至少2个", len(cmd.Examples)),
				})
			}

			// 风险级别按数值比较，避免字符串字典序误判
			riskValues := map[model.RiskLevel]int{
				model.RiskLevelLow:      1,
				model.RiskLevelMedium:   2,
				model.RiskLevelHigh:     3,
				model.RiskLevelCritical: 4,
			}
			if riskValues[cmd.GetRiskLevel()] >= riskValues[model.RiskLevelHigh] {
				if len(cmd.Risks) < 2 {
					report.Warnings = append(report.Warnings, ValidationWarning{
						File:    dataFile,
						Command: cmd.Name,
						Message: "高风险命令建议提供详细的风险说明",
					})
				}
			}
		}
	}

	// 全局唯一性检查：命令名重复会破坏单一事实来源
	for name, files := range commandLocations {
		if len(files) > 1 {
			report.Errors = append(report.Errors, ValidationError{
				Command: name,
				Message: fmt.Sprintf("命令名重复，出现在多个文件中: %v", files),
			})
		}
	}

	return report, nil
}

// calculateScores 计算验证评分
func calculateScores(report *ValidationReport) (completeness, accuracy, warningRate, overallScore float64) {
	completeness = float64(report.TotalCommands) / 350.0 * 100
	if report.TotalFiles > 0 {
		accuracy = float64(report.SuccessFiles) / float64(report.TotalFiles) * 100
	}
	if report.TotalCommands > 0 {
		warningRate = float64(len(report.Warnings)) / float64(report.TotalCommands) * 100
	}
	overallScore = (accuracy*0.6 + (100-warningRate)*0.2 + completeness*0.2)
	return
}

func main() {
	dataDir := flag.String("d", "./data", "数据目录路径")
	verbose := flag.Bool("v", false, "详细输出")
	flag.Parse()

	fmt.Println("CMD4Coder 数据验证工具")
	fmt.Println("====================")
	fmt.Printf("数据目录: %s\n\n", *dataDir)

	report, err := validateDataDir(*dataDir)
	if err != nil {
		fmt.Printf("❌ %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("✓ 元数据加载成功\n")
	fmt.Printf("  - 数据文件数: %d\n\n", report.TotalFiles)

	fmt.Println("开始验证数据文件...")
	fmt.Println("----------------------------------------")

	for i := 0; i < report.TotalFiles; i++ {
		found := false
		for _, e := range report.Errors {
			if e.File != "" {
				found = true
				break
			}
		}
		_ = found
	}

	// 输出报告
	fmt.Println("\n========================================")
	fmt.Println("验证报告")
	fmt.Println("========================================")
	fmt.Printf("总文件数: %d\n", report.TotalFiles)
	fmt.Printf("成功: %d\n", report.SuccessFiles)
	fmt.Printf("失败: %d\n", report.FailedFiles)
	fmt.Printf("总命令数: %d\n", report.TotalCommands)

	if len(report.Errors) > 0 {
		fmt.Printf("\n❌ 错误 (%d):\n", len(report.Errors))
		for i, e := range report.Errors {
			if i < 20 {
				fmt.Printf("  [%s] %s: %s\n", e.File, e.Command, e.Message)
			}
		}
		if len(report.Errors) > 20 {
			fmt.Printf("  ... 还有 %d 个错误\n", len(report.Errors)-20)
		}
	}

	if len(report.Warnings) > 0 && *verbose {
		fmt.Printf("\n⚠️  警告 (%d):\n", len(report.Warnings))
		for i, w := range report.Warnings {
			if i < 10 {
				fmt.Printf("  [%s] %s: %s\n", w.File, w.Command, w.Message)
			}
		}
		if len(report.Warnings) > 10 {
			fmt.Printf("  ... 还有 %d 个警告\n", len(report.Warnings)-10)
		}
	}

	// 分类统计
	fmt.Println("\n分类统计:")
	fmt.Println("----------------------------------------")
	for category, count := range report.CommandsByCategory {
		fmt.Printf("  %-40s %3d 个命令\n", category, count)
	}

	// 质量评分
	fmt.Println("\n数据质量评分:")
	fmt.Println("----------------------------------------")

	completeness, accuracy, warningRate, overallScore := calculateScores(report)
	fmt.Printf("完整度: %.1f%% (%d/350)\n", completeness, report.TotalCommands)
	fmt.Printf("准确率: %.1f%% (%d/%d 文件通过验证)\n", accuracy, report.SuccessFiles, report.TotalFiles)
	fmt.Printf("警告率: %.1f%% (%d 个警告)\n", warningRate, len(report.Warnings))

	fmt.Printf("\n总体评分: %.1f/100\n", overallScore)

	if overallScore >= 90 {
		fmt.Println("评级: ⭐⭐⭐⭐⭐ 优秀")
	} else if overallScore >= 80 {
		fmt.Println("评级: ⭐⭐⭐⭐ 良好")
	} else if overallScore >= 70 {
		fmt.Println("评级: ⭐⭐⭐ 中等")
	} else {
		fmt.Println("评级: ⭐⭐ 需要改进")
	}

	// 根据结果设置退出码
	if len(report.Errors) > 0 {
		os.Exit(1)
	}
}
