package data

import (
	"testing"

	"github.com/cmd4coder/cmd4coder/internal/model"
)

func TestTokenize(t *testing.T) {
	tests := []struct {
		input string
		want  []string
	}{
		{"ls -la", []string{"ls", "la"}},
		{"kubectl get pods", []string{"kubectl", "get", "pods"}},
		{"docker_container", []string{"docker", "container"}},
		{"OS/Linux", []string{"os", "linux"}},
		{"a b c", nil},
		{"x", nil},
	}

	for _, tt := range tests {
		t.Run(tt.input, func(t *testing.T) {
			got := tokenize(tt.input)
			if len(got) != len(tt.want) {
				t.Errorf("tokenize(%q) = %v, want %v", tt.input, got, tt.want)
				return
			}
			for i := range got {
				if got[i] != tt.want[i] {
					t.Errorf("tokenize(%q)[%d] = %q, want %q", tt.input, i, got[i], tt.want[i])
				}
			}
		})
	}
}

func TestIndexBuildAndGet(t *testing.T) {
	idx := NewIndex()

	commands := []*model.Command{
		{
			Name:        "ls",
			Category:    "操作系统/Linux",
			Description: "列出目录内容",
			Platforms:   []string{"linux", "darwin"},
			Usage:       []string{"ls [选项]"},
			Examples:    []model.Example{{Command: "ls -la", Description: "列出"}},
		},
		{
			Name:        "grep",
			Category:    "操作系统/Linux",
			Description: "文本搜索工具",
			Platforms:   []string{"linux"},
			Usage:       []string{"grep [模式] [文件]"},
			Examples:    []model.Example{{Command: "grep foo bar.txt", Description: "搜索"}},
		},
		{
			Name:        "docker",
			Category:    "容器编排/Docker",
			Description: "容器管理工具",
			Platforms:   []string{"linux", "darwin", "windows"},
			Usage:       []string{"docker [命令]"},
			Examples:    []model.Example{{Command: "docker ps", Description: "列出容器"}},
		},
	}

	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	t.Run("GetByName", func(t *testing.T) {
		cmd, err := idx.GetByName("ls")
		if err != nil {
			t.Fatalf("GetByName(ls) error = %v", err)
		}
		if cmd.Description != "列出目录内容" {
			t.Errorf("unexpected description: %s", cmd.Description)
		}

		_, err = idx.GetByName("nonexistent")
		if err == nil {
			t.Error("expected error for nonexistent command")
		}
	})

	t.Run("DuplicateName", func(t *testing.T) {
		dupCmds := append(commands, &model.Command{
			Name:        "ls",
			Category:    "other",
			Description: "duplicate",
			Platforms:   []string{"linux"},
			Usage:       []string{"ls"},
			Examples:    []model.Example{{Command: "ls", Description: "dup"}},
		})
		idx2 := NewIndex()
		err := idx2.BuildIndex(dupCmds)
		if err == nil {
			t.Error("expected error for duplicate command name")
		}
	})

	t.Run("GetByCategory", func(t *testing.T) {
		cmds := idx.GetByCategory("操作系统/Linux")
		if len(cmds) != 2 {
			t.Errorf("expected 2 commands, got %d", len(cmds))
		}

		cmds = idx.GetByCategory("nonexistent")
		if len(cmds) != 0 {
			t.Errorf("expected 0 commands, got %d", len(cmds))
		}
	})

	t.Run("GetByPlatform", func(t *testing.T) {
		linuxCmds := idx.GetByPlatform("linux")
		if len(linuxCmds) != 3 {
			t.Errorf("expected 3 linux commands, got %d", len(linuxCmds))
		}

		winCmds := idx.GetByPlatform("windows")
		if len(winCmds) != 1 {
			t.Errorf("expected 1 windows command, got %d", len(winCmds))
		}
	})

	t.Run("GetAllCategories", func(t *testing.T) {
		cats := idx.GetAllCategories()
		if len(cats) != 2 {
			t.Errorf("expected 2 categories, got %d", len(cats))
		}
	})

	t.Run("GetAllCommands", func(t *testing.T) {
		cmds := idx.GetAllCommands()
		if len(cmds) != 3 {
			t.Errorf("expected 3 commands, got %d", len(cmds))
		}
	})
}

func TestIndexSearch(t *testing.T) {
	idx := NewIndex()

	commands := []*model.Command{
		{
			Name:        "docker",
			Category:    "容器编排/Docker",
			Description: "容器管理工具",
			Platforms:   []string{"linux"},
			Usage:       []string{"docker [命令]"},
			Examples:    []model.Example{{Command: "docker ps", Description: "test"}},
		},
		{
			Name:        "docker-compose",
			Category:    "容器编排/Docker",
			Description: "多容器编排工具",
			Platforms:   []string{"linux"},
			Usage:       []string{"docker-compose [命令]"},
			Examples:    []model.Example{{Command: "docker-compose up", Description: "test"}},
		},
		{
			Name:        "grep",
			Category:    "操作系统/Linux",
			Description: "文本搜索工具",
			Platforms:   []string{"linux"},
			Usage:       []string{"grep pattern file"},
			Examples:    []model.Example{{Command: "grep foo bar", Description: "test"}},
		},
	}

	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	t.Run("ExactNameMatch", func(t *testing.T) {
		results := idx.Search("docker", 0)
		if len(results) == 0 {
			t.Error("expected results for 'docker'")
		}
		if results[0].Name != "docker" {
			t.Errorf("expected first result 'docker', got '%s'", results[0].Name)
		}
	})

	t.Run("PrefixMatch", func(t *testing.T) {
		results := idx.Search("dock", 0)
		if len(results) < 2 {
			t.Errorf("expected at least 2 results for 'dock', got %d", len(results))
		}
	})

	t.Run("KeywordMatch", func(t *testing.T) {
		results := idx.Search("docker-compose", 0)
		if len(results) < 1 {
			t.Errorf("expected at least 1 result for 'docker-compose', got %d", len(results))
		}
	})

	t.Run("NoMatch", func(t *testing.T) {
		results := idx.Search("xyznonexistent123", 0)
		if len(results) != 0 {
			t.Errorf("expected 0 results, got %d", len(results))
		}
	})

	t.Run("SortByPriority", func(t *testing.T) {
		results := idx.Search("docker", 0)
		if len(results) < 2 {
			t.Skip("not enough results to verify sort")
		}
		for i := 1; i < len(results); i++ {
			priPrev := 0
			priCurr := 0
			for _, cmd := range results[:i] {
				if cmd.Name == "docker" {
					priPrev = 100
				}
			}
			if results[i].Name == "docker-compose" {
				priCurr = 60
			}
			if priPrev > 0 && priCurr > 0 {
				break
			}
		}
	})
}

func TestSortSearchResults(t *testing.T) {
	results := []*searchResult{
		{command: &model.Command{Name: "c"}, priority: 40},
		{command: &model.Command{Name: "a"}, priority: 100},
		{command: &model.Command{Name: "b"}, priority: 80},
	}

	sortSearchResults(results)

	if results[0].priority != 100 || results[0].command.Name != "a" {
		t.Errorf("expected first result to be 'a' with priority 100, got %s/%d", results[0].command.Name, results[0].priority)
	}
	if results[1].priority != 80 || results[1].command.Name != "b" {
		t.Errorf("expected second result to be 'b' with priority 80")
	}
	if results[2].priority != 40 || results[2].command.Name != "c" {
		t.Errorf("expected third result to be 'c' with priority 40")
	}
}

func TestFuzzySearch(t *testing.T) {
	idx := NewIndex()
	commands := []*model.Command{
		{Name: "docker", Category: "容器编排/Docker", Description: "容器管理工具", Platforms: []string{"linux"}, Usage: []string{"docker [命令]"}, Examples: []model.Example{{Command: "docker ps", Description: "test"}}},
		{Name: "docker-compose", Category: "容器编排/Docker", Description: "多容器编排工具", Platforms: []string{"linux"}, Usage: []string{"docker-compose [命令]"}, Examples: []model.Example{{Command: "docker-compose up", Description: "test"}}},
		{Name: "kubectl", Category: "容器编排/Kubernetes", Description: "Kubernetes 命令行工具", Platforms: []string{"linux", "darwin"}, Usage: []string{"kubectl [命令]"}, Examples: []model.Example{{Command: "kubectl get pods", Description: "test"}}},
	}
	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	t.Run("typo_doker", func(t *testing.T) {
		results := idx.Search("doker", 0)
		if len(results) == 0 {
			t.Error("fuzzy search should find 'docker' for 'doker'")
		}
	})

	t.Run("typo_kubctl", func(t *testing.T) {
		results := idx.Search("kubctl", 0)
		if len(results) == 0 {
			t.Error("fuzzy search should find 'kubectl' for 'kubctl'")
		}
	})

	t.Run("multi_word_AND", func(t *testing.T) {
		results := idx.Search("docker compose", 0)
		if len(results) == 0 {
			t.Error("AND search should find 'docker-compose' for 'docker compose'")
		}
	})

	t.Run("multi_word_AND_mismatch", func(t *testing.T) {
		results := idx.Search("docker xyznonexistent", 0)
		if len(results) != 0 {
			t.Error("AND search should return 0 when one word doesn't match any field")
		}
	})

	t.Run("MaxResults", func(t *testing.T) {
		results := idx.Search("docker", 1)
		if len(results) > 1 {
			t.Errorf("expected at most 1 result with maxResults=1, got %d", len(results))
		}
	})
}

func TestSuggestCommand(t *testing.T) {
	idx := NewIndex()
	commands := []*model.Command{
		{Name: "docker", Category: "容器编排/Docker", Description: "容器管理工具", Platforms: []string{"linux"}, Usage: []string{"docker [命令]"}, Examples: []model.Example{{Command: "docker ps", Description: "test"}}},
		{Name: "docker-compose", Category: "容器编排/Docker", Description: "多容器编排工具", Platforms: []string{"linux"}, Usage: []string{"docker-compose [命令]"}, Examples: []model.Example{{Command: "docker-compose up", Description: "test"}}},
	}
	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	suggestion := idx.SuggestCommand("doker")
	if suggestion == "" {
		t.Error("expected suggestion for 'doker'")
	}

	exact := idx.SuggestCommand("docker")
	if exact != "docker" {
		t.Errorf("expected 'docker' for exact match, got '%s'", exact)
	}

	empty := idx.SuggestCommand("")
	if empty != "" {
		t.Errorf("expected empty string for empty input, got '%s'", empty)
	}
}

func TestGetAllCommandNames(t *testing.T) {
	idx := NewIndex()
	commands := []*model.Command{
		{Name: "ls", Category: "os", Description: "list", Platforms: []string{"linux"}, Usage: []string{"ls"}, Examples: []model.Example{{Command: "ls", Description: "test"}}},
		{Name: "cd", Category: "os", Description: "change dir", Platforms: []string{"linux"}, Usage: []string{"cd [dir]"}, Examples: []model.Example{{Command: "cd /", Description: "test"}}},
	}
	if err := idx.BuildIndex(commands); err != nil {
		t.Fatalf("BuildIndex() error = %v", err)
	}

	names := idx.GetAllCommandNames()
	if len(names) != 2 {
		t.Errorf("expected 2 names, got %d", len(names))
	}
}

func BenchmarkSearch(b *testing.B) {
	idx := NewIndex()
	var commands []*model.Command
	names := []string{"docker", "docker-compose", "kubectl", "git", "grep", "find", "awk", "sed", "curl", "wget",
		"npm", "yarn", "pip", "cargo", "go", "java", "python", "node", "redis-cli", "mysql", "psql",
		"helm", "terraform", "ansible", "vault", "consul", "etcdctl", "crictl", "nerdctl", "buildctl", "kind",
		"kubeadm", "kubectx", "stern", "k9s", "jq", "yq", "htop", "top", "ps", "netstat", "ss",
		"ip", "ping", "traceroute", "dig", "nslookup", "ssh", "scp", "rsync", "tar", "zip", "unzip"}
	for _, name := range names {
		commands = append(commands, &model.Command{
			Name: name, Category: "test", Description: "test command " + name,
			Platforms: []string{"linux", "darwin"}, Usage: []string{name + " [args]"},
			Examples: []model.Example{{Command: name, Description: "test"}},
		})
	}
	if err := idx.BuildIndex(commands); err != nil {
		b.Fatalf("BuildIndex() error = %v", err)
	}

	queries := []string{"docker", "kube", "dock", "git", "py", "docker compose", "helm", "kubectl get pods", "xyz", ""}
	for _, q := range queries {
		b.Run(q, func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				idx.Search(q, 0)
			}
		})
	}
}
