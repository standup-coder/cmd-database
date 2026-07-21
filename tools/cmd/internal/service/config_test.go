package service

import (
	"path/filepath"
	"testing"

	"github.com/cmd4coder/cmd4coder/internal/model"
)

func newTestConfigService(t *testing.T) *ConfigService {
	t.Helper()
	svc, err := NewConfigServiceWithDir(t.TempDir())
	if err != nil {
		t.Fatalf("NewConfigServiceWithDir() error = %v", err)
	}
	return svc
}

func TestConfigServiceNew(t *testing.T) {
	svc := newTestConfigService(t)

	config := svc.GetConfig()
	if config.Language == "" {
		t.Error("expected non-empty language")
	}
}

func TestConfigServiceSetLanguage(t *testing.T) {
	svc := newTestConfigService(t)

	if err := svc.SetLanguage("en"); err != nil {
		t.Fatalf("SetLanguage() error = %v", err)
	}

	config := svc.GetConfig()
	if config.Language != "en" {
		t.Errorf("expected language 'en', got '%s'", config.Language)
	}
}

func TestConfigServiceSetTheme(t *testing.T) {
	svc := newTestConfigService(t)

	if err := svc.SetTheme("dark"); err != nil {
		t.Fatalf("SetTheme() error = %v", err)
	}

	config := svc.GetConfig()
	if config.Theme != "dark" {
		t.Errorf("expected theme 'dark', got '%s'", config.Theme)
	}
}

func TestConfigServiceSetPageSize(t *testing.T) {
	svc := newTestConfigService(t)

	if err := svc.SetPageSize(50); err != nil {
		t.Fatalf("SetPageSize() error = %v", err)
	}

	config := svc.GetConfig()
	if config.PageSize != 50 {
		t.Errorf("expected page size 50, got %d", config.PageSize)
	}
}

func TestConfigServiceSetLanguageInvalid(t *testing.T) {
	svc := newTestConfigService(t)

	err := svc.SetLanguage("fr")
	if err == nil {
		t.Error("expected error for invalid language")
	}
}

func TestConfigServiceSetPageSizeInvalid(t *testing.T) {
	svc := newTestConfigService(t)

	err := svc.SetPageSize(0)
	if err == nil {
		t.Error("expected error for invalid page size")
	}
}

func TestConfigServiceFavorites(t *testing.T) {
	svc := newTestConfigService(t)

	err := svc.AddFavorite("ls", "操作系统/Linux", "list files")
	if err != nil {
		t.Fatalf("AddFavorite() error = %v", err)
	}

	if !svc.IsFavorite("ls") {
		t.Error("expected ls to be favorite")
	}

	favs := svc.GetFavorites()
	if len(favs) == 0 {
		t.Error("expected at least 1 favorite")
	}

	err = svc.RemoveFavorite("ls")
	if err != nil {
		t.Fatalf("RemoveFavorite() error = %v", err)
	}

	if svc.IsFavorite("ls") {
		t.Error("expected ls to not be favorite after removal")
	}

	err = svc.RemoveFavorite("nonexistent")
	if err != nil {
		t.Fatalf("RemoveFavorite() nonexistent error = %v", err)
	}
}

func TestConfigServiceHistory(t *testing.T) {
	svc := newTestConfigService(t)

	err := svc.AddHistory("ls", "操作系统/Linux")
	if err != nil {
		t.Fatalf("AddHistory() error = %v", err)
	}

	err = svc.AddHistory("cd", "操作系统/Linux")
	if err != nil {
		t.Fatalf("AddHistory() error = %v", err)
	}

	recent := svc.GetRecentHistory(10)
	if len(recent) < 2 {
		t.Errorf("expected at least 2 recent entries, got %d", len(recent))
	}

	if recent[0].CommandName != "cd" {
		t.Errorf("expected most recent to be 'cd', got '%s'", recent[0].CommandName)
	}

	err = svc.ClearHistory()
	if err != nil {
		t.Fatalf("ClearHistory() error = %v", err)
	}

	recent = svc.GetRecentHistory(10)
	if len(recent) != 0 {
		t.Errorf("expected 0 entries after clear, got %d", len(recent))
	}
}

func TestConfigServiceGetRecentHistoryZeroLimit(t *testing.T) {
	svc := newTestConfigService(t)

	recent := svc.GetRecentHistory(0)
	if len(recent) != 0 {
		t.Errorf("expected 0 entries for limit 0, got %d", len(recent))
	}

	recent = svc.GetRecentHistory(-1)
	if len(recent) != 0 {
		t.Errorf("expected 0 entries for limit -1, got %d", len(recent))
	}
}

func TestConfigServiceSetDefaultExportFormat(t *testing.T) {
	svc := newTestConfigService(t)

	if err := svc.SetDefaultExportFormat("json"); err != nil {
		t.Fatalf("SetDefaultExportFormat() error = %v", err)
	}

	config := svc.GetConfig()
	if config.Export.DefaultFormat != "json" {
		t.Errorf("expected format 'json', got '%s'", config.Export.DefaultFormat)
	}
}

func TestConfigServiceSaveUserData(t *testing.T) {
	svc := newTestConfigService(t)

	if err := svc.SaveUserData(); err != nil {
		t.Fatalf("SaveUserData() error = %v", err)
	}
}

func TestConfigServiceGetUserData(t *testing.T) {
	svc := newTestConfigService(t)

	svc.AddHistory("git", "版本控制/Git命令")
	ud := svc.GetUserData()
	if ud == nil {
		t.Fatal("expected non-nil UserData")
	}
}

func TestConfigModelSaveAndLoad(t *testing.T) {
	tmpDir := t.TempDir()
	configPath := filepath.Join(tmpDir, "config.json")

	config := model.DefaultConfig()
	config.Language = "en"
	config.PageSize = 50

	if err := config.Save(configPath); err != nil {
		t.Fatalf("Save() error = %v", err)
	}

	loaded, err := model.LoadConfig(configPath)
	if err != nil {
		t.Fatalf("LoadConfig() error = %v", err)
	}

	if loaded.Language != "en" {
		t.Errorf("expected language 'en', got '%s'", loaded.Language)
	}

	if loaded.PageSize != 50 {
		t.Errorf("expected page size 50, got %d", loaded.PageSize)
	}
}

func TestConfigModelLoadNonExistent(t *testing.T) {
	config, err := model.LoadConfig(filepath.Join(t.TempDir(), "nonexistent.json"))
	if err != nil {
		t.Fatalf("LoadConfig() should not error on non-existent file, got %v", err)
	}
	if config == nil {
		t.Fatal("LoadConfig() should return default config")
	}
	if config.Language != "zh" {
		t.Errorf("expected default language 'zh', got '%s'", config.Language)
	}
}

func TestConfigModelValidate(t *testing.T) {
	tests := []struct {
		name    string
		config  *model.Config
		wantErr bool
	}{
		{
			name:   "valid default",
			config: model.DefaultConfig(),
		},
		{
			name: "invalid page size 0",
			config: &model.Config{
				Language: "zh", PageSize: 0,
				Search: model.SearchConfig{MaxResults: 10, CacheSize: 10},
				Export: model.ExportConfig{DefaultFormat: "markdown"},
			},
			wantErr: true,
		},
		{
			name: "invalid language",
			config: &model.Config{
				Language: "fr", PageSize: 10,
				Search: model.SearchConfig{MaxResults: 10, CacheSize: 10},
				Export: model.ExportConfig{DefaultFormat: "markdown"},
			},
			wantErr: true,
		},
		{
			name: "invalid export format",
			config: &model.Config{
				Language: "zh", PageSize: 10,
				Search: model.SearchConfig{MaxResults: 10, CacheSize: 10},
				Export: model.ExportConfig{DefaultFormat: "xml"},
			},
			wantErr: true,
		},
		{
			name: "invalid max results 0",
			config: &model.Config{
				Language: "zh", PageSize: 10,
				Search: model.SearchConfig{MaxResults: 0, CacheSize: 10},
				Export: model.ExportConfig{DefaultFormat: "markdown"},
			},
			wantErr: true,
		},
		{
			name: "invalid cache size 0",
			config: &model.Config{
				Language: "zh", PageSize: 10,
				Search: model.SearchConfig{MaxResults: 10, CacheSize: 0},
				Export: model.ExportConfig{DefaultFormat: "markdown"},
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

func TestGetRecentHistoryPanicGuard(t *testing.T) {
	ud := model.NewUserData()
	ud.AddHistory("a", "cat")

	result := ud.GetRecentHistory(0)
	if result != nil {
		t.Errorf("expected nil for limit 0, got %v", result)
	}

	result = ud.GetRecentHistory(-5)
	if result != nil {
		t.Errorf("expected nil for negative limit, got %v", result)
	}
}

func TestUpdateConfigMutationSafety(t *testing.T) {
	svc := newTestConfigService(t)

	original := svc.GetConfig()

	err := svc.UpdateConfig(func(c *model.Config) {
		c.PageSize = -1
	})
	if err == nil {
		t.Fatal("expected error for invalid PageSize -1")
	}

	after := svc.GetConfig()
	if after.PageSize != original.PageSize {
		t.Errorf("PageSize mutated after failed update: was %d, now %d", original.PageSize, after.PageSize)
	}
}

func TestSetTheme(t *testing.T) {
	svc := newTestConfigService(t)

	tests := []struct {
		theme   string
		wantErr bool
	}{
		{"default", false},
		{"dark", false},
		{"light", false},
		{"nonexistent", true},
	}

	for _, tt := range tests {
		t.Run(tt.theme, func(t *testing.T) {
			err := svc.SetTheme(tt.theme)
			if (err != nil) != tt.wantErr {
				t.Errorf("SetTheme(%q) error = %v, wantErr %v", tt.theme, err, tt.wantErr)
			}
		})
	}
}

func TestSetPageSizeValidAndInvalid(t *testing.T) {
	svc := newTestConfigService(t)

	tests := []struct {
		name    string
		size    int
		wantErr bool
	}{
		{"positive", 10, false},
		{"large", 1000, false},
		{"zero", 0, true},
		{"negative", -1, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := svc.SetPageSize(tt.size)
			if (err != nil) != tt.wantErr {
				t.Errorf("SetPageSize(%d) error = %v, wantErr %v", tt.size, err, tt.wantErr)
			}
		})
	}
}

func TestSaveConfig(t *testing.T) {
	tmpDir := t.TempDir()
	svc, err := NewConfigServiceWithDir(tmpDir)
	if err != nil {
		t.Fatalf("NewConfigServiceWithDir() error = %v", err)
	}

	if err := svc.SetPageSize(42); err != nil {
		t.Fatalf("SetPageSize() error = %v", err)
	}

	if err := svc.SaveConfig(); err != nil {
		t.Fatalf("SaveConfig() error = %v", err)
	}

	svc2, err := NewConfigServiceWithDir(tmpDir)
	if err != nil {
		t.Fatalf("NewConfigServiceWithDir() reload error = %v", err)
	}

	config := svc2.GetConfig()
	if config.PageSize != 42 {
		t.Errorf("expected PageSize 42 after reload, got %d", config.PageSize)
	}
}
