package data

import (
	"testing"
)

func BenchmarkLoadMetadata(b *testing.B) {
	loader := NewLoader("../../data")

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_, err := loader.LoadMetadata()
		if err != nil {
			b.Fatalf("failed to load metadata: %v", err)
		}
	}
}

func BenchmarkLoadAllCommands(b *testing.B) {
	loader := NewLoader("../../data")

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_, err := loader.LoadAllCommands()
		if err != nil {
			b.Fatalf("failed to load commands: %v", err)
		}
	}
}

func BenchmarkBuildIndex(b *testing.B) {
	loader := NewLoader("../../data")
	commands, err := loader.LoadAllCommands()
	if err != nil {
		b.Fatalf("failed to load commands: %v", err)
	}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		index := NewIndex()
		if err := index.BuildIndex(commands); err != nil {
			b.Fatalf("failed to build index: %v", err)
		}
	}
}

func BenchmarkIndexSearch(b *testing.B) {
	loader := NewLoader("../../data")
	commands, err := loader.LoadAllCommands()
	if err != nil {
		b.Fatalf("failed to load commands: %v", err)
	}

	index := NewIndex()
	if err := index.BuildIndex(commands); err != nil {
		b.Fatalf("failed to build index: %v", err)
	}

	queries := []string{"ls", "docker", "git", "kubectl", "java"}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		query := queries[i%len(queries)]
		index.Search(query, 0)
	}
}

func BenchmarkCacheSetGet(b *testing.B) {
	cache := NewSearchCache(100)

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		key := "query" + string(rune(i%26+'a'))
		cache.SetSearchResult(key, nil)
		cache.GetSearchResult(key)
	}
}
