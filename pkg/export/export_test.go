package export

import (
	"encoding/json"
	"os"
	"path/filepath"
	"strings"
	"testing"

	"github.com/cmd4coder/cmd4coder/internal/model"
	"gopkg.in/yaml.v3"
)

func TestExportToMarkdown(t *testing.T) {
	// 创建测试命令
	commands := []*model.Command{
		{
			Name:        "test-cmd",
			Category:    "test",
			Description: "Test command",
			Platforms:   []string{"linux"},
			Usage:       []string{"test-cmd [options]"},
			Options: []model.Option{
				{Flag: "-h", Description: "Show help"},
			},
			Examples: []model.Example{
				{Command: "test-cmd -h", Description: "Show help"},
			},
			Risks: []model.Risk{
				{Level: model.RiskLevelLow, Description: "No risk"},
			},
		},
	}

	// 创建临时目录
	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "test.md")

	// 测试导出
	err := ExportToMarkdown(commands, testFile)
	if err != nil {
		t.Fatalf("ExportToMarkdown() error = %v", err)
	}

	// 验证文件存在
	if _, err := os.Stat(testFile); os.IsNotExist(err) {
		t.Errorf("Output file was not created")
	}

	// 读取文件内容
	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	// 验证内容包含关键信息
	contentStr := string(content)
	expectedStrings := []string{
		"# 命令行工具大全",
		"test-cmd",
		"Test command",
		"linux",
	}

	for _, expected := range expectedStrings {
		if !contains(contentStr, expected) {
			t.Errorf("Output does not contain expected string: %s", expected)
		}
	}
}

func TestExportToJSON(t *testing.T) {
	commands := []*model.Command{
		{
			Name:        "test-cmd",
			Category:    "test",
			Description: "Test command",
			Platforms:   []string{"linux"},
		},
	}

	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "test.json")

	err := ExportToJSON(commands, testFile)
	if err != nil {
		t.Fatalf("ExportToJSON() error = %v", err)
	}

	// 验证文件存在
	if _, err := os.Stat(testFile); os.IsNotExist(err) {
		t.Errorf("Output file was not created")
	}

	// 读取并验证JSON格式
	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	contentStr := string(content)
	if !contains(contentStr, "test-cmd") {
		t.Errorf("JSON output does not contain command name")
	}
	if !contains(contentStr, "version") {
		t.Errorf("JSON output does not contain version field")
	}
}

func TestExportToJSONCompact(t *testing.T) {
	commands := []*model.Command{
		{
			Name:        "test-cmd",
			Category:    "test",
			Description: "Test command",
		},
	}

	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "test-compact.json")

	err := ExportToJSONCompact(commands, testFile)
	if err != nil {
		t.Fatalf("ExportToJSONCompact() error = %v", err)
	}

	// 验证文件存在
	if _, err := os.Stat(testFile); os.IsNotExist(err) {
		t.Errorf("Output file was not created")
	}

	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	// 紧凑格式应该更小（没有缩进）
	if len(content) == 0 {
		t.Errorf("Compact JSON output is empty")
	}
}

func contains(s, substr string) bool {
	return strings.Contains(s, substr)
}

func TestExportToJSONCompact_ValidStructure(t *testing.T) {
	commands := []*model.Command{
		{
			Name:        "cmd1",
			Category:    "cat1",
			Description: "first command",
			Platforms:   []string{"linux"},
		},
		{
			Name:        "cmd2",
			Category:    "cat2",
			Description: "second command",
			Platforms:   []string{"darwin"},
		},
	}

	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "compact.json")

	err := ExportToJSONCompact(commands, testFile)
	if err != nil {
		t.Fatalf("ExportToJSONCompact() error = %v", err)
	}

	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	var parsed []model.Command
	if err := json.Unmarshal(content, &parsed); err != nil {
		t.Fatalf("output is not valid JSON: %v", err)
	}

	if len(parsed) != 2 {
		t.Fatalf("expected 2 commands in parsed JSON, got %d", len(parsed))
	}

	if parsed[0].Name != "cmd1" {
		t.Errorf("expected first command name 'cmd1', got %q", parsed[0].Name)
	}

	if parsed[1].Name != "cmd2" {
		t.Errorf("expected second command name 'cmd2', got %q", parsed[1].Name)
	}
}

func TestExportToJSONCompact_EmptyCommands(t *testing.T) {
	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "empty-compact.json")

	err := ExportToJSONCompact([]*model.Command{}, testFile)
	if err != nil {
		t.Fatalf("ExportToJSONCompact() error = %v", err)
	}

	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	if string(content) != "[]" {
		t.Errorf("expected '[]' for empty commands, got %q", string(content))
	}
}

func TestExportToMarkdown_ContentSections(t *testing.T) {
	commands := []*model.Command{
		{
			Name:        "grep",
			Category:    "text",
			Description: "Search for patterns in text",
			Platforms:   []string{"linux", "darwin", "windows"},
			Usage:       []string{"grep [options] pattern [file]"},
			Options: []model.Option{
				{Flag: "-i", Description: "Ignore case"},
				{Flag: "-r", Description: "Recursive"},
			},
			Examples: []model.Example{
				{Command: "grep -r 'TODO' src/", Description: "Find TODO comments"},
				{Command: "grep -i 'error' log.txt", Description: "Case-insensitive search"},
			},
			Risks: []model.Risk{
				{Level: model.RiskLevelLow, Description: "Safe to use"},
			},
		},
	}

	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "full.md")

	err := ExportToMarkdown(commands, testFile)
	if err != nil {
		t.Fatalf("ExportToMarkdown() error = %v", err)
	}

	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	contentStr := string(content)

	expected := []string{
		"grep",
		"Search for patterns in text",
		"linux, darwin, windows",
		"grep [options] pattern [file]",
		"-i",
		"-r",
		"Ignore case",
		"Recursive",
		"Find TODO comments",
		"grep -r 'TODO' src/",
	}

	for _, s := range expected {
		if !strings.Contains(contentStr, s) {
			t.Errorf("markdown output missing %q", s)
		}
	}
}

func TestExportToMarkdown_MultipleCategories(t *testing.T) {
	commands := []*model.Command{
		{Name: "ls", Category: "os", Description: "list files", Platforms: []string{"linux"}},
		{Name: "cat", Category: "os", Description: "concatenate", Platforms: []string{"linux"}},
		{Name: "git", Category: "vcs", Description: "version control", Platforms: []string{"linux"}},
	}

	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "multi.md")

	err := ExportToMarkdown(commands, testFile)
	if err != nil {
		t.Fatalf("ExportToMarkdown() error = %v", err)
	}

	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	contentStr := string(content)

	if !strings.Contains(contentStr, "## os") {
		t.Error("markdown should have category heading 'os'")
	}
	if !strings.Contains(contentStr, "## vcs") {
		t.Error("markdown should have category heading 'vcs'")
	}
}

func TestExportToJSON_ValidStructure(t *testing.T) {
	commands := []*model.Command{
		{Name: "docker", Category: "containers", Description: "container runtime", Platforms: []string{"linux"}},
	}

	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "structured.json")

	err := ExportToJSON(commands, testFile)
	if err != nil {
		t.Fatalf("ExportToJSON() error = %v", err)
	}

	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	var result struct {
		Version  string          `json:"version"`
		Total    int             `json:"total"`
		Commands []model.Command `json:"commands"`
	}
	if err := json.Unmarshal(content, &result); err != nil {
		t.Fatalf("output is not valid JSON: %v", err)
	}

	if result.Version != "1.8.0" {
		t.Errorf("expected version '1.8.0', got %q", result.Version)
	}
	if result.Total != 1 {
		t.Errorf("expected total 1, got %d", result.Total)
	}
	if len(result.Commands) != 1 || result.Commands[0].Name != "docker" {
		t.Error("expected 1 command named 'docker'")
	}
}

func TestExportToYAML_ValidStructure(t *testing.T) {
	commands := []*model.Command{
		{Name: "git", Category: "vcs", Description: "version control", Platforms: []string{"linux", "darwin"}},
		{Name: "docker", Category: "containers", Description: "container runtime", Platforms: []string{"linux"}},
	}

	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "test.yaml")

	err := ExportToYAML(commands, testFile)
	if err != nil {
		t.Fatalf("ExportToYAML() error = %v", err)
	}

	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	var result struct {
		Version  string          `yaml:"version"`
		Total    int             `yaml:"total"`
		Commands []model.Command `yaml:"commands"`
	}
	if err := yaml.Unmarshal(content, &result); err != nil {
		t.Fatalf("output is not valid YAML: %v", err)
	}

	if result.Version != "1.8.0" {
		t.Errorf("expected version '1.8.0', got %q", result.Version)
	}
	if result.Total != 2 {
		t.Errorf("expected total 2, got %d", result.Total)
	}
	if len(result.Commands) != 2 {
		t.Fatalf("expected 2 commands, got %d", len(result.Commands))
	}
	if result.Commands[0].Name != "git" {
		t.Errorf("expected first command 'git', got %q", result.Commands[0].Name)
	}
	if result.Commands[1].Name != "docker" {
		t.Errorf("expected second command 'docker', got %q", result.Commands[1].Name)
	}

	contentStr := string(content)
	if !strings.Contains(contentStr, "version:") {
		t.Error("YAML output missing 'version:' field")
	}
	if !strings.Contains(contentStr, "total:") {
		t.Error("YAML output missing 'total:' field")
	}
	if !strings.Contains(contentStr, "commands:") {
		t.Error("YAML output missing 'commands:' field")
	}
}

func TestExportToYAML_EmptyCommands(t *testing.T) {
	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "empty.yaml")

	err := ExportToYAML([]*model.Command{}, testFile)
	if err != nil {
		t.Fatalf("ExportToYAML() error = %v", err)
	}

	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	var result struct {
		Version  string          `yaml:"version"`
		Total    int             `yaml:"total"`
		Commands []model.Command `yaml:"commands"`
	}
	if err := yaml.Unmarshal(content, &result); err != nil {
		t.Fatalf("output is not valid YAML: %v", err)
	}

	if result.Total != 0 {
		t.Errorf("expected total 0, got %d", result.Total)
	}
	if len(result.Commands) != 0 {
		t.Errorf("expected empty commands array, got %d", len(result.Commands))
	}
}

func TestExportToYAML_InvalidPath(t *testing.T) {
	commands := []*model.Command{
		{Name: "test", Category: "test", Description: "test", Platforms: []string{"linux"}},
	}

	err := ExportToYAML(commands, "/proc/nonexistent/file.yaml")
	if err == nil {
		t.Fatal("expected error for invalid path, got nil")
	}
}

func TestGetRiskEmoji_AllLevels(t *testing.T) {
	tests := []struct {
		level model.RiskLevel
		want  string
	}{
		{model.RiskLevelLow, "🟢"},
		{model.RiskLevelMedium, "🟡"},
		{model.RiskLevelHigh, "🟠"},
		{model.RiskLevelCritical, "🔴"},
	}

	for _, tt := range tests {
		t.Run(string(tt.level), func(t *testing.T) {
			got := getRiskEmoji(tt.level)
			if got != tt.want {
				t.Errorf("getRiskEmoji(%q) = %q, want %q", tt.level, got, tt.want)
			}
		})
	}
}

func TestGetRiskEmoji_UnknownLevel(t *testing.T) {
	got := getRiskEmoji(model.RiskLevel("unknown"))
	if got != "⚪" {
		t.Errorf("getRiskEmoji(unknown) = %q, want '⚪'", got)
	}
}

func TestExportToMarkdown_AllRiskLevels(t *testing.T) {
	commands := []*model.Command{
		{
			Name:        "low-cmd",
			Category:    "test",
			Description: "low risk",
			Platforms:   []string{"linux"},
			Risks:       []model.Risk{{Level: model.RiskLevelLow, Description: "safe"}},
		},
		{
			Name:        "med-cmd",
			Category:    "test",
			Description: "medium risk",
			Platforms:   []string{"linux"},
			Risks:       []model.Risk{{Level: model.RiskLevelMedium, Description: "caution"}},
		},
		{
			Name:        "high-cmd",
			Category:    "test",
			Description: "high risk",
			Platforms:   []string{"linux"},
			Risks:       []model.Risk{{Level: model.RiskLevelHigh, Description: "danger"}},
		},
		{
			Name:        "crit-cmd",
			Category:    "test",
			Description: "critical risk",
			Platforms:   []string{"linux"},
			Risks:       []model.Risk{{Level: model.RiskLevelCritical, Description: "destructive"}},
		},
	}

	tmpDir := t.TempDir()
	testFile := filepath.Join(tmpDir, "risks.md")

	err := ExportToMarkdown(commands, testFile)
	if err != nil {
		t.Fatalf("ExportToMarkdown() error = %v", err)
	}

	content, err := os.ReadFile(testFile)
	if err != nil {
		t.Fatalf("Failed to read output file: %v", err)
	}

	contentStr := string(content)
	emojis := []string{"🟢", "🟡", "🟠", "🔴"}
	for _, emoji := range emojis {
		if !strings.Contains(contentStr, emoji) {
			t.Errorf("markdown output missing risk emoji %q", emoji)
		}
	}
}

func TestExportToJSON_ErrorPath(t *testing.T) {
	commands := []*model.Command{
		{Name: "test", Category: "test", Description: "test", Platforms: []string{"linux"}},
	}

	err := ExportToJSON(commands, "/proc/nonexistent/file.json")
	if err == nil {
		t.Fatal("expected error for invalid path, got nil")
	}
}
