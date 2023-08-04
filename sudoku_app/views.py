from rest_framework.response import Response
from rest_framework.decorators import api_view
from . sudoku.sudoku_logic import SudokuPuzzleGenerator, ValidSodukuPuzzle
from rest_framework import status
import random

# Custom error if Difficulty is not easy, medium or hard.


class InvalidDifficultyException(ValueError):
    pass

# generates sudoku puzzle of certain level of difficulty based on api


def getSudokuPuzzle(diff='easy'):
    # Error checking diff set.
    if diff not in ['easy', 'medium', 'hard']:
        raise InvalidDifficultyException(
            "Invalid difficulty. Valid options are 'easy', 'medium', or 'hard'.")

    # Creates Puzzle
    sudoku = SudokuPuzzleGenerator()
    # Checks for single solution
    check = ValidSodukuPuzzle()
    holes = 0
    # Sets the amount of holes in the puzle based on diff
    if diff == 'easy':
        holes = random.randint(15, 20)
    elif diff == 'medium':
        holes = random.randint(25, 30)
    elif diff == 'hard':
        holes = random.randint(32, 38)
    else:
        holes = random.randint(40, 42)

    removedVals, startingBoard, solvedBoard = sudoku.newStartingBoard(holes)
    # Runs until a single solution is found
    while check.multiplePossibleSolutions(startingBoard) == False:
        removedVals, startingBoard, solvedBoard = sudoku.newStartingBoard(
            holes)

    return removedVals, startingBoard, solvedBoard


@api_view(['GET'])
def getData(request, arg):
    try:
        vals, board, solved = getSudokuPuzzle(arg)
        response_data = {
            'values': vals,
            'board': board,
            'solved': solved
        }

        return Response(response_data, status=status.HTTP_200_OK)

    except InvalidDifficultyException as e:
        # Get the error message from the exception (optional)
        error_message = str(e)
        # You can customize the error response as needed
        error_data = {'error': error_message}
        return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
