# AI 8-Puzzle Project

This project is an implementation of the 8-puzzle problem for my AI class. It includes representation of the puzzle state, a command interface for interaction, and a test case file for validation.

## Structure
- `src/`: Source code.
    - `EightPuzzle/`: Eight Puzzle Project
        - `EightPuzzle.py`: Puzzle module
        - `EightPuzzle.ipynb`: Jupyter Notebook
        - `testcmds.txt`: Text of commands to feed the command line
- `documentation/`: Documentation.
    - I'll get Sphinx up, but unfortunately, it is not working yet. -Ryan

## API

### Puzzle

A 3x3 puzzle that has values 0-8 included, with the 0 value being the free space. The values are stored in an array, with the first 3 values representing the values from left to right of the first row of the puzzle, followed by the second row, then the third.

Example:
```python
puzzle_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
