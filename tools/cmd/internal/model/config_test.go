package model

import (
	"path/filepath"
	"testing"
	"time"
)

func TestDefaultConfig(t *testing.T) {
	config := DefaultConfig()

	if config.Language != "zh" {
		t.Errorf("Expected language zh, got %s", config.Language)
	}

	if config.PageSize != 20 {
		t.Errorf("Expected page size 20, got %d", config.PageSize)
	}

	if !config.TUI.Enabled {
		t.Error("Expected TUI to be enabled by default")
	}

	if config.Search.MaxResults != 50 {
		t.Errorf("Expected max results 50, got %d", config.Search.MaxResults)
	}
}

func TestConfigValidation(t *testing.T) {
	tests := []struct {
		name    string
		config  *Config
		wantErr bool
	}{
		{
			name:    "valid config",
			config:  DefaultConfig(),
			wantErr: false,
		},
		{
			name: "invalid page size",
			config: &Config{
				Language: "zh",
				PageSize: 0,
				Search:   SearchConfig{MaxResults: 10, CacheSize: 10},
				Export:   ExportConfig{DefaultFormat: "markdown"},
			},
			wantErr: true,
		},
		{
			name: "invalid language",
			config: &Config{
				Language: "fr",
				PageSize: 10,
				Search:   SearchConfig{MaxResults: 10, CacheSize: 10},
				Export:   ExportConfig{DefaultFormat: "markdown"},
			},
			wantErr: true,
		},
		{
			name: "invalid export format",
			config: &Config{
				Language: "zh",
				PageSize: 10,
				Search:   SearchConfig{MaxResults: 10, CacheSize: 10},
				Export:   ExportConfig{DefaultFormat: "xml"},
			},
			wantErr: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := tt.config.Validate()
			if (err != nil) != tt.wantErr {
				t.Errorf("Validate() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestConfigSaveAndLoad(t *testing.T) {
	// 创建临时目录
	tmpDir := t.TempDir()
	configPath := filepath.Join(tmpDir, "config.json")

	// 创建配置
	config := DefaultConfig()
	config.Language = "en"
	config.PageSize = 30

	// 保存配置
	if err := config.Save(configPath); err != nil {
		t.Fatalf("Save() error = %v", err)
	}

	// 加载配置
	loaded, err := LoadConfig(configPath)
	if err != nil {
		t.Fatalf("LoadConfig() error = %v", err)
	}

	// 验证
	if loaded.Language != "en" {
		t.Errorf("Expected language en, got %s", loaded.Language)
	}

	if loaded.PageSize != 30 {
		t.Errorf("Expected page size 30, got %d", loaded.PageSize)
	}
}

func TestConfigLoadNonExistent(t *testing.T) {
	config, err := LoadConfig("/nonexistent/path/config.json")
	if err != nil {
		t.Fatalf("LoadConfig() should not error on non-existent file, got %v", err)
	}

	if config == nil {
		t.Fatal("LoadConfig() should return default config")
	}

	// 应该返回默认配置
	if config.Language != "zh" {
		t.Errorf("Expected default language zh, got %s", config.Language)
	}
}

func TestNewUserData(t *testing.T) {
	userData := NewUserData()

	if userData.Favorites == nil {
		t.Error("Favorites should not be nil")
	}

	if userData.History == nil {
		t.Error("History should not be nil")
	}

	if len(userData.Favorites) != 0 {
		t.Errorf("Expected 0 favorites, got %d", len(userData.Favorites))
	}
}

func TestUserDataAddFavorite(t *testing.T) {
	userData := NewUserData()

	// 添加收藏
	userData.AddFavorite("ls", "操作系统/Linux", "列出目录")

	if len(userData.Favorites) != 1 {
		t.Errorf("Expected 1 favorite, got %d", len(userData.Favorites))
	}

	// 添加重复的收藏
	userData.AddFavorite("ls", "操作系统/Linux", "列出目录")

	if len(userData.Favorites) != 1 {
		t.Errorf("Expected 1 favorite after duplicate add, got %d", len(userData.Favorites))
	}

	// 检查收藏
	if !userData.IsFavorite("ls") {
		t.Error("ls should be favorited")
	}

	if userData.IsFavorite("cd") {
		t.Error("cd should not be favorited")
	}
}

func TestUserDataRemoveFavorite(t *testing.T) {
	userData := NewUserData()

	// 添加收藏
	userData.AddFavorite("ls", "操作系统/Linux", "")
	userData.AddFavorite("cd", "操作系统/Linux", "")

	if len(userData.Favorites) != 2 {
		t.Errorf("Expected 2 favorites, got %d", len(userData.Favorites))
	}

	// 删除收藏
	userData.RemoveFavorite("ls")

	if len(userData.Favorites) != 1 {
		t.Errorf("Expected 1 favorite after removal, got %d", len(userData.Favorites))
	}

	if userData.IsFavorite("ls") {
		t.Error("ls should not be favorited after removal")
	}
}

func TestUserDataAddHistory(t *testing.T) {
	userData := NewUserData()

	// 添加历史记录
	userData.AddHistory("ls", "操作系统/Linux")
	userData.AddHistory("cd", "操作系统/Linux")
	userData.AddHistory("pwd", "操作系统/Linux")

	if len(userData.History) != 3 {
		t.Errorf("Expected 3 history entries, got %d", len(userData.History))
	}

	// 最新的应该在前面
	if userData.History[0].CommandName != "pwd" {
		t.Errorf("Expected most recent to be pwd, got %s", userData.History[0].CommandName)
	}

	// 重复访问
	userData.AddHistory("ls", "操作系统/Linux")

	if len(userData.History) != 3 {
		t.Errorf("Expected 3 history entries after duplicate, got %d", len(userData.History))
	}

	// ls应该移到最前面
	if userData.History[0].CommandName != "ls" {
		t.Errorf("Expected most recent to be ls after re-access, got %s", userData.History[0].CommandName)
	}
}

func TestUserDataGetRecentHistory(t *testing.T) {
	userData := NewUserData()

	// 添加历史记录
	for i := 0; i < 10; i++ {
		userData.AddHistory("cmd"+string(rune('0'+i)), "test")
	}

	// 获取最近5条
	recent := userData.GetRecentHistory(5)

	if len(recent) != 5 {
		t.Errorf("Expected 5 recent entries, got %d", len(recent))
	}

	// 请求超过实际数量
	recent = userData.GetRecentHistory(20)

	if len(recent) != 10 {
		t.Errorf("Expected 10 recent entries, got %d", len(recent))
	}
}

func TestUserDataHistoryLimit(t *testing.T) {
	userData := NewUserData()

	// 添加超过限制的历史记录
	for i := 0; i < 150; i++ {
		userData.AddHistory("cmd"+string(rune(i)), "test")
	}

	// 应该被限制在100条
	if len(userData.History) != 100 {
		t.Errorf("Expected history to be limited to 100, got %d", len(userData.History))
	}
}

func TestUserDataClearHistory(t *testing.T) {
	userData := NewUserData()

	// 添加历史记录
	userData.AddHistory("ls", "test")
	userData.AddHistory("cd", "test")

	if len(userData.History) != 2 {
		t.Errorf("Expected 2 history entries, got %d", len(userData.History))
	}

	// 清空历史
	userData.ClearHistory()

	if len(userData.History) != 0 {
		t.Errorf("Expected 0 history entries after clear, got %d", len(userData.History))
	}
}

func TestUserDataSaveAndLoad(t *testing.T) {
	// 创建临时目录
	tmpDir := t.TempDir()
	dataPath := filepath.Join(tmpDir, "userdata.json")

	// 创建用户数据
	userData := NewUserData()
	userData.AddFavorite("ls", "操作系统/Linux", "list files")
	userData.AddHistory("cd", "操作系统/Linux")

	// 保存
	if err := userData.Save(dataPath); err != nil {
		t.Fatalf("Save() error = %v", err)
	}

	// 加载
	loaded, err := LoadUserData(dataPath)
	if err != nil {
		t.Fatalf("LoadUserData() error = %v", err)
	}

	// 验证
	if len(loaded.Favorites) != 1 {
		t.Errorf("Expected 1 favorite, got %d", len(loaded.Favorites))
	}

	if len(loaded.History) != 1 {
		t.Errorf("Expected 1 history entry, got %d", len(loaded.History))
	}

	if loaded.Favorites[0].CommandName != "ls" {
		t.Errorf("Expected favorite ls, got %s", loaded.Favorites[0].CommandName)
	}
}

func TestUserDataLoadNonExistent(t *testing.T) {
	userData, err := LoadUserData("/nonexistent/path/userdata.json")
	if err != nil {
		t.Fatalf("LoadUserData() should not error on non-existent file, got %v", err)
	}

	if userData == nil {
		t.Fatal("LoadUserData() should return new user data")
	}

	if len(userData.Favorites) != 0 {
		t.Errorf("Expected 0 favorites, got %d", len(userData.Favorites))
	}
}

func TestFavoriteStructure(t *testing.T) {
	now := time.Now()
	fav := Favorite{
		CommandName: "ls",
		Category:    "操作系统/Linux",
		Note:        "test note",
		AddedAt:     now,
	}

	if fav.CommandName != "ls" {
		t.Errorf("Expected command name ls, got %s", fav.CommandName)
	}

	if fav.Note != "test note" {
		t.Errorf("Expected note 'test note', got %s", fav.Note)
	}
}

func TestHistoryEntryStructure(t *testing.T) {
	now := time.Now()
	entry := HistoryEntry{
		CommandName: "cd",
		Category:    "操作系统/Linux",
		AccessedAt:  now,
	}

	if entry.CommandName != "cd" {
		t.Errorf("Expected command name cd, got %s", entry.CommandName)
	}

	if entry.AccessedAt != now {
		t.Errorf("Expected accessed at %v, got %v", now, entry.AccessedAt)
	}
}

func TestUserData_AddFavorite_DuplicatePrevention(t *testing.T) {
	ud := NewUserData()

	ud.AddFavorite("git", "vcs", "")
	ud.AddFavorite("git", "vcs", "different note")

	if len(ud.Favorites) != 1 {
		t.Fatalf("expected 1 favorite, got %d", len(ud.Favorites))
	}

	if ud.Favorites[0].Note != "" {
		t.Errorf("note should remain empty after duplicate add, got %q", ud.Favorites[0].Note)
	}
}

func TestUserData_RemoveFavorite_NotExists(t *testing.T) {
	ud := NewUserData()
	ud.AddFavorite("ls", "os", "")

	ud.RemoveFavorite("nonexistent")

	if len(ud.Favorites) != 1 {
		t.Fatalf("expected 1 favorite after removing nonexistent, got %d", len(ud.Favorites))
	}
}

func TestUserData_AddHistory_DedupAndOrdering(t *testing.T) {
	ud := NewUserData()

	ud.AddHistory("a", "cat1")
	ud.AddHistory("b", "cat1")
	ud.AddHistory("c", "cat1")
	ud.AddHistory("a", "cat1")

	if len(ud.History) != 3 {
		t.Fatalf("expected 3 entries, got %d", len(ud.History))
	}

	if ud.History[0].CommandName != "a" {
		t.Errorf("expected first entry to be 'a' after re-add, got %q", ud.History[0].CommandName)
	}
	if ud.History[1].CommandName != "c" {
		t.Errorf("expected second entry to be 'c', got %q", ud.History[1].CommandName)
	}
	if ud.History[2].CommandName != "b" {
		t.Errorf("expected third entry to be 'b', got %q", ud.History[2].CommandName)
	}
}

func TestUserData_GetRecentHistory_ZeroLimit(t *testing.T) {
	ud := NewUserData()
	ud.AddHistory("ls", "os")

	recent := ud.GetRecentHistory(0)
	if recent != nil {
		t.Fatalf("expected nil for limit 0, got %v", recent)
	}
}

func TestUserData_GetRecentHistory_NegativeLimit(t *testing.T) {
	ud := NewUserData()
	ud.AddHistory("ls", "os")

	recent := ud.GetRecentHistory(-1)
	if recent != nil {
		t.Fatalf("expected nil for negative limit, got %v", recent)
	}
}

func TestUserData_ClearHistory_Empty(t *testing.T) {
	ud := NewUserData()
	ud.ClearHistory()

	if len(ud.History) != 0 {
		t.Fatalf("expected 0 entries after clear of empty history, got %d", len(ud.History))
	}
}

func TestMetadata_Validate(t *testing.T) {
	t.Run("valid metadata", func(t *testing.T) {
		m := Metadata{
			Version:   "1.0",
			DataFiles: []string{"data.yaml"},
			Categories: map[string]Category{
				"cat1": {ID: "cat1", Name: "Cat1", Order: 1},
			},
		}
		if err := m.Validate(); err != nil {
			t.Errorf("expected valid, got err: %v", err)
		}
	})

	t.Run("missing version", func(t *testing.T) {
		m := Metadata{
			DataFiles:  []string{"data.yaml"},
			Categories: map[string]Category{"cat1": {ID: "cat1", Name: "Cat1", Order: 1}},
		}
		if err := m.Validate(); err == nil {
			t.Error("expected error for missing version")
		}
	})

	t.Run("missing categories", func(t *testing.T) {
		m := Metadata{
			Version:   "1.0",
			DataFiles: []string{"data.yaml"},
		}
		if err := m.Validate(); err == nil {
			t.Error("expected error for missing categories")
		}
	})

	t.Run("missing data files", func(t *testing.T) {
		m := Metadata{
			Version:    "1.0",
			Categories: map[string]Category{"cat1": {ID: "cat1", Name: "Cat1", Order: 1}},
		}
		if err := m.Validate(); err == nil {
			t.Error("expected error for missing data files")
		}
	})

	t.Run("invalid category in metadata", func(t *testing.T) {
		m := Metadata{
			Version:   "1.0",
			DataFiles: []string{"data.yaml"},
			Categories: map[string]Category{
				"bad": {ID: "", Name: "Bad", Order: 1},
			},
		}
		if err := m.Validate(); err == nil {
			t.Error("expected error for invalid category in metadata")
		}
	})
}

func TestCommandList_Validate(t *testing.T) {
	t.Run("valid command list", func(t *testing.T) {
		cl := &CommandList{
			Category:    "test-cat",
			Description: "test desc",
			Commands: []*Command{
				{
					Name:        "cmd1",
					Category:    "test-cat",
					Description: "a command",
					Usage:       []string{"cmd1"},
					Examples:    []Example{{Command: "cmd1", Description: "test"}},
					Platforms:   []string{"linux"},
				},
			},
		}
		if err := cl.Validate(); err != nil {
			t.Errorf("expected valid, got err: %v", err)
		}
	})

	t.Run("missing category", func(t *testing.T) {
		cl := &CommandList{Description: "test"}
		if err := cl.Validate(); err == nil {
			t.Error("expected error for missing category")
		}
	})

	t.Run("missing description", func(t *testing.T) {
		cl := &CommandList{Category: "test"}
		if err := cl.Validate(); err == nil {
			t.Error("expected error for missing description")
		}
	})

	t.Run("invalid command in list", func(t *testing.T) {
		cl := &CommandList{
			Category:    "test-cat",
			Description: "test desc",
			Commands: []*Command{
				{Name: "bad-cmd"},
			},
		}
		if err := cl.Validate(); err == nil {
			t.Error("expected error for invalid command in list")
		}
	})
}
