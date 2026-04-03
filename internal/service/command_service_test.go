package service

import (
	"testing"

	"github.com/cmd4coder/cmd4coder/internal/model"
)

func TestCommandServiceNew(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	if svc == nil {
		t.Fatal("expected non-nil service")
	}

	if svc.GetCommandCount() == 0 {
		t.Error("expected non-zero command count")
	}

	if svc.GetCategoryCount() == 0 {
		t.Error("expected non-zero category count")
	}
}

func TestCommandServiceGetCommand(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	_, err = svc.GetCommand("nonexistent_command_xyz")
	if err == nil {
		t.Error("expected error for nonexistent command")
	}

	commands := svc.GetAllCommands()
	if len(commands) == 0 {
		t.Skip("no commands loaded")
	}

	cmd, err := svc.GetCommand(commands[0].Name)
	if err != nil {
		t.Fatalf("GetCommand() error = %v", err)
	}
	if cmd.Name != commands[0].Name {
		t.Errorf("expected name %s, got %s", commands[0].Name, cmd.Name)
	}
}

func TestCommandServiceListByCategory(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	categories := svc.GetAllCategories()
	if len(categories) == 0 {
		t.Skip("no categories")
	}

	cmds := svc.ListCommandsByCategory(categories[0])
	for _, cmd := range cmds {
		if cmd.Category != categories[0] {
			t.Errorf("command %s has wrong category: %s", cmd.Name, cmd.Category)
		}
	}

	cmds = svc.ListCommandsByCategory("nonexistent")
	if len(cmds) != 0 {
		t.Errorf("expected 0 commands, got %d", len(cmds))
	}
}

func TestCommandServiceListByPlatform(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	linuxCmds := svc.ListCommandsByPlatform("linux")
	if len(linuxCmds) == 0 {
		t.Error("expected at least one linux command")
	}

	for _, cmd := range linuxCmds {
		found := false
		for _, p := range cmd.Platforms {
			if p == "linux" {
				found = true
				break
			}
		}
		if !found {
			t.Errorf("command %s not for linux platform", cmd.Name)
		}
	}
}

func TestCommandServiceSearch(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	commands := svc.GetAllCommands()
	if len(commands) == 0 {
		t.Skip("no commands loaded")
	}

	results := svc.SearchCommands(commands[0].Name)
	if len(results) == 0 {
		t.Errorf("expected results for '%s'", commands[0].Name)
	}

	results = svc.SearchCommands("xyznonexistent123")
	if len(results) != 0 {
		t.Error("expected no results for gibberish query")
	}
}

func TestCommandServiceSearchCache(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	r1 := svc.SearchCommands("docker")
	r2 := svc.SearchCommands("docker")
	if len(r1) != len(r2) {
		t.Error("cached results should match")
	}
}

func TestCommandServiceFilterByRisk(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	lowCmds := svc.FilterCommandsByRisk(model.RiskLevelLow)
	for _, cmd := range lowCmds {
		if cmd.GetRiskLevel() != model.RiskLevelLow {
			t.Errorf("command %s is not low risk: %s", cmd.Name, cmd.GetRiskLevel())
		}
	}

	highCmds := svc.GetHighRiskCommands()
	for _, cmd := range highCmds {
		risk := cmd.GetRiskLevel()
		if risk != model.RiskLevelHigh && risk != model.RiskLevelCritical {
			t.Errorf("command %s is not high risk: %s", cmd.Name, risk)
		}
	}
}

func TestCommandServiceReload(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	countBefore := svc.GetCommandCount()
	if err := svc.Reload(); err != nil {
		t.Fatalf("Reload() error = %v", err)
	}
	countAfter := svc.GetCommandCount()

	if countBefore != countAfter {
		t.Errorf("expected same count after reload: before=%d, after=%d", countBefore, countAfter)
	}
}

func TestCommandServiceGetMetadata(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	metadata := svc.GetMetadata()
	if metadata == nil {
		t.Error("expected non-nil metadata")
	}
}

func TestGetAllCommandNames(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	names := svc.GetAllCommandNames()
	if len(names) == 0 {
		t.Fatal("expected non-empty command names slice")
	}

	for _, name := range names {
		if name == "" {
			t.Error("expected non-empty command name")
		}
	}
}

func TestSuggestCommand(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	commands := svc.GetAllCommands()
	if len(commands) == 0 {
		t.Skip("no commands loaded")
	}

	exact := svc.SuggestCommand(commands[0].Name)
	if exact != commands[0].Name {
		t.Errorf("exact match: expected %s, got %s", commands[0].Name, exact)
	}

	docker := svc.SuggestCommand("dock")
	if docker == "" {
		t.Error("expected suggestion for 'dock' prefix")
	}

	empty := svc.SuggestCommand("")
	if empty != "" {
		t.Errorf("expected empty string for empty input, got %s", empty)
	}
}

func TestFilterCommandsByRisk(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	tests := []struct {
		name  string
		level model.RiskLevel
	}{
		{"low", model.RiskLevelLow},
		{"medium", model.RiskLevelMedium},
		{"high", model.RiskLevelHigh},
		{"critical", model.RiskLevelCritical},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			cmds := svc.FilterCommandsByRisk(tt.level)
			for _, cmd := range cmds {
				if cmd.GetRiskLevel() != tt.level {
					t.Errorf("command %s risk = %s, want %s", cmd.Name, cmd.GetRiskLevel(), tt.level)
				}
			}
		})
	}
}

func TestGetHighRiskCommands(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	highRisk := svc.GetHighRiskCommands()
	for _, cmd := range highRisk {
		risk := cmd.GetRiskLevel()
		if risk != model.RiskLevelHigh && risk != model.RiskLevelCritical {
			t.Errorf("command %s risk = %s, want high or critical", cmd.Name, risk)
		}
	}
}

func TestReloadClearsCacheAndSearchStillWorks(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	_ = svc.SearchCommands("docker")

	if err := svc.Reload(); err != nil {
		t.Fatalf("Reload() error = %v", err)
	}

	results := svc.SearchCommands("docker")
	if len(results) == 0 {
		t.Error("expected search results after reload")
	}

	results = svc.SearchCommands("ls")
	if len(results) == 0 {
		t.Error("expected search results for 'ls' after reload")
	}
}

func TestGetMetadataNonNil(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	metadata := svc.GetMetadata()
	if metadata == nil {
		t.Fatal("expected non-nil metadata")
	}
}

func TestListCommandsByPlatform(t *testing.T) {
	svc, err := NewCommandService("")
	if err != nil {
		t.Fatalf("NewCommandService() error = %v", err)
	}

	tests := []struct {
		platform string
	}{
		{"linux"},
		{"macos"},
		{"windows"},
	}

	for _, tt := range tests {
		t.Run(tt.platform, func(t *testing.T) {
			cmds := svc.ListCommandsByPlatform(tt.platform)
			for _, cmd := range cmds {
				found := false
				for _, p := range cmd.Platforms {
					if p == tt.platform {
						found = true
						break
					}
				}
				if !found {
					t.Errorf("command %s does not support platform %s", cmd.Name, tt.platform)
				}
			}
		})
	}

	cmds := svc.ListCommandsByPlatform("nonexistent_os")
	if len(cmds) != 0 {
		t.Errorf("expected 0 commands for nonexistent platform, got %d", len(cmds))
	}
}
