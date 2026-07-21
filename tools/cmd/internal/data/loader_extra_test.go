package data

import (
	"testing"
)

func TestGetSortedCategories(t *testing.T) {
	loader := NewLoader("")

	_, err := loader.LoadMetadata()
	if err != nil {
		t.Fatalf("LoadMetadata() error = %v", err)
	}

	cats := loader.GetSortedCategories()
	if len(cats) == 0 {
		t.Fatal("expected non-empty categories")
	}

	metadata := loader.GetMetadata()
	orders := make(map[string]int)
	for _, cat := range metadata.Categories {
		orders[cat.Name] = cat.Order
	}

	for i := 1; i < len(cats); i++ {
		prev, ok1 := orders[cats[i-1]]
		curr, ok2 := orders[cats[i]]
		if !ok1 || !ok2 {
			t.Fatalf("category name from GetSortedCategories not found in metadata: %q or %q", cats[i-1], cats[i])
		}
		if prev > curr {
			t.Errorf("categories not sorted by order: %q (order=%d) before %q (order=%d)", cats[i-1], prev, cats[i], curr)
		}
	}
}

func TestGetSortedCategories_NilMetadata(t *testing.T) {
	loader := NewLoader("")
	cats := loader.GetSortedCategories()
	if cats != nil {
		t.Errorf("expected nil when metadata not loaded, got %v", cats)
	}
}

func TestCountCommands(t *testing.T) {
	loader := NewLoader("")
	commands, err := loader.LoadAllCommands()
	if err != nil {
		t.Fatalf("LoadAllCommands() error = %v", err)
	}

	idx := NewIndex()
	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	count := idx.CountCommands()
	if count <= 0 {
		t.Errorf("expected positive command count, got %d", count)
	}
	if count != len(commands) {
		t.Errorf("CountCommands() = %d, want %d", count, len(commands))
	}
}

func TestCountCategories(t *testing.T) {
	loader := NewLoader("")
	commands, err := loader.LoadAllCommands()
	if err != nil {
		t.Fatalf("LoadAllCommands() error = %v", err)
	}

	idx := NewIndex()
	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	count := idx.CountCategories()
	if count <= 0 {
		t.Errorf("expected positive category count, got %d", count)
	}
}

func TestGetAllCommandNames_Integration(t *testing.T) {
	loader := NewLoader("")
	commands, err := loader.LoadAllCommands()
	if err != nil {
		t.Fatalf("LoadAllCommands() error = %v", err)
	}

	idx := NewIndex()
	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	names := idx.GetAllCommandNames()
	if len(names) != len(commands) {
		t.Errorf("GetAllCommandNames() returned %d names, want %d", len(names), len(commands))
	}

	nameSet := make(map[string]bool, len(names))
	for _, n := range names {
		if nameSet[n] {
			t.Errorf("duplicate name: %q", n)
		}
		nameSet[n] = true
	}

	for _, cmd := range commands {
		if !nameSet[cmd.Name] {
			t.Errorf("command %q missing from GetAllCommandNames()", cmd.Name)
		}
	}
}

func TestGetByPlatform(t *testing.T) {
	loader := NewLoader("")
	commands, err := loader.LoadAllCommands()
	if err != nil {
		t.Fatalf("LoadAllCommands() error = %v", err)
	}

	idx := NewIndex()
	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	tests := []struct {
		platform string
		wantGt   int
	}{
		{"linux", 0},
		{"darwin", 0},
		{"windows", 0},
		{"nonexistent_platform", 0},
	}

	for _, tt := range tests {
		t.Run(tt.platform, func(t *testing.T) {
			cmds := idx.GetByPlatform(tt.platform)
			if len(cmds) < tt.wantGt {
				t.Errorf("GetByPlatform(%q) returned %d commands, want at least %d", tt.platform, len(cmds), tt.wantGt)
			}

			if tt.platform == "nonexistent_platform" && len(cmds) != 0 {
				t.Errorf("GetByPlatform(%q) should return 0 commands, got %d", tt.platform, len(cmds))
			}

			for _, cmd := range cmds {
				found := false
				for _, p := range cmd.Platforms {
					if p == tt.platform {
						found = true
						break
					}
				}
				if !found {
					t.Errorf("command %q does not support platform %q", cmd.Name, tt.platform)
				}
			}
		})
	}
}

func TestGetAllCategories(t *testing.T) {
	loader := NewLoader("")
	commands, err := loader.LoadAllCommands()
	if err != nil {
		t.Fatalf("LoadAllCommands() error = %v", err)
	}

	idx := NewIndex()
	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	cats := idx.GetAllCategories()
	if len(cats) == 0 {
		t.Fatal("expected non-empty categories")
	}

	expectedCats := make(map[string]bool)
	for _, cmd := range commands {
		expectedCats[cmd.Category] = true
	}

	if len(cats) != len(expectedCats) {
		t.Errorf("GetAllCategories() returned %d categories, want %d", len(cats), len(expectedCats))
	}

	catSet := make(map[string]bool)
	for _, c := range cats {
		if !expectedCats[c] {
			t.Errorf("unexpected category %q", c)
		}
		if catSet[c] {
			t.Errorf("duplicate category %q", c)
		}
		catSet[c] = true
	}
}

func TestGetSortedCategories_MatchesMetadataCount(t *testing.T) {
	loader := NewLoader("")

	metadata, err := loader.LoadMetadata()
	if err != nil {
		t.Fatalf("LoadMetadata() error = %v", err)
	}

	cats := loader.GetSortedCategories()
	if len(cats) != len(metadata.Categories) {
		t.Errorf("GetSortedCategories() returned %d, want %d (metadata category count)", len(cats), len(metadata.Categories))
	}
}

func TestGetAllCommandNames_EmptyIndex(t *testing.T) {
	idx := NewIndex()
	names := idx.GetAllCommandNames()
	if len(names) != 0 {
		t.Errorf("expected 0 names from empty index, got %d", len(names))
	}
}

func TestCountCommands_EmptyIndex(t *testing.T) {
	idx := NewIndex()
	if idx.CountCommands() != 0 {
		t.Errorf("expected 0 commands from empty index")
	}
}

func TestCountCategories_EmptyIndex(t *testing.T) {
	idx := NewIndex()
	if idx.CountCategories() != 0 {
		t.Errorf("expected 0 categories from empty index")
	}
}

func TestGetAllCategories_EmptyIndex(t *testing.T) {
	idx := NewIndex()
	cats := idx.GetAllCategories()
	if len(cats) != 0 {
		t.Errorf("expected 0 categories from empty index, got %d", len(cats))
	}
}

func TestGetByPlatform_EmptyIndex(t *testing.T) {
	idx := NewIndex()
	cmds := idx.GetByPlatform("linux")
	if len(cmds) != 0 {
		t.Errorf("expected 0 commands from empty index, got %d", len(cmds))
	}
}

func TestGetAllCommandNames_NoDuplicates(t *testing.T) {
	loader := NewLoader("")
	commands, err := loader.LoadAllCommands()
	if err != nil {
		t.Fatalf("LoadAllCommands() error = %v", err)
	}

	idx := NewIndex()
	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	names := idx.GetAllCommandNames()
	nameSet := make(map[string]bool, len(names))
	for _, n := range names {
		if nameSet[n] {
			t.Errorf("duplicate name: %q", n)
		}
		nameSet[n] = true
	}

	if len(nameSet) != len(names) {
		t.Errorf("name count mismatch: set=%d, slice=%d", len(nameSet), len(names))
	}
}
