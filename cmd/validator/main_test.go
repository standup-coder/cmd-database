package main

import (
	"testing"
)

func TestValidateDataDir_Success(t *testing.T) {
	report, err := validateDataDir("../../data")
	if err != nil {
		t.Fatalf("expected no error, got: %v", err)
	}

	if report.TotalFiles == 0 {
		t.Error("expected at least one data file")
	}

	if report.SuccessFiles == 0 {
		t.Error("expected at least one successful file")
	}

	if report.TotalCommands == 0 {
		t.Error("expected at least one command")
	}
}

func TestValidateDataDir_InvalidDir(t *testing.T) {
	// When an invalid directory is given, the loader falls back to embedded data.
	// So we expect success (embedded data) rather than an error.
	report, err := validateDataDir("/nonexistent/path/12345")
	if err != nil {
		t.Fatalf("expected fallback to embedded data, but got error: %v", err)
	}
	if report.TotalFiles == 0 {
		t.Error("expected at least one data file from embedded data")
	}
}

func TestValidateDataDir_EmptyDir(t *testing.T) {
	// Empty temp dir will fall back to embedded data since there's no metadata.yaml
	report, err := validateDataDir(t.TempDir())
	if err != nil {
		t.Fatalf("expected fallback to embedded data, but got error: %v", err)
	}
	if report.TotalFiles == 0 {
		t.Error("expected at least one data file from embedded data")
	}
}

func TestCalculateScores_Perfect(t *testing.T) {
	report := &ValidationReport{
		TotalFiles:    10,
		SuccessFiles:  10,
		TotalCommands: 500,
	}

	completeness, accuracy, warningRate, overall := calculateScores(report)

	if completeness <= 0 {
		t.Errorf("expected positive completeness, got %f", completeness)
	}

	if accuracy != 100.0 {
		t.Errorf("expected accuracy 100.0, got %f", accuracy)
	}

	if warningRate != 0.0 {
		t.Errorf("expected warningRate 0.0, got %f", warningRate)
	}

	if overall <= 0 {
		t.Errorf("expected positive overall score, got %f", overall)
	}
}

func TestCalculateScores_WithFailures(t *testing.T) {
	report := &ValidationReport{
		TotalFiles:    10,
		SuccessFiles:  5,
		TotalCommands: 200,
		Warnings: []ValidationWarning{
			{File: "test.yaml", Command: "cmd1", Message: "warn"},
			{File: "test.yaml", Command: "cmd2", Message: "warn"},
		},
	}

	completeness, accuracy, warningRate, overall := calculateScores(report)

	if accuracy != 50.0 {
		t.Errorf("expected accuracy 50.0, got %f", accuracy)
	}

	if warningRate != 1.0 {
		t.Errorf("expected warningRate 1.0, got %f", warningRate)
	}

	expectedOverall := 50.0*0.6 + 99.0*0.2 + completeness*0.2
	// Use approximate comparison for floating point
	diff := overall - expectedOverall
	if diff < 0 {
		diff = -diff
	}
	if diff > 0.0001 {
		t.Errorf("expected overall %f, got %f (diff %f)", expectedOverall, overall, diff)
	}
}

func TestCalculateScores_ZeroCommands(t *testing.T) {
	report := &ValidationReport{
		TotalFiles:    1,
		SuccessFiles:  1,
		TotalCommands: 0,
	}

	_, _, warningRate, _ := calculateScores(report)

	if warningRate != 0.0 {
		t.Errorf("expected warningRate 0.0 with zero commands, got %f", warningRate)
	}
}

func TestValidationReport_Struct(t *testing.T) {
	report := &ValidationReport{
		TotalFiles:         5,
		TotalCommands:      100,
		SuccessFiles:       4,
		FailedFiles:        1,
		Errors:             []ValidationError{{File: "a.yaml", Message: "error"}},
		Warnings:           []ValidationWarning{{File: "b.yaml", Command: "cmd", Message: "warn"}},
		CommandsByCategory: map[string]int{"os": 50, "net": 50},
	}

	if report.TotalFiles != 5 {
		t.Errorf("expected TotalFiles 5, got %d", report.TotalFiles)
	}

	if len(report.Errors) != 1 {
		t.Errorf("expected 1 error, got %d", len(report.Errors))
	}

	if len(report.Warnings) != 1 {
		t.Errorf("expected 1 warning, got %d", len(report.Warnings))
	}

	if report.CommandsByCategory["os"] != 50 {
		t.Errorf("expected os category 50 commands, got %d", report.CommandsByCategory["os"])
	}
}

func BenchmarkValidateDataDir(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := validateDataDir("../../data")
		if err != nil {
			b.Fatalf("validation failed: %v", err)
		}
	}
}
