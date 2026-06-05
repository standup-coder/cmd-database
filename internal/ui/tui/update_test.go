package tui

import (
	"strings"
	"testing"

	"github.com/charmbracelet/bubbles/list"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/cmd4coder/cmd4coder/internal/model"
	"github.com/cmd4coder/cmd4coder/internal/service"
)

func TestUpdate_WindowSize(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)

	newM, cmd := m.Update(tea.WindowSizeMsg{Width: 120, Height: 40})
	model := newM.(Model)

	if model.width != 120 {
		t.Errorf("expected width 120, got %d", model.width)
	}
	if model.height != 40 {
		t.Errorf("expected height 40, got %d", model.height)
	}
	if !model.ready {
		t.Error("expected model to be ready after WindowSizeMsg")
	}
	if cmd != nil {
		t.Error("expected nil cmd for WindowSizeMsg")
	}
}

func TestUpdate_QuitKey(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)
	m.ready = true

	newM, cmd := m.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'q'}})
	_ = newM.(Model)

	if cmd == nil {
		t.Fatal("expected tea.Quit command")
	}
}

func TestUpdate_HelpToggle(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)
	m.ready = true

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'?'}})
	model := newM.(Model)

	if !model.showHelp {
		t.Error("expected showHelp to be true after ? key")
	}

	newM, _ = model.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'?'}})
	model = newM.(Model)

	if model.showHelp {
		t.Error("expected showHelp to be false after second ? key")
	}
}

func TestUpdate_TabSwitch(t *testing.T) {
	m := newTestModel(t)
	m.ready = true

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyTab})
	model := newM.(Model)

	if model.activePanel != 1 {
		t.Errorf("expected activePanel 1 after tab, got %d", model.activePanel)
	}

	newM, _ = model.Update(tea.KeyMsg{Type: tea.KeyTab})
	model = newM.(Model)

	if model.activePanel != 2 {
		t.Errorf("expected activePanel 2 after second tab, got %d", model.activePanel)
	}

	newM, _ = model.Update(tea.KeyMsg{Type: tea.KeyTab})
	model = newM.(Model)

	if model.activePanel != 0 {
		t.Errorf("expected activePanel 0 after third tab, got %d", model.activePanel)
	}
}

func TestUpdate_SearchKey(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 2

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'/'}})
	model := newM.(Model)

	if model.activePanel != 0 {
		t.Errorf("expected activePanel 0 after / key, got %d", model.activePanel)
	}
}

func TestHandlePanelInput_SearchPanelEnter(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 0
	m.searchInput.SetValue("git")

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyEnter})
	model := newM.(Model)

	if model.activePanel != 1 {
		t.Errorf("expected activePanel 1 after enter in search, got %d", model.activePanel)
	}
}

func TestHandlePanelInput_SearchPanelDown(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 0

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyDown})
	model := newM.(Model)

	if model.activePanel != 1 {
		t.Errorf("expected activePanel 1 after down in search, got %d", model.activePanel)
	}
}

func TestHandlePanelInput_CategoryPanelEnter(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 1

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyEnter})
	model := newM.(Model)

	if model.activePanel != 2 {
		t.Errorf("expected activePanel 2 after enter in category, got %d", model.activePanel)
	}
	if model.showHome {
		t.Error("expected showHome to be false after selecting category")
	}
}

func TestHandlePanelInput_CommandPanelBack(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 2
	m.selectedCmd = &model.Command{
		Name:        "test",
		Category:    "test",
		Description: "test",
		Usage:       []string{"test"},
		Examples:    []model.Example{{Command: "test", Description: "test"}},
		Platforms:   []string{"linux"},
	}
	m.relatedCmds = []string{"other"}
	m.relatedIdx = 1

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyEscape})
	model := newM.(Model)

	if model.selectedCmd != nil {
		t.Error("expected selectedCmd to be nil after back")
	}
	if model.relatedCmds != nil {
		t.Error("expected relatedCmds to be nil after back")
	}
}

func TestHandlePanelInput_CommandPanelLeft(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 2

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyLeft})
	model := newM.(Model)

	if model.activePanel != 1 {
		t.Errorf("expected activePanel 1 after left in command panel, got %d", model.activePanel)
	}
}

func TestHandlePanelInput_CommandPanelFavorite(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 2
	m.selectedCmd = &model.Command{
		Name:        "git-log",
		Category:    "git",
		Description: "show log",
		Usage:       []string{"git log"},
		Examples:    []model.Example{{Command: "git log", Description: "show log"}},
		Platforms:   []string{"linux"},
	}
	m.commands = []*model.Command{m.selectedCmd}
	m.commandList.SetItems(m.commandsToListItems(m.commands))

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'f'}})
	model := newM.(Model)

	if model.statusMessage == "" {
		t.Error("expected statusMessage to be set after favorite toggle")
	}
}

func TestHandlePanelInput_CommandPanelExport(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 2
	m.selectedCmd = &model.Command{
		Name:        "ls",
		Category:    "file",
		Description: "list files",
		Usage:       []string{"ls -la"},
		Examples:    []model.Example{{Command: "ls -la", Description: "list all"}},
		Platforms:   []string{"linux"},
	}

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'e'}})
	model := newM.(Model)

	if model.statusMessage == "" {
		t.Error("expected statusMessage to be set after export/copy")
	}
}

func TestUpdate_HomeKey(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 2
	m.showHome = false

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'H'}})
	model := newM.(Model)

	if !model.showHome {
		t.Error("expected showHome to be true after H key in panel 2")
	}
}

func TestUpdate_HomeKeyNotPanel2(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 1
	m.showHome = false

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'H'}})
	model := newM.(Model)

	if model.showHome {
		t.Error("expected showHome to remain false when not in panel 2")
	}
}

func TestUpdate_RelatedKey(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 2
	m.selectedCmd = &model.Command{
		Name:            "git-clone",
		Category:        "git",
		Description:     "clone repo",
		Usage:           []string{"git clone <url>"},
		Examples:        []model.Example{{Command: "git clone url", Description: "clone"}},
		Platforms:       []string{"linux"},
		RelatedCommands: []string{"git-pull"},
	}
	m.relatedCmds = m.selectedCmd.RelatedCommands
	m.relatedIdx = 0

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'r'}})
	model := newM.(Model)

	if model.statusMessage == "" {
		t.Error("expected statusMessage to be set after related command navigation")
	}
}

func TestUpdate_TopBottomKeys(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.activePanel = 1

	// First select a category
	if len(m.categories) > 1 {
		m.categoryList.Select(1)
	}

	newM, _ := m.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'g'}})
	model := newM.(Model)

	if model.categoryList.Index() != 0 {
		t.Errorf("expected category index 0 after 'g', got %d", model.categoryList.Index())
	}

	newM, _ = model.Update(tea.KeyMsg{Type: tea.KeyRunes, Runes: []rune{'G'}})
	model = newM.(Model)

	expectedIdx := len(model.categories) - 1
	if model.categoryList.Index() != expectedIdx {
		t.Errorf("expected category index %d after 'G', got %d", expectedIdx, model.categoryList.Index())
	}
}

func TestInit(t *testing.T) {
	cmdSvc, err := service.NewCommandService("")
	if err != nil {
		t.Fatalf("failed to create command service: %v", err)
	}
	m := NewModel(cmdSvc, nil)

	cmd := m.Init()
	if cmd == nil {
		t.Error("expected non-nil cmd from Init")
	}
}

func TestRenderSearchBar(t *testing.T) {
	m := newTestModel(t)
	m.width = 120

	result := m.renderSearchBar()
	if result == "" {
		t.Error("expected non-empty search bar render")
	}
	if !strings.Contains(result, "搜索命令") {
		t.Errorf("expected search placeholder in render, got: %s", result)
	}
}

func TestRenderCategoryPanel(t *testing.T) {
	m := newTestModel(t)
	m.width = 120
	m.height = 40
	m.ready = true
	m.setupLists()

	result := m.renderCategoryPanel()
	if result == "" {
		t.Error("expected non-empty category panel render")
	}
	if !strings.Contains(result, "分类") {
		t.Errorf("expected '分类' in render, got: %s", result)
	}
}

func TestRenderCommandPanel(t *testing.T) {
	m := newTestModel(t)
	m.width = 120
	m.height = 40
	m.ready = true
	m.setupLists()

	result := m.renderCommandPanel()
	if result == "" {
		t.Error("expected non-empty command panel render")
	}
	if !strings.Contains(result, "命令") {
		t.Errorf("expected '命令' in render, got: %s", result)
	}
}

func TestRenderDetailPanel_NoSelection(t *testing.T) {
	m := newTestModel(t)
	m.width = 120
	m.height = 40
	m.ready = true
	m.selectedCmd = nil

	result := m.renderDetailPanel()
	if result == "" {
		t.Error("expected non-empty detail panel render")
	}
	if !strings.Contains(result, "请选择命令") {
		t.Errorf("expected '请选择命令' in render, got: %s", result)
	}
}

func TestRenderDetailPanel_WithSelection(t *testing.T) {
	m := newTestModel(t)
	m.width = 120
	m.height = 40
	m.ready = true
	m.selectedCmd = &model.Command{
		Name:        "ls",
		Category:    "file",
		Description: "list files",
		Usage:       []string{"ls"},
		Examples:    []model.Example{{Command: "ls", Description: "list"}},
		Platforms:   []string{"linux"},
	}
	m.detailViewport.SetContent(m.formatCommandDetail())

	result := m.renderDetailPanel()
	if result == "" {
		t.Error("expected non-empty detail panel render")
	}
	if !strings.Contains(result, "ls") {
		t.Errorf("expected 'ls' in render, got: %s", result)
	}
}

func TestRenderStatusBar(t *testing.T) {
	m := newTestModel(t)
	m.ready = true

	result := m.renderStatusBar()
	if result == "" {
		t.Error("expected non-empty status bar")
	}
	if !strings.Contains(result, "总命令数") {
		t.Errorf("expected '总命令数' in status bar, got: %s", result)
	}
}

func TestRenderStatusBar_WithSearch(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.currentSearchQuery = "git"
	m.commands = []*model.Command{
		{Name: "git-log", Category: "git", Description: "log", Usage: []string{"git log"}, Examples: []model.Example{{Command: "git log", Description: "log"}}, Platforms: []string{"linux"}},
	}

	result := m.renderStatusBar()
	if !strings.Contains(result, "搜索到") {
		t.Errorf("expected '搜索到' in status bar during search, got: %s", result)
	}
}

func TestRenderHelpBar(t *testing.T) {
	m := newTestModel(t)
	result := m.renderHelpBar()
	if result == "" {
		t.Error("expected non-empty help bar")
	}
	if !strings.Contains(result, "tab") {
		t.Errorf("expected 'tab' in help bar, got: %s", result)
	}
}

func TestRenderHelpOverlay(t *testing.T) {
	m := newTestModel(t)
	m.width = 120
	m.height = 40
	m.ready = true

	base := "test content"
	result := m.renderHelpOverlay(base)
	if result == "" {
		t.Error("expected non-empty help overlay")
	}
	if !strings.Contains(result, "快捷键") {
		t.Errorf("expected '快捷键' in help overlay, got: %s", result)
	}
}

func TestTuiRiskIndicator(t *testing.T) {
	tests := []struct {
		risk     model.RiskLevel
		expected string
	}{
		{model.RiskLevelLow, "[low]"},
		{model.RiskLevelMedium, "[med]"},
		{model.RiskLevelHigh, "[HIGH]"},
		{model.RiskLevelCritical, "[CRIT]"},
		{model.RiskLevel("unknown"), ""},
	}

	for _, tt := range tests {
		t.Run(string(tt.risk), func(t *testing.T) {
			result := tuiRiskIndicator(tt.risk)
			if tt.expected == "" {
				if result != "" {
					t.Errorf("expected empty for unknown risk, got %q", result)
				}
				return
			}
			if !strings.Contains(result, tt.expected) {
				t.Errorf("expected %q in result, got %q", tt.expected, result)
			}
		})
	}
}

func TestLoadHomeCommands(t *testing.T) {
	m := newTestModel(t)
	m.loadHomeCommands()

	// With no history/favorites, should be empty
	if len(m.commands) != 0 {
		t.Errorf("expected 0 home commands with empty history/favorites, got %d", len(m.commands))
	}
}

func TestLoadHomeCommands_WithHistory(t *testing.T) {
	m := newTestModel(t)

	// Add a history entry for a known command
	names := m.commandService.GetAllCommandNames()
	if len(names) == 0 {
		t.Skip("no commands available")
	}

	m.configService.AddHistory(names[0], "test")
	m.loadHomeCommands()

	if len(m.commands) == 0 {
		t.Error("expected at least one home command after adding history")
	}
}

func TestLoadHomeCommands_WithFavorite(t *testing.T) {
	m := newTestModel(t)

	names := m.commandService.GetAllCommandNames()
	if len(names) == 0 {
		t.Skip("no commands available")
	}

	m.configService.AddFavorite(names[0], "test", "")
	m.loadHomeCommands()

	if len(m.commands) == 0 {
		t.Error("expected at least one home command after adding favorite")
	}
}

func TestLoadCommandDetail(t *testing.T) {
	m := newTestModel(t)
	m.ready = true
	m.setupLists()

	names := m.commandService.GetAllCommandNames()
	if len(names) == 0 {
		t.Skip("no commands available")
	}

	cmd, _ := m.commandService.GetCommand(names[0])
	m.commands = []*model.Command{cmd}
	m.commandList.SetItems(m.commandsToListItems(m.commands))

	m.loadCommandDetail()

	if m.selectedCmd == nil {
		t.Fatal("expected selectedCmd to be set")
	}
	if m.selectedCmd.Name != names[0] {
		t.Errorf("expected selectedCmd name %q, got %q", names[0], m.selectedCmd.Name)
	}
}

func TestLoadCommandDetail_Empty(t *testing.T) {
	m := newTestModel(t)
	m.commands = []*model.Command{}
	m.commandList.SetItems([]list.Item{})

	m.loadCommandDetail()

	if m.selectedCmd != nil {
		t.Error("expected selectedCmd to be nil with empty commands")
	}
}

func TestRefreshCommandListItems(t *testing.T) {
	m := newTestModel(t)
	m.commands = []*model.Command{
		{Name: "cmd1", Category: "test", Description: "d1", Usage: []string{"cmd1"}, Examples: []model.Example{{Command: "cmd1", Description: "d1"}}, Platforms: []string{"linux"}},
		{Name: "cmd2", Category: "test", Description: "d2", Usage: []string{"cmd2"}, Examples: []model.Example{{Command: "cmd2", Description: "d2"}}, Platforms: []string{"linux"}},
	}
	m.commandList.SetItems(m.commandsToListItems(m.commands))
	m.commandList.Select(1)

	m.refreshCommandListItems()

	if m.commandList.Index() != 1 {
		t.Errorf("expected index to remain 1, got %d", m.commandList.Index())
	}
}

func TestCommandDelegate_Render(t *testing.T) {
	m := newTestModel(t)
	delegate := &commandDelegate{model: m}
	delegate.SetHeight(1)
	delegate.SetSpacing(0)

	item := listItem{title: "test-cmd", desc: "test desc", riskLevel: model.RiskLevelHigh}

	var buf strings.Builder
	l := list.New([]list.Item{item}, delegate, 40, 10)
	delegate.Render(&buf, l, 0, item)

	rendered := buf.String()
	if rendered == "" {
		t.Error("expected non-empty render output")
	}
}

func TestCommandDelegate_Update(t *testing.T) {
	m := newTestModel(t)
	delegate := &commandDelegate{model: m}

	cmd := delegate.Update(tea.KeyMsg{}, nil)
	if cmd != nil {
		t.Error("expected nil cmd from delegate Update")
	}
}

func TestUpdateFocus(t *testing.T) {
	m := newTestModel(t)
	m.activePanel = 0
	m.updateFocus()

	if !m.searchInput.Focused() {
		t.Error("expected search input to be focused when activePanel is 0")
	}

	m.activePanel = 1
	m.updateFocus()

	if m.searchInput.Focused() {
		t.Error("expected search input to be blurred when activePanel is not 0")
	}
}
