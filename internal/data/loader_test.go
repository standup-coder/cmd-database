package data

import (
	"testing"
)

func TestLoaderLoadMetadata(t *testing.T) {
	loader := NewLoader("")
	metadata, err := loader.LoadMetadata()
	if err != nil {
		t.Fatalf("LoadMetadata() error = %v", err)
	}

	if metadata.Version == "" {
		t.Error("expected non-empty version")
	}

	if len(metadata.Categories) == 0 {
		t.Error("expected non-empty categories")
	}

	if len(metadata.DataFiles) == 0 {
		t.Error("expected non-empty data files")
	}
}

func TestLoaderLoadAllCommands(t *testing.T) {
	loader := NewLoader("")
	commands, err := loader.LoadAllCommands()
	if err != nil {
		t.Fatalf("LoadAllCommands() error = %v", err)
	}

	if len(commands) < 10 {
		t.Errorf("expected at least 10 commands, got %d", len(commands))
	}

	seen := make(map[string]bool)
	for _, cmd := range commands {
		if seen[cmd.Name] {
			t.Errorf("duplicate command name: %s", cmd.Name)
		}
		seen[cmd.Name] = true
	}
}

func TestLoaderLoadCommandList(t *testing.T) {
	loader := NewLoader("")

	metadata, err := loader.LoadMetadata()
	if err != nil {
		t.Fatalf("LoadMetadata() error = %v", err)
	}

	if len(metadata.DataFiles) == 0 {
		t.Skip("no data files")
	}

	cmdList, err := loader.LoadCommandList(metadata.DataFiles[0])
	if err != nil {
		t.Fatalf("LoadCommandList() error = %v", err)
	}

	if cmdList.Category == "" {
		t.Error("expected non-empty category")
	}

	if len(cmdList.Commands) == 0 {
		t.Error("expected at least one command")
	}
}

func TestLoaderLoadInvalidFile(t *testing.T) {
	loader := NewLoader("")
	_, err := loader.LoadCommandList("nonexistent.yaml")
	if err == nil {
		t.Error("expected error for nonexistent file")
	}
}

func TestLoaderGetMetadata(t *testing.T) {
	loader := NewLoader("")

	metadata := loader.GetMetadata()
	if metadata != nil {
		t.Error("expected nil metadata before LoadMetadata")
	}

	_, err := loader.LoadMetadata()
	if err != nil {
		t.Fatalf("LoadMetadata() error = %v", err)
	}

	metadata = loader.GetMetadata()
	if metadata == nil {
		t.Error("expected non-nil metadata after LoadMetadata")
	}
}

func TestLoaderReadDataFile(t *testing.T) {
	loader := NewLoader("")

	data, err := loader.readDataFile("metadata.yaml")
	if err != nil {
		t.Fatalf("readDataFile() error = %v", err)
	}
	if len(data) == 0 {
		t.Error("expected non-empty data")
	}

	_, err = loader.readDataFile("nonexistent.yaml")
	if err == nil {
		t.Error("expected error for nonexistent file")
	}
}
