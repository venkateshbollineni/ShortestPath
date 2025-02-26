# Makefile for CS456 Project Assignment II: Single Source Shortest Path

# Variables
PYTHON = python3
SCRIPT = shortestpath.py

# Default target
.PHONY: run
run: $(SCRIPT)
	@$(PYTHON) $(SCRIPT) || true

# Clean target
.PHONY: clean
clean:
	@rm -f *.pyc
	@rm -rf __pycache__

# Help target
.PHONY: help
help:
	@echo "Makefile for CS456 Project Assignment II: Single Source Shortest Path"
	@echo ""
	@echo "Available targets:"
	@echo "  run      - Run the shortest path algorithms"
	@echo "  clean    - Remove generated files"
	@echo "  help     - Display this help message"

# Ensure the script is executable
$(SCRIPT):
	@chmod +x $(SCRIPT)
