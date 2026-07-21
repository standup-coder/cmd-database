package export

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"

	"github.com/cmd4coder/cmd4coder/internal/model"
	"github.com/cmd4coder/cmd4coder/internal/version"
)

func ensureDir(filename string) error {
	dir := filepath.Dir(filename)
	return os.MkdirAll(dir, 0755)
}

// ExportToJSON 导出命令到JSON格式
func ExportToJSON(commands []*model.Command, filename string) error {
	if err := ensureDir(filename); err != nil {
		return fmt.Errorf("failed to create directory: %w", err)
	}
	// 创建文件
	f, err := os.Create(filename)
	if err != nil {
		return fmt.Errorf("failed to create file: %w", err)
	}
	defer f.Close()

	// 创建导出结构
	export := struct {
		Version  string           `json:"version"`
		Total    int              `json:"total"`
		Commands []*model.Command `json:"commands"`
	}{
		Version:  version.Version,
		Total:    len(commands),
		Commands: commands,
	}

	// 编码为JSON（格式化输出）
	encoder := json.NewEncoder(f)
	encoder.SetIndent("", "  ")

	if err := encoder.Encode(export); err != nil {
		return fmt.Errorf("failed to encode JSON: %w", err)
	}

	return nil
}

// ExportToJSONCompact 导出为紧凑的JSON格式
func ExportToJSONCompact(commands []*model.Command, filename string) error {
	if err := ensureDir(filename); err != nil {
		return fmt.Errorf("failed to create directory: %w", err)
	}
	data, err := json.Marshal(commands)
	if err != nil {
		return fmt.Errorf("failed to marshal JSON: %w", err)
	}

	if err := os.WriteFile(filename, data, 0644); err != nil {
		return fmt.Errorf("failed to write file: %w", err)
	}

	return nil
}
