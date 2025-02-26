Venkatesh Bollineni 800792618  vbollin@siue.edu

# CS456 Project I: Sorting and Heap 

## Description
This project implements three sorting algorithms: InsertionSort, MergeSort, and HeapSort. The algorithms are tested on both permuted and sorted input files,
and the results are plotted to analyze their performance.

## Files Included
- 'sortingandheaps.py': The main Python script containing the implementation of the sorting algorithms and code to run them.
- 'README.md': This file with instructions.
- 'Makefile': Instructions for setting up and running the project.
- 'Project 1 - REPORT.pdf': A detailed report with analysis and plots.

## Requirements
- Python 3.x


## How to Run

To run the sorting and heap algorithms source code, execute the following command:

python sortingandheaps.py

This script will:
- Prompt you to select input file type (numeric value) from 1 or 2.
- Prompt you to select the file size (numeric value) from 1 - 10.
- Prompt you to select the sorting algorithm (numeric value) from 1 - 3
- Output the sorted results to a file and print the runtime.
- Prompt you to select the choice to continue the next operation (continue or exit) from 1 - 2


## Output
- The sorted files will be named as 'IS15K.txt', 'MS15K.txt', 'HS15K.txt'for permuted input files.
- The sorted files will be named as 'ISS15K.txt', 'MSS15K.txt', 'HSS15K.txt' for sorted input files.

If you prefer to use 'make', use the following command:
make run

To clean up generated files, use the following command:
make clean

For help, use the following command:
make help

## Makefile
If you need to set up and run the project using `make`, refer to the `Makefile` document.
