# Sudokool Backend API

The Sudokool Backend API is a Django-based API that generates Sudoku puzzles of varying degrees of difficulty based on user requests. It provides endpoints to retrieve puzzles and their solutions along with missing values. This API is used in conjunction with the Sudokool frontend to provide users with an interactive Sudoku puzzle-solving experience.

## Table of Contents

- [Getting Started](#started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Server](#server)
- [Endpoints](#endpoints)
  - [Generate Sudoku Puzzle](#puzzle)
- [Response Format](#format)
- [Error Handling](#error)

## Getting Started {#started}

#### Prerequisites {#prerequisites}

- Python 3.10 or higher
- Django 4.2.2

#### Installation {#installation}

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Running the Server {#server}

To run the development server, execute the following command:

```bash
python manage.py runserver
```

The API server will now be running at _'http://127.0.0.1:8000/'_.

## Endpoints {#endpoints}

### Generate Sudoku Puzzle {#puzzle}

- _URL: `/api/sudoku/<difficulty>/`_
- _Method:_ GET
- _Parameters:_
  - _`difficulty`_ (string, required) - The degree of difficulty for the generated Sudoku puzzle. Possible values are _"easy"_, _"medium"_, or _"hard"_.
- _Response:_
  - A JSON object containing the generated Sudoku puzzle and its solution.

## Response Format {#format}

The response for the "Generate Sudoku Puzzle" endpoint will have the following format:

```json
{
	"board": [
		[5, 3, 0, 0, 7, 0, 0, 0, 0]
		// ... (rest of the puzzle data)
	],
	"solved": [
		[5, 3, 4, 6, 7, 8, 9, 1, 2]
		// ... (rest of the solved puzzle data)
	]
}
```

The `board` field represents the Sudoku puzzle with missing values (0 for missing values), and the `solved` field represents the solution to the puzzle.

## Error Handling {#error}

If there is an error generating the Sudoku puzzle, the API will respond with an appropriate error message and status code.

Sample error response:

```json
{
	"error": "Difficulty not recognized",
	"status": 400
}
```
