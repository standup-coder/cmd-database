package tui

import (
	"fmt"
	"io"
	"strings"

	"github.com/atotto/clipboard"
	"github.com/charmbracelet/bubbles/key"
	"github.com/charmbracelet/bubbles/list"
	"github.com/charmbracelet/bubbles/textinput"
	"github.com/charmbracelet/bubbles/viewport"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
	"github.com/cmd4coder/cmd4coder/internal/model"
	"github.com/cmd4coder/cmd4coder/internal/service"
)

const (
	maxSearchHistory = 50
	homeRecentCount  = 20
)

type Model struct {
	commandService *service.CommandService
	configService  *service.ConfigService

	categories  []string
	commands    []*model.Command
	selectedCmd *model.Command

	searchInput    textinput.Model
	categoryList   list.Model
	commandList    list.Model
	detailViewport viewport.Model

	activePanel   int
	width         int
	height        int
	ready         bool
	statusMessage string

	showHelp           bool
	showHome           bool
	currentSearchQuery string
	searchHistory      []string
	searchHistoryIdx   int
	relatedCmds        []string
	relatedIdx         int

	keys keyMap
}

type keyMap struct {
	Up       key.Binding
	Down     key.Binding
	Left     key.Binding
	Right    key.Binding
	Enter    key.Binding
	Tab      key.Binding
	Search   key.Binding
	Favorite key.Binding
	Export   key.Binding
	Help     key.Binding
	Back     key.Binding
	Quit     key.Binding
	Home     key.Binding
	Related  key.Binding
	Top      key.Binding
	Bottom   key.Binding
	HalfUp   key.Binding
	HalfDown key.Binding
}

var defaultKeys = keyMap{
	Up: key.NewBinding(
		key.WithKeys("up", "k"),
		key.WithHelp("↑/k", "向上"),
	),
	Down: key.NewBinding(
		key.WithKeys("down", "j"),
		key.WithHelp("↓/j", "向下"),
	),
	Left: key.NewBinding(
		key.WithKeys("left", "h"),
		key.WithHelp("←/h", "向左"),
	),
	Right: key.NewBinding(
		key.WithKeys("right", "l"),
		key.WithHelp("→/l", "向右"),
	),
	Enter: key.NewBinding(
		key.WithKeys("enter"),
		key.WithHelp("enter", "选择"),
	),
	Tab: key.NewBinding(
		key.WithKeys("tab"),
		key.WithHelp("tab", "切换面板"),
	),
	Search: key.NewBinding(
		key.WithKeys("/"),
		key.WithHelp("/", "搜索"),
	),
	Favorite: key.NewBinding(
		key.WithKeys("f"),
		key.WithHelp("f", "收藏"),
	),
	Export: key.NewBinding(
		key.WithKeys("e"),
		key.WithHelp("e", "导出"),
	),
	Help: key.NewBinding(
		key.WithKeys("?"),
		key.WithHelp("?", "帮助"),
	),
	Back: key.NewBinding(
		key.WithKeys("esc", "backspace"),
		key.WithHelp("esc", "返回"),
	),
	Quit: key.NewBinding(
		key.WithKeys("q", "ctrl+c"),
		key.WithHelp("q", "退出"),
	),
	Home: key.NewBinding(
		key.WithKeys("H"),
		key.WithHelp("H", "首页"),
	),
	Related: key.NewBinding(
		key.WithKeys("r"),
		key.WithHelp("r", "相关命令"),
	),
	Top: key.NewBinding(
		key.WithKeys("g"),
		key.WithHelp("g", "跳到顶部"),
	),
	Bottom: key.NewBinding(
		key.WithKeys("G"),
		key.WithHelp("G", "跳到底部"),
	),
	HalfUp: key.NewBinding(
		key.WithKeys("ctrl+u"),
		key.WithHelp("ctrl+u", "上半页"),
	),
	HalfDown: key.NewBinding(
		key.WithKeys("ctrl+d"),
		key.WithHelp("ctrl+d", "下半页"),
	),
}

func NewModel(cmdService *service.CommandService, cfgService *service.ConfigService) *Model {
	ti := textinput.New()
	ti.Placeholder = "搜索命令..."
	ti.Focus()
	ti.CharLimit = 100
	ti.Width = 50

	return &Model{
		commandService: cmdService,
		configService:  cfgService,
		searchInput:    ti,
		activePanel:    0,
		showHome:       true,
		keys:           defaultKeys,
	}
}

func (m Model) Init() tea.Cmd {
	return textinput.Blink
}

func (m Model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	var cmd tea.Cmd
	var cmds []tea.Cmd

	switch msg := msg.(type) {
	case tea.WindowSizeMsg:
		m.width = msg.Width
		m.height = msg.Height

		if m.ready {
			m.resizeLists()
		} else {
			m.setupLists()
			m.ready = true
		}
		return m, nil

	case tea.KeyMsg:
		if m.showHelp {
			if key.Matches(msg, m.keys.Help) || key.Matches(msg, m.keys.Back) {
				m.showHelp = false
				return m, nil
			}
			return m, nil
		}

		switch {
		case key.Matches(msg, m.keys.Quit):
			return m, tea.Quit

		case key.Matches(msg, m.keys.Help):
			m.showHelp = !m.showHelp
			return m, nil

		case key.Matches(msg, m.keys.Tab):
			m.activePanel = (m.activePanel + 1) % 3
			m.updateFocus()
			return m, nil

		case key.Matches(msg, m.keys.Search):
			m.activePanel = 0
			m.searchInput.Focus()
			m.searchHistoryIdx = len(m.searchHistory)
			return m, nil

		case key.Matches(msg, m.keys.Home):
			if m.activePanel == 2 {
				m.showHome = true
				m.loadHomeCommands()
				return m, nil
			}

		case key.Matches(msg, m.keys.Related):
			if m.selectedCmd != nil && len(m.selectedCmd.RelatedCommands) > 0 {
				m.loadRelatedCommand()
				return m, nil
			}

		case m.activePanel == 1 || m.activePanel == 2:
			if key.Matches(msg, m.keys.Top) {
				if m.activePanel == 1 {
					m.categoryList.Select(0)
				} else {
					m.commandList.Select(0)
				}
				return m, nil
			}
			if key.Matches(msg, m.keys.Bottom) {
				if m.activePanel == 1 {
					m.categoryList.Select(len(m.categories) - 1)
				} else {
					m.commandList.Select(len(m.commands) - 1)
				}
				return m, nil
			}
			if key.Matches(msg, m.keys.HalfUp) {
				if m.activePanel == 1 {
					items := m.categoryList.Items()
					half := len(items) / 2
					if half < 1 {
						half = 1
					}
					m.categoryList.Select(max(0, m.categoryList.Index()-half))
				} else {
					half := len(m.commands) / 2
					if half < 1 {
						half = 1
					}
					m.commandList.Select(max(0, m.commandList.Index()-half))
				}
				return m, nil
			}
			if key.Matches(msg, m.keys.HalfDown) {
				if m.activePanel == 1 {
					items := m.categoryList.Items()
					half := len(items) / 2
					if half < 1 {
						half = 1
					}
					m.categoryList.Select(min(len(items)-1, m.categoryList.Index()+half))
				} else {
					half := len(m.commands) / 2
					if half < 1 {
						half = 1
					}
					m.commandList.Select(min(len(m.commands)-1, m.commandList.Index()+half))
				}
				return m, nil
			}
		}

		return m.handlePanelInput(msg)
	}

	oldValue := m.searchInput.Value()
	m.searchInput, cmd = m.searchInput.Update(msg)
	if m.searchInput.Value() != oldValue {
		m.performSearch()
	}
	cmds = append(cmds, cmd)

	return m, tea.Batch(cmds...)
}

func (m Model) handlePanelInput(msg tea.KeyMsg) (tea.Model, tea.Cmd) {
	var cmd tea.Cmd

	switch m.activePanel {
	case 0:
		switch {
		case key.Matches(msg, m.keys.Enter):
			query := m.searchInput.Value()
			if query != "" {
				m.saveSearchHistory(query)
			}
			m.activePanel = 1
			return m, nil
		case key.Matches(msg, m.keys.Down):
			m.activePanel = 1
			m.updateFocus()
			return m, nil
		case msg.String() == "up":
			if len(m.searchHistory) > 0 && m.searchHistoryIdx > 0 {
				m.searchHistoryIdx--
				m.searchInput.SetValue(m.searchHistory[m.searchHistoryIdx])
				m.searchInput.CursorEnd()
				return m, nil
			}
		case msg.String() == "down":
			if len(m.searchHistory) > 0 && m.searchHistoryIdx < len(m.searchHistory)-1 {
				m.searchHistoryIdx++
				m.searchInput.SetValue(m.searchHistory[m.searchHistoryIdx])
				m.searchInput.CursorEnd()
				return m, nil
			} else if len(m.searchHistory) > 0 && m.searchHistoryIdx == len(m.searchHistory)-1 {
				m.searchHistoryIdx = len(m.searchHistory)
				m.searchInput.SetValue("")
				return m, nil
			}
		}

	case 1:
		switch {
		case key.Matches(msg, m.keys.Up):
			if m.categoryList.Index() == 0 {
				m.activePanel = 0
				m.searchInput.Focus()
			}
		case key.Matches(msg, m.keys.Enter), key.Matches(msg, m.keys.Right):
			m.showHome = false
			m.loadCategoryCommands()
			m.activePanel = 2
			m.updateFocus()
			return m, nil
		}
		m.categoryList, cmd = m.categoryList.Update(msg)

	case 2:
		switch {
		case key.Matches(msg, m.keys.Back):
			m.deselectCommand()
			return m, nil
		case key.Matches(msg, m.keys.Left):
			m.activePanel = 1
			m.updateFocus()
			return m, nil
		case key.Matches(msg, m.keys.Enter):
			m.loadCommandDetail()
			return m, nil
		case key.Matches(msg, m.keys.Favorite):
			m.toggleFavorite()
			return m, nil
		case key.Matches(msg, m.keys.Export):
			m.copyCommand()
			return m, nil
		}
		m.commandList, cmd = m.commandList.Update(msg)
	}

	return m, cmd
}

func (m Model) View() string {
	if !m.ready {
		return "初始化中..."
	}

	docStyle := lipgloss.NewStyle().Padding(1, 2)

	title := lipgloss.NewStyle().
		Bold(true).
		Foreground(lipgloss.Color("170")).
		Render("CMD4Coder - 命令速查工具")

	searchBar := m.renderSearchBar()

	panels := lipgloss.JoinHorizontal(
		lipgloss.Top,
		m.renderCategoryPanel(),
		m.renderCommandPanel(),
		m.renderDetailPanel(),
	)

	statusBar := m.renderStatusBar()

	helpBar := m.renderHelpBar()

	content := lipgloss.JoinVertical(
		lipgloss.Left,
		title,
		searchBar,
		panels,
		statusBar,
		helpBar,
	)

	rendered := docStyle.Render(content)

	if m.showHelp {
		rendered = m.renderHelpOverlay(rendered)
	}

	return rendered
}

func (m Model) renderSearchBar() string {
	style := lipgloss.NewStyle().
		Border(lipgloss.RoundedBorder()).
		BorderForeground(lipgloss.Color("62")).
		Padding(0, 1).
		Width(m.width - 6)

	if m.activePanel == 0 {
		style = style.BorderForeground(lipgloss.Color("170"))
	}

	return style.Render(m.searchInput.View())
}

func (m Model) panelLayout() (catW, cmdW, detailW, panelH int) {
	w := m.width
	h := m.height
	if w < 20 {
		w = 20
	}
	if h < 12 {
		h = 12
	}
	catW = w * 20 / 100
	cmdW = w * 30 / 100
	detailW = w - catW - cmdW - 6
	panelH = h - 12
	return
}

func (m Model) renderCategoryPanel() string {
	catW, _, _, panelH := m.panelLayout()

	style := lipgloss.NewStyle().
		Border(lipgloss.RoundedBorder()).
		BorderForeground(lipgloss.Color("62")).
		Width(catW).
		Height(panelH)

	if m.activePanel == 1 {
		style = style.BorderForeground(lipgloss.Color("170"))
	}

	title := lipgloss.NewStyle().Bold(true).Render("📁 分类")

	if len(m.categories) == 0 {
		return style.Render(title + "\n\n无数据")
	}

	return style.Render(title + "\n" + m.categoryList.View())
}

func (m Model) renderCommandPanel() string {
	_, cmdW, _, panelH := m.panelLayout()

	style := lipgloss.NewStyle().
		Border(lipgloss.RoundedBorder()).
		BorderForeground(lipgloss.Color("62")).
		Width(cmdW).
		Height(panelH)

	if m.activePanel == 2 {
		style = style.BorderForeground(lipgloss.Color("170"))
	}

	title := lipgloss.NewStyle().Bold(true).Render("📝 命令")

	if m.showHome && len(m.commands) == 0 {
		return style.Render(title + "\n\n无最近使用和收藏")
	}

	if !m.showHome && len(m.commands) == 0 {
		return style.Render(title + "\n\n请选择分类")
	}

	return style.Render(title + "\n" + m.commandList.View())
}

func (m Model) renderDetailPanel() string {
	_, _, detailW, panelH := m.panelLayout()

	style := lipgloss.NewStyle().
		Border(lipgloss.RoundedBorder()).
		BorderForeground(lipgloss.Color("62")).
		Width(detailW).
		Height(panelH)

	if m.selectedCmd != nil {
		style = style.BorderForeground(lipgloss.Color("170"))
	}

	title := lipgloss.NewStyle().Bold(true).Render("📖 详情")

	if m.selectedCmd == nil {
		return style.Render(title + "\n\n请选择命令")
	}

	vpView := m.detailViewport.View()

	return style.Render(title + "\n" + vpView)
}

func (m Model) renderStatusBar() string {
	style := lipgloss.NewStyle().
		Foreground(lipgloss.Color("240")).
		Render

	totalCmds := m.commandService.GetCommandCount()
	var status string

	if m.currentSearchQuery != "" {
		status = fmt.Sprintf("总命令数: %d | 搜索到 %d 个结果", totalCmds, len(m.commands))
	} else {
		status = fmt.Sprintf("总命令数: %d | 当前分类: %d 个命令", totalCmds, len(m.commands))
	}

	if m.statusMessage != "" {
		status += " | " + m.statusMessage
	}

	return style(status)
}

func (m Model) renderHelpBar() string {
	style := lipgloss.NewStyle().
		Foreground(lipgloss.Color("241")).
		Render

	help := "tab:切换 /:搜索 f:收藏 e:导出 ?:帮助 H:首页 r:相关 g/G:首尾 ctrl+u/d:翻页 q:退出"
	return style(help)
}

func (m Model) renderHelpOverlay(base string) string {
	overlayWidth := min(60, m.width-4)
	overlayHeight := min(24, m.height-4)

	overlayStyle := lipgloss.NewStyle().
		Width(overlayWidth).
		Height(overlayHeight).
		Border(lipgloss.RoundedBorder()).
		BorderForeground(lipgloss.Color("170")).
		Background(lipgloss.Color("235")).
		Align(lipgloss.Center, lipgloss.Center).
		Padding(1, 2)

	titleStyle := lipgloss.NewStyle().
		Bold(true).
		Foreground(lipgloss.Color("170")).
		MarginBottom(1)

	keyStyle := lipgloss.NewStyle().
		Foreground(lipgloss.Color("51")).
		Bold(true).
		Width(16)

	descStyle := lipgloss.NewStyle().
		Foreground(lipgloss.Color("252")).
		Width(30)

	bindings := [][]string{
		{"↑ / k", "向上移动"},
		{"↓ / j", "向下移动"},
		{"← / h", "向左/返回首页"},
		{"→ / l", "向右/选择"},
		{"enter", "选择/查看详情"},
		{"tab", "切换面板"},
		{"/", "搜索"},
		{"↑/↓ (搜索)", "搜索历史"},
		{"f", "收藏/取消收藏"},
		{"e", "复制命令"},
		{"r", "跳转相关命令"},
		{"H", "回到首页"},
		{"g", "跳到列表顶部"},
		{"G", "跳到列表底部"},
		{"ctrl+u", "上半页"},
		{"ctrl+d", "下半页"},
		{"?", "显示/关闭帮助"},
		{"esc", "返回/关闭"},
		{"q / ctrl+c", "退出"},
	}

	var rows []string
	for _, b := range bindings {
		row := lipgloss.JoinHorizontal(lipgloss.Top, keyStyle.Render(b[0]), descStyle.Render(b[1]))
		rows = append(rows, row)
	}

	content := titleStyle.Render("⌨  键盘快捷键") + "\n\n" + strings.Join(rows, "\n")
	overlay := overlayStyle.Render(content)

	return lipgloss.Place(m.width, m.height, lipgloss.Center, lipgloss.Center, overlay, lipgloss.WithWhitespaceBackground(lipgloss.Color("235")))
}

func (m Model) formatCommandDetail() string {
	cmd := m.selectedCmd

	var b strings.Builder
	b.Grow(1024)
	b.WriteString(fmt.Sprintf("Name: %s\n\n", cmd.Name))
	b.WriteString(fmt.Sprintf("Desc: %s\n\n", cmd.Description))
	b.WriteString(fmt.Sprintf("Category: %s\n", cmd.Category))
	b.WriteString(fmt.Sprintf("Platforms: %s\n\n", strings.Join(cmd.Platforms, ", ")))

	if cmd.InstallRequired {
		b.WriteString(fmt.Sprintf("Install: %s\n\n", cmd.InstallMethod))
	}

	if len(cmd.Usage) > 0 {
		b.WriteString("Usage:\n")
		for _, u := range cmd.Usage {
			b.WriteString(fmt.Sprintf("  %s\n", u))
		}
		b.WriteString("\n")
	}

	if len(cmd.Options) > 0 {
		b.WriteString("Options:\n")
		for _, opt := range cmd.Options {
			b.WriteString(fmt.Sprintf("  %-18s %s\n", opt.Flag, opt.Description))
		}
		b.WriteString("\n")
	}

	if len(cmd.Examples) > 0 {
		b.WriteString("Examples:\n")
		for _, ex := range cmd.Examples {
			b.WriteString(fmt.Sprintf("  $ %s\n  %s\n\n", ex.Command, ex.Description))
		}
	}

	if len(cmd.Notes) > 0 {
		b.WriteString("Notes:\n")
		for _, note := range cmd.Notes {
			b.WriteString(fmt.Sprintf("  - %s\n", note))
		}
		b.WriteString("\n")
	}

	if len(cmd.Risks) > 0 {
		b.WriteString("Risks:\n")
		for _, risk := range cmd.Risks {
			b.WriteString(fmt.Sprintf("  %s [%s] %s\n", tuiRiskIndicator(risk.Level), risk.Level, risk.Description))
		}
		b.WriteString("\n")
	}

	if len(cmd.RelatedCommands) > 0 {
		b.WriteString(fmt.Sprintf("Related: %s\n", strings.Join(cmd.RelatedCommands, ", ")))
		b.WriteString("\n")
	}

	return b.String()
}

func (m *Model) setupLists() {
	cats := m.commandService.GetSortedCategories()
	m.categories = cats

	catW, cmdW, _, panelH := m.panelLayout()

	items := make([]list.Item, len(cats))
	for i, cat := range cats {
		items[i] = listItem{title: cat, desc: ""}
	}

	catDelegate := list.NewDefaultDelegate()
	catDelegate.SetHeight(1)
	catDelegate.SetSpacing(0)

	m.categoryList = list.New(items, catDelegate, catW, panelH)
	m.categoryList.Title = ""
	m.categoryList.SetShowStatusBar(false)
	m.categoryList.SetFilteringEnabled(false)
	m.categoryList.SetShowHelp(false)

	cmdDelegate := &commandDelegate{
		DefaultDelegate: list.NewDefaultDelegate(),
		model:           m,
	}
	cmdDelegate.SetHeight(1)
	cmdDelegate.SetSpacing(0)

	m.commandList = list.New([]list.Item{}, cmdDelegate, cmdW, panelH)
	m.commandList.Title = ""
	m.commandList.SetShowStatusBar(false)
	m.commandList.SetFilteringEnabled(false)
	m.commandList.SetShowHelp(false)

	_, _, detailW, _ := m.panelLayout()
	m.detailViewport = viewport.New(detailW-4, panelH-4)
	m.detailViewport.SetContent("")

	if m.showHome {
		m.loadHomeCommands()
	}
}

func (m *Model) resizeLists() {
	catW, cmdW, _, panelH := m.panelLayout()

	catIdx := m.categoryList.Index()
	cmdIdx := m.commandList.Index()

	m.categoryList, _ = m.categoryList.Update(tea.WindowSizeMsg{Width: catW, Height: panelH})
	m.commandList, _ = m.commandList.Update(tea.WindowSizeMsg{Width: cmdW, Height: panelH})

	catItems := m.categoryList.Items()
	if catIdx >= 0 && catIdx < len(catItems) {
		m.categoryList.Select(catIdx)
	}
	cmdItems := m.commandList.Items()
	if cmdIdx >= 0 && cmdIdx < len(cmdItems) {
		m.commandList.Select(cmdIdx)
	}

	_, _, detailW, _ := m.panelLayout()
	m.detailViewport.Width = detailW - 4
	m.detailViewport.Height = panelH - 4
}

func (m *Model) commandsToListItems(cmds []*model.Command) []list.Item {
	items := make([]list.Item, len(cmds))
	for i, cmd := range cmds {
		isFav := false
		if m.configService != nil {
			isFav = m.configService.IsFavorite(cmd.Name)
		}
		items[i] = listItem{
			title:      cmd.Name,
			desc:       cmd.Description,
			riskLevel:  cmd.GetRiskLevel(),
			isFavorite: isFav,
		}
	}
	return items
}

func (m *Model) performSearch() {
	query := m.searchInput.Value()
	m.currentSearchQuery = query

	if query == "" {
		m.commands = nil
		m.commandList.SetItems([]list.Item{})
		return
	}

	results := m.commandService.SearchCommands(query)
	m.commands = results
	m.showHome = false

	items := m.commandsToListItems(results)
	m.commandList.SetItems(items)
}

func (m *Model) loadCategoryCommands() {
	if len(m.categories) == 0 {
		return
	}

	selectedIdx := m.categoryList.Index()
	if selectedIdx < 0 || selectedIdx >= len(m.categories) {
		return
	}

	category := m.categories[selectedIdx]
	cmds := m.commandService.ListCommandsByCategory(category)
	m.commands = cmds
	m.currentSearchQuery = ""

	items := m.commandsToListItems(cmds)
	m.commandList.SetItems(items)
}

func (m *Model) loadHomeCommands() {
	var homeCmds []*model.Command
	seen := make(map[string]bool)

	if m.configService != nil {
		recent := m.configService.GetRecentHistory(homeRecentCount)
		for _, h := range recent {
			if seen[h.CommandName] {
				continue
			}
			cmd, err := m.commandService.GetCommand(h.CommandName)
			if err == nil {
				homeCmds = append(homeCmds, cmd)
				seen[h.CommandName] = true
			}
		}

		favs := m.configService.GetFavorites()
		for _, f := range favs {
			if seen[f.CommandName] {
				continue
			}
			cmd, err := m.commandService.GetCommand(f.CommandName)
			if err == nil {
				homeCmds = append(homeCmds, cmd)
				seen[f.CommandName] = true
			}
		}
	}

	m.commands = homeCmds
	m.currentSearchQuery = ""

	items := m.commandsToListItems(homeCmds)
	m.commandList.SetItems(items)
}

func (m *Model) loadCommandDetail() {
	if len(m.commands) == 0 {
		return
	}

	selectedIdx := m.commandList.Index()
	if selectedIdx < 0 || selectedIdx >= len(m.commands) {
		return
	}

	m.selectedCmd = m.commands[selectedIdx]
	m.relatedCmds = m.selectedCmd.RelatedCommands
	m.relatedIdx = 0

	if m.configService != nil {
		m.configService.AddHistory(m.selectedCmd.Name, m.selectedCmd.Category)
	}

	m.detailViewport.SetContent(m.formatCommandDetail())
	m.detailViewport.GotoTop()
}

func (m *Model) loadRelatedCommand() {
	if len(m.relatedCmds) == 0 {
		return
	}

	if m.relatedIdx >= len(m.relatedCmds) {
		m.relatedIdx = 0
	}

	name := m.relatedCmds[m.relatedIdx]
	m.relatedIdx++

	cmd, err := m.commandService.GetCommand(name)
	if err != nil {
		m.statusMessage = fmt.Sprintf("未找到命令: %s", name)
		return
	}

	m.selectedCmd = cmd
	m.relatedCmds = cmd.RelatedCommands
	m.relatedIdx = 0

	if m.configService != nil {
		m.configService.AddHistory(cmd.Name, cmd.Category)
	}

	m.statusMessage = fmt.Sprintf("已跳转到: %s", cmd.Name)

	m.detailViewport.SetContent(m.formatCommandDetail())
	m.detailViewport.GotoTop()
}

func (m *Model) toggleFavorite() {
	if m.selectedCmd == nil || m.configService == nil {
		return
	}

	if m.configService.IsFavorite(m.selectedCmd.Name) {
		err := m.configService.RemoveFavorite(m.selectedCmd.Name)
		if err != nil {
			m.statusMessage = fmt.Sprintf("Error: %v", err)
		} else {
			m.statusMessage = fmt.Sprintf("已取消收藏: %s", m.selectedCmd.Name)
		}
	} else {
		err := m.configService.AddFavorite(m.selectedCmd.Name, m.selectedCmd.Category, "")
		if err != nil {
			m.statusMessage = fmt.Sprintf("Error: %v", err)
		} else {
			m.statusMessage = fmt.Sprintf("★ 已收藏: %s", m.selectedCmd.Name)
		}
	}

	m.refreshCommandListItems()
}

func (m *Model) refreshCommandListItems() {
	items := m.commandsToListItems(m.commands)
	curIdx := m.commandList.Index()
	m.commandList.SetItems(items)
	if curIdx >= 0 && curIdx < len(items) {
		m.commandList.Select(curIdx)
	}
}

func (m *Model) deselectCommand() {
	m.selectedCmd = nil
	m.relatedCmds = nil
	m.relatedIdx = 0
	m.detailViewport.SetContent("")
}

func (m *Model) copyCommand() {
	if m.selectedCmd == nil {
		m.statusMessage = "No command selected"
		return
	}

	var b strings.Builder
	b.WriteString(m.selectedCmd.Name)
	for _, u := range m.selectedCmd.Usage {
		b.WriteString("\n")
		b.WriteString(u)
	}
	for _, ex := range m.selectedCmd.Examples {
		b.WriteString("\n")
		b.WriteString(ex.Command)
	}

	if err := clipboard.WriteAll(b.String()); err != nil {
		m.statusMessage = fmt.Sprintf("Copy failed: %v", err)
	} else {
		m.statusMessage = fmt.Sprintf("Copied: %s", m.selectedCmd.Name)
	}
}

func (m *Model) updateFocus() {
	if m.activePanel == 0 {
		m.searchInput.Focus()
	} else {
		m.searchInput.Blur()
	}
}

func (m *Model) saveSearchHistory(query string) {
	for i, h := range m.searchHistory {
		if h == query {
			m.searchHistory = append(m.searchHistory[:i], m.searchHistory[i+1:]...)
			break
		}
	}
	m.searchHistory = append(m.searchHistory, query)
	if len(m.searchHistory) > maxSearchHistory {
		m.searchHistory = m.searchHistory[len(m.searchHistory)-maxSearchHistory:]
	}
	m.searchHistoryIdx = len(m.searchHistory)
}

type listItem struct {
	title      string
	desc       string
	riskLevel  model.RiskLevel
	isFavorite bool
}

func (i listItem) Title() string       { return i.title }
func (i listItem) Description() string { return i.desc }
func (i listItem) FilterValue() string { return i.title }

type commandDelegate struct {
	list.DefaultDelegate
	model *Model
}

func (d *commandDelegate) Render(w io.Writer, m list.Model, index int, item list.Item) {
	li, ok := item.(listItem)
	if !ok {
		d.DefaultDelegate.Render(w, m, index, item)
		return
	}

	isSelected := index == m.Index()

	prefix := ""
	if li.isFavorite {
		prefix = "★ "
	}

	riskColor := ""
	switch li.riskLevel {
	case model.RiskLevelCritical:
		riskColor = "196"
	case model.RiskLevelHigh:
		riskColor = "208"
	case model.RiskLevelMedium:
		riskColor = "220"
	}

	title := li.title
	desc := li.desc

	query := ""
	if d.model != nil {
		query = d.model.currentSearchQuery
	}

	titleStr := title
	if query != "" {
		lowerName := strings.ToLower(title)
		lowerQuery := strings.ToLower(query)
		if idx := strings.Index(lowerName, lowerQuery); idx >= 0 {
			end := idx + len(query)
			titleStr = title[:idx] +
				lipgloss.NewStyle().Bold(true).Render(title[idx:end]) +
				title[end:]
		}
	}

	displayTitle := prefix + titleStr

	var titleStyle lipgloss.Style
	if isSelected {
		titleStyle = d.Styles.SelectedTitle
	} else {
		titleStyle = d.Styles.NormalTitle
	}

	if riskColor != "" && isSelected {
		titleStyle = titleStyle.Foreground(lipgloss.Color(riskColor))
	}

	titleStr = titleStyle.Width(m.Width() - 4).Render(displayTitle)

	var descStyle lipgloss.Style
	if isSelected {
		descStyle = d.Styles.SelectedDesc
	} else {
		descStyle = d.Styles.NormalDesc
	}

	descStr := descStyle.Width(m.Width() - 4).Render(desc)

	spacing := strings.Repeat(" ", d.Spacing())
	fmt.Fprintf(w, "%s\n%s%s", titleStr, descStr, spacing)
}

func (d *commandDelegate) Update(msg tea.Msg, m *list.Model) tea.Cmd {
	return nil
}

func tuiRiskIndicator(risk model.RiskLevel) string {
	switch risk {
	case model.RiskLevelLow:
		return lipgloss.NewStyle().Foreground(lipgloss.Color("76")).Render("[low]")
	case model.RiskLevelMedium:
		return lipgloss.NewStyle().Foreground(lipgloss.Color("220")).Render("[med]")
	case model.RiskLevelHigh:
		return lipgloss.NewStyle().Foreground(lipgloss.Color("208")).Render("[HIGH]")
	case model.RiskLevelCritical:
		return lipgloss.NewStyle().Foreground(lipgloss.Color("196")).Render("[CRIT]")
	default:
		return ""
	}
}
