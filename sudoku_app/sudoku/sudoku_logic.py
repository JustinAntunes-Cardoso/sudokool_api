import copy
import random
from .utils import shuffle


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

# Generates Sudoku Puzzle


class SudokuPuzzleGenerator:
    def __init__(self) -> None:
        self.counter = 0
        self.numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.BLANK_BOARD = [
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

    # Find the next Empty cell
    def nextEmptyCell(self, puzzle):
        colPosition, rowPosition = -1, -1

        for rowIndex, row in enumerate(puzzle):
            if colPosition != -1:
                continue  # If this key has already been assigned, skip iteration

            try:
                firstZero = next(i for i in range(len(puzzle))
                                 if row[i] == 0)  # find first zero-element
            except StopIteration:
                continue  # if no zero present, skip to next row

            rowPosition = rowIndex
            colPosition = firstZero

        if colPosition != -1:
            return rowPosition, colPosition
        # If emptyCell was never assigned, there are no more zeros
        return -1, -1

    # Script to find Puzzle solution.
    def fillPuzzle(self, startingBoard):
        emptyRowIndex, emptyColIndex = self.nextEmptyCell(startingBoard)
        isValid = ValidSudoku()
        # If there are no more zeros, the board is finished, return it
        if (emptyRowIndex == -1 or emptyColIndex == -1):
            return startingBoard

        # Shuffled [0 - 9] list fills board randomly each pass
        for num in shuffle(self.numList):
            self.counter += 1
            if self.counter > 20_000_000:
                raise RecursionError('Recursion Timeout')

            if isValid.safeToPlace(startingBoard, emptyRowIndex, emptyColIndex, num):
                # If safe to place number, place it
                startingBoard[emptyRowIndex][emptyColIndex] = num
                # Recursively call the fill function to place num in next empty cell
                if self.fillPuzzle(startingBoard):
                    return startingBoard
                # If we were unable to place the future num, that num was wrong. Reset it and try next value
                startingBoard[emptyRowIndex][emptyColIndex] = 0

        return False  # If unable to place any number, return false, which triggers previous round to go to next num

    # Creates a new Solved Sudoku board which validates the sudoku conditions
    def newSolvedBoard(self):
        # Create an deep copy of a fresh board
        newBoard = copy.deepcopy(self.BLANK_BOARD)
        # Populate the board using backtracking algorithm
        self.fillPuzzle(newBoard)
        return newBoard

    # pokes holes randomly in the board depending on difficulty
    def pokeHoles(self, startingBoard, holes):
        removedVals = []

        while len(removedVals) < holes:
            val = random.randint(0, 81)  # Value between 0-81
            randomRowIndex = val // 9  # Integer 0-8 for row index
            randomColIndex = val % 9

            if not 0 <= randomRowIndex < len(startingBoard):
                continue  # guard against cloning error
            if startingBoard[randomRowIndex][randomColIndex] == 0:
                continue  # If cell already empty, restart loop

            removedVals.append(dict(
                # Store the current value at the coordinates
                rowIndex=randomRowIndex,
                colIndex=randomColIndex,
                val=startingBoard[randomRowIndex][randomColIndex],
            ))
            # "poke a hole" in the board at the coords
            startingBoard[randomRowIndex][randomColIndex] = 0
            proposedBoard = copy.deepcopy(
                startingBoard)  # Clone this changed board

            # Attempt to solve the board after removing value. If it cannot be solved, restore the old value.
            # and remove that option from the list
            if (not self.fillPuzzle(proposedBoard)):
                removed = removedVals.pop()
                startingBoard[randomRowIndex][randomColIndex] = removed['val']

        return removedVals, startingBoard

    def newStartingBoard(self, holes):
        # Reset global iteration counter to 0 and tries to generate a new game.
        # If counter reaches its maximum limit in the fillPuzzle function, the current attemp will abort
        # Error is caught and used to re-run the function until new board is created

        try:
            self.counter = 0
            solvedBoard = self.newSolvedBoard()

            # Clone the populated board and poke holes in it.
            # Stored the removed values for clues
            removedVals, startingBoard = self.pokeHoles(
                copy.deepcopy(solvedBoard),
                holes
            )

            return removedVals, startingBoard, solvedBoard

        except RuntimeError:
            return self.newStartingBoard(holes)


class ValidSodukuPuzzle:
    def __init__(self) -> None:
        self.numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Get a list of all empty cells in the board from top-left to bottom-right
    def emptyCellCoords(self, startingBoard):
        listOfEmptyCells = []
        for row in range(9):
            for col in range(9):
                if startingBoard[row][col] == 0:
                    listOfEmptyCells.append({'rowIndex': row, 'colIndex': col})
        return listOfEmptyCells

    # As numbers get placed, not all of the initial cells are still empty.
    # This will find the next still empty cell in the list
    def nextStillEmptyCell(self, startingBoard, emptyCellList):
        for coords in emptyCellList:
            if startingBoard[coords['rowIndex']][coords['colIndex']] == 0:
                return {'rowIndex': coords['rowIndex'], 'colIndex': coords['colIndex']}

        return False

    # This will attempt to solve the puzzle by placing values into the board in the order that
    # the empty cells list presents
    def fillFromList(self, startingBoard, emptyCellList):
        emptyCell = self.nextStillEmptyCell(startingBoard, emptyCellList)
        pokeCounter = 0
        isValid = ValidSudoku()
        if not emptyCell:
            return startingBoard
        for num in shuffle(self.numList):
            pokeCounter += 1
            if pokeCounter > 60_000_000:
                raise RecursionError('Poke Timeout')
            if isValid.safeToPlace(startingBoard, emptyCell['rowIndex'], emptyCell['colIndex'], num):
                startingBoard[emptyCell['rowIndex']
                              ][emptyCell['colIndex']] = num
                if self.fillFromList(startingBoard, emptyCellList):
                    return startingBoard
                startingBoard[emptyCell['rowIndex']][emptyCell['colIndex']] = 0

        return False

    def multiplePossibleSolutions(self, boardToCheck):
        possibleSolutions = []
        emptyCellList = self.emptyCellCoords(boardToCheck)
        for index in range(len(emptyCellList)):
            # Rotate a clone of the emptyCellList by one for each iteration
            emptyCellClone = copy.deepcopy(emptyCellList)
            startingPoint = emptyCellClone.pop(index)
            emptyCellClone.insert(0, startingPoint)
            board = copy.deepcopy(boardToCheck)

            thisSolution = self.fillFromList(board, emptyCellClone)
            if isinstance(thisSolution, list):
                possibleSolutions.append(','.join(map(str, thisSolution)))

            if len(set(possibleSolutions)) > 1:
                return True

        return False
