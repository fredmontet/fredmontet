.PHONY: preview build clean sync dev publish help

help:
	@echo "Available commands:"
	@echo "  make preview   - Start the preview server"
	@echo "  make build     - Build the static site"
	@echo "  make sync      - Sync dependencies"
	@echo "  make clean     - Remove generated files"
	@echo "  make dev       - Sync and start preview"
	@echo "  make publish   - Clean and build for deployment"

clean:
	rm -rf _site .quarto

sync:
	uv sync

preview:
	uv run quarto preview

build:
	uv run quarto render

publish:
	uv run quarto publish --no-prompt --no-browser

dev: sync preview

.DEFAULT_GOAL := help
