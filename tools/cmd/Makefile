VERSION ?= 1.8.0
COMMIT_HASH ?= $(shell git rev-parse --short HEAD 2>/dev/null || echo "unknown")
BUILD_TIME ?= $(shell date -u +%Y-%m-%dT%H:%M:%SZ)
LDFLAGS := -s -w -X 'main.Version=$(VERSION)' -X 'main.BuildTime=$(BUILD_TIME)' -X 'main.CommitHash=$(COMMIT_HASH)'

.PHONY: build test test-integration test-short test-race bench cover lint vet fmt clean install run tidy help

build:
	CGO_ENABLED=0 go build -ldflags "$(LDFLAGS)" -trimpath -o bin/cmd4coder ./cmd/cli
	@ls -lh bin/cmd4coder | awk '{print "Built: " $$5 " (" $$9 ")"}'

build-all:
	@bash scripts/build/build.sh

test:
	go test -v -cover ./...

test-short:
	go test -short -cover ./...

test-integration:
	go test -v -tags=integration ./test/...

test-race:
	go test -race ./...

bench:
	go test -bench=. -benchmem ./...

cover:
	go test -coverprofile=coverage.out ./...
	go tool cover -html=coverage.out -o coverage.html
	go tool cover -func=coverage.out

lint:
	golangci-lint run ./...

vet:
	go vet ./...

fmt:
	go fmt ./...

clean:
	rm -rf bin/ build/ coverage_reports/coverage.out coverage_reports/coverage.html

tidy:
	go mod tidy

install: build
	@mkdir -p $(GOPATH)/bin
	cp bin/cmd4coder $(GOPATH)/bin/

run:
	go run ./cmd/cli

validator:
	go run ./cmd/validator -d ./data -v

help:
	@echo "cmd4coder Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make build        Build the binary"
	@echo "  make build-all    Build for all platforms"
	@echo "  make test         Run all tests with coverage"
	@echo "  make test-short   Run tests (skip slow tests)"
	@echo "  make test-race    Run tests with race detector"
	@echo "  make bench        Run benchmarks"
	@echo "  make cover        Generate coverage report"
	@echo "  make lint         Run linter"
	@echo "  make vet          Run go vet"
	@echo "  make fmt          Format code"
	@echo "  make clean        Clean build artifacts"
	@echo "  make test-integration Run integration tests"
	@echo "  make tidy         Run go mod tidy"
	@echo "  make install      Build and install to GOPATH/bin"
	@echo "  make run          Run without building"
	@echo "  make validator    Run data validator"
