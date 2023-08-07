from django.db import models

# Create your models here.


def default_board():
    # Create a 9x9 list with all elements set to 0
    return [[0] * 9 for _ in range(9)]


class SudokuBoard(models.Model):
    # A Sudoku board is a 9x9 matrix, and each cell contains a digit (0 for empty cells)
    board = models.JSONField(default=default_board)
    answer = models.JSONField(default=default_board)

    def __str__(self):
        return f"Sudoku Board {self.id}"
