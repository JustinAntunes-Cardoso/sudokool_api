from django.test import TestCase
from ..sudoku.sudoku_logic import ValidSudoku

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


class TestBoard(TestCase):
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
