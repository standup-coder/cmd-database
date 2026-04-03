package export

import (
	"fmt"
	"os"

	"github.com/cmd4coder/cmd4coder/internal/model"
	"github.com/cmd4coder/cmd4coder/internal/version"
	"gopkg.in/yaml.v3"
)

func ExportToYAML(commands []*model.Command, filename string) error {
	if err := ensureDir(filename); err != nil {
		return fmt.Errorf("failed to create directory: %w", err)
	}

	export := struct {
		Version  string           `yaml:"version"`
		Total    int              `yaml:"total"`
		Commands []*model.Command `yaml:"commands"`
	}{
		Version:  version.Version,
		Total:    len(commands),
		Commands: commands,
	}

	data, err := yaml.Marshal(export)
	if err != nil {
		return fmt.Errorf("failed to marshal YAML: %w", err)
	}

	if err := os.WriteFile(filename, data, 0644); err != nil {
		return fmt.Errorf("failed to write file: %w", err)
	}

	return nil
}
