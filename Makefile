# Makefile for CS456 Project - I: Sorting and Heap

# Define variables
PYTHON=python
SCRIPT=sortingandheaps.py

# Default target
all: run

# Target to run the sorting algorithms
run:
	$(PYTHON) $(SCRIPT)

# Target to clean up generated files
clean:
	rm -f *.txt

# Target to show help
help:
	@echo "Makefile for CS456 Project - I: Sorting and Heap"
	@echo "Usage:"
	@echo "  make run       Run the sorting algorithms script"
	@echo "  make clean     Clean up generated files"
	@echo "  make help      Show this help message"
