package model

import (
	"errors"
	"fmt"
	"strings"
	"testing"
)

func TestCommand_Validate(t *testing.T) {
	tests := []struct {
		name    string
		cmd     Command
		wantErr bool
	}{
		{
			name: "valid command",
			cmd: Command{
				Name:            "ls",
				Category:        "操作系统/通用Linux命令",
				InstallRequired: false,
				Description:     "列出目录内容",
				Usage:           []string{"ls [选项] [目录]"},
				Platforms:       []string{"linux", "darwin"},
				Examples: []Example{
					{Command: "ls -l", Description: "长格式列表"},
				},
			},
			wantErr: false,
		},
		{
			name: "missing name",
			cmd: Command{
				Category:    "操作系统/通用Linux命令",
				Description: "列出目录内容",
			},
			wantErr: true,
		},
		{
			name: "missing category",
			cmd: Command{
				Name:        "ls",
				Description: "列出目录内容",
			},
			wantErr: true,
		},
		{
			name: "missing description",
			cmd: Command{
				Name:     "ls",
				Category: "操作系统/通用Linux命令",
			},
			wantErr: true,
		},
		{
			name: "invalid risk level",
			cmd: Command{
				Name:        "test",
				Category:    "test",
				Description: "test",
				Platforms:   []string{"linux"},
				Risks: []Risk{
					{Level: "invalid", Description: "test"},
				},
			},
			wantErr: true,
		},
		{
			name: "valid risk levels",
			cmd: Command{
				Name:        "test",
				Category:    "test",
				Description: "test",
				Platforms:   []string{"linux"},
				Usage:       []string{"test"},
				Examples:    []Example{{Command: "test", Description: "test"}},
				Risks: []Risk{
					{Level: RiskLevelLow, Description: "low risk"},
					{Level: RiskLevelMedium, Description: "medium risk"},
					{Level: RiskLevelHigh, Description: "high risk"},
					{Level: RiskLevelCritical, Description: "critical risk"},
				},
			},
			wantErr: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := tt.cmd.Validate()
			if (err != nil) != tt.wantErr {
				t.Errorf("Command.Validate() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestRiskLevel_IsValid(t *testing.T) {
	tests := []struct {
		name  string
		level RiskLevel
		want  bool
	}{
		{"low", RiskLevelLow, true},
		{"medium", RiskLevelMedium, true},
		{"high", RiskLevelHigh, true},
		{"critical", RiskLevelCritical, true},
		{"invalid", RiskLevel("invalid"), false},
		{"empty", RiskLevel(""), false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.level.IsValid(); got != tt.want {
				t.Errorf("RiskLevel.IsValid() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestCommand_GetRiskLevel(t *testing.T) {
	tests := []struct {
		name string
		cmd  Command
		want RiskLevel
	}{
		{
			name: "no risks",
			cmd:  Command{},
			want: RiskLevelLow,
		},
		{
			name: "low risk",
			cmd: Command{
				Risks: []Risk{{Level: RiskLevelLow}},
			},
			want: RiskLevelLow,
		},
		{
			name: "critical risk",
			cmd: Command{
				Risks: []Risk{
					{Level: RiskLevelLow},
					{Level: RiskLevelCritical},
				},
			},
			want: RiskLevelCritical,
		},
		{
			name: "high risk",
			cmd: Command{
				Risks: []Risk{
					{Level: RiskLevelMedium},
					{Level: RiskLevelHigh},
				},
			},
			want: RiskLevelHigh,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.cmd.GetRiskLevel(); got != tt.want {
				t.Errorf("Command.GetRiskLevel() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestCategory_Validate(t *testing.T) {
	tests := []struct {
		name     string
		cat      Category
		wantErr  bool
		errField string
	}{
		{
			name:    "valid category",
			cat:     Category{ID: "cat1", Name: "Test Category", Order: 1},
			wantErr: false,
		},
		{
			name:    "valid with parent",
			cat:     Category{ID: "sub1", Name: "Sub Category", Order: 2, Parent: "cat1"},
			wantErr: false,
		},
		{
			name:     "empty id",
			cat:      Category{ID: "", Name: "Test", Order: 0},
			wantErr:  true,
			errField: "category.id",
		},
		{
			name:     "empty name",
			cat:      Category{ID: "cat1", Name: "", Order: 0},
			wantErr:  true,
			errField: "category.name",
		},
		{
			name:     "negative order",
			cat:      Category{ID: "cat1", Name: "Test", Order: -1},
			wantErr:  true,
			errField: "category.order",
		},
		{
			name:    "zero order is valid",
			cat:     Category{ID: "cat1", Name: "Test", Order: 0},
			wantErr: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := tt.cat.Validate()
			if (err != nil) != tt.wantErr {
				t.Errorf("Category.Validate() error = %v, wantErr %v", err, tt.wantErr)
			}
			if tt.wantErr && tt.errField != "" {
				var mf ErrMissingField
				if !matchError(t, err, &mf) {
					t.Errorf("expected ErrMissingField, got %T: %v", err, err)
				} else if mf.Field != tt.errField {
					t.Errorf("expected field %q, got %q", tt.errField, mf.Field)
				}
			}
		})
	}
}

func TestCategory_IsTopLevel(t *testing.T) {
	tests := []struct {
		cat  Category
		want bool
	}{
		{Category{ID: "cat1", Parent: ""}, true},
		{Category{ID: "sub1", Parent: "cat1"}, false},
	}
	for _, tt := range tests {
		if got := tt.cat.IsTopLevel(); got != tt.want {
			t.Errorf("Category.IsTopLevel() = %v, want %v", got, tt.want)
		}
	}
}

func TestErrorTypes(t *testing.T) {
	t.Run("ErrMissingField", func(t *testing.T) {
		err := ErrMissingField{Field: "name"}
		got := err.Error()
		want := "missing required field: name"
		if got != want {
			t.Errorf("ErrMissingField.Error() = %q, want %q", got, want)
		}
	})

	t.Run("ErrInvalidRiskLevel", func(t *testing.T) {
		err := ErrInvalidRiskLevel{Command: "rm", Index: 0, Level: "extreme"}
		got := err.Error()
		want := "invalid risk level 'extreme' in command 'rm' at index 0"
		if got != want {
			t.Errorf("ErrInvalidRiskLevel.Error() = %q, want %q", got, want)
		}
	})

	t.Run("ErrDuplicateCommand", func(t *testing.T) {
		err := ErrDuplicateCommand{Name: "ls"}
		got := err.Error()
		want := "duplicate command: ls"
		if got != want {
			t.Errorf("ErrDuplicateCommand.Error() = %q, want %q", got, want)
		}
	})

	t.Run("ErrCommandNotFound", func(t *testing.T) {
		err := ErrCommandNotFound{Name: "foobar"}
		got := err.Error()
		want := "command not found: foobar"
		if got != want {
			t.Errorf("ErrCommandNotFound.Error() = %q, want %q", got, want)
		}
	})

	t.Run("ErrDataLoadFailed", func(t *testing.T) {
		inner := fmt.Errorf("file not found")
		err := ErrDataLoadFailed{File: "data.yaml", Err: inner}
		got := err.Error()
		if !strings.Contains(got, "data.yaml") || !strings.Contains(got, "file not found") {
			t.Errorf("ErrDataLoadFailed.Error() = %q, want file and inner error", got)
		}
		unwrapped := err.Unwrap()
		if unwrapped != inner {
			t.Errorf("ErrDataLoadFailed.Unwrap() = %v, want %v", unwrapped, inner)
		}
	})

	t.Run("ErrDataLoadFailed_NilErr", func(t *testing.T) {
		err := ErrDataLoadFailed{File: "data.yaml", Err: nil}
		unwrapped := err.Unwrap()
		if unwrapped != nil {
			t.Errorf("expected nil Unwrap, got %v", unwrapped)
		}
	})
}

func matchError(t *testing.T, err error, target interface{}) bool {
	t.Helper()
	switch target.(type) {
	case *ErrMissingField:
		var mf ErrMissingField
		if !errors.As(err, &mf) {
			return false
		}
		*target.(*ErrMissingField) = mf
		return true
	}
	return false
}

func TestCommand_Validate_Platforms(t *testing.T) {
	validPlatforms := []string{"linux", "darwin", "windows", "unix"}
	invalidPlatforms := []string{"macos", "linus", "freebsd", "", "LINUX"}

	for _, p := range validPlatforms {
		t.Run("valid_platform_"+p, func(t *testing.T) {
			cmd := Command{
				Name:        "test",
				Category:    "test",
				Description: "test",
				Platforms:   []string{p},
				Usage:       []string{"test"},
				Examples:    []Example{{Command: "test", Description: "test"}},
			}
			if err := cmd.Validate(); err != nil {
				t.Errorf("platform %q should be valid, got err: %v", p, err)
			}
		})
	}

	for _, p := range invalidPlatforms {
		t.Run("invalid_platform_"+p, func(t *testing.T) {
			cmd := Command{
				Name:        "test",
				Category:    "test",
				Description: "test",
				Platforms:   []string{p},
				Usage:       []string{"test"},
				Examples:    []Example{{Command: "test", Description: "test"}},
			}
			if err := cmd.Validate(); err == nil {
				t.Errorf("platform %q should be invalid", p)
			}
		})
	}
}

func TestCommand_Validate_MissingFields(t *testing.T) {
	tests := []struct {
		name    string
		cmd     Command
		wantErr bool
	}{
		{
			name:    "missing usage",
			cmd:     Command{Name: "t", Category: "t", Description: "t", Platforms: []string{"linux"}, Examples: []Example{{Command: "t", Description: "t"}}},
			wantErr: true,
		},
		{
			name:    "missing examples",
			cmd:     Command{Name: "t", Category: "t", Description: "t", Platforms: []string{"linux"}, Usage: []string{"t"}},
			wantErr: true,
		},
		{
			name:    "missing platforms",
			cmd:     Command{Name: "t", Category: "t", Description: "t", Usage: []string{"t"}, Examples: []Example{{Command: "t", Description: "t"}}},
			wantErr: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := tt.cmd.Validate()
			if (err != nil) != tt.wantErr {
				t.Errorf("Command.Validate() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestCommand_SupportsPlatform(t *testing.T) {
	cmd := Command{
		Platforms: []string{"linux", "darwin"},
	}

	tests := []struct {
		platform string
		want     bool
	}{
		{"linux", true},
		{"darwin", true},
		{"windows", false},
		{"", false},
	}

	for _, tt := range tests {
		t.Run(tt.platform, func(t *testing.T) {
			if got := cmd.SupportsPlatform(tt.platform); got != tt.want {
				t.Errorf("Command.SupportsPlatform(%v) = %v, want %v", tt.platform, got, tt.want)
			}
		})
	}
}
