BLANK_BOARD = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

counter = 0
numArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Verifies Valid Sudoku placement.


class ValidSudoku:
    def _rowSafe(self, puzzle, row, num):
        # -1 is return value of .find() if value not found
        return not num in puzzle[row]

    def _colSafe(self, puzzle, col, num):
        return not any(puzzle[row][col] == num for row in range(len(puzzle)))

    def _boxSafe(self, puzzle, row, col, num):
        # Define top left corner of box region for empty cell
        boxStartRow = row - (row % 3)
        boxStartCol = col - (col % 3)
        safe = True

        for boxRow in [0, 1, 2]:
            # Each box region has 3 rows
            for boxCol in [0, 1, 2]:
                # Each box region has 3 columns
                if puzzle[boxStartRow + boxRow][boxStartCol + boxCol] == num:
                    # Num is present in box region?
                    safe = False  # If number is found, it is not safe to place

        return safe

    # Can only place if num is row, col and box safe
    def safeToPlace(self, puzzle, row, col, num):
        return (
            self._rowSafe(puzzle, row, num) and
            self._colSafe(puzzle, col, num) and
            self._boxSafe(puzzle, row, col, num)
        )
