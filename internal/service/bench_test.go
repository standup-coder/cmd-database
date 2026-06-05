package service

import (
	"testing"
)

func BenchmarkNewCommandService(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := NewCommandService("../../data")
		if err != nil {
			b.Fatalf("failed to create service: %v", err)
		}
	}
}

func BenchmarkSearchCommands(b *testing.B) {
	svc, err := NewCommandService("../../data")
	if err != nil {
		b.Fatalf("failed to create service: %v", err)
	}

	queries := []string{"ls", "docker", "git", "kubectl", "java", "nginx"}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		query := queries[i%len(queries)]
		svc.SearchCommands(query)
	}
}

func BenchmarkSearchCommandsCached(b *testing.B) {
	svc, err := NewCommandService("../../data")
	if err != nil {
		b.Fatalf("failed to create service: %v", err)
	}

	// Pre-populate cache
	svc.SearchCommands("cached_query")

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		svc.SearchCommands("cached_query")
	}
}

func BenchmarkGetCommand(b *testing.B) {
	svc, err := NewCommandService("../../data")
	if err != nil {
		b.Fatalf("failed to create service: %v", err)
	}

	names := svc.GetAllCommandNames()
	if len(names) == 0 {
		b.Skip("no commands available")
	}

	name := names[0]

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		svc.GetCommand(name)
	}
}

func BenchmarkListCommandsByCategory(b *testing.B) {
	svc, err := NewCommandService("../../data")
	if err != nil {
		b.Fatalf("failed to create service: %v", err)
	}

	categories := svc.GetAllCategories()
	if len(categories) == 0 {
		b.Skip("no categories available")
	}

	category := categories[0]

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		svc.ListCommandsByCategory(category)
	}
}

func BenchmarkGetAllCommands(b *testing.B) {
	svc, err := NewCommandService("../../data")
	if err != nil {
		b.Fatalf("failed to create service: %v", err)
	}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		svc.GetAllCommands()
	}
}

func BenchmarkGetHighRiskCommands(b *testing.B) {
	svc, err := NewCommandService("../../data")
	if err != nil {
		b.Fatalf("failed to create service: %v", err)
	}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		svc.GetHighRiskCommands()
	}
}
