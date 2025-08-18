# Sudoku Solver using Backtracking

# Function to print Sudoku grid
def print_grid(grid):
    for row in grid:
        print(row)

# Function to find an empty cell in Sudoku (marked as 0)
def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:  # Empty cell
                return i, j
    return None

# Function to check if placing a number is safe
def is_safe(grid, row, col, num):
    # Check row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

# Backtracking solver
def solve_sudoku(grid):
    empty = find_empty_location(grid)
    if not empty:
        return True  # Solved
    row, col = empty

    for num in range(1, 10):  # Numbers 1-9
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            # Undo assignment (backtrack)
            grid[row][col] = 0

    return False

# Example Sudoku Puzzle (0 means empty)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Puzzle:")
print_grid(sudoku_grid)
print("\nSolving Sudoku...\n")
if solve_sudoku(sudoku_grid):
    print("Sudoku Solved Successfully:")
    print_grid(sudoku_grid)
else:
    print("No solution exists!")
