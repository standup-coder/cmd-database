package main

import (
	"io"
	"os"
	"strings"
	"testing"
	"unicode/utf8"

	"github.com/cmd4coder/cmd4coder/internal/model"
	"github.com/cmd4coder/cmd4coder/internal/service"
)

func TestEmptyResultSlice(t *testing.T) {
	result := emptyResultSlice()

	if result == nil {
		t.Fatal("expected non-nil slice")
	}
	if len(result) != 0 {
		t.Fatalf("expected length 0, got %d", len(result))
	}
	if cap(result) != 0 {
		t.Fatalf("expected capacity 0, got %d", cap(result))
	}
}

func TestSeparator(t *testing.T) {
	tests := []struct {
		name  string
		width int
		want  int
	}{
		{"zero", 0, 0},
		{"ten", 10, 10},
		{"eighty", 80, 80},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := separator(tt.width)
			if utf8.RuneCountInString(got) != tt.want {
				t.Fatalf("expected length %d, got %d", tt.want, utf8.RuneCountInString(got))
			}
			if got != strings.Repeat("─", tt.width) {
				t.Fatalf("expected all '─' characters")
			}
		})
	}
}

func TestFilterCommands_NilInput(t *testing.T) {
	result := filterCommands(nil, "high", "linux")
	if result != nil {
		t.Fatalf("expected nil, got %v", result)
	}
}

func TestFilterCommands_EmptyInput(t *testing.T) {
	result := filterCommands([]*model.Command{}, "high", "linux")
	if len(result) != 0 {
		t.Fatalf("expected empty slice, got %d", len(result))
	}
}

func TestFilterCommands_NoFilters(t *testing.T) {
	cmds := []*model.Command{
		{Name: "a", Risks: []model.Risk{{Level: model.RiskLevelLow}}, Platforms: []string{"linux"}},
		{Name: "b", Risks: []model.Risk{{Level: model.RiskLevelHigh}}, Platforms: []string{"darwin"}},
	}
	result := filterCommands(cmds, "", "")
	if len(result) != 2 {
		t.Fatalf("expected 2 commands, got %d", len(result))
	}
}

func TestFilterCommands_ByRisk(t *testing.T) {
	cmds := []*model.Command{
		{Name: "a", Risks: []model.Risk{{Level: model.RiskLevelLow}}, Platforms: []string{"linux"}},
		{Name: "b", Risks: []model.Risk{{Level: model.RiskLevelHigh}}, Platforms: []string{"linux"}},
		{Name: "c", Risks: []model.Risk{{Level: model.RiskLevelHigh}}, Platforms: []string{"darwin"}},
	}
	result := filterCommands(cmds, "high", "")
	if len(result) != 2 {
		t.Fatalf("expected 2 commands, got %d", len(result))
	}
	for _, c := range result {
		if c.Name != "b" && c.Name != "c" {
			t.Fatalf("unexpected command %q in filtered result", c.Name)
		}
	}
}

func TestFilterCommands_ByPlatform(t *testing.T) {
	cmds := []*model.Command{
		{Name: "a", Risks: []model.Risk{{Level: model.RiskLevelLow}}, Platforms: []string{"linux"}},
		{Name: "b", Risks: []model.Risk{{Level: model.RiskLevelLow}}, Platforms: []string{"darwin"}},
		{Name: "c", Risks: []model.Risk{{Level: model.RiskLevelLow}}, Platforms: []string{"linux", "darwin"}},
	}
	result := filterCommands(cmds, "", "linux")
	if len(result) != 2 {
		t.Fatalf("expected 2 commands, got %d", len(result))
	}
	for _, c := range result {
		if c.Name != "a" && c.Name != "c" {
			t.Fatalf("unexpected command %q in filtered result", c.Name)
		}
	}
}

func TestFilterCommands_ByRiskAndPlatform(t *testing.T) {
	cmds := []*model.Command{
		{Name: "a", Risks: []model.Risk{{Level: model.RiskLevelLow}}, Platforms: []string{"linux"}},
		{Name: "b", Risks: []model.Risk{{Level: model.RiskLevelHigh}}, Platforms: []string{"linux"}},
		{Name: "c", Risks: []model.Risk{{Level: model.RiskLevelHigh}}, Platforms: []string{"darwin"}},
		{Name: "d", Risks: []model.Risk{{Level: model.RiskLevelLow}}, Platforms: []string{"linux", "darwin"}},
	}
	result := filterCommands(cmds, "high", "linux")
	if len(result) != 1 {
		t.Fatalf("expected 1 command, got %d", len(result))
	}
	if result[0].Name != "b" {
		t.Fatalf("expected command 'b', got %q", result[0].Name)
	}
}

func TestFilterCommands_NoMatch(t *testing.T) {
	cmds := []*model.Command{
		{Name: "a", Risks: []model.Risk{{Level: model.RiskLevelLow}}, Platforms: []string{"linux"}},
	}
	result := filterCommands(cmds, "critical", "windows")
	if len(result) != 0 {
		t.Fatalf("expected 0 commands, got %d", len(result))
	}
}

func TestFilterCommands_PlatformCaseInsensitive(t *testing.T) {
	cmds := []*model.Command{
		{Name: "a", Risks: []model.Risk{{Level: model.RiskLevelLow}}, Platforms: []string{"Linux"}},
	}
	result := filterCommands(cmds, "", "linux")
	if len(result) != 1 {
		t.Fatalf("expected 1 command, got %d", len(result))
	}
}

func TestGetRiskStyle(t *testing.T) {
	tests := []struct {
		risk model.RiskLevel
	}{
		{model.RiskLevelLow},
		{model.RiskLevelMedium},
		{model.RiskLevelHigh},
		{model.RiskLevelCritical},
	}

	for _, tt := range tests {
		t.Run(string(tt.risk), func(t *testing.T) {
			style := getRiskStyle(tt.risk)
			rendered := style.Render(string(tt.risk))
			if rendered == "" {
				t.Fatal("expected non-empty rendered output")
			}
		})
	}
}

func TestGetRiskStyle_UnknownRisk(t *testing.T) {
	style := getRiskStyle(model.RiskLevel("unknown"))
	rendered := style.Render("test")
	if rendered != "test" {
		t.Fatalf("default style should render plain text, got %q", rendered)
	}
}

func TestGetRiskIndicator(t *testing.T) {
	tests := []struct {
		risk model.RiskLevel
	}{
		{model.RiskLevelLow},
		{model.RiskLevelMedium},
		{model.RiskLevelHigh},
		{model.RiskLevelCritical},
	}

	for _, tt := range tests {
		t.Run(string(tt.risk), func(t *testing.T) {
			indicator := getRiskIndicator(tt.risk)
			if indicator == "" {
				t.Fatal("expected non-empty indicator")
			}
		})
	}
}

func TestGetTerminalWidth_Default(t *testing.T) {
	os.Unsetenv("COLUMNS")
	w := getTerminalWidth()
	if w != 80 {
		t.Fatalf("expected default width 80, got %d", w)
	}
}

func TestGetTerminalWidth_FromEnv(t *testing.T) {
	os.Setenv("COLUMNS", "120")
	defer os.Unsetenv("COLUMNS")

	w := getTerminalWidth()
	if w != 120 {
		t.Fatalf("expected width 120, got %d", w)
	}
}

func TestGetTerminalWidth_InvalidEnv(t *testing.T) {
	os.Setenv("COLUMNS", "abc")
	defer os.Unsetenv("COLUMNS")

	w := getTerminalWidth()
	if w != 80 {
		t.Fatalf("expected default width 80 for invalid env, got %d", w)
	}
}

func TestGetTerminalWidth_NegativeEnv(t *testing.T) {
	os.Setenv("COLUMNS", "-5")
	defer os.Unsetenv("COLUMNS")

	w := getTerminalWidth()
	if w != 80 {
		t.Fatalf("expected default width 80 for negative env, got %d", w)
	}
}

func TestGetTerminalWidth_ZeroEnv(t *testing.T) {
	os.Setenv("COLUMNS", "0")
	defer os.Unsetenv("COLUMNS")

	w := getTerminalWidth()
	if w != 80 {
		t.Fatalf("expected default width 80 for zero env, got %d", w)
	}
}

func initTestServices(t *testing.T) {
	t.Helper()
	tmpDir := t.TempDir()

	outputFormat = ""
	listLimit = 0
	listRisk = ""
	listPlatform = ""
	searchLimit = 0
	searchRisk = ""
	searchPlatform = ""
	exportFormat = "markdown"
	exportOutput = ""
	exportCompact = false
	exportStdout = false
	exportAllRisk = ""
	exportAllPlatform = ""

	var err error
	cmdService, err = service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}

	cfgService, err = service.NewConfigServiceWithDir(tmpDir)
	if err != nil {
		t.Fatalf("failed to create config service: %v", err)
	}
}

func executeTestCommand(t *testing.T, args ...string) (string, int) {
	t.Helper()
	initTestServices(t)

	// Reset root command state to avoid cross-test pollution
	rootCmd.SilenceErrors = false
	rootCmd.SilenceUsage = false
	rootCmd.SetArgs(nil)

	oldStdout := os.Stdout
	oldStderr := os.Stderr
	rOut, wOut, _ := os.Pipe()
	rErr, wErr, _ := os.Pipe()
	os.Stdout = wOut
	os.Stderr = wErr

	var outBuf, errBuf strings.Builder
	done := make(chan struct{})
	go func() {
		io.Copy(&outBuf, rOut)
		io.Copy(&errBuf, rErr)
		close(done)
	}()

	code := 0
	func() {
		defer func() {
			if r := recover(); r != nil {
				code = 1
			}
		}()
		rootCmd.SetArgs(args)
		if err := rootCmd.Execute(); err != nil {
			code = 1
		}
	}()

	wOut.Close()
	wErr.Close()
	<-done

	os.Stdout = oldStdout
	os.Stderr = oldStderr

	return outBuf.String() + errBuf.String(), code
}

func TestCLI_ListCommand(t *testing.T) {
	output, code := executeTestCommand(t, "list", "-f", "json")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, "name") {
		t.Errorf("expected JSON output with 'name' field, got: %s", truncate(output, 200))
	}
}

func TestCLI_CategoriesCommand(t *testing.T) {
	output, code := executeTestCommand(t, "categories")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, "分类") && !strings.Contains(output, "Kubernetes") {
		t.Errorf("expected categories output, got: %s", truncate(output, 200))
	}
}

func TestCLI_VersionCommand(t *testing.T) {
	output, code := executeTestCommand(t, "version")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, "version") {
		t.Errorf("expected version output to contain 'version', got: %s", truncate(output, 200))
	}
}

func TestCLI_SearchCommand(t *testing.T) {
	output, code := executeTestCommand(t, "search", "git", "-f", "json")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, "name") {
		t.Errorf("expected search JSON output with 'name' field, got: %s", truncate(output, 200))
	}
}

func TestCLI_SearchNoResults(t *testing.T) {
	output, code := executeTestCommand(t, "search", "zzznonexistent12345")
	if code != 0 {
		t.Fatalf("expected exit code 0 for no results, got %d", code)
	}
	if !strings.Contains(output, "未找到") && !strings.Contains(output, "[]") {
		t.Errorf("expected '未找到' or empty JSON, got: %s", truncate(output, 200))
	}
}

func TestCLI_ShowCommand(t *testing.T) {
	names := cmdService.GetAllCommandNames()
	if len(names) == 0 {
		t.Skip("no commands available")
	}

	output, code := executeTestCommand(t, "show", names[0], "-f", "json")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, names[0]) {
		t.Errorf("expected output to contain command name %q, got: %s", names[0], truncate(output, 200))
	}
}

func truncate(s string, maxLen int) string {
	if len(s) <= maxLen {
		return s
	}
	return s[:maxLen] + "..."
}

func TestCLI_ListCommand_YAML(t *testing.T) {
	output, code := executeTestCommand(t, "list", "-f", "yaml")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, "name:") {
		t.Errorf("expected YAML output with 'name:' field, got: %s", truncate(output, 200))
	}
	if !strings.Contains(output, "risk:") {
		t.Errorf("expected YAML output with 'risk:' field, got: %s", truncate(output, 200))
	}
	if !strings.Contains(output, "description:") {
		t.Errorf("expected YAML output with 'description:' field, got: %s", truncate(output, 200))
	}
}

func TestCLI_SearchCommand_YAML(t *testing.T) {
	output, code := executeTestCommand(t, "search", "docker", "-f", "yaml")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, "name:") {
		t.Errorf("expected YAML output with 'name:' field, got: %s", truncate(output, 200))
	}
	if !strings.Contains(output, "docker") {
		t.Errorf("expected YAML output to contain 'docker', got: %s", truncate(output, 200))
	}
}

func TestCLI_CategoriesCommand_YAML(t *testing.T) {
	output, code := executeTestCommand(t, "categories", "-f", "yaml")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, "name:") {
		t.Errorf("expected YAML output with 'name:' field, got: %s", truncate(output, 200))
	}
	if !strings.Contains(output, "command_count:") {
		t.Errorf("expected YAML output with 'command_count:' field, got: %s", truncate(output, 200))
	}
}

func TestCLI_ExportAll_YAML(t *testing.T) {
	output, code := executeTestCommand(t, "export-all", "--format", "yaml", "--stdout")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, "name:") {
		t.Errorf("expected YAML output with 'name:' field, got: %s", truncate(output, 200))
	}
	if !strings.Contains(output, "category:") {
		t.Errorf("expected YAML output with 'category:' field, got: %s", truncate(output, 200))
	}
}

func TestCLI_Export_YAML(t *testing.T) {
	names := cmdService.GetAllCommandNames()
	if len(names) == 0 {
		t.Skip("no commands available")
	}

	output, code := executeTestCommand(t, "export", names[0], "--format", "yaml", "--stdout")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}
	if !strings.Contains(output, "name:") {
		t.Errorf("expected YAML output with 'name:' field, got: %s", truncate(output, 200))
	}
	if !strings.Contains(output, names[0]) {
		t.Errorf("expected YAML output to contain %q, got: %s", names[0], truncate(output, 200))
	}
}

func TestCLI_InvalidRisk(t *testing.T) {
	output, code := executeTestCommand(t, "list", "--risk", "invalid")
	if code == 0 {
		t.Fatal("expected non-zero exit code for invalid risk")
	}
	if !strings.Contains(output, "无效的风险级别") {
		t.Errorf("expected error about invalid risk level, got: %s", truncate(output, 200))
	}
}

func TestCLI_InvalidPlatform(t *testing.T) {
	output, code := executeTestCommand(t, "list", "--platform", "invalid")
	if code == 0 {
		t.Fatal("expected non-zero exit code for invalid platform")
	}
	if !strings.Contains(output, "无效的平台") {
		t.Errorf("expected error about invalid platform, got: %s", truncate(output, 200))
	}
}

func TestCLI_ShowNotFound(t *testing.T) {
	output, code := executeTestCommand(t, "show", "nonexistentcommandxyz")
	if code == 0 {
		t.Fatal("expected non-zero exit code for nonexistent command")
	}
	if !strings.Contains(output, "未找到") {
		t.Errorf("expected '未找到' in error output, got: %s", truncate(output, 200))
	}
}

func TestCLI_ExportAllFilter(t *testing.T) {
	output, code := executeTestCommand(t, "export-all", "--risk", "low", "--stdout", "--format", "json")
	if code != 0 {
		t.Fatalf("expected exit code 0, got %d, output: %s", code, output)
	}

	if strings.Contains(output, `"level": "high"`) {
		t.Error("expected only low-risk commands, but found high-risk")
	}

	if !strings.Contains(output, `"level": "low"`) {
		t.Errorf("expected at least one low-risk command in output, got: %s", truncate(output, 300))
	}
}
