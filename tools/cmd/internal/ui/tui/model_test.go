package tui

import (
	"fmt"
	"strings"
	"testing"

	"github.com/cmd4coder/cmd4coder/internal/model"
	"github.com/cmd4coder/cmd4coder/internal/service"
)

func newTestModel(t *testing.T) *Model {
	t.Helper()
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	cfgSvc, err := service.NewConfigServiceWithDir(t.TempDir())
	if err != nil {
		t.Fatalf("failed to create config service: %v", err)
	}
	m := NewModel(cmdSvc, cfgSvc)
	m.width = 120
	m.height = 40
	m.setupLists()
	return m
}

func TestCommandsToListItems_Empty(t *testing.T) {
	m := newTestModel(t)

	items := m.commandsToListItems([]*model.Command{})

	if len(items) != 0 {
		t.Fatalf("expected 0 items, got %d", len(items))
	}
}

func TestCommandsToListItems_NilConfigService(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)
	m.width = 120
	m.height = 40
	m.setupLists()

	cmds := []*model.Command{
		{
			Name:        "rm",
			Category:    "file",
			Description: "remove files",
			Usage:       []string{"rm file"},
			Examples:    []model.Example{{Command: "rm file.txt", Description: "remove a file"}},
			Platforms:   []string{"linux", "macos"},
		},
	}

	items := m.commandsToListItems(cmds)

	if len(items) != 1 {
		t.Fatalf("expected 1 item, got %d", len(items))
	}

	li, ok := items[0].(listItem)
	if !ok {
		t.Fatal("expected listItem type")
	}
	if li.isFavorite {
		t.Error("expected isFavorite=false when configService is nil")
	}
}

func TestCommandsToListItems_DifferentRiskLevels(t *testing.T) {
	m := newTestModel(t)

	cmds := []*model.Command{
		{
			Name:        "ls",
			Category:    "file",
			Description: "list files",
			Usage:       []string{"ls"},
			Examples:    []model.Example{{Command: "ls", Description: "list files"}},
			Platforms:   []string{"linux", "macos"},
		},
		{
			Name:        "rm",
			Category:    "file",
			Description: "remove files",
			Usage:       []string{"rm file"},
			Examples:    []model.Example{{Command: "rm file.txt", Description: "remove a file"}},
			Platforms:   []string{"linux", "macos"},
			Risks:       []model.Risk{{Level: model.RiskLevelHigh, Description: "data loss"}},
		},
		{
			Name:        "dd",
			Category:    "disk",
			Description: "disk dump",
			Usage:       []string{"dd if=... of=..."},
			Examples:    []model.Example{{Command: "dd if=/dev/zero of=/dev/sda", Description: "wipe disk"}},
			Platforms:   []string{"linux"},
			Risks: []model.Risk{
				{Level: model.RiskLevelCritical, Description: "destroys data"},
			},
		},
	}

	items := m.commandsToListItems(cmds)

	if len(items) != 3 {
		t.Fatalf("expected 3 items, got %d", len(items))
	}

	expectedRisks := []model.RiskLevel{
		model.RiskLevelLow,
		model.RiskLevelHigh,
		model.RiskLevelCritical,
	}
	for i, item := range items {
		li := item.(listItem)
		if li.riskLevel != expectedRisks[i] {
			t.Errorf("item %d: expected risk %q, got %q", i, expectedRisks[i], li.riskLevel)
		}
	}
}

func TestFormatCommandDetail_FullCommand(t *testing.T) {
	m := newTestModel(t)

	m.selectedCmd = &model.Command{
		Name:            "git-rebase",
		Category:        "git",
		Description:     "Rebase current branch onto another branch",
		Usage:           []string{"git rebase main", "git rebase -i HEAD~3"},
		InstallRequired: true,
		InstallMethod:   "package manager",
		Options: []model.Option{
			{Flag: "-i", Description: "Interactive rebase"},
			{Flag: "--continue", Description: "Continue rebase after conflict"},
		},
		Examples: []model.Example{
			{Command: "git rebase main", Description: "Rebase onto main"},
			{Command: "git rebase -i HEAD~3", Description: "Interactive rebase last 3 commits"},
		},
		Notes: []string{
			"Rewrites commit history",
			"Avoid rebasing shared branches",
		},
		Risks: []model.Risk{
			{Level: model.RiskLevelHigh, Description: "Rewrites commit history"},
			{Level: model.RiskLevelMedium, Description: "Merge conflicts possible"},
		},
		Platforms:       []string{"linux", "macos", "windows"},
		RelatedCommands: []string{"git-merge", "git-cherry-pick", "git-reset"},
	}

	result := m.formatCommandDetail()

	checks := []string{
		"git-rebase",
		"Rebase current branch",
		"git rebase main",
		"git rebase -i HEAD~3",
		"-i",
		"--continue",
		"Interactive rebase",
		"Install: package manager",
		"Rewrites commit history",
		"linux, macos, windows",
		"git-merge",
		"git-cherry-pick",
		"git-reset",
		"Related:",
		"Risks:",
		"Notes:",
		"Usage:",
		"Options:",
		"Examples:",
		"Category: git",
	}

	for _, check := range checks {
		if !strings.Contains(result, check) {
			t.Errorf("expected output to contain %q", check)
		}
	}
}

func TestFormatCommandDetail_MinimalCommand(t *testing.T) {
	m := newTestModel(t)

	m.selectedCmd = &model.Command{
		Name:        "echo",
		Category:    "basic",
		Description: "Print text to stdout",
		Usage:       []string{"echo hello"},
		Examples:    []model.Example{{Command: "echo hello", Description: "print hello"}},
		Platforms:   []string{"linux", "macos", "windows"},
	}

	result := m.formatCommandDetail()

	mustContain := []string{
		"echo",
		"Print text to stdout",
		"Category: basic",
		"linux, macos, windows",
	}
	for _, s := range mustContain {
		if !strings.Contains(result, s) {
			t.Errorf("expected output to contain %q", s)
		}
	}

	mustNotContain := []string{
		"Install:",
		"Options:",
		"Risks:",
		"Related:",
		"Notes:",
	}
	for _, s := range mustNotContain {
		if strings.Contains(result, s) {
			t.Errorf("expected output NOT to contain %q", s)
		}
	}
}

func TestCopyCommand_NoPanic(t *testing.T) {
	m := newTestModel(t)

	m.selectedCmd = &model.Command{
		Name:        "ls",
		Category:    "file",
		Description: "list files",
		Usage:       []string{"ls -la"},
		Examples:    []model.Example{{Command: "ls -la /tmp", Description: "list tmp"}},
		Platforms:   []string{"linux"},
	}

	m.copyCommand()

	if m.statusMessage == "" {
		t.Error("expected statusMessage to be set after copyCommand")
	}
}

func TestCopyCommand_NoSelection(t *testing.T) {
	m := newTestModel(t)
	m.selectedCmd = nil

	m.copyCommand()

	if m.statusMessage != "No command selected" {
		t.Errorf("expected 'No command selected', got %q", m.statusMessage)
	}
}

func TestToggleFavorite_NilConfigService(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)
	m.width = 120
	m.height = 40
	m.setupLists()

	m.selectedCmd = &model.Command{
		Name:        "ls",
		Category:    "file",
		Description: "list files",
		Usage:       []string{"ls"},
		Examples:    []model.Example{{Command: "ls", Description: "list"}},
		Platforms:   []string{"linux"},
	}

	m.toggleFavorite()

	if m.statusMessage != "" {
		t.Errorf("expected empty statusMessage with nil configService, got %q", m.statusMessage)
	}
}

func TestToggleFavorite_NilSelectedCmd(t *testing.T) {
	m := newTestModel(t)
	m.selectedCmd = nil

	m.toggleFavorite()

	if m.statusMessage != "" {
		t.Errorf("expected empty statusMessage with nil selectedCmd, got %q", m.statusMessage)
	}
}

func TestToggleFavorite_AddAndRemove(t *testing.T) {
	m := newTestModel(t)

	m.selectedCmd = &model.Command{
		Name:        "git-log",
		Category:    "git",
		Description: "show commit log",
		Usage:       []string{"git log"},
		Examples:    []model.Example{{Command: "git log", Description: "show log"}},
		Platforms:   []string{"linux", "macos"},
	}

	if m.configService.IsFavorite("git-log") {
		t.Fatal("expected git-log to not be favorite initially")
	}

	m.toggleFavorite()

	if !strings.Contains(m.statusMessage, "已收藏") {
		t.Errorf("expected favorite added status, got %q", m.statusMessage)
	}
	if !m.configService.IsFavorite("git-log") {
		t.Error("expected git-log to be favorite after toggle")
	}

	m.toggleFavorite()

	if !strings.Contains(m.statusMessage, "已取消收藏") {
		t.Errorf("expected favorite removed status, got %q", m.statusMessage)
	}
	if m.configService.IsFavorite("git-log") {
		t.Error("expected git-log to not be favorite after second toggle")
	}
}

func TestSaveSearchHistory_AddsToHistory(t *testing.T) {
	m := newTestModel(t)

	m.saveSearchHistory("git")
	m.saveSearchHistory("docker")
	m.saveSearchHistory("kubectl")

	if len(m.searchHistory) != 3 {
		t.Fatalf("expected 3 history entries, got %d", len(m.searchHistory))
	}

	expected := []string{"git", "docker", "kubectl"}
	for i, h := range m.searchHistory {
		if h != expected[i] {
			t.Errorf("history[%d]: expected %q, got %q", i, expected[i], h)
		}
	}

	if m.searchHistoryIdx != 3 {
		t.Errorf("expected searchHistoryIdx=3, got %d", m.searchHistoryIdx)
	}
}

func TestSaveSearchHistory_DuplicateHandled(t *testing.T) {
	m := newTestModel(t)

	m.saveSearchHistory("git")
	m.saveSearchHistory("docker")
	m.saveSearchHistory("git")

	if len(m.searchHistory) != 2 {
		t.Fatalf("expected 2 history entries after duplicate, got %d", len(m.searchHistory))
	}

	if m.searchHistory[0] != "docker" {
		t.Errorf("expected first entry to be 'docker', got %q", m.searchHistory[0])
	}
	if m.searchHistory[1] != "git" {
		t.Errorf("expected last entry to be 'git', got %q", m.searchHistory[1])
	}
}

func TestSaveSearchHistory_MaxLimit(t *testing.T) {
	m := newTestModel(t)

	for i := 0; i < 55; i++ {
		m.saveSearchHistory(fmt.Sprintf("query-%d", i))
	}

	if len(m.searchHistory) != 50 {
		t.Fatalf("expected history capped at 50, got %d", len(m.searchHistory))
	}

	if m.searchHistory[0] != "query-5" {
		t.Errorf("expected oldest entry to be 'query-5', got %q", m.searchHistory[0])
	}
	if m.searchHistory[49] != "query-54" {
		t.Errorf("expected newest entry to be 'query-54', got %q", m.searchHistory[49])
	}
}

func TestNewModel(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)

	if !m.showHome {
		t.Error("expected showHome to be true")
	}
	if m.activePanel != 0 {
		t.Errorf("expected activePanel 0, got %d", m.activePanel)
	}
	if m.searchInput.Placeholder != "搜索命令..." {
		t.Errorf("expected searchInput placeholder '搜索命令...', got %q", m.searchInput.Placeholder)
	}
	if m.searchInput.CharLimit != 100 {
		t.Errorf("expected charLimit 100, got %d", m.searchInput.CharLimit)
	}
	if len(m.searchHistory) != 0 {
		t.Errorf("expected empty searchHistory, got %d", len(m.searchHistory))
	}
	if m.statusMessage != "" {
		t.Errorf("expected empty statusMessage, got %q", m.statusMessage)
	}
}

func TestModelView(t *testing.T) {
	m := newTestModel(t)

	view := m.View()
	if view == "" {
		t.Error("View() should return a non-empty string")
	}
}

func TestModelView_NotReady(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)

	view := m.View()
	if !strings.Contains(view, "初始化中...") {
		t.Errorf("expected '初始化中...' when not ready, got %q", view)
	}
}

func TestPanelLayout_EdgeCases(t *testing.T) {
	tests := []struct {
		name   string
		width  int
		height int
	}{
		{"small 20x12", 20, 12},
		{"normal 120x40", 120, 40},
		{"wide 200x50", 200, 50},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			cmdSvc, err := service.NewCommandService("")
			if err != nil {
				t.Fatalf("failed to create command service: %v", err)
			}
			m := NewModel(cmdSvc, nil)
			m.width = tt.width
			m.height = tt.height

			catW, cmdW, detailW, panelH := m.panelLayout()

			if catW < 1 {
				t.Errorf("catW should be >= 1, got %d", catW)
			}
			if cmdW < 1 {
				t.Errorf("cmdW should be >= 1, got %d", cmdW)
			}
			if detailW < 1 {
				t.Errorf("detailW should be >= 1, got %d", detailW)
			}
			if panelH < 0 {
				t.Errorf("panelH should be >= 0, got %d", panelH)
			}
		})
	}
}

func TestPanelLayout_BelowMinimum(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)
	m.width = 5
	m.height = 3

	catW, cmdW, detailW, panelH := m.panelLayout()

	if panelH != 0 {
		t.Errorf("expected panelH=0 for very small window, got %d", panelH)
	}
	_ = catW + cmdW + detailW
}

func TestSearchHistoryEdgeCases(t *testing.T) {
	t.Run("empty history navigation", func(t *testing.T) {
		m := newTestModel(t)

		if len(m.searchHistory) != 0 {
			t.Fatalf("expected empty history, got %d", len(m.searchHistory))
		}
		if m.searchHistoryIdx != 0 {
			t.Errorf("expected searchHistoryIdx=0, got %d", m.searchHistoryIdx)
		}
	})

	t.Run("single item history", func(t *testing.T) {
		m := newTestModel(t)
		m.saveSearchHistory("git")

		if len(m.searchHistory) != 1 {
			t.Fatalf("expected 1 entry, got %d", len(m.searchHistory))
		}
		if m.searchHistory[0] != "git" {
			t.Errorf("expected 'git', got %q", m.searchHistory[0])
		}
		if m.searchHistoryIdx != 1 {
			t.Errorf("expected searchHistoryIdx=1, got %d", m.searchHistoryIdx)
		}
	})
}

func TestPerformSearch(t *testing.T) {
	m := newTestModel(t)

	m.searchInput.SetValue("git")
	m.performSearch()

	if len(m.commands) == 0 {
		t.Fatal("expected commands to be populated after search for 'git'")
	}
	if m.currentSearchQuery != "git" {
		t.Errorf("expected currentSearchQuery='git', got %q", m.currentSearchQuery)
	}
	if m.showHome {
		t.Error("expected showHome to be false after search")
	}
}

func TestPerformSearch_Empty(t *testing.T) {
	m := newTestModel(t)

	m.searchInput.SetValue("")
	m.performSearch()

	if len(m.commands) != 0 {
		t.Fatalf("expected 0 commands for empty search, got %d", len(m.commands))
	}
}

func TestLoadCategoryCommands(t *testing.T) {
	m := newTestModel(t)

	if len(m.categories) == 0 {
		t.Fatal("expected categories to be loaded")
	}

	foundNonEmpty := false
	for i := range m.categories {
		m.categoryList.Select(i)
		m.loadCategoryCommands()
		if len(m.commands) > 0 {
			foundNonEmpty = true
			break
		}
	}

	if !foundNonEmpty {
		t.Fatal("expected at least one category to have commands")
	}
}

func TestLoadCategoryCommands_EmptyCategories(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)
	m.categories = []string{}

	m.loadCategoryCommands()

	if len(m.commands) != 0 {
		t.Fatal("expected no commands for empty categories")
	}
}

func TestLoadRelatedCommand(t *testing.T) {
	m := newTestModel(t)

	m.selectedCmd = &model.Command{
		Name:            "git clone",
		Category:        "vcs",
		Description:     "Clone a repository",
		Usage:           []string{"git clone <url>"},
		Examples:        []model.Example{{Command: "git clone url", Description: "clone"}},
		Platforms:       []string{"linux", "darwin"},
		RelatedCommands: []string{"git pull", "git fetch"},
	}
	m.relatedCmds = m.selectedCmd.RelatedCommands
	m.relatedIdx = 0

	m.detailViewport.SetContent("old content")

	m.loadRelatedCommand()

	if m.statusMessage == "" {
		t.Error("expected statusMessage to be set after loadRelatedCommand")
	}

	newDetail := m.detailViewport.View()
	if strings.Contains(newDetail, "old content") {
		t.Error("expected detail panel content to change after loadRelatedCommand")
	}

	if m.selectedCmd == nil {
		t.Error("expected selectedCmd to be non-nil after loadRelatedCommand")
	}
}

func TestLoadRelatedCommand_NoRelated(t *testing.T) {
	m := newTestModel(t)

	m.selectedCmd = &model.Command{
		Name:        "echo",
		Category:    "basic",
		Description: "Print text",
		Usage:       []string{"echo hello"},
		Examples:    []model.Example{{Command: "echo hello", Description: "print"}},
		Platforms:   []string{"linux"},
	}
	m.relatedCmds = nil
	m.relatedIdx = 0

	m.loadRelatedCommand()

	if m.selectedCmd == nil {
		t.Error("selectedCmd should remain non-nil")
	}
	if m.selectedCmd.Name != "echo" {
		t.Errorf("selectedCmd should still be 'echo', got %q", m.selectedCmd.Name)
	}
}

func TestDeselectCommand_ClearsRelated(t *testing.T) {
	m := newTestModel(t)

	m.selectedCmd = &model.Command{
		Name:            "git clone",
		Category:        "git",
		Description:     "Clone branch",
		Usage:           []string{"git clone <url>"},
		Examples:        []model.Example{{Command: "git clone url", Description: "clone"}},
		Platforms:       []string{"linux"},
		RelatedCommands: []string{"git pull", "git fetch"},
	}
	m.relatedCmds = []string{"git pull", "git fetch"}
	m.relatedIdx = 1
	m.detailViewport.SetContent("some detail content")

	m.deselectCommand()

	if m.selectedCmd != nil {
		t.Error("expected selectedCmd to be nil after deselect")
	}
	if m.relatedCmds != nil {
		t.Errorf("expected relatedCmds to be nil after deselect, got %v", m.relatedCmds)
	}
	if m.relatedIdx != 0 {
		t.Errorf("expected relatedIdx to be 0 after deselect, got %d", m.relatedIdx)
	}
	content := m.detailViewport.View()
	if strings.Contains(content, "some detail content") {
		t.Error("expected detail viewport content to be cleared after deselect")
	}
}
