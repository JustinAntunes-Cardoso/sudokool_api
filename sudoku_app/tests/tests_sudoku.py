import copy
from django.test import TestCase
from ..sudoku.sudoku_logic import ValidSudoku, SudokuPuzzleGenerator, ValidSodukuPuzzle

TEST_BOARD = [
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

FULL_BOARD = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


class TestValidity(TestCase):
    def test_valid_row(self):
        # Test for valid or invalid row number placement
        isValid = ValidSudoku()
        self.assertEqual(isValid._rowSafe(TEST_BOARD, 0, 1), True)
        self.assertEqual(isValid._rowSafe(TEST_BOARD, 0, 3), False)

    def test_valid_col(self):
        # Test for valid or invalid col number placement
        isValid = ValidSudoku()
        self.assertEqual(isValid._colSafe(TEST_BOARD, 0, 1), True)
        self.assertEqual(isValid._colSafe(TEST_BOARD, 0, 5), False)

    def test_valid_box(self):
        # Test for valid or invalid box number placement
        isValid = ValidSudoku()
        self.assertEqual(isValid._boxSafe(TEST_BOARD, 0, 0, 1), True)
        self.assertEqual(isValid._boxSafe(TEST_BOARD, 0, 0, 3), False)

    def test_valid_safe_placement(self):
        # Test for safeToPlace return value
        isValid = ValidSudoku()
        self.assertEqual(isValid.safeToPlace(TEST_BOARD, 0, 0, 1), True)
        self.assertEqual(isValid.safeToPlace(TEST_BOARD, 0, 0, 3), False)


class TestBoardSetup(TestCase):
    def test_next_empty_cell(self):
        # Test if function returns position of the empty cell
        empty = SudokuPuzzleGenerator()
        row, col = empty.nextEmptyCell(TEST_BOARD)
        # Test if function return -1 if board is full
        rowFull, colFull = empty.nextEmptyCell(FULL_BOARD)
        # Test empty space abstraction
        self.assertIsNot(row, -1)
        self.assertIsNot(col, -1)
        self.assertEqual(row, 0)
        self.assertEqual(col, 2)
        # Test full board recognition
        self.assertEqual(rowFull, -1)
        self.assertEqual(colFull, -1)

    def test_poke_holes(self):

        # Test if holes poked in the puzzle the same amount as needed
        sudoku = SudokuPuzzleGenerator()
        board = copy.deepcopy(FULL_BOARD)
        removedCells, pokedBoard = sudoku.pokeHoles(board, 25)
        holes = 0
        for row in pokedBoard:
            holes += row.count(0)

        # Test amount of holes poked
        self.assertEqual(holes, 25)
        self.assertEqual(len(removedCells), 25)

    def test_solved_board(self):

        # Test to see if puzzle can fill itself
        sudoku = SudokuPuzzleGenerator()

        board = sudoku.newSolvedBoard()
        zeros = 0
        for row in board:
            zeros += row.count(0)
            self.assertIn(1, row)
            self.assertIn(2, row)
            self.assertIn(3, row)
            self.assertIn(4, row)
            self.assertIn(5, row)
            self.assertIn(6, row)
            self.assertIn(7, row)
            self.assertIn(8, row)
            self.assertIn(9, row)

        self.assertEqual(zeros, 0)

    def test_solved_board(self):

        # Test to see if puzzle can fill itself
        sudoku = SudokuPuzzleGenerator()

        removedVals, startingBoard, solvedBoard = sudoku.newStartingBoard(25)
        holes = 0
        for row in startingBoard:
            holes += row.count(0)

        zeros = 0
        for row in solvedBoard:
            zeros += row.count(0)

        self.assertEqual(len(removedVals), 25)
        self.assertEqual(holes, 25)
        self.assertEqual(zeros, 0)


class TestMultipleSolutions(TestCase):

    def test_empty_cells(self):
        emptyCells = ValidSodukuPuzzle().emptyCellCoords(TEST_BOARD)
        fullCells = ValidSodukuPuzzle().emptyCellCoords(FULL_BOARD)

        self.assertEqual(len(emptyCells), 51)
        self.assertEqual(len(fullCells), 0)

    def test_next_empty_cell(self):
        # abstract empty cells
        emptyCells = ValidSodukuPuzzle().emptyCellCoords(TEST_BOARD)

        # Gives next empty cell
        nextEmpty = ValidSodukuPuzzle().nextStillEmptyCell(TEST_BOARD, emptyCells)
        self.assertEqual(nextEmpty['rowIndex'], 0)
        self.assertEqual(nextEmpty['colIndex'], 2)
