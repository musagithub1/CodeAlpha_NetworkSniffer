# CodeAlpha Network Packet Sniffer Makefile
# Cybersecurity Internship Project

# Default target
.DEFAULT_GOAL := help

# Variables
PYTHON := python3
SCRIPT := packet_sniffer.py
REQUIREMENTS := requirements.txt

# Colors for output
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[1;33m
BLUE := \033[0;34m
NC := \033[0m # No Color

# Help target - shows available commands
help:
	@echo "$(BLUE)CodeAlpha Network Packet Sniffer$(NC)"
	@echo "$(BLUE)================================$(NC)"
	@echo ""
	@echo "$(YELLOW)Available commands:$(NC)"
	@echo "  $(GREEN)install$(NC)      - Install Python dependencies"
	@echo "  $(GREEN)run$(NC)          - Run packet sniffer (default mode)"
	@echo "  $(GREEN)run-count$(NC)    - Run with packet count limit (3 packets)"
	@echo "  $(GREEN)run-filter$(NC)   - Run with HTTP traffic filter"
	@echo "  $(GREEN)run-dns$(NC)      - Run with DNS traffic filter"
	@echo "  $(GREEN)run-save$(NC)     - Run and save packets to JSON file"
	@echo "  $(GREEN)demo$(NC)         - Run a quick demo (5 packets, save results)"
	@echo "  $(GREEN)check$(NC)        - Check if dependencies are installed"
	@echo "  $(GREEN)clean$(NC)        - Clean temporary files and cache"
	@echo "  $(GREEN)permissions$(NC)  - Check if script has necessary permissions"
	@echo "  $(GREEN)help$(NC)         - Show this help message"
	@echo ""
	@echo "$(YELLOW)Examples:$(NC)"
	@echo "  sudo make run"
	@echo "  sudo make run-filter"
	@echo "  sudo make demo"
	@echo ""
	@echo "$(RED)Note: Most commands require sudo privileges!$(NC)"

# Install dependencies
install:
	@echo "$(YELLOW)Installing dependencies...$(NC)"
	pip install -r $(REQUIREMENTS)
	@echo "$(GREEN)Dependencies installed successfully!$(NC)"

# Check if dependencies are installed
check:
	@echo "$(YELLOW)Checking dependencies...$(NC)"
	@$(PYTHON) -c "import scapy; print('✓ Scapy is installed')" || (echo "$(RED)✗ Scapy is not installed. Run 'make install'$(NC)" && exit 1)
	@echo "$(GREEN)All dependencies are installed!$(NC)"

# Check permissions
permissions:
	@echo "$(YELLOW)Checking permissions...$(NC)"
	@if [ "$(shell id -u)" -ne 0 ]; then \
		echo "$(RED)✗ Root privileges required for packet capture$(NC)"; \
		echo "$(YELLOW)Please run with sudo: sudo make run$(NC)"; \
	else \
		echo "$(GREEN)✓ Running with root privileges$(NC)"; \
	fi

# Basic run
run: check
	@echo "$(YELLOW)Starting packet sniffer...$(NC)"
	@echo "$(BLUE)Press Ctrl+C to stop$(NC)"
	sudo $(PYTHON) $(SCRIPT)

# Run with count limit
run-count: check
	@echo "$(YELLOW)Starting packet sniffer (3 packets)...$(NC)"
	sudo $(PYTHON) $(SCRIPT) -c 3

# Run with HTTP filter
run-filter: check
	@echo "$(YELLOW)Starting packet sniffer (HTTP traffic only)...$(NC)"
	sudo $(PYTHON) $(SCRIPT) -f "tcp port 80"

# Run with DNS filter
run-dns: check
	@echo "$(YELLOW)Starting packet sniffer (DNS traffic only)...$(NC)"
	sudo $(PYTHON) $(SCRIPT) -f "port 53"

# Run with HTTPS filter
run-https: check
	@echo "$(YELLOW)Starting packet sniffer (HTTPS traffic only)...$(NC)"
	sudo $(PYTHON) $(SCRIPT) -f "tcp port 443"

# Run and save results
run-save: check
	@echo "$(YELLOW)Starting packet sniffer (saving to file)...$(NC)"
	sudo $(PYTHON) $(SCRIPT) -c 10 --save
	@echo "$(GREEN)Results saved to captured_packets.json$(NC)"

# Quick demo
demo: check
	@echo "$(BLUE)Running packet sniffer demo...$(NC)"
	@echo "$(YELLOW)Capturing 5 packets and saving results$(NC)"
	sudo $(PYTHON) $(SCRIPT) -c 5 --save
	@echo "$(GREEN)Demo completed! Check captured_packets.json$(NC)"

# Interactive mode - let user choose options
interactive: check
	@echo "$(BLUE)Interactive Packet Sniffer$(NC)"
	@echo "Select capture mode:"
	@echo "1) All traffic (default)"
	@echo "2) HTTP traffic only"
	@echo "3) HTTPS traffic only" 
	@echo "4) DNS traffic only"
	@echo "5) Custom filter"
	@read -p "Choice (1-5): " choice; \
	case $$choice in \
		1) sudo $(PYTHON) $(SCRIPT) ;; \
		2) sudo $(PYTHON) $(SCRIPT) -f "tcp port 80" ;; \
		3) sudo $(PYTHON) $(SCRIPT) -f "tcp port 443" ;; \
		4) sudo $(PYTHON) $(SCRIPT) -f "port 53" ;; \
		5) read -p "Enter BPF filter: " filter; sudo $(PYTHON) $(SCRIPT) -f "$$filter" ;; \
		*) echo "$(RED)Invalid choice$(NC)" ;; \
	esac

# Clean temporary files
clean:
	@echo "$(YELLOW)Cleaning temporary files...$(NC)"
	rm -f *.pyc
	rm -f *.log
	rm -rf __pycache__/
	rm -f .DS_Store
	rm -f captured_packets.json
	@echo "$(GREEN)Cleanup completed!$(NC)"

# Development setup
dev-setup: install
	@echo "$(YELLOW)Setting up development environment...$(NC)"
	@echo "$(GREEN)Development setup completed!$(NC)"

# Test basic functionality
test: check
	@echo "$(YELLOW)Testing packet sniffer (1 packet)...$(NC)"
	timeout 10s sudo $(PYTHON) $(SCRIPT) -c 1 || true
	@echo "$(GREEN)Test completed!$(NC)"

# Show project info
info:
	@echo "$(BLUE)CodeAlpha Network Packet Sniffer$(NC)"
	@echo "$(BLUE)================================$(NC)"
	@echo "Project: Cybersecurity Internship - Task 1"
	@echo "Language: Python 3"
	@echo "Main Library: Scapy"
	@echo "Purpose: Network traffic analysis and protocol learning"
	@echo ""
	@echo "$(YELLOW)Files in project:$(NC)"
	@ls -la *.py *.txt Makefile 2>/dev/null || true

# Declare phony targets
.PHONY: help install check permissions run run-count run-filter run-dns run-https run-save demo interactive clean dev-setup test info