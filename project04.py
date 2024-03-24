class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def is_safe(self, row, col, num):
        # Check if num is already in the row
        if num in self.grid[row]:
            return False

        # Check if num is already in the column
        if num in [self.grid[i][col] for i in range(9)]:
            return False

        # Check if num is already in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve_sudoku(self):
        # Find an empty cell
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    # Try placing numbers 1-9 in the empty cell
                    for num in range(1, 10):
                        if self.is_safe(row, col, num):
                            self.grid[row][col] = num

                            # Recursively solve the puzzle
                            if self.solve_sudoku():
                                return True

                            # If placing num at (row, col) doesn't lead to a solution, backtrack
                            self.grid[row][col] = 0

                    # No solution found for this cell
                    return False

        # Puzzle solved successfully
        return True


if __name__ == "__main__":
    # Input the Sudoku puzzle
    print("Enter the Sudoku puzzle (use 0 for empty cells):")
    grid = [list(map(int, input().split())) for _ in range(9)]

    sudoku_solver = SudokuSolver(grid)

    # Solve the Sudoku puzzle
    if sudoku_solver.solve_sudoku():
        print("Sudoku puzzle solved successfully!")
        # Print the solved puzzle
        sudoku_solver.print_grid()
    else:
        print("No solution exists for the given Sudoku puzzle.")
