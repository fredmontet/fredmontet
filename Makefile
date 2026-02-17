.PHONY: preview build clean sync dev publish help

help:
	@echo "Available commands:"
	@echo "  make preview   - Start the preview server"
	@echo "  make build     - Build the static site"
	@echo "  make sync      - Sync dependencies"
	@echo "  make clean     - Remove generated files"
	@echo "  make dev       - Sync and start preview"
	@echo "  make publish   - Clean and build for deployment"

preview:
	uv run quarto preview

build:
	uv run quarto render

sync:
	uv sync

clean:
	rm -rf _site .quarto

dev: sync preview

publish: clean build

.DEFAULT_GOAL := help
