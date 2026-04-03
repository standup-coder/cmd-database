package data

import (
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"sync"

	rootpkg "github.com/cmd4coder/cmd4coder"
	"github.com/cmd4coder/cmd4coder/internal/model"
	"gopkg.in/yaml.v3"
)

// Loader 数据加载器
type Loader struct {
	dataDir  string
	metadata *model.Metadata
	mu       sync.RWMutex
}

// NewLoader 创建数据加载器，优先使用本地 data 目录，不存在时回退到嵌入数据
func NewLoader(dataDir string) *Loader {
	return &Loader{
		dataDir: dataDir,
	}
}

const embedPrefix = "data"

// readDataFile reads a data file, preferring local filesystem over embedded data
func (l *Loader) readDataFile(path string) ([]byte, error) {
	if l.dataDir != "" {
		fullPath := filepath.Join(l.dataDir, path)
		absPath, err := filepath.Abs(fullPath)
		if err != nil {
			return nil, err
		}
		absDataDir, err := filepath.Abs(l.dataDir)
		if err != nil {
			return nil, err
		}
		if !strings.HasPrefix(absPath, absDataDir+string(filepath.Separator)) {
			return nil, fmt.Errorf("path traversal detected: %s", path)
		}
		data, err := os.ReadFile(fullPath)
		if err == nil {
			return data, nil
		}
	}
	return rootpkg.EmbeddedData.ReadFile(filepath.Join(embedPrefix, path))
}

// LoadMetadata 加载元数据
func (l *Loader) LoadMetadata() (*model.Metadata, error) {
	l.mu.Lock()
	defer l.mu.Unlock()

	data, err := l.readDataFile("metadata.yaml")
	if err != nil {
		return nil, model.ErrDataLoadFailed{File: "metadata.yaml", Err: err}
	}

	var metadata model.Metadata
	if err := yaml.Unmarshal(data, &metadata); err != nil {
		return nil, model.ErrDataLoadFailed{File: "metadata.yaml", Err: err}
	}

	if err := metadata.Validate(); err != nil {
		return nil, err
	}

	l.metadata = &metadata
	return &metadata, nil
}

// LoadCommandList 加载单个命令列表文件
func (l *Loader) LoadCommandList(filePath string) (*model.CommandList, error) {
	data, err := l.readDataFile(filePath)
	if err != nil {
		return nil, model.ErrDataLoadFailed{File: filePath, Err: err}
	}

	var cmdList model.CommandList
	if err := yaml.Unmarshal(data, &cmdList); err != nil {
		return nil, model.ErrDataLoadFailed{File: filePath, Err: err}
	}

	if err := cmdList.Validate(); err != nil {
		return nil, err
	}

	return &cmdList, nil
}

// LoadAllCommands 加载所有命令
func (l *Loader) LoadAllCommands() ([]*model.Command, error) {
	metadata, err := l.LoadMetadata()
	if err != nil {
		return nil, err
	}

	type cmdResult struct {
		commands []*model.Command
		err      error
	}

	results := make(chan cmdResult, len(metadata.DataFiles))
	var wg sync.WaitGroup

	for _, dataFile := range metadata.DataFiles {
		wg.Add(1)
		go func(file string) {
			defer wg.Done()
			cmdList, err := l.LoadCommandList(file)
			if err != nil {
				results <- cmdResult{err: err}
				return
			}
			results <- cmdResult{commands: cmdList.Commands}
		}(dataFile)
	}

	wg.Wait()
	close(results)

	seen := make(map[string]struct{})
	var allCommands []*model.Command
	var duplicates []string

	for r := range results {
		if r.err != nil {
			return nil, r.err
		}
		for _, cmd := range r.commands {
			if _, exists := seen[cmd.Name]; exists {
				duplicates = append(duplicates, cmd.Name)
				continue
			}
			seen[cmd.Name] = struct{}{}
			allCommands = append(allCommands, cmd)
		}
	}

	if len(duplicates) > 0 {
		absDataDir, err := filepath.Abs(l.dataDir)
		if err != nil {
			absDataDir = l.dataDir
		}
		fmt.Fprintf(os.Stderr, "Warning: %d duplicate command(s) skipped: %v (data dir: %s)\n",
			len(duplicates), duplicates, absDataDir)
	}

	return allCommands, nil
}

// GetMetadata 获取元数据
func (l *Loader) GetMetadata() *model.Metadata {
	l.mu.RLock()
	defer l.mu.RUnlock()
	return l.metadata
}

// GetSortedCategories 获取按 order 排序的分类名列表
func (l *Loader) GetSortedCategories() []string {
	l.mu.RLock()
	defer l.mu.RUnlock()

	if l.metadata == nil {
		return nil
	}

	type catOrder struct {
		name  string
		order int
	}

	items := make([]catOrder, 0, len(l.metadata.Categories))
	for _, cat := range l.metadata.Categories {
		items = append(items, catOrder{name: cat.Name, order: cat.Order})
	}

	sort.Slice(items, func(i, j int) bool {
		return items[i].order < items[j].order
	})

	names := make([]string, len(items))
	for i, item := range items {
		names[i] = item.name
	}
	return names
}
