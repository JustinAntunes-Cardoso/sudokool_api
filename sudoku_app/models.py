from django.db import models

# Create your models here.


class SudokuBoard(models.Model):
    # A Sudoku board is a 9x9 matrix, and each cell contains a digit (0 for empty cells)
    board = models.JSONField(default=[[0]*9 for _ in range(9)])
    answer = models.JSONField(default=[[0]*9 for _ in range(9)])

    def __str__(self):
        return f"Sudoku Board {self.id}"
